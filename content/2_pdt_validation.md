# Validation of analytical models {#sec:validation}
The reliability of any free-space quantum protocol analysis depends on the accuracy of the PDT.
Any inaccuracies in the PDT modelling inevitably lead to inaccurate estimations of the quantum states at the receiver.
Consequently, rigorous validation of these models is essential to ensure that predictions of models provide accurate results.
This section addresses these challenges by providing a comparative analysis of the analytical PDT against numerical simulations, presenting the results published in our work \ref{mypaper1}.

Several analytical models of the PDT have been proposed (see ^[sec:pdt]).
The earliest approach adopts statistical models of optical intensity fluctuations from classical optics.
Since the transmittance is bounded by unity, events exceeding one must be discarded.
This leads to the truncated lognormal model.
A second class of models is based on a phenomenological description of the beam in the receiver aperture plane.
The beam centroid is assumed to undergo two-dimensional Gaussian wandering.
Under a fixed-size circular beam approximation, this yields the beam-wandering model.
By introducing additional assumptions on elliptical-beam deformation, the elliptical-beam model provides an improved description of atmospheric quantum channels.
A later model assumes statistical independence between beam wandering and beam shape deformations.
These effects are combined to construct the total probability PDT model.

There remains significant uncertainty regarding the physical regimes in which these models are applicable.
The lognormal distribution of the optical field is derived within the weak turbulence Rytov approximation.
Nevertheless, the truncated lognormal models has been reported to fit experimental data obtained under strong turbulence conditions^[@capraro2012].
Beam wandering is a pronounced feature of light propagation through weak turbulenceo and the beam-wandering model is therefore commonly associated with this regime.
The elliptical-beam model is reported to reproduce experimental data under weak to moderate turbulence.
This turbulence-based classification is incomplete, which motivates a more systematic analysis of model applicability.

In this section, numerical simulations of atmospheric channels are performed for three different turbulence conditions, which are characterized by the value of the Rytov parameter $\sigma_{\mathrm{R}}^2 = 1.23 \, C_n^2 k^{7/6} z_\mathrm{ap}^{11/6}$.
The results are used to validate existing analytical models and to identify their ranges of applicability.
Model comparison is carried out using the Kolmogorov-Smirnov (KS) statistic^[@conover1999], defined as
$$D_M = \sup_{\eta} \left| F_M(\eta) - F(\eta) \right|,$$
where $F(\eta)$ is the cumulative distribution function of the analytical model and $F_M(\eta)$ denotes the empirical distribution function obtained from simulation
$$F_M(\eta)=\frac{1}{M}\sum_{i=1}^M\theta(\eta-\eta_i),$$
where $M$ is the sample size, $\theta(\eta)$ is the Heaviside step function.
The goal is to determine which model performs best in a given scenario rather than to perform formal hypothesis testing.
The Kolmogorov-Smirnov statistic therefore provides a simple and sufficient metric.
It directly quantifies discrepancies between cumulative distributions, which is especially relevant for tasks where tail probabilities such as exceedance $1 - F(\eta)$ determine system performance^[@vasylyev2012].

Existing analytical models are typically parametrized by quantities derived from second- and fourth-order field correlation functions $\Gamma_2$ and $\Gamma_4$ (see ^[sec:light_in_turb]) in the aperture plane.
In particular, the first and second moments of the transmittance $\left<\eta\right>$ and $\left<\eta^2\right>$ can be obtained from the field correlation functions and can be easily estimated from experimental data.
Beam shape parameters such as long-term beam-spot radius, short-term beam-spot radius, beam-wandering variance, and beam size fluctuations require more involved measurements but remain experimentally accessible.

In theoretical analyses, deriving the correlation functions in terms of channel parameters such as the refractive index structure constant, inner and outer scales, and propagation distance requires restrictive approximations that become impractical in moderate to strong turbulence.
This leads to additional error in the PDT when it is inferred from the channel parameters.
To isolate the performance of the PDT models from these analytical approximations, this work estimates all model parameters directly from phase-screen simulations.
This approach provides unbiased parameter estimation and enables the validation of analytical models independently of external parameter errors.

> - [ ] No determenistic losses!

> - table of models (there are a lot, means that the reader need visual aid)

