# Time correlations in Atmospheric Quantum Channels
- introduction
    - in previous section PDT as ensemble of quantum states propagation in turb atmos. Or as a sequence of transmissions separated by huge time interval, so no correlation.
    - In practice, the time interval is short... typical transmittance rate is of order of 1MHz, so pulses are correlated. 
    - previous works...
    - was shown that entanglement depends on correlation between transmittance
    - in this section we quntify correlations ... in the next session we apply the results to practical task of entrnglement and adaptive selection
- theory
  $$
\mathcal{L}\left[\boldsymbol{\eta}\right]P_\mathrm{in}(\alpha_0,\alpha_\tau)=
\frac{1}{\eta_0\eta_\tau}P_\mathrm{in}\left(\frac{\alpha_0}{\sqrt{\eta_0}},\frac{\alpha_\tau}{\sqrt{\eta_\tau}}\right).
$$
$n_t(\mathbf{r},z)=1+\delta n_t(\mathbf{r},z)$
$$
2ik\frac{\partial u_t(\mathbf{r},z)}{\partial z}+\Delta_\mathbf{r}
u_t(\mathbf{r},z)+2k^2\delta n_t(\mathbf{r},z) u_t(\mathbf{r},z)=0,
$$
$$
\eta_t=\int_\mathcal{A}d^2\mathbf{r} \left|u_t(\mathbf{r},z_\mathrm{ap})\right|^2.
$$
- simulation parameters
    - $z_\text{ap}=50\text{km}$, ($C_n^2=1\times10^{-16}~\textrm{m}^{-2/3}$, $C_n^2=2\times10^{-16}~\textrm{m}^{-2/3}$, and $C_n^2=3\times10^{-16}~\textrm{m}^{-2/3}$)  inner and outer turbulence scales $\ell_0=1~\textrm{mm}$ and $L_0=80~\textrm{m}$, respectively.  wavelength $\lambda=808~\textrm{nm}$. the Rytov parameter $\sigma_{\mathrm{R}}^2$ is $5.5$, $11$, $16.5$.
    - $W_0=8~\textrm{cm}$, $F_0=50~\textrm{km}$
    - numerical simulations: "spatial grid 2048 points along each axis. The spatial grid step is $1~\textrm{mm}$. The number of spectral rings is 1024. The inner and outer bounds of the spectrum are $K_\mathrm{min}=1/15 L_0$ and $K_\mathrm{max}=2/\ell_0$. The number of phase screens is 15, ^[@Schmidt_book,Martin1988].  number of samples is $5\times10^4$".
    - wind-driven shift $s$, transverse wind velocity $v=10~\textrm{m/s}$, $\tau=s/v$
- results
    - spatial coherence radius
        - img: pearson coorelation by time for weak for two apertures
            - The simulated Pearson correlation of aperture-integrated transmittance shows a strictly monotonic decrease with increasing pulse separation time $\tau$ (equivalently, wind-driven shift $s=v\tau$).
            - To quantify correlation decay, we define the aperture-averaged spatial coherence radius $\rho_0$ as the value of the wind-driven shift $s$ for which the Pearson correlation drops to $e^{-1}$^[@andrws].
            - This value provides a physically meaningful measure of the transverse displacement over which statistical correlations persists.
            - In practical communication settings this parameter quantifies the minimal pulse rate $v/\rho_0$ above which successive quantum signals experience non-negligible temporal correlations.
            - For weak turbulence and small receiving aperture $R_\text{ap}=2\text{ cm}$, the observed spatial coherence radius is $\rho_0=5\text{ cm}$. For the larger aperture $R_\text{ap}=8\text{ cm}$ the coherence radius increases to $\rho_0=12\text{ cm}$.  
            - This can be explained by noting that a larger aperture captures a broader region of the wavefront, so the turbulence-induced intensity pattern must be shifted much farther by the wind before the transmittance changes noticeably.
        - img: strong two apertures
            - Repeating the analysis under strong turbulence conditions yields smaller correlations for the same aperture radii.
            - For receiving aperture $R_\text{ap}=2\text{ cm}$ the spatial coherence radius is $\rho_0=4\text{ cm}$, while for $R_\text{ap}=8\text{ cm}$ the coherence radius is $\rho_0=10\text{ cm}$.  
            - Nevertheless, the relative reduction compared to weak turbulence remains modest compared with the much larger variation produced by changing the aperture size.
            - This indicates that receiver geometry, rather than turbulence strength, is the dominant factor controlling temporal correlation of the measured transmittance.
        - Plotting $\rho_0$ as a function of aperture radius for all simulated turbulence regimes shows a monotonic increase with aperture size ^[fig:scr_ap]. 
          ![[corr.png|400]]
        - The curves for different Rytov parameters lie close to one another, confirming that $\rho_0$ is weakly depended by turbulence strength.
    - Conclusion:
        - As the conclusion, the obtained spatial coherence radii $\rho_0$ determine the temporal window within which successive pulses remain statistically correlated, directly influencing the decay of quantum correlations in turbulent atmospheric channels.
        - The spatial coherence radius differ much less with turbulence strength variation than might be expected, while the receiver geometry is the primary parameter.
        - Overall these results justify using $\rho_0(R_\text{a]})$ as a practical parameter for studying entanglement propagation in turbulent atmosphere.
        - The obtained spatial coherence scales also provide guidance for choosing pulse repetition rates where temporal correlation either must be exploited or can be safely neglected.
    - conditional probability
        - weak channel
        - strong
          ![[cond_pdt.png|400]]

>- The role of coherence length at Rap = 0? 
>    - [ ] Should we plot and compare with the Rayleigh length in coherencsByApert plot?
## Simulation results

## CV entanglement

## DV entanglement

## Adaptive selection protocol
