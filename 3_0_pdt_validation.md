# Validation of existing models
 - why pdf study matters - repeat the problem statement idea of "lognomal for strong or weak"
 - (goal) validate analytical models of PDT against numerical simulations and to identify their ranges of applicability across three system conditions.
 - description of parameters
 - evaluation metric
     - pros: in many task excidance is important - CDF. So the KS shows the difference between CDFs. 
 - structure

## Type of parameters
- (Nature -) Experiment - Kolmogorov theory - Correlation function - Model parameters ??..
- Cn2 parameters and Gamma2 parameters 
- table of models (there are a lot so the reader need visual aid)

## Beta distribution model
Before performing the validation of existing analytical models, we introduce an additional empirical model of the probability distribution of transmittance based on the Beta distribution^[@beta].
The PDT in this model is defined by the Beta probability density function:

$$
%\label{Eq:pdt_beta}
\mathcal{P}(\eta; a, b) = \frac{1}{B(a, b)} \eta^{a-1} (1-\eta)^{b-1}.
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

## Results and discussion
### Weak channel
- Rytov parameter $\sigma_\mathrm{R}^2=0.2$ 
- Overview
    - channel length $z_\mathrm{ap}=1\text{ km}$
    - structure constant for the index of refraction $C_n^2=5\times10^{-15}$ (m$^{-2/3}$)
    - initial beam-spot radius at the transmitter, $W_0=2$~(cm)
    - wavelength $\lambda=2\pi/k=809$~(nm) 
    - outer scale $L_0=80$~(m)
    - inner scale $\ell_0=10^{-3}$~(m)
- "For $F_0=+\infty$, the Rayleigh length is $z_\mathrm{R}=kW_0^2/2\approx1.553~\mathrm{km}$, which is greater than the channel length $z_\mathrm{ap}{=}1~\mathrm{km}$."
- Simulation parameters:
    -  spatial grid with 512 points along one axis
    - spatial grid steps are 0.3 mm
    - The number of spectral rings is $N=1024$
    - "The inner and outer bounds of the spectrum are $K_\mathrm{min}=1/15 L_0$ and $K_\mathrm{max}=2/\ell_0$, respectively"
    - "The number of phase screens is chosen from the condition that the Rytov parameter for the interscreen distance does not exceed $0.1$ (cf.~Refs.~\cite{Schmidt_book,Martin1988}). It is equal to 10" 
        - the Rytov parameter for the interscreen distances in these cases are $3\times10^{-3}$ 
    - The number of samples $M=10^5$ for all channels
- we will consider two types of source beam collimated -- F = infty -- and focused -- F = z_ap.
    - this will have significant differece in some aspects.
- note logarithmic scale. we recall the the same visual distance between for example 10-3 to 10-2 and 10-2 to 10-1 corresponds to 10 times different actual distance.
#### Collimated beam


![\label{fig:ks_weak_inf}Weak zap](images/validation/weak_inf_ks_values.svg)
- Despite the physically motivated nature of the beam wandering and elliptical beam models they show the worst agreement with the numerical PDT.
    - elliptic beam minima, of fig 2
- The truncated lognormal model reproduces the numerical PDT fairly well for small apertures, but its accuracy degrades for larger apertures. 
- The reason is the change of skewness in the numerical PDT—from positive to negative—as the aperture increases, while the truncated lognormal distribution remains positively skewed for any parameters.
- The total probability models show performance nearly identical to their base distributions. 
    - ?since beam wander effects are weak?.
- The beta distribution provides the best overall agreement, with its KS statistic reaching a minimum around $\langle\eta\rangle=0.5$, where the numerical PDT is nearly symmetric.

![\label{fig:pdt_weak_inf}Weak inf](images/validation/weak_inf_pdt_0_03.svg)

- At the aperture corresponding to the elliptical beam model’s KS minimum, the mode of the distribution coincides with the mode of the numerical PDT, which can be seen in the fig X. 
    - At other aperture sizes this model has biased mode and transmittance modes.
- the BW assumes fixed shape of the beam, so the transmittance can't be bigger then the trasmittance of the coaxial circular beam of coresponding width.
    - this is reflected in the distinct shape of the beam wandering model, which can't catch the right tail of the numerical distribution.
