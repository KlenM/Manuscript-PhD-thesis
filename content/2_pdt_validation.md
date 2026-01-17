# Validation of existing models

The probability distribution of transmittance describes an atmospheric quantum channel.
It defines the input-output relation between quantum states and enables quantitative analysis of protocol performance in free space links.
Proper characterization of the PDT is essential, since the correctness of any protocol analysis depends directly on the accuracy of the assumed model.

Several analytical models of the PDT have been proposed.
The earliest approach adopts statistical models of optical intensity fluctuations from classical optics.
Since the transmittance is bounded by unity, events exceeding one must be discarded.
This leads to the truncated lognormal model.
A second class of models is based on a phenomenological description of the beam in the receiver aperture plane.
The beam centroid is assumed to undergo two dimensional Gaussian wandering.
Under a fixed size circular beam approximation this yields the beam wandering model.
By introducing additional assumptions on elliptical beam deformation, the elliptical beam model provides an improved description of atmospheric quantum channels.
A later model assumes statistical independence between beam wandering and beam shape deformations.
These effects are combined to construct the total probability PDT model.

There remains significant uncertainty regarding the physical regimes in which these models are applicable.
The lognormal distribution of the optical field is derived within the weak turbulence Rytov approximation.
Nevertheless, the truncated lognormal models has been reported to fit experimental data obtained under strong turbulence conditions^[@exp].
Beam wandering is a pronounced feature of light propagation through weak turbulence and the beam wandering model is therefore commonly associated with this regime.
The elliptical beam model is reported to reproduce experimental data under weak to moderate turbulence.
This turbulence based classification is incomplete which motivates a more systematic analysis of model applicability.

In this section, numerical simulations of atmospheric channels are performed for three different turbulence conditions which are characterized with the value of the Rytov parameter $\sigma_{\mathrm{R}}^2 = 1.23 \, C_n^2 k^{7/6} z_\text{ap}^{11/6}$.
The results are used to validate existing analytical models and to identify their ranges of applicability.
Model comparison is carried out using the Kolmogorov-Smirnov statistic, defined as

$$D_M = \sup_{\eta} \left| F_M(\eta) - F(\eta) \right|$$
where $F_M(\eta)=M^{-1}\sum_{i=1}^M\theta(\eta-\eta_i)$ denotes the empirical distribution function obtained from simulation, $M$ is the sample size, $\theta(\eta)$ is the Heaviside step function, and $F(\eta)$ cumulative distribution function of the analytical model.
The goal is to determine which model performs best in a given scenario rather than to perform formal hypothesis testing.
The Kolmogorov-Smirnov (KS) statistic therefore provides a simple and sufficient metric.
It directly quantifies discrepancies between cumulative distributions, which is especially relevant for tasks where tail probabilities such as exceedance $1 - F(\eta)$ determine system performance.

Existing analytical models are typically parametrized by quantities derived from second and fourth order field correlation functions $\Gamma_2$ and $\Gamma_4$^[sec:gamma] in the aperture plane.
In particular, the first and second moments of the transmittance $\left<\eta\right>$ and $\left<\eta^2\right>$ can be obtained^[sec:eta12] from the field correlation functions and can be easily measured experimentally.
Beam shape parameters such as long term beam size, short term beam size, beam wandering variance, and beam size fluctuations^[sec:bwetc] require more involved measurements but remain experimentally accessible.

In theoretical analyses, deriving the correlation functions in terms of channel parameters such as the refractive index structure constant, inner and outer scales, and propagation distance requires restrictive approximations that become impractical in moderate to strong turbulence. 
This leads to additional error in the PDT when it is inferred from the channel parameters.
To isolate the performance of the PDT models from these analytical approximations, this work estimates all model parameters directly from phase screen simulations.
This approach provides unbiased parameter estimation and enables the validation of analytical models independently of external parameter errors

> - [ ] No determenistic losses!

> - table of models (there are a lot so the reader need visual aid)

## Beta distribution model
Before performing the validation of existing analytical models, we introduce an additional empirical model of the probability distribution of transmittance based on the Beta distribution^[@beta].
The PDT in this model is defined by the Beta probability density function:

$$
%\label{Eq:pdt_beta}
\mathcal{P}\!\left(\eta\,; \left<\eta\right>, \left<\eta^2\right>\right) = \frac{1}{B(a, b)} \eta^{a-1} (1-\eta)^{b-1}.
$$
where $B(a,b)$ is the Beta function.
The internal parameters $a$ and $b$ are expressed through the first two moments of the transmittance, $\left<\eta\right>$ and $\left<\eta^2\right>$, as

