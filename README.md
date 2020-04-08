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
| 2020-04-08     | 1629     | 1774     |
| 2020-04-09     | 1731     | 1892     |
| 2020-04-10     | 1828     | 2007     |
| 2020-04-11     | 1920     | 2117     |
| 2020-04-12     | 2006     | 2221     |
| 2020-04-13     | 2085     | 2320     |
| 2020-04-14     | 2191     | 2446     |
| 2020-04-15     | 2283     | 2560     |
| 2020-04-16     | 2361     | 2660     |
| 2020-04-17     | 2425     | 2748     |
| 2020-04-18     | 2477     | 2823     |
| 2020-04-19     | 2518     | 2888     |
| 2020-04-20     | 2548     | 2943     |
| 2020-04-21     | 2570     | 2989     |
| 2020-04-22     | 2584     | 3028     |
| 2020-04-23     | 2591     | 3061     |
| **2020-04-24** | **2594** | **3088** |
| 2020-04-25     | 2591     | 3110     |
| 2020-04-26     | 2585     | 3129     |
| 2020-04-27     | 2576     | 3145     |
| 2020-04-28     | 2564     | 3158     |

### Optimized SIR parameters

```
N = 3223.6095079244647
beta = 0.22526423570778623
gamma = 0.00953987398124003
delta = 0.7169503451863574
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
