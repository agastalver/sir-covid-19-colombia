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
| 2020-04-13     | 2531     | 2852     |
| 2020-04-14     | 2711     | 3065     |
| 2020-04-15     | 2892     | 3282     |
| 2020-04-16     | 3073     | 3501     |
| 2020-04-17     | 3254     | 3721     |
| 2020-04-18     | 3431     | 3941     |
| 2020-04-19     | 3604     | 4158     |
| 2020-04-20     | 3771     | 4372     |
| 2020-04-21     | 3931     | 4581     |
| 2020-04-22     | 4083     | 4784     |
| 2020-04-23     | 4226     | 4979     |
| 2020-04-24     | 4359     | 5167     |
| 2020-04-25     | 4482     | 5346     |
| 2020-04-26     | 4594     | 5515     |
| 2020-04-27     | 4813     | 5793     |
| 2020-04-28     | 5000     | 6042     |
| 2020-04-29     | 5156     | 6263     |
| 2020-04-30     | 5283     | 6456     |
| 2020-05-01     | 5382     | 6623     |
| 2020-05-02     | 5457     | 6766     |
| 2020-05-03     | 5510     | 6888     |
| 2020-05-04     | 5543     | 6991     |
| 2020-05-05     | 5560     | 7079     |
| **2020-05-06** | **5563** | **7152** |
| 2020-05-07     | 5554     | 7213     |
| 2020-05-08     | 5536     | 7265     |

### Optimized SIR parameters

```
N = 7536.130858731971
beta = 0.234843685449866
gamma = 0.01253337096113215
delta = 0.5638500223715831
delay = 8
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
