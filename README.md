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
| 2020-04-20     | 2892     | 3684     |
| 2020-04-21     | 2932     | 3778     |
| 2020-04-22     | 2963     | 3862     |
| 2020-04-23     | 2986     | 3939     |
| 2020-04-24     | 3001     | 4009     |
| 2020-04-25     | 3009     | 4072     |
| 2020-04-26     | 3010     | 4128     |
| 2020-04-27     | 3029     | 4202     |
| **2020-04-28** | **3037** | **4265** |
| 2020-04-29     | 3036     | 4319     |
| 2020-04-30     | 3026     | 4365     |
| 2020-05-01     | 3010     | 4403     |
| 2020-05-02     | 2988     | 4436     |
| 2020-05-03     | 2961     | 4463     |
| 2020-05-04     | 2930     | 4486     |
| 2020-05-05     | 2897     | 4506     |
| 2020-05-06     | 2861     | 4522     |
| 2020-05-07     | 2823     | 4536     |
| 2020-05-08     | 2784     | 4548     |
| 2020-05-09     | 2744     | 4558     |
| 2020-05-10     | 2703     | 4567     |

### Optimized SIR parameters

```
N = 4621.329993585541
beta = 0.24694254318890543
gamma = 0.018042359977681475
delta = 0.6671333420255441
delay = 7
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
  * https://e.infogram.com/api/live/flex/4524241a-91a7-4bbd-a58e-63c12fb2952f/302a0531-1ec8-4444-aa4f-f8cfd1d6492d

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
