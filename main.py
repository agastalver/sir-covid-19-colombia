import os
import json
import requests

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy import optimize
from scipy.integrate import odeint

if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists("images"):
    os.makedirs("images")

# download file

url = "https://e.infogram.com/api/live/flex/bc384047-e71c-47d9-b606-1eb6a29962e3/972157a6-eaf7-4cde-a65b-8579bd4b0af1"
s = requests.get(url).text

# read file

columns = json.loads(s)["data"][0][0]
data = json.loads(s)["data"][0][1:]
dft = pd.DataFrame(data, columns=columns)

dft.to_csv(os.path.join("data", "original-data.csv"), index=None)

# prepare

dft.columns = ["date", "dead", "recovered", "cases"]
dft["date"] = pd.to_datetime(dft["date"], format="%d/%m")
dft["date"] = dft["date"] + pd.offsets.DateOffset(year=2020)
dft = dft.set_index("date")
dft = dft.replace("",0).astype(np.float)

dfto = dft.copy()

dfpct = 100*dft["dead"]/dft["cases"]
dft["recovered"] = dft["recovered"] + dft["dead"] # as SIR model defines
dft["infected"] = dft["cases"] - dft["recovered"]

# optimization SIR

def sir(N, beta, gamma, days):
    I0 = 1
    R0 = 0
    S0 = N - I0 - R0
    def deriv(y, t, N, beta, gamma):
        S, I, R = y
        dSdt = -beta * S * I / N
        dIdt = beta * S * I / N - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt
    y0 = S0, I0, R0
    t = np.linspace(0, days, days)
    ret = odeint(deriv, y0, t, args=(N, beta, gamma))
    S, I, R = ret.T
    return S, I, R

def fdelay(delay):
    def f(x):
        N = x[0]
        beta = x[1]
        gamma = x[2]
        days = len(dft)
        S, I, R = sir(N, beta, gamma, days + abs(delay))
        lim = abs(delay)
        S, I, R = S[lim:lim+days], I[lim:lim+days], R[lim:lim+days]
        Io, Ro = dft["infected"].values, dft["recovered"].values
        So = N - Io
        #loss = ((S - So)**2).sum()/days + ((I - Io)**2).sum()/days + ((R - Ro)**2).sum()/days
        loss = ((I - Io)**2).sum()/days + ((R - Ro)**2).sum()/days
        return loss
    result = optimize.minimize(f, [80000, 1, 1], method="Nelder-Mead")
    return result

delay = 0
result = fdelay(delay)
for d in range(15):
    r2 = fdelay(d)
    print("delay: {}, fun: {}".format(d, r2.fun))
    if r2.fun < result.fun:
        delay = d
        result = r2

N = result.x[0]
beta = result.x[1]
gamma = result.x[2]
days = len(dft)

print("optimal: N = {}, beta = {}, gamma = {}, delay = {}".format(N, beta, gamma, delay))
print("error: {}".format(result.fun))

S, I, R = sir(N, beta, gamma, days + abs(delay))
lim = abs(delay)
S, I, R = S[lim:lim+days], I[lim:lim+days], R[lim:lim+days]

dft["S"] = S
dft["I"] = I
dft["R"] = R

dft["susceptible"] = N - dft["infected"]

# forecasting

far = 60 # days

S, I, R =  sir(N, beta, gamma, days + far + abs(delay))
lim = abs(delay)
S, I, R = S[lim:lim+days+far], I[lim:lim+days+far], R[lim:lim+days+far]
d = {
    "S": S,
    "I": I,
    "R": R,
    "susceptible": list(dft["susceptible"].values) + [np.nan]*far,
    "infected": list(dft["infected"].values) + [np.nan]*far,
    "recovered": list(dft["recovered"].values) + [np.nan]*far,
}
dff = pd.DataFrame(d)
dff["date"] = pd.date_range(dft.index[0],periods=days+far,freq="D")
dff = dff.set_index("date")

dff["cases"] = dff["recovered"] + dff["infected"]
dff["forecast"] = dff["R"] + dff["I"]
dff[["forecast", "cases"]].to_csv(os.path.join("data", "generated-cases.csv"))

# graph

metadata = {'Creator': None, 'Producer': None, 'CreationDate': None}


fig, ax = plt.subplots(figsize=(8,6))
dfto[["cases", "dead", "recovered"]].plot(ax=ax)
ax.set_title("Totals in Colombia")
ax.set_xlabel("")
ax.set_ylabel("# of occurences")
ax.grid(True, which="both")
dfto[["cases", "dead", "recovered"]].to_csv(os.path.join("data", "generated-total.csv"))
plt.savefig(os.path.join("images", "generated-total.png"), format="png", dpi=300)
plt.savefig(os.path.join("images", "generated-total.pdf"), format="pdf", dpi=300, metadata=metadata)

fig, ax = plt.subplots(figsize=(8,6))
dfpct.plot(ax=ax)
ax.set_title("Percentage of dead")
ax.set_xlabel("")
ax.set_ylabel("%")
ax.grid(True, which="both")
plt.savefig(os.path.join("images", "generated-deadpct.png"), format="png", dpi=300)
plt.savefig(os.path.join("images", "generated-deadpct.pdf"), format="pdf", dpi=300, metadata=metadata)

fig, ax = plt.subplots(figsize=(8,6))
dff[["susceptible", "infected", "recovered"]].plot(ax=ax)
dff[["S", "I", "R"]].plot(ax=ax, linestyle=":")
ax.set_title("SIR model")
ax.set_xlabel("")
ax.set_ylabel("# of people")
ax.grid(True, which="both")
dff.to_csv(os.path.join("data", "generated-sir.csv"))
plt.savefig(os.path.join("images", "generated-sir.png"), format="png", dpi=300)
plt.savefig(os.path.join("images", "generated-sir.pdf"), format="pdf", dpi=300, metadata=metadata)

fig, ax = plt.subplots(figsize=(8,6))
dff[["cases"]].plot(ax=ax)
dff[["forecast"]].plot(ax=ax, linestyle=":")
ax.set_title("Cases forecasting")
ax.set_xlabel("")
ax.set_ylabel("# of occurences")
ax.grid(True, which="both")
plt.savefig(os.path.join("images", "generated-sir-cases.png"), format="png", dpi=300)
plt.savefig(os.path.join("images", "generated-sir-cases.pdf"), format="pdf", dpi=300, metadata=metadata)
