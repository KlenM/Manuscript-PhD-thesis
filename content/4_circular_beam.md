# Beam based model with moment matching
## Introduction

In ^[sec:validation] we demonstrated that the beam based models like beam wandering model and elliptical beam model exhibit misspecification bias. 
This bias affects the first two moments of the transmittance distribution, $\langle \eta \rangle$ and $\langle \eta^2 \rangle$. 
As a consequence, these models show poor agreement with the numerical simulations. 
Since many quantum protocols in turbulent atmosphere, including those analysed in ^[sec:validation], rely directly on the transmittance moments, this bias propagates into degraded protocol performance.

This problem arise because the models are parametrised through statistical moments of beam shape variables rather than through moments of the transmittance itself. 
The mapping from beam shape statistics to transmittance moments is nonlinear and model dependent. 
As a result, fixing beam parameters does not guarantee correct transmittance moments. 
In this section we address this problem by introducing a beam shape model augmented with a moment matching procedure. 
The goal is to enforce agreement with the transmittance moments while maintaining a physically interpretable model description.

Beam based models are specified in terms of low order statistics of the beam shape. 
These statistics are summarised in ^[tab:beamshapestats]. 
They include the mean and variance of the beam centroid position and the mean and variance of an effective beam size parameter $S$.

|                   |        in average         |       variability       |
| :---------------- | :-----------------------: | :---------------------: |
| **beam position** | $\langle x_0 \rangle = 0$ | $\langle x^2_0 \rangle$ |
| **beam size**     |    $\langle S \rangle$    |  $\langle S^2 \rangle$  |

The beam wandering model $\mathcal{P}_\text{BW}(\eta \mid \langle x_0^2 \rangle, \langle S \rangle)$ is a two parameter model. 
It assumes a circular beam with fixed size $\langle S \rangle$ and neglects beam size fluctuations $\langle S^2 \rangle$.
The elliptical beam model extends this description to four parameters. 
Additionally  to the beam position variability $\langle x^2_0 \rangle$ it accounts for fluctuations of the beam semiaxes $W_{1,2}$^[sec:semiaxes] and their correlations. 
While the beam wandering model admits a fully analytical expression for the probability distribution of transmittance, the elliptical beam model requires Monte Carlo sampling to evaluate the PDT.

The complexity of the elliptical beam model makes a direct reparametrisation in terms of transmittance moments impractical.
In addition, the number of model parameters would require more than two transmittance moments for a physically meaningful reparametrisation.
For this reason, we consider an intermediate case with three effective parameters. 
This model bridges the beam wandering and elliptical beam descriptions. 
It remains analytically tractable while incorporating beam size variability. 
We further introduce a moment matching procedure that enforces agreement with selected transmittance moments.

Even though the proposed approach does not explicitly model beam ellipticity, which enters at higher order in the beam shape description, it enforces consistency with low order transmittance moments. 
As a result of transmittance matching, the effective beam size moments $\langle S \rangle$ and $\langle S^2 \rangle$ become biased. 
They absorb contributions from higher order beam deformations and scintillation effects that are not explicitly included. 
This model remains simple and analytically tractable, and is shown to improve protocol performance.


## The model

This is the conditional distribution..  It describes the probability of transmittance given a specific, fixed beam size $S$.

To account for the variability of the beam spot size $S$ in a turbulent medium, the static Beam Wandering model is generalized by treating $S$ as a stochastic variable. 
The resulting global probability density $\mathcal{P}(\eta)$ is obtained by marginalizing over the fluctuations of $S$ ~~"like" the law of total probability~~ obtainingn in the result the compound probability distribution
$$\mathcal{P}\!\left(\,\eta\mid\langle x^2_0 \rangle,\langle \eta \rangle,\langle \eta^2 \rangle\right)=\int_{0}^\infty dS \,\mathcal{P}_\text{BW}\!\left(\,\eta\mid\langle x^2_0 \rangle,S\right) P(S\mid\mu,\sigma)$$
where $P(S\mid\mu,\sigma)$ is the pdf of the beam width $S$, defined as the log-normal
$$P(S\mid\mu,\sigma)=\frac{1}{S\sigma\sqrt{2\pi}}\exp{-\frac{\left(\ln{S}-\mu\right)^2}{2\sigma^2}},
$$
it depends on $\mu=\mu(\langle \eta \rangle,\langle \eta^2 \rangle)$ and $\sigma=\sigma(\langle \eta \rangle,\langle \eta^2 \rangle)$. In ^[sec:beamshape] we show the existing correlation between $S$ and $x_0$, but it's small for weak and moderate turbulnce, so here assume not correlated. 

- Lognormal validation..

Calculting the first two moment of the ^[eq:acb] we found the implicit definition for the parameters $\mu$ and $\sigma$
$$
\begin{cases} 
\langle \eta \rangle &= \int_0^\infty \mathrm{d}S \, P(S\mid\mu,\sigma) \, \langle \eta \rangle_{\mathrm{BW}} \\ 
\langle \eta^2 \rangle &= \int_0^\infty \mathrm{d}S \, P(S\mid\mu,\sigma) \, \langle \eta^2 \rangle_{\mathrm{BW}} 
\end{cases}
$$
where $\langle \eta^2 \rangle$ and $\langle \eta^2 \rangle$ are the first moment of the Beam wandering model which was found in ^[@esposito]
$$\langle \eta \rangle_{\mathrm{BW}} = 1 - \exp\left(-2\frac{a^2}{4\langle x_0^2 \rangle + S}\right)$$

$$
\begin{split}
\langle \eta^2 \rangle_{\mathrm{BW}} &= 1 - 2 \exp\left(-2\frac{a^2}{4\langle x_0^2 \rangle + S}\right) + \\ 
&\exp\left(-\frac{\alpha^2}{2}\right) \left[1 - Q\left(\frac{\alpha}{\sqrt{1-\beta^2}}, \frac{\alpha \beta}{\sqrt{1-\beta^2}}\right) + Q\left(\frac{\alpha \beta}{\sqrt{1-\beta^2}}, \frac{\alpha}{\sqrt{1-\beta^2}}\right)\right]
\end{split}
$$

where:
$$\alpha = \frac{2a}{\sqrt{S}} \left[\frac{2 p(p+1)}{2 p^2+3 p+1}\right]^{1/2}$$
$$\beta = (2p+1)^{-1}, \quad p = \frac{1}{8}\frac{S}{\langle x_0^2 \rangle}$$

and $Q$ is the Marcum Q-function of order 1. 
They can be calculated numerically using any optimization algorithm, starting from the initial point $\mu_0 = \ln\left(\frac{\langle S \rangle^2}{\sqrt{\langle S^2 \rangle}}\right), \sigma^2_0 = \ln\left(\frac{\langle S^2 \rangle}{\langle S \rangle^2}\right)$ if $\langle S \rangle$ and $\langle S^2 \rangle$ are known.
* To deal with the infinite upper limit of the integral, we can truncate the tail at the point $S_{\mathrm{max}}$, where $P(S > S_{\mathrm{max}}) < \delta$. This point can be found using the Percentage Point Function (also known as the inverse CDF) of the log-normal distribution as $S_{\mathrm{max}} = \mathrm{PPF}(1 - \delta)$.

## Validation
- show my own that first plots - KS values as in validation section of CBm, BWm, EB, ..

## Conclusion

