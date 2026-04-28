# Time correlations in Atmospheric Quantum Channels {#sec:timecorr}

In the previous sections we treated the PDT as describing an ensemble of independent single-shot propagations of quantum states of light through a turbulent atmosphere.
This can also be viewed as a sequence of quantum states transmitted with sufficiently large time intervals, such that each transmission is effectively independent and no temporal correlations exist between them.
In practice, this idealization is overly simplistic.
Modern quantum optical systems often operate at MHz repetition rates.
At these repetition rates, consecutive pulses experience highly correlated atmospheric realizations.
As a result, the transmittance $\eta_t$ of consecutive pulses is correlated at different times $t$.

In this section we analyze the case of two consecutive pulses separated by a time interval $\tau$.
With the numerical model, we compute the joint statistics of two consecutive transmittances.
In particular, we study how the temporal correlation of the transmittance depends on the time separation $\tau$.
We also describe the PDT in scenarios relevant for adaptive selection techniques^[@vallone2015], where the first signal is a strong classical pulse used to estimate the channel transmittance, and the second is a quantum signal whose transmittance is conditioned on the measured transmittance of the first.
In ^[sec:application], we will demonstrate how these results guide continuous-variable and discrete-variable entanglement propagation protocols, and how they can be employed to enhance the preservation of nonclassicality through adaptive selection techniques.
This chapter is based on results presented in our works \ref{mypaper2} and \ref{mypaper4}.

## Two-time PDT
To describe the two-time PDT, we extend the PDT framework (see ^[sec:aqc]) to account for time-dependent fluctuations of the refractive index. In this approach, the refractive index is represented as
$$n_t(\mathbf{r},z)=1+\delta n_t(\mathbf{r},z),$$
where $\delta n_t(\mathbf{r},z)$ denotes the small, time-dependent, stochastic perturbation caused by atmospheric turbulence.
The evolution of the complex field amplitude $u_t(\mathbf{r},z)$ under these conditions is governed by the paraxial wave equation (see ^[eq:parax]), which, for a time-dependent refractive index, takes the form
$$
2ik\frac{\partial u_t(\mathbf{r},z)}{\partial z}+\Delta_\mathbf{r}
u_t(\mathbf{r},z)+2k^2\delta n_t(\mathbf{r},z) u_t(\mathbf{r},z)=0.
$$
To specify the temporal evolution of the refractive index we adopt the Taylor frozen-turbulence hypothesis (see ^[eq:taylor_n]) described in ^[sec:turb].
Under this assumption, time-dependent turbulence can be represented as a frozen spatial pattern advected by the wind.

The transmittance through a receiving aperture $\mathcal{A}$ at time $t$ is then given by the aperture-averaged intensity of the propagated field
$$
\eta_t=\int_\mathcal{A}d^2\mathbf{r} \left|u_t(\mathbf{r},z_\mathrm{ap})\right|^2.
$$
We consider two temporal modes at $t=0$ and $t=\tau$.
The two-mode input–output relation for the Glauber P function for channels with fixed linear losses $\eta_0$ and $\eta_\tau$ reads by analogy with the single-time relation (see ^[eq:PoutPin])
$$
P_\mathrm{out}(\alpha_0,\alpha_\tau|\eta_0,\eta_\tau)=
\frac{1}{\eta_0\eta_\tau}P_\mathrm{in}\left(\frac{\alpha_0}{\sqrt{\eta_0}},\frac{\alpha_\tau}{\sqrt{\eta_\tau}}\right).
$$
Averaging over the atmospheric realizations leads to the input-output relation for the two-time channel
$$P_\mathrm{out}(\alpha_0,\alpha_\tau)=
\int_\Xi d\eta_0d\eta_\tau \left[\frac{1}{\eta_0\eta_\tau}P_\mathrm{in}\left(\frac{\alpha_0}{\sqrt{\eta_0}},\frac{\alpha_\tau}{\sqrt{\eta_\tau}}\right)\right]\, \mathcal{P}(\eta_0,\eta_\tau),$$
where $\Xi=[0,1]\times[0,1]$, and where the joint distribution $\mathcal{P}(\eta_0,\eta_\tau)$ is the two-time PDT.