$$
\begin{split}
a = a\left(\langle\eta\rangle,\langle\eta^2\rangle\right)&= \frac{\langle\eta\rangle - \langle\eta^2\rangle}{ \langle\eta^2\rangle- \langle\eta\rangle^2}\langle \eta \rangle, \\
b =b\left(\langle\eta\rangle,\langle\eta^2\rangle\right)&=  \frac{\langle\eta\rangle - \langle\eta^2\rangle}{ \langle\eta^2\rangle- \langle\eta\rangle^2} \left( 1 - \langle\eta\rangle \right).
\end{split}
$$

This model is particularly convenient for several reasons.
First, it has a natural support on the physically meaningful interval $[0,1]$, which corresponds directly to the possible range of transmittance values.
Second, it provides a simple analytical expression, whose parameters can be determined directly from the first two statistical moments of transmittance.
This makes the model straightforward to implement and interpret.
Finally, the shape of the Beta distribution PDT generally resembles the numerically obtained transmittance distributions across a wide range of turbulence conditions.
Therefore, we expect it to exhibit good agreement with numerical simulations, as will be shown in the following sections.

> rewrite params?

## Results and discussion
### Weak channel

We consider a weak turbulence channel with Rytov parameter $\sigma_\mathrm{R}^2 = 0.2$.
Physical and numerical parameters are listed in ^[tab:weak_params].

```{=latex}
\begin{table*}[t]
\centering
\caption{Weak turbulence channel parameters ($\sigma_{\mathrm{R}}^2 = 0.2$).}
\label{tab:weak_params}
\small
\begin{tabularx}{\textwidth}{l l l | l l}
\toprule
\textbf{Physical Parameter} & \textbf{Symbol} & \textbf{Value} & \textbf{Numerical Setting} & \textbf{Value} \\ 
\midrule
Channel length & $z_{\mathrm{ap}}$ & $1$~km & Phase screens & $10$ \\
Structure constant & $C_n^2$ & $5 \times 10^{-15}$ & Grid size & $512 \times 512$ \\
Inner scale & $\ell_0$ & $1$~mm & Spatial step & $0.3$~mm \\
Outer scale & $L_0$ & $80$~m & Spectral rings & $1024$ \\
Wavelength & $\lambda$ & $809$~nm & Interscreen Rytov parameter & $3 \times 10^{-3}$ \\
Beam radius & $W_0$ & $2$~cm & Sample size & $10^5$ \\
\bottomrule
\end{tabularx}
\end{table*}
```


Two initial beam curvatures are examined.
The first case uses $F_0 = +\infty$ and corresponds to a collimated beam.
The second case uses $F_0 = z_\text{ap}$ and corresponds to a geometrically focused beam that minimizes the beam radius at the aperture plane in the absence of turbulence ^[@geomfocus].

#### Collimated beam.

For the collimated beam with $F_0 = +\infty$, the Kolmogorov-Smirnov statistics comparing analytical models to the numerical PDT are shown in ^[@fig:ks_weak_inf].
The vertical axis is plotted on a logarithmic scale, so equal visual separations correspond to order of magnitude differences in the actual KS distance.


![\label{fig:ks_weak_inf}Weak zap](validation/weak_inf_ks_values.svg)

Despite their direct physical motivation, the beam wandering and elliptic beam models exhibit the poorest agreement with the numerical distributions across most aperture sizes.
The elliptic beam model nevertheless displays pronounced minima of the KS statistic when the aperture radius slightly exceeds the long term beam radius.

The truncated lognormal model reproduces the numerical transmittance distribution reasonably well.
Its accuracy degrades as the aperture radius increases because the numerical distribution changes its skewness from positive to negative values, while the truncated lognormal distribution remains positively skewed for any choice of parameters.

The total probability model perform nearly identically to the underlying lognormal distribution in this regime, which contradicts the interpretation that beam wandering plays a dominant role in shaping transmittance statistics under weak turbulence.

Among all considered models, the beta distribution yields the best overall agreement.
Its KS statistic reaches a minimum near $\langle \eta \rangle \approx 0.5$, where the numerical probability distribution of transmittance is close to symmetric.
This behavior is consistent with the flexibility of the beta distribution in interpolating between positively and negatively skewed shapes.

At the aperture corresponding to the KS minimum of the elliptic beam model, the mode of this analytical distribution coincides with the mode of the numerical distribution, as shown in ^[@fig:pdt_weak_inf].

