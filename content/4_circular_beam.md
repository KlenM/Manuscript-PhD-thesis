# Beam-based model with moment matching
## Introduction {#sec:intro_mm}

In ^[sec:validation] we demonstrated that the beam-based models like beam wandering model and elliptical beam model exhibit misspecification bias.
This bias affects the first two moments of the transmittance distribution, $\langle \eta \rangle$ and $\langle \eta^2 \rangle$.
As a consequence, these models show poor agreement with the numerical simulations.
Since many quantum protocols in turbulent atmosphere, including those that will be analysed in ^[sec:application], rely directly on the transmittance moments, this bias propagates into degraded protocol performance.

This problem arise because the models are parameterized through statistical moments of beam shape variables rather than through moments of the transmittance itself.
The mapping from beam shape statistics to transmittance moments is nonlinear and model dependent.
As a result, fixing beam parameters does not guarantee correct transmittance moments.
In this section we address this problem by introducing a beam shape model augmented with a moment matching procedure.
The goal is to enforce agreement with the transmittance moments while maintaining a physically interpretable model description.

Beam-based models are specified in terms of low order statistics of the beam shape.
These statistics are summarised in ^[tab:beamshapestats].
They include the mean and variance of the beam centroid position and the mean and variance of an effective beam size parameter $S$.

```{=latex}
\begin{table}[h!]
\centering
\caption{Summary of beam shape statistics used for beam-shape based models parameterization.}
\label{tab:beamshapestats}
\begin{tabular}{l c c}
\hline
                   & {in average}      & {variability}   \\
\hline
{beam position} & $\langle x_0 \rangle = 0$ & $\langle x_0^2 \rangle$ \\
{beam size}     & $\langle S \rangle$       & $\langle S^2 \rangle$   \\
\hline
\end{tabular}
\end{table}
```

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
Numerical simulations further show that its empirical distribution is well approximated by a log normal distribution for all considered in ^[sec:validation] channels.
This observation aligns with the treatment of turbulence-induced distortions as multiplicative, which often leads to log normal statistics.
Therefore the beam size distribution is chosen as
$$P(S\mid\mu,\sigma)=\frac{1}{S\sigma\sqrt{2\pi}}\exp\left[{-\frac{\left(\ln{S}-\mu\right)^2}{2\sigma^2}}\right],
$$

^[fig:lognormvalid] illustrates this agreement for a channel of moderate turbulence with $F_0 = z_\mathrm{ap}$, which represents the worst-case scenario among all channels.
The channel of strong turbulence exhibits slightly better but similar agreement, while weak turbulence channels show much better correspondence.
This agreement supports the use of the log-normal approximation for the beam size distribution across different turbulence regimes.

![\label{fig:lognormvalid}Verification of the log-normal approximation for the effective beam size $S$. The plot compares the empirical probability density function obtained from $5\cdot10^5$ numerical beam-propagation simulations (blue histogram) against a fitted log-normal distribution (dashed line). The data corresponds to a moderate turbulence channel with a focused beam ($F_0 = z_\mathrm{ap}$), representing the regime with the worst-case scenario.](moment_matching/MM_Spdf.pdf)

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

As derived in ^[@esposito1967], these moments of the beam wandering model take the form
$$\langle \eta \rangle_{\mathrm{BW}} = 1 - \exp\left(-2\frac{a^2}{4\langle x_0^2 \rangle + S}\right)$$
$$
\begin{split}
\langle \eta^2 \rangle_{\mathrm{BW}} &= 1 - 2 \exp\left(-2\frac{a^2}{4\langle x_0^2 \rangle + S}\right) + \\
&\exp\left(-\frac{\alpha^2}{2}\right) \left[1 - Q\left(\frac{\alpha}{\sqrt{1-\beta^2}}, \frac{\alpha \beta}{\sqrt{1-\beta^2}}\right) + Q\left(\frac{\alpha \beta}{\sqrt{1-\beta^2}}, \frac{\alpha}{\sqrt{1-\beta^2}}\right)\right]
\end{split}
$$
where the function $Q$ denotes the Marcum $Q$ function of order one ^[@marcum1960], and the auxiliary parameters are defined as
$$\alpha = \frac{2a}{\sqrt{S}} \left[\frac{2 p(p+1)}{2 p^2+3 p+1}\right]^{1/2}$$
$$\beta = (2p+1)^{-1}, \quad p = \frac{1}{8}\frac{S}{\langle x_0^2 \rangle}$$

Because the resulting system of equations have no closed form solution exists, the parameters $\mu$ and $\sigma$ are obtained numerically.
When estimates of $\langle S\rangle$ and $\langle S^2\rangle$ are available they provide a convenient initial guess
$$
\mu_0 = \ln\left(\frac{\langle S \rangle^2}{\sqrt{\langle S^2 \rangle}}\right), \quad \sigma^2_0 = \ln\left(\frac{\langle S^2 \rangle}{\langle S \rangle^2}\right)$$
After determining the parameters $\mu$ and $\sigma$, the PDT is evaluated by numerical integration over the beam size variable $S$.

Finally the infinite support of the log normal distribution requires truncation for numerical implementation.
The upper limit is chosen as $S_{\mathrm{max}}$ such that the tail probability satisfies $P(S>S_{\mathrm{max}})<\delta$.
This cutoff is obtained from the percentage point function (PPF) of the log normal distribution as $S_{\mathrm{max}} = \mathrm{PPF}(1 - \delta)$.
This truncation bounds the neglected probability mass and has negligible impact on the evaluated transmittance moments.