## Results and discussion
### Weak channel {#sec:valid_weak}

We consider a weak turbulence channel with Rytov parameter $\sigma_\mathrm{R}^2 = 0.2$.
Physical and numerical parameters are listed in ^[tab:weak_params].
Two initial beam curvatures are examined.
The first case uses $F_0 = +\infty$ and corresponds to a collimated beam.
The second case uses $F_0 = z_\mathrm{ap}$ and corresponds to a geometrically focused beam that minimizes the beam radius at the aperture plane in the absence of turbulence ^[@andrews2005].

```{=latex}
\renewcommand{\arraystretch}{1.2}
\begin{table}[h]
\centering
\caption{Weak turbulence channel parameters ($\sigma_{\mathrm{R}}^2 = 0.2$).}
\label{tab:weak_params}
\small
\begin{tabular}{|l l l | l l|}
\hline
\textbf{Physical Parameter} & \textbf{Symbol} & \textbf{Value} & \textbf{Numerical Setting} & \textbf{Value} \\
\hline
Channel length & $z_{\mathrm{ap}}$ & $1$~km & Phase screens & $10$ \\
Structure constant & $C_n^2$ & $5 \times 10^{-15}$ & Grid size & $512 \times 512$ \\
Inner scale & $\ell_0$ & $1$~mm & Spatial step & $0.3$~mm \\
Outer scale & $L_0$ & $80$~m & Spectral rings & $1024$ \\
Wavelength & $\lambda$ & $809$~nm & Interscreen Rytov parameter & $3 \times 10^{-3}$ \\
Beam radius & $W_0$ & $2$~cm & Sample size & $10^5$ \\
\hline
\end{tabular}
\end{table}
```

#### Collimated beam.

For the collimated beam with $F_0 = +\infty$, the Kolmogorov-Smirnov statistics comparing analytical models to the numerical PDT are shown in ^[fig:ks_weak_inf].
The vertical axis is plotted on a logarithmic scale, such that equal visual separations correspond to order-of-magnitude differences in the actual KS distance.
Despite their direct physical motivation, the beam-wandering and elliptical-beam models exhibit the poorest agreement with the numerical distributions across most aperture sizes.
The elliptical-beam model nevertheless displays pronounced minima of the KS statistic when the aperture radius slightly exceeds the long-term beam radius.

![\label{fig:ks_weak_inf}Kolmogorov-Smirnov (KS) statistic $D_M$ as a function of the aperture radius for a collimated beam $F_0=\infty$ in a weak turbulence channel ($\sigma_{\mathrm{R}}^2 = 0.2$). The performance of the beam-wandering (W), elliptical-beam (E), truncated lognormal (L), total probability (T), and Beta distribution (B) models are compared against numerical simulation data. The vertical line indicates the aperture radius ($R_\mathrm{ap} = 3~\text{cm}$) where the elliptical-beam model achieves its minimum KS distance.](validation/weak_inf_ks_values.pdf)

The truncated lognormal model reproduces the numerical transmittance distribution reasonably well.
Its accuracy degrades as the aperture radius increases because the numerical distribution changes its skewness from positive to negative values, while the truncated lognormal distribution remains positively skewed for any choice of parameters.
The total probability model performs nearly identically to the underlying lognormal distribution in this regime, which contradicts the interpretation that beam wandering plays a dominant role in shaping transmittance statistics under weak turbulence.

Among all considered models, the Beta distribution yields the best overall agreement.
Its KS statistic reaches a minimum near $\langle \eta \rangle \approx 0.5$, where the numerical PDT is close to symmetric.
This behavior is consistent with the flexibility of the Beta distribution in interpolating between positively and negatively skewed shapes.

At the aperture corresponding to the KS minimum of the elliptical-beam model, the mode of this analytical distribution coincides with the mode of the numerical distribution, as shown in ^[fig:pdt_weak_inf].
This aperture is indicated by the vertical line in ^[fig:ks_weak_inf].
For other aperture sizes, the elliptical-beam model exhibits biased values of both the mode and the mean transmittance $\langle \eta \rangle$.

