# Moment matching for the Circular-beam model
## Introduction {#sec:intro_mm}

In ^[sec:validation], we demonstrated that models based on statistics of beam parameters, such as the beam-wandering model and the elliptical-beam model, exhibit misspecification bias.
This bias affects the first two moments of the transmittance distribution, $\langle \eta \rangle$ and $\langle \eta^2 \rangle$.
As a consequence, these models show poor agreement with numerical simulations.
Since many quantum protocols in turbulent atmospheres, including those that will be analysed in ^[sec:application], rely directly on the transmittance moments, this bias leads to degraded protocol performance.

In this section, we address this problem by introducing a moment matching procedure for such models.
The goal is to enforce agreement with the transmittance moments while maintaining a physically interpretable model description.
Physically based models are specified in terms of low-order statistics of the beam shape, which are summarised in ^[tab:beamshapestats].
These include the mean and variance of the beam centroid position and the mean and variance of an effective beam size parameter $S$.

```{=latex}
\begin{table}[h!]
\centering
\caption{Summary of beam shape statistics used for physically based model parameterisation.}
\label{tab:beamshapestats}
\begin{tabular}{l c c}
\hline
                   & {on average}      & {variability}   \\
\hline
{beam position} & $\langle x_0 \rangle = 0$ & $\langle x_0^2 \rangle$ \\
{beam size}     & $\langle S \rangle$       & $\langle S^2 \rangle$   \\
\hline
\end{tabular}
\end{table}
```

The beam-wandering model $\mathcal{P}_\mathrm{BW}(\eta \mid \langle x_0^2 \rangle, \langle S \rangle)$ is a two-parameter model.
It assumes a circular beam with fixed size $\langle S \rangle$ and neglects beam size fluctuations $\langle S^2 \rangle$.
The elliptical-beam model extends this description to four parameters.
In addition to the beam position variability $\langle x^2_0 \rangle$, it accounts for fluctuations of the beam semiaxes $W_{1,2}$ (see ^[sec:semiaxes]) and their correlations.
While the beam-wandering model admits a fully analytical expression for the PDT, the elliptical-beam model requires Monte Carlo sampling to evaluate the PDT.

The complexity of the elliptical-beam model makes a direct reparametrisation in terms of transmittance moments impractical.
In addition, the number of model parameters would require more than two transmittance moments for a physically meaningful reparametrisation.
For this reason, we consider an intermediate case with three effective parameters, referred to as the Circular-beam model \ref{mypaper3}.
This model bridges the beam-wandering and elliptical-beam descriptions.
It remains analytically tractable while incorporating beam size variability.
We further introduce a moment matching procedure that enforces agreement with selected transmittance moments.

Even though the proposed approach does not explicitly model beam ellipticity, which enters at higher order in the beam shape description, it enforces consistency with low-order transmittance moments.
As a result of transmittance matching, the effective beam size moments $\langle S \rangle$ and $\langle S^2 \rangle$ become biased.
They absorb contributions from higher-order beam deformations and scintillation effects that are not explicitly included.
This approach remains simple and analytically tractable, and it is shown to improve protocol performance.

## The model
The PDT of the Circular-beam model is defined as a compound distribution that extends the beam-wandering model by treating the beam size $S$ as a random variable
$$
%\label{eq:acbpdt}
\mathcal{P}\!\left(\,\eta\mid\langle x^2_0 \rangle,\langle \eta \rangle,\langle \eta^2 \rangle\right)=\int_0^\infty dS \,\mathcal{P}_\mathrm{BW}\!\left(\,\eta\mid\langle x^2_0 \rangle,S\right) P(S\mid\mu,\sigma).$$
The fluctuations of the beam size $S$ are incorporated through the distribution ${P(S\mid\mu,\sigma)}$.
Its parameters $\mu=\mu(\langle \eta \rangle,\langle \eta^2 \rangle)$ and $\sigma=\sigma(\langle \eta \rangle,\langle \eta^2 \rangle)$ are fixed by enforcing the prescribed moments $\langle\eta\rangle$ and $\langle\eta^2\rangle$.
As a result, the transmittance statistics simultaneously account for beam displacement and beam deformation, and are specified by the second moment of beam displacement $\langle x_0^2\rangle$ and the first two moments of the transmittance.

Since the beam size is strictly positive, its distribution must have positive support.
Numerical simulations further show that its empirical distribution is well approximated by a lognormal distribution for all considered channels in ^[sec:validation].
This observation aligns with the treatment of turbulence-induced distortions as multiplicative, which often leads to lognormal statistics.
Therefore, the beam size distribution is chosen as
$$P(S\mid\mu,\sigma)=\frac{1}{S\sigma\sqrt{2\pi}}\exp\left[{-\frac{\left(\ln{S}-\mu\right)^2}{2\sigma^2}}\right].
$$
\Cref{fig:lognormvalid} illustrates this agreement for a channel of moderate turbulence with $F_0 = z_\mathrm{ap}$, which represents the worst-case scenario among all channels.
The strong-turbulence channel exhibits slightly better but similar agreement, while weak-turbulence channels show much better correspondence.
This agreement supports the use of the lognormal approximation for the beam size distribution across different turbulence regimes.

