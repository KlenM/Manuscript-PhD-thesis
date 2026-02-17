# Statistical properties of the beam shape parameters {#sec:beamshape}
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
Consequently, it is sufficient to consider only a single-dimensional projection along the $x$-axis---the beam-centroid coordinate $x_0$, defined as^[eq:x0].
To verify whether the distribution is Gaussian, we generate $5\cdot10^{5}$ realizations of beam propagation, compute the corresponding values of $x_0$ according to ^[eq:x0], and estimate the higher-order moments---the skewness and excess kurtosis^[@joanes1998].
These higher-order moments provide a quantitative measure of deviations from the Gaussian assumption: skewness captures asymmetry in the distribution, while excess kurtosis reflects the presence of heavy tails or peakedness.

To systematically evaluate the effect of turbulence strength, we perform this analysis across a range of atmospheric conditions, spanning weak to strong turbulence.
The same three types of propagation channels considered in ^[sec:validation] will be used to maintain consistency with previous analyses.

>The parameters of these channels are listed in ^[tab:channels].
> - [ ] BW not depends of F

### Weak turbulence channel

We begin with the weak-turbulence channel of propagation length $L=1\text{km}$, characterized by a Rytov variance $\sigma_\mathrm{R}^2=0.2$.
The full set of channel parameters is listed in ^[tab:weak_params].
For this channel, the distribution of the beam-centroid coordinate $x_0$ was estimated using a kernel density method for both the collimated and focused cases.
The resulting probability density functions are shown in ^[fig:x0_weak].

![\label{fig:x0_weak}Probability density function of the beam-centroid coordinate $x_0$ for a collimated and focused beam after propagation through a weak-turbulence channel ($\sigma_\mathrm{R}^2 = 0.2$). The shaded areas represent the distributions estimated from $5\cdot10^5$ numerical realizations using kernel density estimation, while the dashed lines indicate the theoretical Gaussian distribution.](beam_shape/bw_weak_inf_zap.svg)

When compared with the Gaussian probability density function, both simulated curves exhibit an almost perfect match.
The numerical values of skewness and excess kurtosis, listed in ^[tab:x0_weak], confirm this observation.

```{=latex}
\begin{table}[h]
\centering
\caption{Results for skewness and excess kurtosis for weak channels.}
\label{tab:x0_weak}
\begin{tabular}{l c c}
\hline
Weak channel & Skewness & Excess kurtosis \\
\hline
Collimated $F=\infty$ & 0.0058 & 0.014 \\
Focused $F=z_{\text{ap}}$ & $-0.0043$ & $-0.0038$ \\
\hline
\end{tabular}
\end{table}
```

> | Weak channel            | Skewness | Excess curtosis |
> | :---------------------- | :------: | :-------------: |
> | Collimated $F=\infty$   |  0.0058  |      0.014      |
> | Focused $F=z_\text{ap}$ | −0.0043  |     −0.0038     |

The skewness and excess kurtosis are effectively zero.
These results indicate that, under weak turbulence, the beam-centroid displacement can be reliably modeled as a two-dimensional Gaussian random variable for both collimated and focused beams.
This directly supports the standard assumption used in analytical models for the weak-turbulence regime.

### Moderate turbulence channel
We next consider a stronger turbulence condition with propagation length $L=1.6\text{km}$ and Rytov variance $\sigma^2_\text{R}=1.5$.
The full set of channel parameters is given in ^[tab:moderate_params].
The kernel-estimated probability density functions of the beam-centroid coordinate $x_0$ for both the collimated and focused beams are shown in ^[fig:x0_moderate].

![\label{fig:x0_moderate}Probability density function of the beam-centroid coordinate $x_0$ for a collimated and focused beam after propagation through a moderate-turbulence channel ($\sigma_\mathrm{R}^2 = 1.5$). The shaded areas represent the distributions estimated from $5\cdot10^5$ numerical realizations using kernel density estimation, while the dashed lines indicate the theoretical Gaussian distribution. ](beam_shape/bw_moderate_inf_zap.svg)

Both distributions remain very close to the Gaussian reference.
In the focused case, the peak appears slightly asymmetric by visual inspection, but the numerical skewness reported in ^[tab:x0_moderate] is essentially zero, indicating that this deviation can be considered as statistical noise.

```{=latex}
\begin{table}[h]
\centering
\caption{Results for skewness and excess kurtosis for moderate channels.}
\label{tab:x0_moderate}
\begin{tabular}{l c c}
\hline
Weak channel & Skewness & Excess kurtosis \\
\hline
Collimated $F=\infty$ & 0.0172 & $-0.0046$ \\
Focused $F=z_{\text{ap}}$ & $-0.003$ & $-0.0279$ \\
\hline
\end{tabular}
\end{table}
```