![\label{fig:pdt_weak_inf}PDT for a collimated beam $F_0=\infty$ in a weak turbulence channel ($\sigma_{\mathrm{R}}^2 = 0.2$) with an aperture radius of $R_\mathrm{ap} = 3~\text{cm}$. The numerical simulation (N) is compared with the beam-wandering (W), truncated lognormal (L), elliptical-beam (E), and Beta distribution (B) models.](validation/weak_inf_pdt_0_03.pdf)

The beam-wandering model assumes a fixed circular beam profile, which implies that the transmittance cannot exceed that of a perfectly coaxial beam.
This constraint manifests as a sharp cutoff of the right tail of the distribution and prevents the model from reproducing the high transmittance events observed numerically.
Overall, under weak turbulence the transmittance fluctuations remain small, and for $0 \ll \langle \eta \rangle \ll 1$ the numerical distributions approach a quasi-Gaussian shape.

#### Focused beam.

For the focused configuration with $F_0 = z_\mathrm{ap}$, the KS statistics are shown in ^[fig:ks_weak_zap].
All analytical models demonstrate systematically poorer agreement with numerical probability distributions compared to the collimated case.
This deterioration should not be interpreted as reduced channel performance.
A focused beam produces a smaller spot at the aperture plane and therefore achieves a higher average transmittance for the same aperture radius, which improves link efficiency.
The larger KS values instead indicate that existing analytical models do not adequately capture the more complex field statistics.

![\label{fig:ks_weak_zap}Kolmogorov-Smirnov (KS) statistic $D_M$ as a function of the aperture radius for a focused beam ($F_0 = z_{\mathrm{ap}}$) in a weak turbulence channel ($\sigma_{\mathrm{R}}^2 = 0.2$). The performance of the beam-wandering (W), elliptical-beam (E), truncated lognormal (L), total probability (T), and Beta distribution (B) models are compared against numerical simulation data. The vertical line indicates the aperture radius ($R_{\text{ap}} = 1.5$ cm) where the total probability model achieves its minimum KS distance.](validation/weak_zap_ks_values.pdf)

Among all considered models, the total probability model provides the best overall agreement for small and moderate aperture radii.
However, when the aperture radius satisfies $R_\mathrm{ap} \gtrsim W_\mathrm{LT}$, the model is no longer defined.
In this domain, the Beta distribution yields the smallest KS distance among the remaining models.

The numerical and analytical PDTs corresponding to the minima of the total probability model are shown in ^[fig:pdt_weak_zap].
The truncated lognormal distribution exhibits an incorrect skewness and an unphysical finite probability density at $\eta = 1$, which arises from the imposed truncation.
The elliptical-beam model again shows biased estimates of both the mode and the mean transmittance.

![\label{fig:pdt_weak_zap}PDT for a focused beam ($F_0 = z_{\mathrm{ap}}$) with an aperture radius of $R_{\text{ap}} = 1.5$ cm  in a weak turbulence channel ($\sigma_{\mathrm{R}}^2 = 0.2$). The numerical simulation (N) is compared with the truncated lognormal (L), elliptical-beam (E), total probability (T) and Beta distribution (B) models.](validation/weak_zap_pdt_0_015.pdf)

The Beta distribution, while matching the first two moments by construction, underestimates higher-order moments such as skewness and kurtosis.
In the focused beam weak turbulence regime, the total probability approach provides the closest overall agreement with the numerical results.
However, when the total probability model is not applicable, the Beta distribution yields the best agreement among the remaining analytical models.

### Moderate channel {#sec:valid_moderate}

We next consider a moderate turbulence channel with Rytov parameter $\sigma_\mathrm{R}^2 = 1.5$. 
This regime corresponds to realistic atmospheric conditions for the horizontal atmospheric channel in Erlangen, Germany^[@peuntinger2014,usenko2012].
The physical and numerical parameters used in the simulations are summarized in ^[tab:moderate_params].