## Validation

We apply the same validation procedure as in ^[sec:validation].
We compare the proposed model with beam-based models and with other well performing models.
The comparison is based on the Kolmogorov-Smirnov statistic^[sec:validation] between numerically obtained PDT and the analytical models.
The results are summarized in ^[fig:acbks].

![\label{fig:acbks}Kolmogorov-Smirnov (KS) statistic comparing the proposed beam-based model with moment matching (C) against the beam wandering (W), elliptical beam (E), total probability (T) and Beta distribution (B) models. The left panel shows the weak turbulence channel with focused beams ($F_0 = z_\text{ap}$), where the proposed model achieves the lowest overall error in the region of small apertures. The right panel displays the strong turbulence regime, where the proposed model significantly outperforms other physical models despite the Beta distribution providing a closer fit.](moment_matching/MM_ks_values.pdf)

The left part of ^[fig:acbks] corresponds to the channel with weak turbulence and $F_0 = z_\text{ap}$.
This case yields the best overall performance of the proposed model.
The improvement over beam shape based models is pronounced, in particular for small aperture radii compared to the beam size $W_\text{LT}$.
Moreover, in this region the proposed model yields the smallest KS statistic among all considered analytical models.
An explicit example of PDT for $R_\text{ap} = 0.45~\text{cm}$ is shown in ^[fig:acbpdt].

![\label{fig:acbpdt}Comparison of the PDT for a weak turbulence channel ($F_0 = z_\text{ap}$) at an aperture radius $R_\text{ap} = 0.45$ cm. While the Beta distribution (B) is constrained by the same first two moments as the proposed model, it fails to capture the precise shape of the distribution. In contrast, the beam-based model with the moment-matching technique (C) provides best agreement with the numerical simulations (N). Traditional beam-based models, such as beam wandering (W) and the elliptical beam model (E), show completely mismatched PDTs due to misspecification bias.](moment_matching/MM_weak_zap_pdt_0_0045.pdf)

We see that the beta distribution model deviates in shape from the numerically simulated distribution, despite being defined through the same first moments of the transmittance.
The beam-based model with moment matching shows an almost perfect agreement in this specific case, since the skewness, given by the third moment of the transmittance, as well as the kurtosis are reproduced more accurately.

For apertures large compared to the beam size, the agreement of the proposed model is reduced.
A distinct discrepancy appears near the local minimum of the elliptical beam transmittance at $R_\text{ap}/W_\text{LT} \approx 1.2$.
At this point the elliptical beam model outperforms the proposed model, since its transmittance mode coincides with the mode of the numerically obtained distribution.
Mode matching could in principle improve the agreement of the proposed model.
However, such approach is not practical because the transmittance mode cannot be reliably estimated in experiments and no closed analytical expression for transmittance mode is available.

The right panel of ^[fig:acbks] shows the results for the strong turbulence channel, which exhibits the largest overall deviations.
In this case the beta distribution model provides better agreement over the full aperture range.
The proposed model still significantly outperforms the other physically motivated models.
Channels with weak turbulence and $F_0 = \infty$ and with moderate turbulence and $F_0 = \infty$ show similar behavior with slightly better performance.
The channel with moderate turbulence and $F_0 = z_\text{ap}$ yields intermediate results between these two extremes.

## Conclusion {#sec:conclusion_mm}

We introduced a physically motivated PDT model complemented by transmittance moment matching.
While the model provides an intermediate approximation of the beam shape between the beam wandering and elliptical beam approaches, its first two moments of the transmittance are imposed by design.
This removes the misspecification bias observed in the beam-based models and directly targets the quantities relevant for quantum protocol performance.

The model relies on two structural assumptions.
First, we assume that fluctuations of the beam centroid $x_0$ and of the beam spot size $S$ occur on distinct spatial scales of turbulence, allowing them to be treated as statistically independent.
As shown in ^[sec:beamshape], small correlations between $x_0$ and $S$ exist but remain negligible for weak and moderate turbulence.
Second, beam ellipticity and higher-order deformations are not modeled explicitly.
Their contributions are absorbed into effective beam size fluctuations through moment matching.
Consequently, the inferred moments of $S$ lose a direct physical interpretation but achieve consistency at the level of transmittance statistics.

Validation against numerical simulations demonstrates a substantial improvement over existing physically motivated models across most channels.
In the weak turbulence regime with $F_0=z_\text{ap}$ and small apertures, the model outperforms all existing analytical approaches.
More generally, performance is better for $F_0=z_\text{ap}$ compared to $F_0=z_\infty$ and for aperture radii smaller than the average beam size.

Validation was performed using the first two transmittance moments, $\langle \eta \rangle$ and $\langle \eta^2 \rangle$, obtained directly from simulations.
When analytical approximations of these moments are used, or when experimental noise and systematic errors affect their estimation, the model’s performance can degrade.
This limitation motivates further work on improved analytical expressions for low-order transmittance moments.

Overall, the model provides a robust physically grounded description of PDT.
It requires only simple numerical integration and parameter optimization, resulting in substantially lower computational cost than the full phase screen simulations.
Furthermore, it defines PDT in terms of measurable quantities at the aperture plane, such as beam wandering $\langle x_0 \rangle$ and the first two transmittance moments $\langle \eta \rangle$ and $\langle \eta^2 \rangle$, whereas the phase screen method requires detailed turbulence profiles.
These features make it suitable for practical applications in quantum communication.