- Overall, for weak turbulence the transmittance fluctuations are small, and the PDT tends to a quasi-Gaussian shape whenever $0 \ll \langle\eta\rangle \ll 1$.

#### Focused beam


![\label{fig:ks_weak_zap}Weak zap](images/validation/weak_zap_ks_values.svg)

For the focused beam, all analytical models show poorer agreement with numerical PDTs than in the collimated case. 
This should not be misinterpreted as a degradation of channel performance. 
A focused beam typically produces a smaller spot at the aperture plane and thus achieves a higher average transmittance for the same aperture radius, improving overall link efficiency. 
The lower KS scores here simply indicate that existing analytical PDT models fail to capture the more complex field statistics in this focusing regime.

Among all models, the total probability models demonstrate the best performance, especially for small to moderate aperture sizes.

- However, when the aperture radius $R_\text{ap} \gtrsim W_\text{LT}$  the total probility models can't be defined.
    - In this domain the beta model produce best performance.

![\label{fig:pdt_weak_zap}Weak zap](images/validation/weak_zap_pdt_0_015.svg)

- The truncated lognormal model shows mismatched skewness and a physically unrealistic finite probability density at $\eta \to 1$ due to truncation.
- elliptic beam model have biased mean transmittance 
- The beta model, while based on matching the first two moments, underestimates higher-order moments (skewness and kurtosis).
    - When combined with the beam wandering statistics in the total probability model, however, the resulting PDT matches the numerical distribution almost perfectly in both shape and position.
### Moderate channel

- "is 1.6 km. Such a channel has been implemented in Erlangen, Germany"
#### Collimated Beam
- For small apertures, the beta model provides the best fit to the numerical PDT.
    - However, for small apertures beta total probability model performs even worse than than simple beta model.
- As shown in Fig. X, the beta model reproduces the overall shape and width of the numerical PDT accurately.
    - In contrast, the truncated lognormal model—although defined via the first two moments—produces a narrower distribution and underestimates the variance.
    - This bias originates from the fact that truncation changes the actual moments of the distribution; the fitted parameters correspond to the full (untruncated) lognormal rather than the truncated one.
- At apertures $R_\text{ap}\approx W_\text{LT}$, the total probability models outperform all others. 
    - Here, also, the modes of the beam wandering  and elliptical beam models coincide with the mode of the numerical PDT, resulting in the KS minima for these models.

![\label{fig:pdt_moderate_inf}Moderate inf](images/validation/moderate_inf_ks_values.svg)



![\label{fig:ks_moderate_inf}Moderate inf](images/validation/moderate_inf_pdt_0_05.svg)

#### Focused Beam

![\label{fig:pdt_moderate_zap}Moderate zap](images/validation/moderate_zap_ks_values.svg)

- As in the weak channel, the focused beam results in generally worse agreement between analytical and numerical models than the collimated beam.
- The beta model again performs best, outperformed a bit by the total probability models when the aperture is around $R_\text{ap}\approx W_\text{LT}$.
- When the modes of beam wandering and elliptic beam modes match numerical PDT at ~1 they shows best performance. 
- in the fig X we can see the reason of generally worse performance

![\label{fig:ks_moderate_zap}Moderate zap](images/validation/moderate_zap_pdt_0_012.svg)

- The numerical PDT in this regime develops a highly non-Gaussian plateau, with nearly constant probability density over a finite interval of η.
- This feature cannot be reproduced by any of the studied parametric models, all of which assume unimodal, smoothly decaying distributions.

### Strong channel

![\label{fig:pdt_moderate_inf}Moderate inf](images/validation/strong_inf_ks_values.svg)

- Interestingly, the behavior of the 33 Rytov channel resembles that of the moderate focused channel with sigma_rytov2 = 5.
- The only difference is that for very small apertures $R_\text{ap} \lesssim 0.1W_\text{LT}$ the truncated lognormal model shows slightly better performance (see Fig. X).

![\label{fig:ks_strong_inf}Strong inf](images/validation/strong_inf_pdt_0_1.svg)