```{=latex}
\renewcommand{\arraystretch}{1.2}
\begin{table}[h]
\centering
\caption{Moderate turbulence channel parameters ($\sigma_{\mathrm{R}}^2 = 1.5$).}
\label{tab:moderate_params}
\small
\begin{tabular}{|l l l | l l|}
\hline
\textbf{Physical Parameter} & \textbf{Symbol} & \textbf{Value} & \textbf{Numerical Setting} & \textbf{Value} \\
\hline
Channel length & $z_{\mathrm{ap}}$ & $1.6$~km & Phase screens & $10$ \\
Structure constant & $C_n^2$ & $1.5 \times 10^{-14}$ & Grid size & $512 \times 512$ \\
Inner scale & $\ell_0$ & $1$~mm & Spatial step & $0.4$~mm \\
Outer scale & $L_0$ & $80$~m & Spectral rings & $1024$ \\
Wavelength & $\lambda$ & $809$~nm & Interscreen Rytov parameter & $2.2 \times 10^{-2}$ \\
Beam radius & $W_0$ & $2$~cm & Sample size & $10^5$ \\
\hline
\end{tabular}
\end{table}
```

#### Collimated Beam.

For the collimated configuration with $F_0 = +\infty$, the Kolmogorov-Smirnov statistics comparing analytical models to numerical transmittance distributions are shown in ^[fig:ks_moderate_inf].
The overall behavior is qualitatively similar to the weak turbulence case.
For small aperture radii, the Beta distribution provides the best agreement with the numerical PDT.
As the aperture increases, its performance gradually degrades.

![\label{fig:ks_moderate_inf}Kolmogorov-Smirnov statistic $D_M$ as a function of the aperture radius for a collimated beam ($F_0 = \infty$) in a moderate turbulence channel ($\sigma_{\mathrm{R}}^2 = 1.5$).  The performance of the beam-wandering (W), elliptical-beam (E), truncated lognormal (L), total probability (T), and Beta distribution (B) models are compared against numerical simulation data.](validation/moderate_inf_ks_values.pdf)

As seen in the left panel of ^[fig:pdt_moderate_inf], the Beta model accurately reproduces the overall shape of the numerical distribution in this regime.
In contrast, the truncated lognormal model produces a systematically narrower distribution, despite being parametrized using the first two moments.
This bias arises because truncation alters the effective moments of the distribution, while the fitted parameters correspond to the underlying untruncated lognormal.
An additional contribution may come from mismatched higher-order statistics, in particular the kurtosis.

![\label{fig:pdt_moderate_inf}PDT for a collimated beam in moderate turbulence at an aperture radius of $R_{\text{ap}} = 0.9~\text{cm}$ (left panel) and $R_{\text{ap}} = 5~\text{cm}$ (right panel). The beam-wandering (W), elliptical-beam (E), truncated lognormal (L), total probability (T), and Beta distribution (B) models and numerical simulation results (N).](validation/moderate_inf_pdt_0_05.pdf)

At aperture radii $R_\mathrm{ap} \approx W_\mathrm{LT}$, the total probability model outperforms all other approaches as seen in ^[fig:ks_moderate_inf] and the right panel of ^[fig:pdt_moderate_inf].
In this range, the modes of the beam-wandering and elliptical-beam models coincide with the mode of the numerical distribution, which leads to pronounced minima of the KS statistic for these models.
The Beta distribution, although accurate in mean and variance, underestimates the kurtosis in this regime, which limits its performance compared to the total probability model.

#### Focused Beam.

For the focused configuration with $F_0 = z_\mathrm{ap}$, the KS statistics are shown in ^[fig:ks_moderate_zap].
As in the weak turbulence channel, focusing leads to systematically poorer agreement between analytical models and numerical results compared to the collimated case.
The Beta distribution again provides the best overall performance across most aperture sizes.
Near $R_\mathrm{ap} \approx W_\mathrm{LT}$, the total probability model slightly outperforms the Beta distribution.
At apertures where the modes of the beam-wandering and elliptical-beam models coincide with the numerical mode, these models temporarily achieve their best agreement.


![\label{fig:ks_moderate_zap}Kolmogorov-Smirnov statistic $D_M$ as a function of the aperture radius for a focused beam ($F_0 = z_{\mathrm{ap}}$) in a moderate turbulence channel ($\sigma_{\mathrm{R}}^2 = 1.5$). The performance of the beam-wandering (W), elliptical-beam (E), truncated lognormal (L), total probability (T), and Beta distribution (B) models are compared against numerical simulation data.](validation/moderate_zap_ks_values.pdf)

