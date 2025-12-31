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
The PDT of the proposed model is defined as a compound distribution that extends the beam wandering model by treating the beam size $S$ as a random variable:
$$
%\label{eq:acbpdt}
\mathcal{P}\!\left(\,\eta\mid\langle x^2_0 \rangle,\langle \eta \rangle,\langle \eta^2 \rangle\right)=\int_{0}^\infty dS \,\mathcal{P}_\text{BW}\!\left(\,\eta\mid\langle x^2_0 \rangle,S\right) P(S\mid\mu,\sigma)$$
The fluctuations of the beam size $S$ are incorporated through the distribution $P(S\mid\mu,\sigma)$. 
Its parameters  $\mu=\mu(\langle \eta \rangle,\langle \eta^2 \rangle)$ and $\sigma=\sigma(\langle \eta \rangle,\langle \eta^2 \rangle)$ are fixed by enforcing the prescribed moments $\langle\eta\rangle$ and $\langle\eta^2\rangle$.
As a result the transmittance statistics account simultaneously for beam displacement and beam deformation and specified by the second moment of beam displacement $\langle x_0^2\rangle$ and the first two moments of the transmittance.

Since the beam size is strictly positive its distribution must have positive support.
Numerical simulations further show that its empirical distribution is well approximated by a log normal distribution for all considered in ^[sec:valid] channels.
This observation aligns with the treatment of turbulence-induced distortions as multiplicative, which often leads to log normal statistics.
Therefore the beam size distribution is chosen as
$$P(S\mid\mu,\sigma)=\frac{1}{S\sigma\sqrt{2\pi}}\exp\left[{-\frac{\left(\ln{S}-\mu\right)^2}{2\sigma^2}}\right],
$$

Figure ^[fig:lognormvalid] illustrates this agreement for a channel of moderate turbulence with $F_0 = z_\mathrm{ap}$. 
![[lognormvalidS.png|200]]
Channels with strong turbulence exhibit similar agreement, while weak turbulence channels show even better correspondence.
This agreement supports the use of the log-normal approximation for the beam size distribution across different turbulence regimes.

In principle the parameters $\mu$ and $\sigma$ could be inferred from the moments $\langle S\rangle$ and $\langle S^2\rangle$.
However this choice leads to biased transmittance moments, as discussed above.
Instead the present model applies transmittance moment matching.
The parameters $\mu$ and $\sigma$ are therefore defined implicitly by computing the first two transmittance moments of the model^[eq:acbpdt], which yields
$$
\begin{cases} 
\langle \eta \rangle &= \int_0^\infty \mathrm{d}S \, P(S\mid\mu,\sigma) \, \langle \eta \rangle_{\mathrm{BW}} \\ 
\langle \eta^2 \rangle &= \int_0^\infty \mathrm{d}S \, P(S\mid\mu,\sigma) \, \langle \eta^2 \rangle_{\mathrm{BW}} 
\end{cases}
$$
Here $\langle\eta\rangle_{\mathrm{BW}}$ and $\langle\eta^2\rangle_{\mathrm{BW}}$ denote the moments of the beam wandering model evaluated at fixed $S$.

As derived in ^[@esposito], these moments of the beam wandering model take the form
$$\langle \eta \rangle_{\mathrm{BW}} = 1 - \exp\left(-2\frac{a^2}{4\langle x_0^2 \rangle + S}\right)$$
$$
\begin{split}
\langle \eta^2 \rangle_{\mathrm{BW}} &= 1 - 2 \exp\left(-2\frac{a^2}{4\langle x_0^2 \rangle + S}\right) + \\ 
&\exp\left(-\frac{\alpha^2}{2}\right) \left[1 - Q\left(\frac{\alpha}{\sqrt{1-\beta^2}}, \frac{\alpha \beta}{\sqrt{1-\beta^2}}\right) + Q\left(\frac{\alpha \beta}{\sqrt{1-\beta^2}}, \frac{\alpha}{\sqrt{1-\beta^2}}\right)\right]
\end{split}
$$
where the function $Q$ denotes the Marcum $Q$ function of order one ^[@Qfunc], and the auxiliary parameters are defined as
$$\alpha = \frac{2a}{\sqrt{S}} \left[\frac{2 p(p+1)}{2 p^2+3 p+1}\right]^{1/2}$$
$$\beta = (2p+1)^{-1}, \quad p = \frac{1}{8}\frac{S}{\langle x_0^2 \rangle}$$