The two-time PDT provides a complete description of such atmospheric quantum channels.
The single-time PDT is obtained as its marginal
$$\mathcal{P}(\eta_0) = \int d\eta_\tau \mathcal{P}(\eta_0,\eta_\tau).$$
Adaptive selection protocols rely on conditional statistics.
If the protocol keeps only those events for which the first classical probe pulse has transmittance $\eta_0 \ge \eta_\mathrm{min}$, then the conditional PDT describing the second quantum pulse at time $t=\tau$ is
$$\mathcal{P}(\eta_\tau|\eta_0 \geq  \eta_\mathrm{min}) = \frac{1}{\overline{\mathcal{F}}(\eta_\mathrm{min})} \int_{\eta_\mathrm{min}}^{1} \mathrm{d}\eta_0 \mathcal{P}(\eta_\tau,\eta_0),$$
where
$$\overline{\mathcal{F}}(\eta_\mathrm{min}) = \int_{\eta_\mathrm{min}}^{1} \mathrm{d}\eta_0 \mathcal{P}(\eta_0)$$
is the exceedance.
This conditional PDT directly determines the statistics of accepted pulses and therefore the performance of adaptive schemes.
It also makes it possible to compute the moments that are required for the analysis of entanglement decay in continuous-variable and discrete-variable protocols.
This formulation makes it possible to track how these quantities depend on the pulse separation time, which is crucial for quantifying the influence of temporal correlations in quantum communication protocols.

#### Numerical approach.

For the numerical simulations we use the phase-screen method introduced in ^[sec:numsim].
We extend this model to the time-dependent case by incorporating the Taylor frozen-flow hypothesis.
First, we note that the wind-driven advection has a component in the longitudinal direction and a component in the transverse plane.
The longitudinal component produces pattern shifts that are much smaller than the channel length for the timescales that are relevant for our analysis.
Therefore, this component does not influence the temporal behavior in a measurable way and can be neglected in the simulations.

> to clearly identify the model / explanatory power / tractability / isolating the effect / causality / epistemic effect

We also assume that the advected wind velocity $v$ is constant at all points along the channel length.
While in reality the wind exhibits spatial inhomogeneity across the propagation path, this simplification is necessary to maintain model identifiability and tractability.
In principle, such inhomogeneity could be accounted for by assigning different velocities to each phase screen.
However, this approach would lead to an over-parameterized system with limited explanatory power.
By contrast, using a single velocity parameter $v$ for all phase screens ensures that the model remains tractable and allows us to isolate the specific effect of the wind-driven advection on the channel transmittance.

The coordinate system is rotated such that the new $x$-axis is aligned with the transverse wind direction.
Under this choice of coordinates, consider two optical pulses propagating through the channel, one at time $t=0$ and another at $t=\tau$.
The turbulence along the propagation path is represented by multiple phase screens, and for each screen, the realizations at these two times are related by
$$\varphi_{\tau}(x,y,z) = \varphi_0(x + v \tau, y, z),$$
where $s=v\tau$ represents the wind-driven shift of the turbulent pattern over the time interval $\tau$.

For the given wind velocity, the displacement $s$ and the time interval $\tau$ are interchangeable.
Accordingly, we will present the results mostly in terms of $s$.
For interpretation, we assume a typical wind speed of $v=10\text{m/s}$ unless stated otherwise, which implies that a spatial shift of $1\text{ cm}$ corresponds to $1\text{ ms}$ of the time interval $\tau$.
For any other desired wind speed $v$, the corresponding time interval can be obtained directly from the relation $\tau=s/v$.