The underlying reason for the generally worse performance of all analytical models is illustrated in ^[fig:pdt_moderate_zap].
In this regime, the numerical probability distribution develops a strongly non-Gaussian plateau, with an extended interval of $\eta$ over which the probability density remains approximately constant.
Such a feature cannot be captured by any of the considered analytical models, all of which predict smooth unimodal distributions with decaying tails.
Overall, the agreement between analytical models and numerical results is worse in this regime than in the strong turbulence channel analyzed in the following section.

![\label{fig:pdt_moderate_zap}PDT for a focused beam ($F_0 = z_{\mathrm{ap}}$) with an aperture radius of $R_{\text{ap}} = 1.2~\text{cm}$  in a moderate turbulence channel ($\sigma_{\mathrm{R}}^2 = 1.5$). The numerical simulation (N) is compared with the truncated lognormal (L), beam-wandering (W), elliptical-beam (E), total probability (T) and Beta distribution (B) models.](validation/moderate_zap_pdt_0_012.pdf)

### Strong channel

As the propagation distance increases, the difference between the spot sizes of a geometrically focused beam with $F_0 = z_\mathrm{ap}$ and a collimated beam with $F_0 = +\infty$ becomes negligible at the aperture plane.
Consequently, only the collimated configuration is considered in the strong turbulence regime.
We analyze a strong turbulence channel characterized by the Rytov parameter $\sigma_\mathrm{R}^2 = 33.3$.
The corresponding physical and numerical parameters are listed in ^[tab:strong_params].

```{=latex}
\renewcommand{\arraystretch}{1.2}
\begin{table}[h]
\centering
\caption{Strong turbulence channel parameters ($\sigma_{\mathrm{R}}^2 = 33.3$).}
\label{tab:strong_params}
\small
\begin{tabular}{|l l l | l l|}
\hline
\textbf{Physical Parameter} & \textbf{Symbol} & \textbf{Value} & \textbf{Numerical Setting} & \textbf{Value} \\
\hline
Channel length & $z_{\mathrm{ap}}$ & $50$~km & Phase screens & $30$ \\
Structure constant & $C_n^2$ & $6 \times 10^{-16}$ & Grid size & $4096 \times 4096$ \\
Inner scale & $\ell_0$ & $1$~mm & Spatial step & $1$~mm \\
Outer scale & $L_0$ & $80$~m & Spectral rings & $1024$ \\
Wavelength & $\lambda$ & $808$~nm & Interscreen Rytov parameter & $6.5 \times 10^{-2}$ \\
Beam radius & $W_0$ & $6$~cm & Sample size & $10^5$ \\
\hline
\end{tabular}
\end{table}
```

The Kolmogorov-Smirnov statistics comparing analytical models to numerical transmittance distributions are shown in ^[fig:ks_strong_inf].
Even in this strong turbulence regime, the overall behavior resembles that observed in the previously considered regimes.
However, this regime does reveal one particular feature.

![\label{fig:ks_strong_inf}Kolmogorov-Smirnov (KS) statistic $D_M$ as a function of the aperture radius for a collimated beam $F_0=\infty$ in a strong turbulence channel ($\sigma_{\mathrm{R}}^2 = 33.3$). The performance of the beam-wandering (W), elliptical-beam (E), truncated lognormal (L), total probability (T), and Beta distribution (B) models are compared against numerical simulation data.](validation/strong_inf_ks_values.pdf)

The main qualitative difference appears at very small apertures $R_\mathrm{ap} \lesssim 0.1 W_\mathrm{LT}$.
In this range, the truncated lognormal model exhibits better agreement with the numerical results. 
This finding is illustrated in ^[fig:pdt_strong_inf].

![\label{fig:pdt_strong_inf}PDT for a collimated beam $F_0=\infty$ in a strong turbulence channel ($\sigma_{\mathrm{R}}^2 = 33.3$) with an aperture radius of $R_\mathrm{ap} = 10~\text{cm}$. The numerical simulation (N) is compared with the truncated lognormal (L), elliptical-beam (E), and Beta distribution (B) models.](validation/strong_inf_pdt_0_1.pdf)