> | Weak channel            | Skewness | Excess curtosis |
> | :---------------------- | :------: | :-------------: |
> | Collimated $F=\infty$   |  0.0172  |     −0.0046     |
> | Focused $F=z_\text{ap}$ |  −0.003  |     −0.0279     |

In both cases, the skewness and excess kurtosis remain very small.
Thus, even at moderate turbulence strength, the beam-centroid position continues to be well described by a two-dimensional Gaussian random variable.

### Strong turbulence channel
Finally, we consider the strong-turbulence channel with propagation length $L=50\text{km}$ and Rytov variance $\sigma_\text{R}^2=33.3$.
The full set of channel parameters is given in ^[tab:strong_params].
The kernel-estimated probability density function of the beam-centroid coordinate $x_0$ is shown in ^[fig:x0_strong].

![\label{fig:x0_strong}Probability density function of the beam-centroid coordinate $x_0$ for a collimated beam after propagation through a strong-turbulence channel ($\sigma_\mathrm{R}^2 = 33.3$). The shaded area represents the distributions estimated from $5\cdot10^5$ numerical realizations using kernel density estimation, while the dashed line indicates the theoretical Gaussian distribution. ](beam_shape/bw_strong_inf.svg)

The distribution remains approximately Gaussian, but a noticeable deviation appears at the peak.
This is reflected in the negative excess kurtosis, see ^[tab:x0_strong].

```{=latex}
\begin{table}[h]
\centering
\caption{Results for skewness and excess kurtosis for strong channel.}
\label{tab:x0_strong}
\begin{tabular}{l c c}
\hline
Weak channel & Skewness & Excess kurtosis \\
\hline
Collimated $F=\infty$ & 0.0008 & $-0.1064$ \\
\hline
\end{tabular}
\end{table}
```

> | Weak channel          | Skewness | Excess curtosis |
> | :-------------------- | :------: | :-------------: |
> | Collimated $F=\infty$ |  0.0008  |     −0.1064     |


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

For every atmospheric channel listed in ^[sec:validation] and for each aperture radius, we perform $5\cdot10^5$ independent beam-propagation simulations, compute $r_0 = \sqrt{x_0^2 + y_0^2}$, where $x_0$ is defined as^[eq:x0] and $y_0$ is defined in the same way, evaluate transmittance $\eta$ according to ^[eq:eta] and estimate $S(r_0,\eta)$ ^[eq:r0eta].
The dependence of the correlation on the aperture radius is shown in ^[fig:r0eta].

![\label{fig:r0eta}Pearson correlation coefficient $S(r_0, \eta)$ between the beam-centroid displacement $r_0$ and transmittance $\eta$ as a function of the normalized aperture radius $R_\text{ap}/W_\text{LT}$. The plots compare collimated ($F_0 = +\infty$) and focused ($F_0 = z_\text{ap}$) beams across weak (W), moderate (M), and strong (S) turbulence regimes.](beam_shape/original_r_0_eta.pdf)


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
This also explains why the total-probability model performs particularly well for the corresponding weak channel ^[sec:valid_weak] and for the moderate channel in the region $R_\text{ap} \lesssim W_\text{LT}$ ^[sec:valid_moderate].

It is commonly accepted that in weak turbulence the beam is mainly affected by wandering, while in stronger turbulence small-scale distortions and speckles dominate the beam structure ^[@andrews2005].
Based on these observations, it is often assumed in the literature that models based on the beam-wandering effect should perform better in weak turbulence^[@vasylyev2012,vasylyev2016], whereas in strong turbulence the lognormal model is expected to be more appropriate^[@vasylyev2018], as it represents the limiting statistics of multiplicative small-scale distortions.
Moreover, fitting of such analytical models to experimental data sets for a weak-turbulence channel in Erlangen^[@vasylyev2016,usenko2012] and for a strong-turbulence channel on the Canary Islands^[@capraro2012] has been interpreted as supporting this picture, although this agreement appears to be accidental and results by the particular aperture size used in those experiments^[sec:validation].