- In this range, the beta model changes its shape to the $(1-\eta)^{\beta-1}$ - like shape when the shape of the numerical PDT still resembles the lognormal shape.

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
Among the considered models, the total probability models and the Beta model most successfully reproduce the skewness of the numerical PDT.

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

# Statistical properties of the beam shape parameters
The statistical behavior of optical beam-shape parameters after propagation through a turbulent atmosphere forms the core set of assumptions underlying physically motivated analytical models such as the beam-wandering model, the elliptical-beam model, and the total-probability framework.
These assumptions include: the distribution of the beam-centroid position, the statistical independence between the beam-centroid position and the beam-spot shape, and the Gaussian statistics of the beam semiaxes.
However, these assumptions are accepted without strong empirical support.
This introduces a potential source of systematic inaccuracy.
Therefore, it is essential to examine and validate these assumptions through numerical simulations.

## Distribution of the beam-centroid position
Beam wandering is the most prominent effect of the light beam propagating through a turbulent atmosphere. 
It arises primarily from large-scale turbulent eddies, which cause the entire beam spot to shift away from the propagation axis.
This phenomenon is explicitly included in all three analytical models discussed above, where the beam-centroid displacement is assumed to follow a two-dimensional Gaussian distribution.

Empirical evidence supporting this Gaussian assumption is limited, as the number of realizations is generally small (e.g., ^[@luo2025]). 
Consequently, it does not allow confident estimation of higher-order moments, such as skewness or kurtosis, and it does not cover a wide range of turbulence strengths. 
To address this, we perform a systematic numerical study across several turbulence strengths.

Given the isotropy of turbulence, the distribution of the beam centroid is radially symmetric. 
Consequently, it is sufficient to consider only a single-dimensional projection along the $x$-axis -- the beam-centroid coordinate $x_0$, defined as^[eq:x0].
To verify whether the distribution is Gaussian, we generate $5\cdot10^{5}$ realizations of beam propagation, compute the corresponding values of $x_0$ according to ^[eq:x0], and estimate the higher-order moments -- the skewness and excess kurtosis^[@joanes1998].
These higher-order moments provide a quantitative measure of deviations from the Gaussian assumption: skewness captures asymmetry in the distribution, while excess kurtosis reflects the presence of heavy tails or peakedness.

To systematically evaluate the effect of turbulence strength, we perform this analysis across a range of atmospheric conditions, spanning weak to strong turbulence. 
The same three types of propagation channels considered in ^[sec:validation] will be used to maintain consistency with previous analyses. 

>The parameters of these channels are listed in ^[tab:channels].
> - [ ] BW not depends of F

### Weak turbulence channel

We begin with the weak-turbulence channel of propagation length $L=1\text{km}$, characterized by a Rytov variance $\sigma_\mathrm{R}^2=0.2$. 
The full set of channel parameters is listed in ^[tab:weak]. 
For this channel, the distribution of the beam-centroid coordinate $x_0$ was estimated using a kernel density method for both the collimated and focused cases. 
The resulting probability density functions are shown in ^[fig:x0_weak].

![\label{fig:x0_weak}Weak inf zap](images/beam_shape/bw_weak_inf_zap.svg)

When compared with the Gaussian probability density function, both simulated curves exhibit an almost perfect match. 
The numerical values of skewness and excess kurtosis, listed in ^[tab:x0_weak], confirm this observation.

| Weak channel            | Skewness | Excess curtosis |
| :---------------------- | :------: | :-------------: |
| Collimated $F=\infty$   |  0.0058  |      0.014      |
| Focused $F=z_\text{ap}$ | −0.0043  |     −0.0038     |

The skewness and excess kurtosis are effectively zero. 
These results indicate that, under weak turbulence, the beam-centroid displacement can be reliably modeled as a two-dimensional Gaussian random variable for both collimated and focused beams. 
This directly supports the standard assumption used in analytical models for the weak-turbulence regime.

### Moderate turbulence channel
We next consider a stronger turbulence condition with propagation length $L=1.6\text{km}$ and Rytov variance $\sigma^2_\text{R}=1.5$.
The full set of channel parameters is given in ^[tab:moderate].
The kernel-estimated probability density functions of the beam-centroid coordinate $x_0$ for both the collimated and focused beams are shown in ^[fig:x0_moderate].