Because the resulting system of equations have no closed form solution exists, the parameters $\mu$ and $\sigma$ are obtained numerically. 
When estimates of $\langle S\rangle$ and $\langle S^2\rangle$ are available they provide a convenient initial guess
$$
\mu_0 = \ln\left(\frac{\langle S \rangle^2}{\sqrt{\langle S^2 \rangle}}\right), \quad \sigma^2_0 = \ln\left(\frac{\langle S^2 \rangle}{\langle S \rangle^2}\right)$$
After determining the parameters $\mu$ and $\sigma$, the PDT ^[acbpdt] is evaluated by numerical integration over the beam size variable $S$.

Finally the infinite support of the log normal distribution requires truncation for numerical implementation. 
The upper limit is chosen as $S_{\mathrm{max}}$ such that the tail probability satisfies $P(S>S_{\mathrm{max}})<\delta$. 
This cutoff is obtained from the percentage point function of the log normal distribution as $S_{\mathrm{max}} = \mathrm{PPF}(1 - \delta)$.
This truncation bounds the neglected probability mass and has negligible impact on the evaluated transmittance moments.

## Validation
- we conduct the same procedure as in the ^[sec:validation] section and compare the proposed model with the beam-based models and overal best identified beta distribution model.
- ^[fig:acbks] shows the KS-statistic distance between numerically obtained PDT and the analytical models
- ![[acbks.png|500]]
- left image shows the case of best performance of the proposed model which coresponds to the channel of weak turbulence $F_0=z_\text{ap}$.
    - the proposed modes shows drastic improvement comparing to beam-shape models and the best performance among all existing analyt models in the region of small apertures.
    - In the ^[fig:acbpdt] the example of the PDT for the $R_\text{ap}=0.4~\text{cm}$ is shown.
    - ![[acbpdt.png|250]]
    - We see that the Beta distribution model despite as well beign defined through the first moments of trasmittance has different shape that numerically simulated PDT.
    - The beam-based model with moments matching on the other hand has almost perfect match in this case.
    - In the region of large apertures compared to the beam size, the performance of the proposed model is generally decreased.
        - At the point of local minima of the elliptical beam ($R_\text{ap}/W_\text{LT}\approx1.2$), the proposed model shows worse agreement.
        - At this point, the mode of the elliptical beam model PDT concidance with the mode of the numerically simulated PDT.
        - While the mode matching could in principle show better agreement compared to the moments matchin, it wouldn't be practical to estimate PDT mode in experiment as well .. no analyt expreesions for the transmittance mode.
- right image shows the worst case among channels.
    - Beta model shows better performance across all apertures range.
    - But the proposed model in general significally outperforms the other physical based models. 
    - The other considered channels of weak turbulence with $F_0=\infty$ and moderate turbulence with $F_0=\infty$ shows the similar result.
    - the channel of moderate turbulence with $F_0=z_\text{ap}$ shows intermediate results

## Conclusion

- In ^[sec:beamshape] we show the existing correlation between $S$ and $x_0$, but it's small for weak and moderate turbulnce, so here assume not correlated. 
- We assume the fluctuations of the beam center (wandering) and the fluctuations of the beam spot size (broadening) occur on different spatial scales of turbulence, allowing us to treat $x_0$ and $S$ as statistically independent variables.

- here we assumed maximally good estimated parameters of eta. Noises in experimental measurements or mistakes in analytical approximations can result is worse performance.
    - further study and  improvements for mean eta

- split-step complex and requires huge computation and requires Cn2, this model quick, can be defined from eta, eta2, x0, which can be estimated from mesurements of the beam at aperture plane. 
- From other side it much accurate that other physically based models.