We consider three atmospheric channels characterized by refractive index structure constants $C_n^2 = 1\times10^{-16}~\text{m}^{-2/3}$, $C_n^2 = 2\times10^{-16}~\text{m}^{-2/3}$, and $C_n^2 = 3\times10^{-16}~\text{m}^{-2/3}$.
For all channels the propagation distance is fixed at $z_{\text{ap}} = 50~\text{km}$.
These values correspond to Rytov parameters $\sigma_{\mathrm{R}}^2 = 5.5$, $\sigma_{\mathrm{R}}^2 = 11$, and $\sigma_{\mathrm{R}}^2 = 16.5$.
The inner and outer turbulence scales are set to $\ell_0 = 1~\text{mm}$ and $L_0 = 80~\text{m}$.
The source is a Gaussian beam of wavelength $\lambda = 808~\text{nm}$ with initial beam width $W_0 = 8~\text{cm}$ and curvature radius $F_0 = 50~\text{km}$.

The numerical grid contains $2048$ points in both transverse directions with a grid step of $1~\text{mm}$.
The sparse-spectrum phase-screen method (see ^[sec:numsim]) is used with $1024$ spectral rings.
The spectral bounds are defined as $K_\mathrm{min}=1/15 L_0$ and $K_\mathrm{max}=2/\ell_0$.
The propagation path is discretized into $15$ phase screens (see ^[sec:verification]).
For each of the three channels, we generate $5\times10^4$ independent realizations for different values of the time interval $\tau$ and aperture radius $R_\mathrm{ap}$.

## Results
### Two-time PDT
The joint distribution of the transmittance at two different times offers a direct view of the statistical dependence between consecutive pulses separated by the time interval $\tau=s/v$.
In ^[fig:2timepdt], the two-dimensional kernel density estimates of the joint PDT are shown for short and long pulse separation times for $R_\mathrm{ap}=20~\text{cm}$.
For the smaller time interval $s=3~\text{cm}$ ($\tau=3~\text{ms}$), the distribution is sharply concentrated along the diagonal.
Because the refractive index pattern changes only slightly over such a short interval, the transmittance undergoes only minor variations.
As a result, the two pulses show a high level of temporal correlation, implying a strong potential for entanglement preservation and effective use of adaptive protocols.

![\label{fig:2timepdt}Two-time PDT $\mathcal{P}(\eta_0, \eta_\tau)$ for the channel with $\sigma_{\mathrm{R}}^2 = 5.5$ and $R_\mathrm{ap} = 20~\text{cm}$. The left panel shows a short pulse separation, where the distribution is concentrated along the diagonal, indicating high temporal correlation. The right panel shows a longer separation, where the distribution spreads and approaches a product of marginals $\mathcal{P}(\eta_0)\mathcal{P}(\eta_\tau)$, signifying nearly independent transmittance events. Color intensity indicates density, transitioning from blue for zero values to yellow for peak values.](time_corr/twotimepdt.pdf)

For the larger time interval $s=17~\text{cm}$ ($\tau=17~\text{ms}$), the distribution spreads significantly.
This behavior indicates that the turbulent pattern has moved a much greater transverse distance, hence, the two pulses experience nearly independent transmittance values.
The joint PDT approaches the product of the two single-time distributions $\mathcal{P}(\eta)$, indicating that the channel can be effectively described using only the single-time PDT.
In this regime, adaptive selection becomes less effective because the value of $\eta_0$ carries little information about $\eta_\tau$.
The comparison of these two situations demonstrates that the two-time PDT is the central object for such channels.
It directly reveals how the atmosphere preserves correlations between consecutive pulses.

### Spatial coherence radius
>[!attention] wrong description !
>- what specifically??
>- [ ] fix words about independence on turbulence strength

\Cref{fig:pearson_eta_corr} presents the Pearson correlation between the aperture-averaged transmittances $\eta_0$ and $\eta_\tau$ as a function of the pulse separation time $\tau$ for two receiving apertures.
The correlation exhibits a strictly monotonic decrease as $s$ increases. 
This reflects the decorrelation caused by the transverse motion of refractive-index inhomogeneities.