![\label{fig:bw_moderate}Moderate inf zap](images/beam_shape/bw_moderate_inf_zap.svg)

Both distributions remain very close to the Gaussian reference. 
In the focused case, the peak appears slightly asymmetric by visual inspection, but the numerical skewness reported in ^[tab:x0_moderate] is essentially zero, indicating that this deviation can be considered as statistical noise.

| Weak channel            | Skewness | Excess curtosis |
| :---------------------- | :------: | :-------------: |
| Collimated $F=\infty$   |  0.0172  |     −0.0046     |
| Focused $F=z_\text{ap}$ |  −0.003  |     −0.0279     |

In both cases, the skewness and excess kurtosis remain very small. 
Thus, even at moderate turbulence strength, the beam-centroid position continues to be well described by a two-dimensional Gaussian random variable.

### Strong turbulence channel
Finally, we consider the strong-turbulence channel with propagation length $L=50\text{km}$ and Rytov variance $\sigma_\text{R}^2=33.3$. 
The full set of channel parameters is given in ^[tab:strong].
The kernel-estimated probability density function of the beam-centroid coordinate $x_0$ is shown in ^[fig:bw_strong].

![\label{fig:bw_strong}Strong inf](images/beam_shape/bw_strong_inf.svg)

The distribution remains approximately Gaussian, but a noticeable deviation appears at the peak. 
This is reflected in the negative excess kurtosis reported in^[tab:x0_strong]:

| Weak channel          | Skewness | Excess curtosis |
| :-------------------- | :------: | :-------------: |
| Collimated $F=\infty$ |  0.0008  |     −0.1064     |
The skewness is essentially zero, but the negative excess kurtosis indicates a slight platykurtic shape. 
This confirms a mild departure from Gaussianity at very strong turbulence conditions.
However, the deviation is still modest, so for most analytical purposes the Gaussian assumption remains sufficiently accurate even in this regime.

## Quantifying contribution of beam wandering to the PDT
Beam wandering is one of the dominant low-order turbulence-induced perturbations of an optical beam. 
It appears together with large-scale beam-shape deformation and small-scale scintillation. 
This subsection investigates how beam wandering alone contributes to the transmittance. 

Identifying regimes where beam wandering is the main driver of transmittance variability clarifies when analytical models that include this effect are more applicable, and when more complex models are required. 
In addition, in practical free-space experiments, adaptive-optics systems are often used to mitigate random centroid displacement ^[@tyson2015]. 
When the correlation between wandering and transmittance is high, such techniques can offer substantial performance improvements, emphasizing the practical relevance of this analysis for adaptive-optics applications.

To quantify the contribution of beam wandering, we compute the Pearson correlation coefficient between the centroid displacement $r_0$ and the transmittance $\eta$, defined as

$$%\label{eq:r0eta}
S(r_0,\eta)=\frac{\left\langle\Delta r_0 \Delta\eta\right\rangle}{\sqrt{\left\langle\Delta r_0^2\right\rangle\left\langle \Delta\eta^2\right\rangle}}$$

For every atmospheric channel listed in ^[@sec:validation] and for each aperture radius, we perform $5\cdot10^5$ independent beam-propagation simulations, compute $r_0 = \sqrt{x_0^2 + y_0^2}$, where $x_0$ is defined as^[eq:x0] and $y_0$ is defined in the same way, evaluate transmittance $\eta$ according to ^[eq:eta] and estimate $S(r_0,\eta)$ ^[eq:r0eta].
The dependence of the correlation on the aperture radius is shown in ^[@fig:r0eta].

![\label{fig:fig:r0eta}Strong inf](images/beam_shape/original_r_0_eta.pdf)


Across all atmospheric channels, the correlation between centroid displacement and transmittance is negative, reflecting the obvious fact that larger beam wandering reduces received power.
The magnitude of this correlation strongly depends on the ratio between the aperture radius and the long-term beam radius $R_\text{ap}/W_\text{LT}$.

