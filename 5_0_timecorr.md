# Time correlations in Atmospheric Quantum Channels

In the previous sections we treated the PDT as describing an ensemble of independent single-shot propagations of quantum states of light through a turbulent atmosphere.
This can also be viewed as a sequence of quantum states transmitted with sufficiently large time intervals, such that each transmission is effectively independent and no temporal correlations exist between them.
In practice, this idealization is overly simplistic.
Modern quantum optical systems often operate at MHz repetition rates. 
At these repetition rates, consecutive pulses experience highly correlated atmospheric realizations. 
As a result, the transmittance $\eta_t$ of consecutive pulses is correlated at different times $t$.

In this section we analyze the case of two consecutive pulses separated by a time interval $\tau$.
With the numerical model, we compute the joint statistics of two consecutive transmittances. 
In particular, we study how the temporal correlation of the transmittance depends on the time separation $\tau$. 
We also describe the PDT in scenarios relevant for adaptive selection techniques, where the first signal is a strong classical pulse used to estimate the channel transmittance, and the second is a quantum signal whose transmittance is conditioned on the measured transmittance of the first.
In the ^[sec:application], we will demonstrate how these results guide continuous-variable and discrete-variable entanglement propagation protocols, and how they can be employed to enhance the preservation of nonclassicality through adaptive selection techniques.

## Two-time PDT
To describe the two-time probability distribution of transmittance (PDT), we extend the model introduced in ^[sec:numeroical_model] to account for time-dependent fluctuations of the refractive index. In this approach, the refractive index is represented as
$$n_t(\mathbf{r},z)=1+\delta n_t(\mathbf{r},z)$$
where $\delta n_t(\mathbf{r},z)$ denotes the small, time-dependent, stochastic perturbation caused by atmospheric turbulence.
The evolution of the complex field amplitude $u_t(\mathbf{r},z)$ under these conditions is governed by the paraxial wave equation ^[eq:paraxial], which, for a time-dependent refractive index, takes the form
$$
2ik\frac{\partial u_t(\mathbf{r},z)}{\partial z}+\Delta_\mathbf{r}
u_t(\mathbf{r},z)+2k^2\delta n_t(\mathbf{r},z) u_t(\mathbf{r},z)=0,
$$
To specify the temporal evolution of the refractive index we adopt the Taylor's frozen-turbulence hypothesis ^[eq:taylor] described in ^[sec:taylor].
Under this assumption, time-dependent turbulence can be represented as a frozen spatial pattern advected by the wind.

The transmittance through a receiving aperture $\mathcal{A}$ at time $t$ is then given by the aperture-averaged intensity of the propagated field:
$$
\eta_t=\int_\mathcal{A}d^2\mathbf{r} \left|u_t(\mathbf{r},z_\mathrm{ap})\right|^2.
$$
We consider two temporal modes at $t=0$ and $t=\tau$.
The two mode input output relation for the Glauber P function for channels with fixed linear losses $\eta_0$ and $\eta_\tau$ reads by analogy with single time relation^[eq:Pfunc] ^[@twomodeP]
$$
P_\mathrm{out}(\alpha_0,\alpha_\tau|\eta_0,\eta_\tau)=
\frac{1}{\eta_0\eta_\tau}P_\mathrm{in}\left(\frac{\alpha_0}{\sqrt{\eta_0}},\frac{\alpha_\tau}{\sqrt{\eta_\tau}}\right)
$$
Averaging over the atmospheric realizations leads to the input output relation for the two time channel
$$P_\mathrm{out}(\alpha_0,\alpha_\tau)=
\int_\Xi d\eta_0d\eta_\tau \left[\frac{1}{\eta_0\eta_\tau}P_\mathrm{in}\left(\frac{\alpha_0}{\sqrt{\eta_0}},\frac{\alpha_\tau}{\sqrt{\eta_\tau}}\right)\right]\, \mathcal{P}(\eta_0,\eta_\tau)$$
where $\Xi=[0,1]\times[0,1]$ and where the joint distribution $\mathcal{P}(\eta_0,\eta_\tau)$ is the two time probability distribution of the transmittance.