![\label{fig:pearson_eta_corr}Pearson correlation coefficient between transmittances $\eta_0$ and $\eta_\tau$ as a function of the wind-driven shift $s$ for two different aperture radii $R_\mathrm{ap}$. The horizontal dotted line indicates the $e^{-1}$ threshold used to define the spatial coherence radius $\rho_0$. Results are shown for the turbulence channel with $\sigma_{\mathrm{R}}^2 = 5.5$.](time_corr/corr.pdf)

To quantify this behaviour by a single physically interpretable measure, we introduce the aperture-averaged spatial coherence radius $\rho_0$, defined as the value of the wind-driven shift $s$ for which the Pearson correlation falls to $e^{-1}$^[@andrews2005].
This coherence radius captures the time interval $\tau$ (transverse wind-driven shift $s$) over which statistical correlations persist.
In practical free-space quantum communication, this parameter quantifies the minimal pulse rate $v/\rho_0$ above which successive quantum states experience non-negligible correlations.

For a channel with $C_n^2 = 1 \times 10^{-16}~\text{m}^{-2/3}$ and small receiving aperture $R_\mathrm{ap}=2\text{ cm}$, the observed spatial coherence radius is $\rho_0=6\text{ cm}$, which corresponds to $\tau=6~\text{ms}$.
For the same channel but large aperture $R_\mathrm{ap}=20\text{ cm}$, the coherence radius increases to $\rho_0=13\text{ cm}$.
This can be explained by noting that a larger aperture captures a broader region of the wavefront, which means that the turbulence-induced intensity pattern must be shifted much farther by the wind before the transmittance changes noticeably.

A more systematic view is provided in ^[fig:scr_ap], which shows $\rho_0$ as a function of aperture radius across all simulated turbulence regimes.
The figure indicates that the spatial coherence radius $\rho_0$ grows monotonically as the aperture radius $R_\mathrm{ap}$ becomes larger.
This implies that a wider aperture allows the optical field to maintain its nonclassical features for a longer time.
For a fixed aperture radius, the dependence on the Rytov variance $\sigma_\mathrm{R}^2$ is weak within the analyzed interval from five to sixteen.
This observation suggests that the aperture plays the primary role in setting the coherence properties of such channels.

![\label{fig:scr_ap}Aperture-averaged spatial coherence radius $\rho_0$ as a function of the aperture radius $R_\mathrm{ap}$ for three turbulence regimes.](time_corr/corr_length.pdf)

Summarizing this consideration, we note that the spatial coherence radius $\rho_0$ determines the temporal interval over which successive pulses remain statistically correlated, directly influencing the decay of quantum correlations in turbulent atmospheric channels.
The impact of turbulence strength on $\rho_0$ remains limited across the examined range, while the change produced by the receiver aperture size is noticeably larger.
As a result, $\rho_0(R_\mathrm{ap})$ provides guidance for selecting pulse repetition rates for which temporal correlations can be exploited (or can be safely neglected) in realistic atmospheric quantum channels.

### Conditional PDT

Adaptive selection works by first sending a strong classical pulse through the channel at $t=0$.
If the measured transmittance of this pulse exceeds a threshold $\eta_\mathrm{min}$, the subsequent quantum pulse is transmitted at $t=\tau$.
If the transmittance is less than the threshold, the quantum pulse is discarded.
By selectively transmitting only those quantum pulses that are likely to encounter high transmittance channel conditions, the protocol can enhance the preservation of nonclassical properties and increase the performance of quantum communication protocols.
The conditional PDT provides the exact probability distribution of the transmittance of the second pulse under this selection procedure.

\Cref{fig:condpdt} shows the conditional PDT of the second pulse for different spatial shifts $s$, corresponding to various time intervals $\tau$ between pulses, for $\eta_\mathrm{min}=0.45$.
For small shifts, up to $s \sim 1~\text{cm}$ ($\tau \sim 1~\text{ms}$), the conditional distribution closely resembles the ideal case with $s=0$, indicating that the transmittance of the first pulse reliably predicts the second pulse.
As $s$ increases to several centimeters (several milliseconds), the probability of transmittance values below the threshold $\eta_\mathrm{min}$ becomes more significant.
For tens of centimeters of wind-driven shifts $s$ (tens of milliseconds of $\tau$), the conditional PDT approaches the single-time PDT.