![\label{fig:pdt_weak_inf}Weak inf](validation/weak_inf_pdt_0_03.svg)

This aperture is indicated by the vertical line in ^[@fig:ks_weak_inf].
For other aperture sizes, the elliptic beam model exhibits biased values of both the mode and the mean transmittance $\langle \eta \rangle$.

The beam wandering model assumes a fixed circular beam profile, which implies that the transmittance cannot exceed that of a perfectly coaxial beam.
This constraint manifests as a sharp cutoff of the right tail of the distribution and prevents the model from reproducing the high transmittance events observed numerically.

Overall, under weak turbulence the transmittance fluctuations remain small, and for $0 \ll \langle \eta \rangle \ll 1$ the numerical distributions approach a quasi Gaussian shape.

#### Focused beam.

For the focused configuration with $F_0 = z_\mathrm{ap}$, the KS statistics are shown in ^[@fig:ks_weak_zap].

![\label{fig:ks_weak_zap}Weak zap](validation/weak_zap_ks_values.svg)

All analytical models demonstrate systematically poorer agreement with numerical probability distributions compared to the collimated case.
This deterioration should not be interpreted as reduced channel performance.
A focused beam produces a smaller spot at the aperture plane and therefore achieves a higher average transmittance for the same aperture radius, which improves link efficiency.
The larger KS values instead indicate that existing analytical models do not adequately capture the more complex field statistics.

Among all considered models, the total probability model provide the best overall agreement for small and moderate aperture radii.
However, when the aperture radius satisfies $R_\mathrm{ap} \gtrsim W_\mathrm{LT}$, these models are no longer defined.
In this domain, the beta distribution yields the smallest KS distance among the remaining models.

The numerical and analytical PDTs corresponding to the minima of the total probability models are shown in ^[@fig:pdt_weak_zap].

> - [ ] Change TB to TL

![\label{fig:pdt_weak_zap}Weak zap](validation/weak_zap_pdt_0_015.svg)

The truncated lognormal distribution exhibits an incorrect skewness and an unphysical finite probability density at $\eta = 1$, which arises from the imposed truncation.
The elliptic beam model again shows biased estimates of both the mode and the mean transmittance.

The beta distribution, while matching the first two moments by construction, underestimates higher order moments such as skewness and kurtosis.
In the focused beam weak turbulence regime, the total probability approach provides the closest overall agreement with the numerical results. 
However, when the total probability model is not applicable, the beta distribution yields the best agreement among the remaining analytical models.

### Moderate channel

We next consider a moderate turbulence channel with Rytov parameter $\sigma_\mathrm{R}^2 = 1.5$. This regime corresponds to realistic atmospheric conditions for the horizontal atmospheric channel in Erlangen, Germany. 
The physical and numerical parameters used in the simulations are summarized in Table ^[@tab:moderate_params].

```{=latex}
\begin{table*}[t]
\centering
\caption{Moderate turbulence channel parameters ($\sigma_{\mathrm{R}}^2 = 1.5$).}
\label{tab:moderate_params}
\small
\begin{tabularx}{\textwidth}{l l l | l l}
\toprule
\textbf{Physical Parameter} & \textbf{Symbol} & \textbf{Value} & \textbf{Numerical Setting} & \textbf{Value} \\ 
\midrule
Channel length & $z_{\mathrm{ap}}$ & $1.6$~km & Phase screens & $10$ \\
Structure constant & $C_n^2$ & $1.5 \times 10^{-14}$ & Grid size & $512 \times 512$ \\
Inner scale & $\ell_0$ & $1$~mm & Spatial step & $0.4$~mm \\
Outer scale & $L_0$ & $80$~m & Spectral rings & $1024$ \\
Wavelength & $\lambda$ & $809$~nm & Interscreen Rytov parameter & $2.2 \times 10^{-2}$ \\
Beam radius & $W_0$ & $2$~cm & Sample size & $10^5$ \\
\bottomrule
\end{tabularx}
\end{table*}
```

#### Collimated Beam.

For the collimated configuration with $F_0 = +\infty$, the Kolmogorov-Smirnov statistics comparing analytical models to numerical transmittance distributions are shown in ^[@fig:ks_moderate_inf].

![\label{fig:pdt_moderate_inf}Moderate inf](validation/moderate_inf_ks_values.svg)

The overall behavior is qualitatively similar to the weak turbulence case.
For small aperture radii, the beta distribution provides the best agreement with the numerical PDT.
As the aperture increases, its performance gradually degrades.

