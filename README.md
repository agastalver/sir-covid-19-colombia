# COVID-19 SIR mathematical model for Colombia

SIR mathematical model for infectious diseases optimized for COVID-19 using Colombian National Institute of Health public available data.

> **IMPORTANT NOTE**: The information available is still very poor, please wait a couple of days to obtain a better adjustment.

-----

![sir-cases](https://github.com/agastalver/sir-covid-19-colombia/raw/master/images/generated-sir-cases.png "SIR Model Cases")

![sir](https://github.com/agastalver/sir-covid-19-colombia/raw/master/images/generated-sir.png "SIR Model")

**Note**: 

* `susceptible`, `infected`, and `recovered`, stand for the observable population; thus, the ones that can be detected. The actual values could be higher.
* `susceptible` is an estimated value calculated from `N` with respect to the `infected` and `recovered`, the actual value is not provided by the government.
* `recovered` stands for people who has recovered from the virus or has died; as considered in the SIR model.

-----

## Last optimization

### Case forecasting table

| Date           | Infected | Cases    |
|:--------------:|:--------:|:--------:|
| 2020-04-06     | 1407     | 1516     |
| 2020-04-07     | 1508     | 1631     |
| 2020-04-08     | 1607     | 1744     |
| 2020-04-09     | 1701     | 1853     |
| 2020-04-10     | 1791     | 1958     |
| 2020-04-11     | 1874     | 2058     |
| 2020-04-12     | 1951     | 2152     |
| 2020-04-13     | 2020     | 2240     |
| 2020-04-14     | 2111     | 2350     |
| 2020-04-15     | 2189     | 2447     |
| 2020-04-16     | 2254     | 2532     |
| 2020-04-17     | 2306     | 2605     |
| 2020-04-18     | 2348     | 2668     |
| 2020-04-19     | 2380     | 2722     |
| 2020-04-20     | 2404     | 2767     |
| 2020-04-21     | 2420     | 2805     |
| 2020-04-22     | 2429     | 2837     |
| **2020-04-23** | **2434** | **2863** |
| **2020-04-24** | **2434** | **2885** |
| 2020-04-25     | 2430     | 2904     |
| 2020-04-26     | 2423     | 2919     |
| 2020-04-27     | 2414     | 2931     |
| 2020-04-28     | 2402     | 2942     |










### Optimized SIR parameters

```
N = 2994.144636930857
beta = 0.2252669434598542
gamma = 0.00899172120277862
delta = 0.7287707865648888
delay = 9
```

* `delta` stands for a factor of reduction of `beta` during the lockdown.
* All results are available in the folders `images` and `data`.

-----

## Last data information

### Colombian total cases

![total](https://github.com/agastalver/sir-covid-19-colombia/raw/master/images/generated-total.png "Total cases")

-----

## Methodology

### Data sources

Main data source:

* Colombian government: http://www.ins.gov.co/Noticias/Paginas/Coronavirus.aspx
  * https://e.infogram.com/api/live/flex/bc384047-e71c-47d9-b606-1eb6a29962e3/523ca417-2781-47f0-87e8-1ccc2d5c2839

### Epidemiology model

This is based on the SIR epidemiology model proposed by W. O. Kermack and A. G. McKendrick in:

```
Kermack, W. O.; McKendrick, A. G. (1927). "A Contribution to the Mathematical Theory of Epidemics". Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences. 115 (772): 700. Bibcode:1927RSPSA.115..700K. doi:10.1098/rspa.1927.0118. JSTOR 94815.
```

You can find the description on wikipedia: https://en.wikipedia.org/wiki/Mathematical_modelling_of_infectious_disease#The_SIR_model

### Optimization

The parameters `N`, `beta`, and `gamma`, are unknown. Additionally, a `delay` parameter is considered; defined as a time synchronization parameter in case the available data is not adjusted to day 0.

The optimization method is Nendel-Mead, adjusting mean squares on `I(t)` and `R(t)` to the available data. `S(t)` and `N` are calculated backwards.

```
Nelder, John A.; R. Mead (1965). "A simplex method for function minimization". Computer Journal. 7 (4): 308–313. doi:10.1093/comjnl/7.4.308.
```

## Usage

Execute:

```
$ python main.py
```

## Important note

The mathematical model could not adjust to the real behaviour of the virus. Furthermore, the data can have errors, delays, or be incomplete, so the adjustment can vary in the future.