As the ratio $R_\mathrm{ap} / W_\mathrm{LT} \to 0$, the aperture can be treated as point-like relative to both the overall beam size and the characteristic scintillation scale of the optical field.
The transmittance distribution then approaches the probability distribution of irradiance at a point, rather than an aperture-averaged quantity.
Point irradiance statistics in atmospheric turbulence have been studied extensively in classical atmospheric optics and are discussed in ^[sec:pdf_irradiance].
In this context, the lognormal distribution is a standard model, which explains the relatively good performance of the truncated lognormal model for very small apertures.
For strong turbulence, other irradiance models such as the negative exponential, K-distribution, lognormal-Rician, or Gamma-Gamma distributions, as reviewed in ^[sec:pdf_irradiance], may provide a more accurate description of PDT for the range of very small apertures.

### Summary {#sec:conclusion_validation}

For both weak turbulence channels and the moderate-turbulence collimated beam channel, the numerically obtained PDTs exhibit bell-like, unimodal, and relatively narrow distributions with noticeable asymmetry near the boundaries of the support, $\eta \in [0,1]$.
For the moderate-turbulence focused beam and strong turbulence channels, a similar overall tendency is observed, though the distributions become broader and tend toward a flattened shape.
This feature indicates an increased spread of transmittance values caused by the more complex spatial structure of the beam.

The first important observation is that the physically motivated models (the beam-wandering model and the elliptical-beam model), which are defined in terms of the statistics of the beam-shape parameters, exhibit biased transmittance moments.
This discrepancy arises because idealized circular or elliptical beam shapes fail to account for complex beam deformations.
In some cases, these models reproduce the overall shape of the numerical PDT quite well (see ^[fig:pdt_weak_zap]), although their peaks are shifted relative to the numerical result.
The best agreement in terms of the KS statistic is obtained when the peaks of the analytical and numerical PDTs coincide, as illustrated in ^[fig:ks_moderate_inf].
Thus, because of the inability to fully account for all orders of the beam shape decomposition, it is more appropriate to parameterize analytical models in terms of transmittance moments rather than beam shape statistics.

The second important observation concerns the dominant role of the aperture size in determining the applicability of different PDT models.
The KS statistics show that the models' relative performance is similar across different turbulence strengths.
In contrast, variations in the aperture radius cause significant changes in the KS statistic, indicating a strong dependence of model accuracy on the aperture parameter.

Physically, increasing the turbulence strength primarily leads to a broader PDT (i.e., increased variance), which is captured reasonably well by all the analytical models.
However, changing the aperture size mainly affects the skewness of the numerical PDT, and many analytical models fail to reproduce this asymmetry accurately.
In particular, the lognormal model always yields positively skewed distributions, whereas the beam-wandering model consistently produces negatively skewed ones.
The elliptical-beam model generally yields negative skewness, with only a minor positive skew for small apertures, which remains insufficient to reproduce the numerical PDT.
Among the considered models, the total probability model and the Beta model most successfully reproduce the skewness of the numerical PDT.

Overall, across the entire parameter space examined, the analytical PDT models exhibit distinct strengths and weaknesses, which can be summarized as follows.
The empirical Beta model generally exhibits the best performance according to the KS statistics, thanks to its naturally bounded support $\eta\in [0,1]$ and its ability to reproduce the skewness near the boundary points.
The lognormal model shows decent performance, but it is generally inferior to the Beta model.
An exception occurs for small apertures under strong turbulence, when the numerical PDT is broad and highly skewed.
In this regime, the estimated parameters of the Beta model may result in an L-shaped form, and the lognormal model can outperform the Beta model.

The total probability model, which combines the positively skewed lognormal and negatively skewed beam-wandering models, performs similarly to the base lognormal model for small apertures.
However, when the aperture size becomes comparable to the average beam spot width ($R_\mathrm{ap} \lesssim W_\mathrm{LT}$), the model captures the high kurtosis of the numerical PDT, allowing it to outperform other models in some narrow parameter ranges.
The physically grounded beam-wandering and elliptical-beam models are strongly affected by bias in the first transmittance moments (mean and variance).
This is the reason why they perform well when their parameters are fitted using least-squares methods (see ^[sec:pdt]), but poorly when the beam shape parameters are estimated directly from numerical simulations.
However, when the peaks of the analytical and numerical PDTs are aligned, these models can outperform all others.