As seen in the left panel of ^[@fig:pdt_moderate_inf], the beta model accurately reproduces the overall shape of the numerical distribution in this regime.
In contrast, the truncated lognormal model produces a systematically narrower distribution, despite being parametrized using the first two moments.
This bias likely arises because truncation alters the effective moments of the distribution, while the fitted parameters correspond to the underlying untruncated lognormal.
An additional contribution may come from mismatched higher order statistics, in particular the kurtosis.

![\label{fig:pdt_moderate_inf}Moderate inf](validation/moderate_inf_pdt_0_05.svg)

At aperture radii $R_\mathrm{ap} \approx W_\mathrm{LT}$, the total probability model outperforms all other approaches as it seen in ^[fig:ks_moderate_inf] and the right panel of ^[fig:pdt_moderate_inf].
In this range, the modes of the beam wandering and elliptic beam models coincide with the mode of the numerical distribution, which leads to pronounced minima of the KS statistic for these models.
The beta distribution, although accurate in mean and variance, underestimates the kurtosis in this regime, which limits its performance compare to the total probability model.

#### Focused Beam.

For the focused configuration with $F_0 = z_\mathrm{ap}$, the KS statistics are shown in ^[@fig:ks_moderate_zap].
As in the weak turbulence channel, focusing leads to systematically poorer agreement between analytical models and numerical results compared to the collimated case.


![\label{fig:pdt_moderate_zap}Moderate zap](validation/moderate_zap_ks_values.svg)

The beta distribution again provides the best overall performance across most aperture sizes.
Near $R_\mathrm{ap} \approx W_\mathrm{LT}$, the total probability models slightly outperform the beta distribution.
At apertures where the modes of the beam wandering and elliptic beam models coincide with the numerical mode, these models temporarily achieve their best agreement.

The underlying reason for the generally worse performance of all analytical models is illustrated in ^[@fig:pdt_moderate_zap].
In this regime, the numerical probability distribution develops a strongly non Gaussian plateau, with an extended interval of $\eta$ over which the probability density remains approximately constant.
Such a feature cannot be captured by any of the considered analytical models, all of which predict smooth unimodal distributions with decaying tails.


![\label{fig:pdt_moderate_zap}Moderate zap](validation/moderate_zap_pdt_0_012.svg)

Overall, the agreement between analytical models and numerical results is worse in this regime than in the strong turbulence channel analyzed in the following section.'

### Strong channel

As the propagation distance increases, the difference between the spot sizes of a geometrically focused beam with $F_0 = z_\mathrm{ap}$ and a collimated beam with $F_0 = +\infty$ becomes negligible at the aperture plane.
Consequently, only the collimated configuration is considered in the strong turbulence regime.
We analyze a strong turbulence channel characterized by the Rytov parameter $\sigma_\mathrm{R}^2 = 33.3$.
The corresponding physical and numerical parameters are listed in Table ^[@tab:strong_params].

```{=latex}
\begin{table*}[t]
\centering
\caption{Strong turbulence channel parameters ($\sigma_{\mathrm{R}}^2 = 33.3$).}
\label{tab:strong_params}
\small
\begin{tabularx}{\textwidth}{l l l | l l}
\toprule
\textbf{Physical Parameter} & \textbf{Symbol} & \textbf{Value} & \textbf{Numerical Setting} & \textbf{Value} \\ 
\midrule
Channel length & $z_{\mathrm{ap}}$ & $50$~km & Phase screens & $30$ \\
Structure constant & $C_n^2$ & $6 \times 10^{-16}$ & Grid size & $4096 \times 4096$ \\
Inner scale & $\ell_0$ & $1$~mm & Spatial step & $1$~mm \\
Outer scale & $L_0$ & $80$~m & Spectral rings & $1024$ \\
Wavelength & $\lambda$ & $808$~nm & Interscreen Rytov parameter & $6.5 \times 10^{-2}$ \\
Beam radius & $W_0$ & $6$~cm & Sample size & $10^5$ \\
\bottomrule
\end{tabularx}
\end{table*}
```

The Kolmogorov-Smirnov statistics comparing analytical models to numerical transmittance distributions are shown in ^[@fig:ks_strong_inf].
Even in this strong turbulence regime, the overall behavior resembles that observed in the previously considered regimes.

![\label{fig:pdt_moderate_inf}Moderate inf](validation/strong_inf_ks_values.svg)