The two time distribution provides a complete description of such atmospheric quantum channels. 
The usual single time PDT is obtained as its marginal
  $$\mathcal{P}(\eta_0) = \int d\eta_\tau \mathcal{P}(\eta_0,\eta_\tau)$$
Adaptive selection protocols rely on conditional statistics. 
If the protocol keeps only those events for which the first classical probe pulse has transmittance $\eta_0 \ge \eta_\mathrm{min}$ then the conditional PDT describing the second quantum pulse at time $t=\tau$ is
$$\mathcal{P}(\eta_\tau|\eta_0 \geq  \eta_\mathrm{min}) = \frac{1}{\overline{\mathcal{F}}(\eta_\mathrm{min})} \int_{\eta_\mathrm{min}}^{1} \mathrm{d}\eta_0 \mathcal{P}(\eta_\tau,\eta_0)$$
where
$$\overline{\mathcal{F}}(\eta_\mathrm{min}) = \int_{\eta_\mathrm{min}}^{1} \mathrm{d}\eta_0 \mathcal{P}(\eta_0)$$
is the exceedance. 
This conditional PDT directly determines the statistics of accepted pulses and therefore the performance of adaptive schemes.
It also makes it possible to compute the moments that are required for the analysis of entanglement decay in continuous variable and discrete variable protocols. 
This formulation makes it possible to track how these quantities depend on the pulse separation time, which is crucial for quantifying the influence of temporal correlations in quantum communication protocols.

#### Numerical approach

For the numerical simulations we use the phase screen method introduced in ^[sec:numsim].
We extend this model to the time dependent case by incorporating the Taylor frozen flow hypothesis.

First we note that the wind driven advection has a component in the longitudinal direction and a component in the transverse plane. 
The longitudinal component produces pattern shifts that are much smaller than the channel length for the timescales that are relevant for our analysis. 
Therefore this component does not influence the temporal behavior in a measurable way and can be neglected in the simulations.

> to clearly identify the model / explanatory power / tractability / isolating the effect / causality / epistemic effect

We also assume that the advected wind velocity $v$ is constant at all points along the channel length. 
While in reality the wind exhibits spatial inhomogeneity across the propagation path, this simplification is necessary to maintain model identifiability and tractability. 
In principle, such inhomogeneity could be accounted for by assigning different velocities to each phase screen. 
However, this approach would lead to an over-parameterized system with limited explanatory power. 
By contrast, using a single velocity parameter $v$ for all phase screens ensures that the model remains tractable and allows us to isolate the specific effect of the wind-driven advection on the channel transmittance.

The coordinate system is rotated such that the new $x$ axis is aligned with the transverse wind direction.
Under this choice of coordinates, consider two optical pulses propagating through the channel, one at time $t=0$ and the other at $t=\tau$.
The turbulence along the propagation path is represented by multiple phase screens, and for each screen, the realization at these two times are related by
$$\varphi_{\tau}(x,y,z) = \varphi_0(x + v \tau, y, z)$$
where $s=v\tau$ represents the wind-driven shift of the turbulent pattern over the time interval $\tau$.

For the given wind velocity, the displacement $s$ and the time interval  are interchangeable. 
Accordingly, we will present the results mostly in terms of $s$. 
For interpretation, we assume a typical wind speed of $v=10\text{m/s}$ unless stated otherwise, which implies that a spatial shift of $1\text{ cm}$ corresponds to $1\text{ ms}$ of the time interval $\tau$. 
For any other desired wind speed $v$, the corresponding time interval can be obtained directly from the relation $\tau=s/v$.

