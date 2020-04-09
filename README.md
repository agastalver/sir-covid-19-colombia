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
| 2020-04-09     | 1832     | 2001     |
| 2020-04-10     | 1986     | 2174     |
| 2020-04-11     | 2146     | 2355     |
| 2020-04-12     | 2310     | 2542     |
| 2020-04-13     | 2478     | 2734     |
| 2020-04-14     | 2793     | 3075     |
| 2020-04-15     | 3112     | 3424     |
| 2020-04-16     | 3427     | 3773     |
| 2020-04-17     | 3731     | 4113     |
| 2020-04-18     | 4016     | 4438     |
| 2020-04-19     | 4279     | 4742     |
| 2020-04-20     | 4514     | 5021     |
| 2020-04-21     | 4719     | 5274     |
| 2020-04-22     | 4895     | 5499     |
| 2020-04-23     | 5042     | 5696     |
| 2020-04-24     | 5161     | 5867     |
| 2020-04-25     | 5255     | 6013     |
| 2020-04-26     | 5327     | 6139     |
| 2020-04-27     | 5378     | 6245     |
| 2020-04-28     | 5413     | 6334     |
| 2020-04-29     | 5433     | 6409     |
| **2020-04-30** | **5440** | **6471** |
| 2020-05-01     | 5437     | 6523     |
| 2020-05-02     | 5426     | 6567     |
| 2020-05-03     | 5407     | 6603     |
| 2020-05-04     | 5382     | 6633     |
| 2020-05-05     | 5353     | 6658     |
| 2020-05-06     | 5319     | 6679     |
| 2020-05-07     | 5283     | 6696     |
| 2020-05-08     | 5244     | 6710     |

### Optimized SIR parameters

```
N = 6785.267204925339
beta = 0.22480717411213783
gamma = 0.010035642658845847
delta = 0.5778050657773215
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