>"This is justified for weak turbulence, when speckles play no essential role." ([Vasylyev et al., 2016, p. 1](zotero://select/library/items/QEV8ZWED)) ([pdf](zotero://open-pdf/library/items/J49VGVHY?page=1&annotation=HLNYWFKI))
>"Aperture transmission coefficient.– For weak absorption, beam-wandering losses are dominant." ([Vasylyev et al., 2012, p. 2](zotero://select/library/items/MTFCYJ8H)) ([pdf](zotero://open-pdf/library/items/DHFQCSBE?page=2&annotation=PTZWZMYV))
>"For some cases with long propagation lengths or strong turbulence, the effects of beam-spot distortions significantly dominate the resulting statistics, compared to the effects of beam wandering. In this case, the PDT can be approximated with reasonable accuracy by the truncated log-normal distribution" ([Vasylyev et al., 2018, p. 3](zotero://select/library/items/QRZKWNB4)) ([pdf](zotero://open-pdf/library/items/6VZUIQVQ?page=3&annotation=Z3TGZBAQ))

However, as seen in ^[fig:r0eta], the correlation between centroid displacement and transmittance for the weak-turbulence channel with $F_0=+\infty$ is lower than for all other channels.
In general, the maximal correlation between centroid displacement and transmittance increases with turbulence strength.
This demonstrates that the mentioned above practice of extrapolating statistical observations about the beam shape directly to the statistics of the transmittance is not justified.

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
$$
S(r_0,\eta_{r_0})=\frac{\left\langle\Delta r_0 \Delta\eta_{r_0}\right\rangle}{\sqrt{\left\langle\Delta r_0^2\right\rangle\left\langle \Delta\eta_{r_0}^2\right\rangle}}$$
we isolate the statistical relationship between centroid motion and the residual beam-shape fluctuations, independent of the displacement effect.
The results are summarized in ^[fig:r0eta0].

![\label{fig:r0eta0} Pearson correlation coefficient $S(r_0, \eta_{r_0})$ between the beam-centroid displacement $r_0$ and the tracked transmittance $\eta_{r_0}$ (where the aperture is centered on the instantaneous beam center). The results cover weak (W), moderate (M), and strong (S) turbulence channels for both collimated ($F_0 = +\infty$) and focused ($F_0 = z_\text{ap}$) beams.](beam_shape/original_r_0_eta_tracked.pdf)

For the majority of atmospheric channels and aperture radii, the correlations are very weak, indicating that beam centroid displacements and higher-order beam-shape fluctuations are largely independent.
Slightly higher correlations are observed in the strong-turbulence channel for small aperture radii, where realizations with larger centroid displacements $r_0$ tend to produce smaller transmittance values compared to realizations with $r_0$ near the optical axis.

In the second approach, we focus on the statistical relationship between the beam centroid displacement $r_0$ and the instantaneous beam width.
Unlike the first approach, which evaluates correlations through the measured transmittance and therefore includes aperture effects, this method directly characterizes the intrinsic properties of the beam itself, independent of any receiver geometry.
However, in this approach, small-scale random intensity fluctuations, such as speckles, are effectively excluded, so that the correlation reflects only the large-scale beam spreading.
To properly account for the symmetry of the system, the beam width is defined along the direction of the centroid displacement vector $\mathbf{r}_0$, denoted $W_{r}$ (see example in ^[fig:beamWr0]).

![\label{fig:beamWr0}Representative realization of an instantaneous beam intensity profile illustrating the coordinate rotation used for width measurement. The vector $\mathbf{r}_0$ indicates the displacement of the beam centroid from the optical axis. The coordinate system is rotated by angle $\chi$ to align the $x_r$ axis with the wandering direction, allowing for the direct measurement of the beam width $W_r$ along the axis of displacement.](beam_shape/original_beam_profile.pdf)

For this analysis, we use the same $5\cdot10^5$ simulated realizations of the atmospheric channels.
For each realization, the beam centroid displacement is represented by the vector $\mathbf{r}_0 = (x_0, y_0)^T$.
The coordinate system is subsequently rotated by the angle $\chi=\arctan\left({y_0/x_0}\right)$, yielding a new frame $(x_r, y_r)$ in which the $x_r$ axis is aligned with the direction of the beam-centroid displacement vector $\mathbf{r}_0$.
In this rotated frame, the beam width $W_r$ along the $x_r$ axis is measured for each realization.
The Pearson correlation coefficient between the magnitude of the centroid displacement $r_0$ with the corresponding beam width $W_r$ along the $x_r$ axis is estimated as
$$
S\left(r_0,W_r\right)=\frac{\left\langle\Delta r_0 \Delta W_r\right\rangle}{\sqrt{\left\langle\Delta r_0^2\right\rangle\left\langle \Delta W_r^2\right\rangle}}$$

> - [ ] Define $W_r$...

The resulting correlation values for all atmospheric channels are summarized in ^[tab:r0Wr].

```{=latex}
\begin{table}[h]
\centering
\caption{Pearson correlation coefficient $S(r_0, W_r)$ between beam centroid displacement and beam width in the rotated frame.}
\label{tab:r0Wr}
\begin{tabular}{l c c}
\hline
Channel & $F_0=+\infty$ & $F_0=z_{\text{ap}}$ \\
\hline
Weak & 0.016 & 0.039 \\
Moderate & 0.08 & 0.15 \\
Strong & 0.32 &  \\
\hline
\end{tabular}
\end{table}
```

> | Channel  | $F_0=+\infty$ | $F_0=z_\text{ap}$ |
> | -------- | :-----------: | :---------------: |
> | Weak     |     0.016     |       0.039       |
> | Moderate |     0.08      |       0.15        |
> | Strong   |     0.32      |         -         |

Overall, the correlations are small in the weak and moderate channels, indicating that beam wandering and large-scale spreading remain largely independent in these regimes.
A noticeable increase appears only for the strong-turbulence channel, indicating that, on average, beams become wider when their centroids deviate further from the propagation axis.
The strength of this effect grows with increasing turbulence.

These results complement the conclusions of the first approach: when turbulence is weak or moderate, centroid motion can be treated as effectively independent of beam-shape variations.
Only under strong turbulence a measurable dependence arises, but even then, its impact on the transmittance remains modest.

## Distribution of the beam semi-axes {#sec:semiaxes}

In this section we move beyond the analysis of beam wandering and beam spreading and examine the statistical behavior of the semi-axes of the elliptical Gaussian approximation of the beam shape.
This effect is a central element of the elliptical beam model ^[sec:pdt], which explicitly includes the influence of random fluctuations of the semi-axes $W_{1,2}$.
In this model the logarithms of the squared semi-axes are assumed to follow a bivariate Gaussian distribution.
However, the validity of this assumption is not established.

To test the validity of the Gaussian assumption, we generate $5\cdot10^{5}$ independent realizations of the beam propagations described in ^[sec:validation].
For every realization, we first compute the elements of the spot-shape matrix
$$\mathbf{S} = \begin{pmatrix} S_{xx} & S_{xy} \\ S_{xy} & S_{yy} \end{pmatrix}$$
using the definition given in ^[eq:Sshort_term].
This matrix describes the second-order moments of the beam intensity and determines both the orientation and the magnitudes of the semi-axes.
We then compute the eigenvalues of $\mathbf{S}$ as
$$W_{\pm}^2 = \frac{1}{2}\left( S_{xx}+S_{yy} \pm \sqrt{(S_{xx}-S_{yy})^2 + 4S_{xy}^2} \right)$$
which give the squared semi-axes of the ellipse aligned with the principal axes.

Next, we assign the ordered pair $W_{1}^{2}, W_{2}^{2}$ according to the orientation of the ellipse in the transverse plane.
If $S_{xy}>0$, then the principal axis corresponding to $W_{+}^{2}$ has a positive slope, and we take $W_{1}^{2}=W_{+}^{2}$ and $W_{2}^{2}=W_{-}^{2}$.
If $S_{xy}\le 0$, the orientation is reversed, and we set $W_{1}^{2}=W_{-}^{2}$ and $W_{2}^{2}=W_{+}^{2}$.
Finally, for each realization we compute the logarithmic variables
$$\Theta_{1,2} = \ln(W_{1,2}^2/W_0^2)$$
which are the quantities assumed to follow the bivariate Gaussian distribution in the elliptical beam model.

The scatter plot of the obtained pairs $(\Theta_1,\Theta_2)$ is shown in ^[fig:theta1theta2].

![\label{fig:theta1theta2}Scatter plot of the log-transformed squared semi-axes $(\Theta_1, \Theta_2)$. The result is compared to the covariance ellipse (dashed line).](beam_shape/original_theta_1_theta_2_strong_inf.pdf)

To compare the empirical distribution with the bivariate Gaussian approximation, we compute the sample mean vector $\left<\Theta_i\right>$ and the sample covariance matrix $\Sigma_{ij} = \langle \Delta\Theta_i \Delta\Theta_j \rangle$ and plot the corresponding covariance ellipse, defined by
$$
\sum\limits_{i,j=1}^2\big(\Theta_i-\langle\Theta_i\rangle\big)\Sigma_{ij}^{-1}\big(\Theta_j-\langle\Theta_j\rangle\big)=4$$
which represents the two-sigma contour expected under the Gaussian assumption.

Visual inspection of the scatter plot and the corresponding covariance ellipse shows clear deviations from the bivariate Gaussian model.
The dominant feature is a strong suppression of points along the diagonal $\Theta_{1}=\Theta_{2}$.
Apart from this suppression along the diagonal, there is also a noticeable deviation between the overall shape of the data and the covariance ellipse.
At the same time, the covariance ellipse is nearly circular, indicating that the linear correlation between $\Theta_{1}$ and $\Theta_{2}$ is weak.

To quantify these departures from Gaussianity, we rotate the coordinate system so that the transformed data becomes symmetric around $\Theta_{(s)}=0$.
The transformed variables are defined as
$$
\begin{split}
\Theta_{(s)}&=(\Theta_1-\Theta_2)/\sqrt{2}\\
\Theta_{(a)}&=(\Theta_1+\Theta_2)/\sqrt{2}
\end{split}$$
The variable $\Theta_{(s)}$ is proportional to the logarithm of the ratio of the squared semi-axes and thus captures their relative deformation.
The variable $\Theta_{(a)}$ is proportional to the logarithm of the product $W_1^2 W_2^2$, and therefore characterizes the overall beam area expansion.
For each turbulence regime, we compute the skewness and the excess kurtosis of both $\Theta_{(s)}$ and $\Theta_{(a)}$.
These statistics quantify the degree of non-Gaussianity, with the results summarized in ^[tab:thetasthetaa].

```{=latex}
\begin{table}[h!]
\centering
\caption{Higher-order moments of the transformed beam-shape variables $\Theta_{(s)}$ and $\Theta_{(a)}$ for different turbulence channels.}
\label{tab:thetasthetaa}
\begin{tabular}{|l|l|c|c|c|c|}
\hline
Channel & $F_0$ & \multicolumn{2}{c|}{Skewness} & \multicolumn{2}{c|}{Excess kurtosis} \\ \cline{3-6}
        &                              & $\Theta_{(s)}$ & $\Theta_{(a)}$ & $\Theta_{(s)}$ & $\Theta_{(a)}$ \\ \hline\hline
Weak     & $z_\text{ap}$               & $-0.6\times10^{-3}$ & $0.25$  & $-0.85$ & $0.23$ \\
         & $\infty$                     & $-10\times10^{-3}$  & $-0.1$  & $-1$    & $-0.006$ \\ \hline
Moderate & $z_\text{ap}$               & $9.8\times10^{-3}$  & $0.25$  & $-0.81$ & $0.12$ \\
         & $\infty$                     & $-3.7\times10^{-3}$ & $0.15$  & $-0.99$ & $-0.11$ \\ \hline
Strong   & $\infty$                     & $-9\times10^{-3}$   & $0.32$  & $-0.77$ & $0.25$ \\ \hline
\end{tabular}
\end{table}

```

> | Channel  | Initial beam curvature $F_0$ |            Skewness |                | Excess kurtosis |                |
> | -------- | -------------------------- | ------------------ | ------------- | -------------- | ------------- |
> |          |                              |      $\Theta_{(s)}$ | $\Theta_{(a)}$ |  $\Theta_{(s)}$ | $\Theta_{(a)}$ |
> | Weak     |        $z_\text{ap}$         | $-0.6\times10^{-3}$ |         $0.25$ |         $-0.85$ |         $0.23$ |
> |          |           $\infty$           |  $-10\times10^{-3}$ |         $-0.1$ |            $-1$ |       $-0.006$ |
> | Moderate |        $z_\text{ap}$         |  $9.8\times10^{-3}$ |         $0.25$ |         $-0.81$ |         $0.12$ |
> |          |           $\infty$           | $-3.7\times10^{-3}$ |         $0.15$ |         $-0.99$ |        $-0.11$ |
> | Strong   |           $\infty$           |   $-9\times10^{-3}$ |         $0.32$ |         $-0.77$ |         $0.25$ |

The distribution of $\Theta_{(s)}$ is highly symmetric, yet it is clearly platykurtic.
This behavior directly reflects the strong suppression of probability density at $\Theta_{(s)} = 0$ (equivalently, $\Theta_{1} = \Theta_{2}$), which is the dominant non-Gaussian feature of the data.
In contrast, the distribution of $\Theta_{(a)}$ is notably asymmetric, but its excess kurtosis is closer to zero.

Taken together, these observations show that the joint distribution of $\Theta_1$ and $\Theta_2$ cannot be adequately described by a bivariate Gaussian model, indicating that a deeper analysis of the statistical properties of $\mathbf{S}$ is necessary.
Understanding the behavior of the $\mathbf{S}$ eigenvalues can be further advanced through methods and insights from random matrix theory.

> - [ ] check  $\Theta_1+\Theta_2$ 1d distribution, relate to $S$...

> Conclusion?
>>The PDT depends on the interplay of:
>>beam wandering,
>>beam width variations,
>>beam-shape distortions,
>>speckles,
>>and crucially: aperture size.