- simulation parameters
    - phase screen propagation with a moving wind layer
    - for the details of the simulation method for time dependent transmittance see ^[sec:numsim_time]
    - $z_\text{ap}=50\text{km}$, ($C_n^2=1\times10^{-16}~\textrm{m}^{-2/3}$, $C_n^2=2\times10^{-16}~\textrm{m}^{-2/3}$, and $C_n^2=3\times10^{-16}~\textrm{m}^{-2/3}$)  inner and outer turbulence scales $\ell_0=1~\textrm{mm}$ and $L_0=80~\textrm{m}$, respectively.  wavelength $\lambda=808~\textrm{nm}$. the Rytov parameter $\sigma_{\mathrm{R}}^2$ is $5.5$, $11$, $16.5$.
    - $W_0=8~\textrm{cm}$, $F_0=50~\textrm{km}$
    - numerical simulations: "spatial grid 2048 points along each axis. The spatial grid step is $1~\textrm{mm}$. The number of spectral rings is 1024. The inner and outer bounds of the spectrum are $K_\mathrm{min}=1/15 L_0$ and $K_\mathrm{max}=2/\ell_0$. The number of phase screens is 15, ^[@Schmidt_book,Martin1988].  number of samples is $5\times10^4$".
    - wind-driven shift $s$, transverse wind velocity $v=10~\textrm{m/s}$, $\tau=s/v$

# Two-time PDT
![[twotimepdt.pdf]]

## Spatial coherence radius
>[!attention] wrong description !

Figure ^[fig:weak] presents the Pearson correlation of the aperture-averaged transmittance $\eta_t$ as a function of the pulse separation time $\tau$ (equivalently, wind-driven shift $s=v\tau$) for two receiving apertures under weak turbulence.
![[corr.pdf]]
The correlation exhibits a strictly monotonic decrease as $s$ increases, reflecting the decorrelation caused by the transversal motion of refractive-index inhomogeneities.

To quantify this behaviour by a single physically interpretable measure, we introduce the aperture-averaged spatial coherence radius $\rho_0$, defined as the value of the wind-driven shift $s$ for which the Pearson correlation falls to $e^{-1}$^[@andrws].
This coherence radius captures the transverse displacement over which statistical correlations persist.
In practical free-space quantum communication this parameter quantifies the minimal pulse rate $v/\rho_0$ above which successive quantum states experience non-negligible correlations.

For weak turbulence and small receiving aperture $R_\text{ap}=2\text{ cm}$, the observed spatial coherence radius is $\rho_0=5\text{ cm}$. 
For the larger aperture $R_\text{ap}=8\text{ cm}$ the coherence radius increases to $\rho_0=12\text{ cm}$.  
This can be explained by noting that a larger aperture captures a broader region of the wavefront, so the turbulence-induced intensity pattern must be shifted much farther by the wind before the transmittance changes noticeably.

The same analysis performed for strong turbulence conditions ^[fig:strong] shows overall lower correlations, consistent with enhanced scintillation.
[image here]
The corresponding coherence radii decrease to $\rho_0=4\text{ cm}$ for $R_\text{ap}=2\text{ cm}$, and $\rho_0=10\text{ cm}$ for $R_\text{ap}=8\text{ cm}$.  
However, this reduction is comparatively small when set against the much larger impact of aperture variation. 
The weak sensitivity of $\rho_0$ to turbulence strength indicates that receiver geometry is the dominant parameter determining the temporal correlation structure of the measured transmittance.

A more systematic view is provided in ^[fig:scr_ap], which shows $\rho_0$ as a function of aperture radius across all simulated turbulence regimes.

![[corr_length.pdf]]

The lines for different Rytov parameters lie close to one another, confirming that $\rho_0$ is weakly depended on turbulence strength comparing to the impact of the size of receiving aperture.

In conclusion, the spatial coherence radius $\rho_0$ determines the temporal interval over which successive pulses remain statistically correlated, directly influencing the decay of quantum correlations in turbulent atmospheric channels. 
The dependence of $\rho_0$ on turbulence strength is far weaker than might be expected, whereas its dependence on receiver aperture geometry is substantial. 
As a result, $\rho_0(R_\text{ap})$ serves as a practical parameter for studying entanglement propagation in turbulent atmosphere and provides guidance for selecting pulse repetition rates for which temporal correlations can be exploited (or can be safely neglected) in realistic atmospheric quantum channels.

> - [ ] Check if this claim of weak independence actually true.
> - [ ] Add plots
> - [ ] Check grammar.

- conditional probability
    - weak channel
    - strong
      ![[cond_pdt.pdf]]

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