For aperture radii much larger than $W_\text{LT}$, almost the full beam enters the receiver aperture regardless of its displacement. 
The correlation in this case close to zero.
For aperture radii much smaller than $W_\text{LT}$, the beam is strongly clipped even without wandering. 
Variations in the centroid position change the already-strong clipping only slightly, so the correlation again becomes small.
The strongest correlation appears in the intermediate regime when
$R_\text{ap} \lesssim W_\text{LT}$.
Here, the aperture captures the central part of the beam, and centroid motion produces large changes in overlap of the field intensity and the aperture.
The minimum typically occurs around $R_\text{ap} \approx 0.5 W_\text{LT}$.

A clear trend also appears when comparing channels with initial curvature $F_0 = z_\text{ap}$ and $F_0 = +\infty$. 
Channels with the geometrically focused beams show larger correlations.
A plausible interpretation is that focused beams exhibit smaller spreading fluctuations, meaning that transmittance fluctuations come less from beam-size changes and more from centroid displacement. 
With spreading variation suppressed, wandering has a comparatively stronger impact on the received power, which increases the correlation.
This also explains why the total-probability model performs particularly well for the corresponding weak channel ^[@sec:weak_zap_valid] and for the moderate channel in the region $R_\text{ap} \lesssim W_\text{LT}$ ^[@sec:moderate_zap_valid].

It is commonly accepted that in weak turbulence the beam is mainly affected by wandering, while in stronger turbulence small-scale distortions and speckles dominate the beam structure ^[@Atmos]. 
Based on these observations, it is often assumed in the literature that models based on the beam-wandering effect should perform better in weak turbulence^[@vasylyev2012,vasylyev2016], whereas in strong turbulence the lognormal model is expected to be more appropriate^[@vasylyev2018], as it represents the limiting statistics of multiplicative small-scale distortions. 
Moreover, fitting of such analytical models to experimental data sets for a weak-turbulence channel in Erlangen^[@vasylyev2016,usenko2012] and for a strong-turbulence channel on the Canary Islands^[@capraro2012] has been interpreted as supporting this picture, although this agreement appears to be accidental and results by the particular aperture size used in those experiments^[sec:see_validataion_disscus].