![\label{fig:lognormvalid}Verification of the lognormal approximation for the effective beam size $S$.
The plot compares the empirical probability density function obtained from $5\cdot10^5$ numerical beam-propagation simulations (blue histogram) against a fitted lognormal distribution (dashed line).
The data corresponds to a moderate turbulence channel with a focused beam ($F_0 = z_\mathrm{ap}$), representing the regime with the worst-case scenario.](moment_matching/MM_Spdf.pdf)

In principle, the parameters $\mu$ and $\sigma$ could be inferred from the moments $\langle S\rangle$ and $\langle S^2\rangle$.
However, this choice leads to biased transmittance moments, as discussed above.
Instead, the present approach applies transmittance moment matching to the Circular-beam model.
The parameters $\mu$ and $\sigma$ are therefore defined implicitly by computing the first two transmittance moments of the model (see ^[eq:acbpdt]), which yields
$$
\begin{dcases}
\langle \eta \rangle &= \int_0^\infty \mathrm{d}S \, P(S\mid\mu,\sigma) \, \langle \eta \rangle_{\mathrm{BW}} \\
\langle \eta^2 \rangle &= \int_0^\infty \mathrm{d}S \, P(S\mid\mu,\sigma) \, \langle \eta^2 \rangle_{\mathrm{BW}}.
\end{dcases}
$$
Here $\langle\eta\rangle_{\mathrm{BW}}$ and $\langle\eta^2\rangle_{\mathrm{BW}}$ denote the moments of the beam-wandering model evaluated at fixed $S$.

As derived in ^[@esposito1967], these moments for the beam-wandering model take the form

$$
\begin{split}
\langle \eta \rangle_{\mathrm{BW}} = 1 - \exp\left(-2\frac{a^2}{4\langle x_0^2 \rangle + S}\right)&, \\
\langle \eta^2 \rangle_{\mathrm{BW}} = 1 - 2 \exp\left(-2\frac{a^2}{4\langle x_0^2 \rangle + S}\right)& \\
\quad + \exp\left(-\frac{\alpha^2}{2}\right) \Biggl[ 1 - Q&\left(\frac{\alpha}{\sqrt{1-\beta^2}}, \frac{\alpha \beta}{\sqrt{1-\beta^2}}\right) \\
\quad + Q&\left(\frac{\alpha \beta}{\sqrt{1-\beta^2}}, \frac{\alpha}{\sqrt{1-\beta^2}}\right) \Biggr],
\end{split}
$$
where the function $Q$ denotes the Marcum $Q$ function of order one ^[@marcum1960], and the auxiliary parameters are defined as
$$
\begin{split}
\alpha &= \frac{2a}{\sqrt{S}} \left[\frac{2 p(p+1)}{2 p^2+3 p+1}\right]^{1/2},\\
\beta &= (2p+1)^{-1}, \quad p = \frac{1}{8}\frac{S}{\langle x_0^2 \rangle}.
\end{split}
$$
Because no closed-form solution exists for this system of equations, the parameters $\mu$ and $\sigma$ are obtained numerically.
When estimates of $\langle S\rangle$ and $\langle S^2\rangle$ are available, they provide a convenient initial guess
$$
\mu_0 = \ln\left(\frac{\langle S \rangle^2}{\sqrt{\langle S^2 \rangle}}\right), \quad \sigma^2_0 = \ln\left(\frac{\langle S^2 \rangle}{\langle S \rangle^2}\right).$$
After determining the parameters $\mu$ and $\sigma$, the PDT is evaluated by numerical integration over the beam size variable $S$.

Finally, the infinite support of the lognormal distribution requires truncation for numerical implementation.
The upper limit is chosen as $S_{\mathrm{max}}$ such that the tail probability satisfies $P(S>S_{\mathrm{max}})<\delta$.
This cutoff is obtained from the percentage point function (PPF) of the lognormal distribution as $S_{\mathrm{max}} = \mathrm{PPF}(1 - \delta)$.
This truncation bounds the neglected probability mass and has a negligible impact on the evaluated transmittance moments.

## Validation

We apply the same validation procedure as in ^[sec:validation].
We compare the proposed model against existing physically based models and other well-performing models.
The comparison is based on the Kolmogorov-Smirnov statistic between numerically obtained PDTs and the analytical models.
The results are summarized in ^[fig:acbks].

![\label{fig:acbks}Kolmogorov-Smirnov (KS) statistic comparing the proposed Circular-beam model with moment matching (C) against the beam wandering (W), elliptical beam (E), total probability (T) and Beta distribution (B) models. The left panel shows the weak turbulence channel with focused beams ($F_0 = z_\mathrm{ap}$), where the proposed model achieves the lowest overall error in the region of small apertures. The right panel displays the strong turbulence regime, where the proposed model significantly outperforms other physical models despite the Beta distribution providing a closer fit.](moment_matching/MM_ks_values.pdf)