The main qualitative difference appears at very small apertures $R_\mathrm{ap} \lesssim 0.1 W_\mathrm{LT}$.
In this range, the truncated lognormal model exhibits better agreement with the numerical results, as illustrated in ^[@fig:pdt_strong_inf].

![\label{fig:pdt_strong_inf}Strong inf](validation/strong_inf_pdt_0_1.svg)

As the ratio $R_\mathrm{ap} / W_\mathrm{LT} \to 0$, the aperture can be treated as point like relative to both the overall beam size and the characteristic scintillation scale of the optical field.
The transmittance distribution then approaches the probability distribution of irradiance at a point, rather than an aperture averaged quantity.

Point irradiance statistics in atmospheric turbulence have been studied extensively in classical atmospheric optics and are discussed in^[@sec:pdf_irradiance].
In this context, the lognormal distribution is a standard model, which explains the relatively good performance of the truncated lognormal model for very small apertures.

For strong turbulence, other irradiance models such as the negative exponential, K-distribution, lognormal-Rician, or gamma-gamma distributions, as reviewed in ^[@sec:pdf_irradiance],  may provide a more accurate description of PDT for the range of very small apertures.

### Conclusion

For both weak turbulence channels and the moderate-turbulence collimated beam channel, the numerically obtained probability density of transmittance (PDT) exhibits a bell-like, unimodal, and relatively narrow distribution, with noticeable asymmetry near the boundaries of its support, $\eta \in [0,1]$.
For the moderate-turbulence focused beam and strong turbulence channels, a similar overall tendency is observed, though the distributions become broader and tend toward a flattened shape, indicating an increased spread of transmittance values caused by the more complex spatial structure of the beam.

The first important observation is that the two physically motivated models—the beam wandering model and the elliptical beam model—being defined in terms of beam shape statistics, exhibit biased transmittance moments.
In some cases, these models reproduce the overall shape of the numerical PDT quite well (see Fig. ^[fig:pdt_weak_zap]), although their peaks are shifted relative to the numerical result.
The best agreement in terms of the KS-statistic is obtained when the peaks of the analytical and numerical PDTs coincide, as illustrated in ^[fig:ks_moderate_inf].
Thus, because of the inability to fully account for all orders of the beam shape decomposition, it is more appropriate to parameterize analytical models in terms of transmittance moments rather than beam shape statistics.

The second important observation concerns the dominant role of the aperture size in determining the applicability of different PDT models.
The KS-statistics results show that the models’ relative performance is similar across different turbulence strengths.
In contrast, variations in the aperture radius cause significant changes in the KS-statistic, indicating a strong dependence of model accuracy on the aperture parameter.

Physically, increasing the turbulence strength primarily leads to a broader PDT (i.e., increased variance), which is captured reasonably well by all the analytical models.
However, changing the aperture size mainly affects the skewness of the numerical PDT, and many analytical models fail to reproduce this asymmetry accurately.
In particular, the lognormal model always yields positively skewed distributions, whereas the beam wandering model consistently produces negatively skewed ones.
The elliptical beam model generally yields negative skewness, with only a minor positive skew for small apertures, which remains insufficient to reproduce the numerical PDT.
Among the considered models, the total probability model and the Beta model most successfully reproduce the skewness of the numerical PDT.

Overall, across the entire parameter space examined, the analytical PDT models exhibit distinct strengths and weaknesses, which can be summarized as follows.
The empirical Beta model generally exhibits the best performance according to the KS-statistics, thanks to its naturally bounded support $\eta\in [0,1]$ and its ability to reproduce the skewness near the boundary points.

The lognormal model shows decent performance, but it is generally inferior to the Beta model.
An exception occurs for small apertures under strong turbulence, when the numerical PDT is broad and highly skewed.
In this regime, the Beta model’s estimated parameters may reflect in an unphysical L-shaped form with high probability of $\eta=0$, and the lognormal model can outperform the Beta model.

The total probability model, which combines the positively skewed lognormal and negatively skewed beam wandering models, performs similarly to the base lognormal model for small apertures.
However, when the aperture size becomes comparable to the average beam spot width ($R_\text{ap} \lesssim W_\text{LT}$), the model captures the high kurtosis of the numerical PDT, allowing it to outperform other models in some narrow parameter range.

The physically grounded beam wandering and elliptical beam models are strongly affected by bias in the first transmittance moments (mean and variance).
This is the reason why they perform well when their parameters are fitted using least-squares methods^[@expfit], but poorly when the beam shape parameters are estimated directly from numerical simulations.
However, when the peaks of the analytical and numerical PDTs are aligned, these models can outperform all others.