![\label{fig:condpdt}Conditional PDT $\mathcal{P}(\eta_\tau \mid \eta_0 > \eta_\mathrm{min})$ for varying wind-driven shifts $s$. At small shifts (e.g., $s=1$ cm), the distribution is located at high transmittance values, validating the predictive power of the probe pulse. As the shift increases, the distribution broadens and eventually converges to the unconditioned single-time PDT (grey solid line), marking the limit of adaptive selection effectiveness.](time_corr/cond_pdt.pdf)

These results demonstrate that adaptive selection is most effective for short time intervals, on the order of a few centimeters of wind-driven shift or several milliseconds of time separation between pulses for $v=10~\text{m/s}$.
For longer intervals, the predictive power of the classical probe decreases, and the channel can be accurately described using only the single-time PDT.
This analysis provides a quantitative framework for designing adaptive protocols and predicting their performance in realistic quantum communication systems.
The application of these results for preserving nonclassical properties will be demonstrated in ^[sec:application].

## Summary {#sec:conclusion_timecorr}

The analysis of time correlations in atmospheric quantum channels demonstrates that the transmittance of consecutive optical pulses cannot generally be treated as independent.
The concept of the two-time PDT $\mathcal{P}(\eta_0,\eta_\tau)$ provides a complete and tractable framework to quantify these correlations.
As temporal correlations decay monotonically with pulse separation, the spatial coherence radius $\rho_0$ emerges as the central parameter for characterizing the persistence of temporal correlations between consecutive pulses.
Its value depends primarily on the receiver aperture and only weakly on turbulence strength within the considered range.
This implies that by selecting the aperture size appropriately, one can control the timescale over which successive quantum states remain statistically correlated, which is directly relevant for entanglement preservation in turbulent atmospheric channels.
For the channels studied, these correlations persist over several milliseconds, corresponding to wind-driven shifts of a few centimeters.

The conditional PDT captures a complementary property relevant for adaptive selection protocols.
By selecting quantum pulses based on the measured transmittance of a preceding classical probe, one can enhance the likelihood of transmitting through high-transmittance channel realizations.
The conditional PDT provides a precise description of the second pulse PDT under such selection protocols, directly influencing the preservation of nonclassical properties and the performance of other quantum communication protocols.

Overall, the results show that the two-time PDT and derived quantities such as $\rho_0$ and the conditional PDT are complementary tools.
The spatial coherence radius quantifies the timescale over which successive pulses remain statistically correlated and is essential for entanglement-based protocols, while the conditional PDT captures the potential for adaptive selection protocols, for example to enhance the preservation of nonclassicality.
These findings provide a practical framework for designing and evaluating quantum communication systems.
In ^[sec:application], these results will be applied to study the preservation of continuous-variable and discrete-variable entanglement as a function of pulse separation, as well as the enhancement of nonclassicality through adaptive selection.

>- The role of coherence length at Rap = 0?
>    - [ ] Should we plot and compare with the Rayleigh length in coherencsByApert plot?

> For Application
>
> - previous works...
>     - in work of semenov and other studied the entanglement in atmos channels.
>         - entanglement degradation across a atmospheric channel depends on first two moments including $\langle \eta_t\eta_{t+\tau} \rangle$
>         - in Martin exp results. Copropagated and contr. Contpropagated - obviously no correlateion. For copropagation - due to the lack of study of this question - considered only ideal correlated case, which equivalent to infinitely small time inteval.
>             - (also that paper 2009 and many other)
>         - adaptive selection
>             - adaptive selection operates by discarding low transmittance windows. If transmittance is correlated in time, selection produces temporal clustering of high quality windows.
>             - ...
>