The left panel of ^[fig:acbks] corresponds to the channel with weak turbulence and $F_0 = z_\mathrm{ap}$.
This case yields the best overall performance for the proposed model.
The improvement over traditional physically based models is pronounced, particularly for small aperture radii compared to the beam size $W_\mathrm{LT}$.
Moreover, in this region, the proposed model yields the smallest KS statistic among all considered analytical models.
An explicit example of the PDT for $R_\mathrm{ap} = 0.45~\text{cm}$ is shown in ^[fig:acbpdt].

![\label{fig:acbpdt}Comparison of the PDT for a weak turbulence channel ($F_0 = z_\mathrm{ap}$) at an aperture radius $R_\mathrm{ap} = 0.45$ cm. While the Beta distribution (B) is constrained by the same first two moments as the proposed model, it fails to capture the precise shape of the distribution. In contrast, the Circular-beam model with the moment-matching technique (C) provides the best agreement with the numerical simulations (N). Traditional physically based models, such as beam wandering (W) and the elliptical-beam model (E), show completely mismatched PDTs due to misspecification bias.](moment_matching/MM_weak_zap_pdt_0_0045.pdf)

We see that the Beta distribution model deviates in shape from the numerically simulated distribution, despite being defined through the same first two moments of transmittance.
The Circular-beam model with moment matching shows almost perfect agreement in this specific case.
This is because the skewness, given by the third moment of the transmittance, and the kurtosis are reproduced more accurately.

For apertures larger than the beam size, the agreement of the proposed model is reduced.
A distinct discrepancy appears near the local minimum of the elliptical-beam model when $R_\mathrm{ap}/W_\mathrm{LT} \approx 1.2$.
At this point, the elliptical-beam model outperforms the proposed model because the statistical mode of its PDT coincides with the mode of the numerically obtained distribution.
Mode matching, instead of moment matching, could in principle improve the agreement of the proposed model.
However, such an approach is not practical because the transmittance mode cannot be reliably estimated in experiments and no closed-form analytical expression for the transmittance mode is available.

The right panel of ^[fig:acbks] shows the results for the strong turbulence channel, which exhibits the largest overall deviations.
In this case, the Beta distribution model provides better agreement over the full aperture range.
However, the Circular-beam model with moment matching still outperforms the other physically motivated models.
Channels with weak turbulence and $F_0 = \infty$ and with moderate turbulence and $F_0 = \infty$ show similar behavior with slightly better performance.
The channel with moderate turbulence and $F_0 = z_\mathrm{ap}$ yields intermediate results.

## Conclusion {#sec:conclusion_mm}

We introduced a physically motivated PDT model complemented by transmittance moment matching.
While the Circular-beam model provides an intermediate approximation of the beam shape between the beam-wandering and elliptical-beam approaches, our moment matching procedure ensures that its first two transmittance moments are imposed by design.
This removes the model misspecification bias observed in traditional physically based models and directly targets the quantities most relevant for quantum protocol performance.

The model relies on two structural assumptions.
First, we assume that fluctuations of the beam centroid $x_0$ and of the beam spot size $S$ occur on distinct spatial scales of turbulence, allowing them to be treated as statistically independent.
As shown in ^[sec:beamshape], small correlations between $x_0$ and $S$ exist but remain negligible for weak and moderate turbulence.
Second, beam ellipticity and higher-order deformations are not modeled explicitly.
Their contributions are absorbed into effective beam size fluctuations through moment matching.
Consequently, the inferred moments of $S$ lose a direct physical interpretation but achieve consistency at the level of transmittance statistics.

Validation against numerical simulations demonstrates a substantial improvement over existing physically motivated models across most channels.
In the weak turbulence regime with $F_0=z_\mathrm{ap}$ and small apertures, the model outperforms all existing analytical approaches.
More generally, performance is better for $F_0=z_\mathrm{ap}$ compared to $F_0=z_\infty$ and for aperture radii smaller than the average beam size.

Validation was performed using the first two transmittance moments, $\langle \eta \rangle$ and $\langle \eta^2 \rangle$, obtained directly from simulations.
If analytical approximations of these moments are used, or if experimental noise and systematic errors affect their estimation, the performance of the model may degrade.
This limitation motivates further work on improved analytical expressions for low-order transmittance moments.

Overall, the proposed application of moment matching to the Circular-beam model provides a robust, physically grounded description of the PDT.
It requires only simple numerical integration and parameter optimization, resulting in substantially lower computational costs than full phase-screen simulations.
Furthermore, it defines the PDT in terms of measurable quantities at the aperture plane--- such as beam wandering $\langle x_0 \rangle$ and the first two transmittance moments $\langle \eta \rangle$ and $\langle \eta^2 \rangle$---whereas the phase-screen method requires a detailed turbulence profile description.
These features make it suitable for practical applications in quantum communication.