>“This is justified for weak turbulence, when speckles play no essential role.” ([Vasylyev et al., 2016, p. 1](zotero://select/library/items/QEV8ZWED)) ([pdf](zotero://open-pdf/library/items/J49VGVHY?page=1&annotation=HLNYWFKI))
>“Aperture transmission coefficient.– For weak absorption, beam-wandering losses are dominant.” ([Vasylyev et al., 2012, p. 2](zotero://select/library/items/MTFCYJ8H)) ([pdf](zotero://open-pdf/library/items/DHFQCSBE?page=2&annotation=PTZWZMYV))
>“For some cases with long propagation lengths or strong turbulence, the effects of beam-spot distortions significantly dominate the resulting statistics, compared to the effects of beam wandering. In this case, the PDT can be approximated with reasonable accuracy by the truncated log-normal distribution” ([Vasylyev et al., 2018, p. 3](zotero://select/library/items/QRZKWNB4)) ([pdf](zotero://open-pdf/library/items/6VZUIQVQ?page=3&annotation=Z3TGZBAQ))

However, as seen in ^[@fig:r0eta], the correlation between centroid displacement and transmittance for the weak-turbulence channel with $F_0=+\infty$ is lower than for all other channels. 
In general, the maximal correlation between centroid displacement and transmittance increases with turbulence strength. 
This demonstrates that the mentioned above practice of extrapolating *statistical observations about the beam shape* directly to the *statistics of the transmittance* is not justified.

> Unnecessary:
>- Its impact is also strongly modulated by the receiver aperture.
>    - in this section, the importance of aperture isn't clear. It's for validation section

## Beam-wandering and beam-shape correlations

A fundamental assumption of the total-probability model is that beam wandering and beam-shape fluctuations are statistically independent.
Validating this assumption is crucial for understanding the interplay between beam-centroid wandering and beam-shape distortions, as well as for evaluating the validity of analytical models that factorize these contributions.

We address this question using two complementary approaches.
The first approach is a natural extension of the analysis presented in the previous subsection, with one key modification.
As before, for each of the $5\cdot10^5$ simulated realizations we calculate the centroid displacement $r_0$.
However, instead of measuring the transmittance $\eta$, we shift the receiver aperture to the instantaneous centroid position and evaluate the resulting transmittance, denoted $\eta_{r_0}$.
This procedure emulates an ideal adaptive-optics system that fully compensates for beam wandering.
By analyzing the correlation between $r_0$ and $\eta_{r_0}$ with the Pearson correlation coefficient
$$%\label{eq:r0etar0}
S(r_0,\eta_{r_0})=\frac{\left\langle\Delta r_0 \Delta\eta_{r_0}\right\rangle}{\sqrt{\left\langle\Delta r_0^2\right\rangle\left\langle \Delta\eta_{r_0}^2\right\rangle}}$$
we isolate the statistical relationship between centroid motion and the residual beam-shape fluctuations, independent of the displacement effect.
The results are summarized in ^[@fig:r0eta0].

![\label{fig:fig:r0eta0}corr](images/beam_shape/original_r_0_eta_tracked.pdf)

For the majority of atmospheric channels and aperture radii, the correlations are very weak, indicating that beam centroid displacements and higher-order beam-shape fluctuations are largely independent.
Slightly higher correlations are observed in the strong-turbulence channel for small aperture radii, where realizations with larger centroid displacements $r_0$ tend to produce smaller transmittance values compared to realizations with $r_0$ near the optical axis.

In the second approach, we focus on the statistical relationship between the beam centroid displacement $r_0$ and the instantaneous beam width.
Unlike the first approach, which evaluates correlations through the measured transmittance and therefore includes aperture effects, this method directly characterizes the intrinsic properties of the beam itself, independent of any receiver geometry.
However, in this approach, small-scale random intensity fluctuations, such as speckles, are effectively excluded, so that the correlation reflects only the large-scale beam spreading.
To properly account for the symmetry of the system, the beam width is defined along the direction of the centroid displacement vector $\mathbf{r}_0$, denoted $W_{r}$ (see example in ^[@fig:beamWr0]).

![\label{fig:beamWr0}example](images/beam_shape/original_beam_profile.pdf)

For this analysis, we use the same $5\cdot10^5$ simulated realizations of the atmospheric channels.
For each realization, the beam centroid displacement is represented by the vector $\mathbf{r}_0 = (x_0, y_0)^T$.
The coordinate system is subsequently rotated by the angle $\chi=\arctan\left({y_0/x_0}\right)$, yielding a new frame $(x_r, y_r)$ in which the $x_r$ axis is aligned with the direction of the beam-centroid displacement vector $\mathbf{r}_0$.
In this rotated frame, the beam width $W_r$ along the $x_r$ axis is measured^[eq:ST2] for each realization.
The Pearson correlation coefficient between the magnitude of the centroid displacement $r_0$ with the corresponding beam width $W_r$ along the $x_r$ axis is estimated as
$$%\label{eq:r0etar0}
S\left(r_0,W_r\right)=\frac{\left\langle\Delta r_0 \Delta W_r\right\rangle}{\sqrt{\left\langle\Delta r_0^2\right\rangle\left\langle \Delta W_r^2\right\rangle}}$$

The resulting correlation values for all atmospheric channels are summarized in ^[@tab:r0Wr].

| Channel  | $F_0=+\infty$ | $F_0=z_\text{ap}$ |
| -------- | :-----------: | :---------------: |
| Weak     |     0.016     |       0.039       |
| Moderate |     0.08      |       0.15        |
| Strong   |     0.32      |         -         |

Overall, the correlations are small in the weak and moderate channels, indicating that beam wandering and large-scale spreading remain largely independent in these regimes.
A noticeable increase appears only for the strong-turbulence channel, indicating that, on average, beams become wider when their centroids deviate further from the propagation axis.
The strength of this effect grows with increasing turbulence.

These results complement the conclusions of the first approach: when turbulence is weak or moderate, centroid motion can be treated as effectively independent of beam-shape variations.
Only under strong turbulence a measurable dependence arises, but even then, its impact on the transmittance remains modest.

## Distribution of the beam semiaxis

> Conclusion?
>>The PDT depends on the interplay of:
>>beam wandering,
>>beam width variations,
>>beam-shape distortions,
>>speckles,
>>and crucially: aperture size.