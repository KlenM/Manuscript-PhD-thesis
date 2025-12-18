# Application
## Introduction
## Quadrature-squeezed light
## Gaussian entanglement between pulses
#### Quantum entanglement 
describes correlations between distinct subsystems that cannot be explained by classical physics and that arise from the non separability of the joint quantum state.
The conceptual origin of entanglement can be traced to the Einstein Podolsky Rosen paradox. 
In its original formulation, the EPR argument considers two spatially separated systems prepared in a correlated state. 
If the value of one observable of the first system can be predicted with certainty by measuring the second system, then this observable is considered an element of reality. 
If this holds simultaneously for two non commuting observables, then the quantum mechanical description appears incomplete. 
The EPR paradox was originally presented as a critique of quantum mechanics, but it later became a cornerstone for understanding nonclassical correlations.

In modern quantum information theory, entanglement is no longer viewed as a sign of incompleteness, but as a well defined physical resource.
It is a central resource in quantum information science, where it enables tasks that are impossible or inefficient using classical correlations alone.
In this section, the focus is on continuous variable entanglement realized in optical systems.

#### Continuous variable systems 
are quantum systems whose observables have continuous spectra. 
In quantum optics, such systems arise naturally from bosonic modes of the electromagnetic field. 
Each optical mode can be modeled as a quantum harmonic oscillator, and its physical observables are given by field quadratures.

Continuous variable entanglement appears as nonclassical correlations between the quadratures of different optical modes. 
These correlations can be measured using well-studied homodyne detection^[@10.1364/OL.8.000177] ^[@10.1103/RevModPhys.81.299]. 
As a result, such systems are widely used in optical implementations of quantum communication, quantum key distribution, and quantum enhanced metrology ^[@sbraunstein2005; @sweedbrook2012].

#### The two-mode squeezed vacuum (TMSV) state $\left|\xi\right>$
is the canonical example of a continuous variable entangled state. 
In this state, the quantum noise of two optical modes is strongly correlated. Fluctuations of one quadrature in the first mode are correlated with the corresponding quadrature of the second mode, while the conjugate quadratures are anticorrelated. 
The strength of these correlations increases with the squeezing parameter $\xi$.
In the limit of infinite squeezing, the TMSV approaches the idealized EPR state discussed in the original paradox^[@10.1088/0256-307X/21/10/003] ^[@10.1103/PhysRevLett.68.3663]. 

Two mode squeezed vacuum states can be generated using nondegenerate optical parametric oscillators or by interfering two single mode squeezed states on a balanced beam splitter. 
In the photon number basis, the TMSV state can be written as
$$
\ket{\xi}=\cosh^{-1}\xi\sum_{n=0}^{\infty}(-\tanh \xi)^n\ket{n,n}
$$

#### Simon certifier.
Detecting entanglement in continuous variable systems requires criteria that can distinguish separable states from entangled states. 
The fundamental conceptual basis for separability in bipartite quantum systems is given by the Peres Horodecki criterion^[@PH]. 
This criterion states that any separable quantum state must remain a valid physical state after partial transposition with respect to one subsystem.
In general infinite dimensional Hilbert spaces, this condition is necessary but not sufficient for separability.
However Simon showed that for two mode Gaussian states such as the TMSV state the partial transposition criterion is both necessary and sufficient for separability ^[@simon2000] ^[@shchukin2005].
This makes the Simon criterion a useful and complete tool for Gaussian entanglement detection for TMSV states.

The effect of atmospheric turbulence on continuous variable entanglement depends on temporal correlations of the channel transmittance. 
The limiting cases of fully correlated transmittances, corresponding to time separation $\tau\to 0$, and fully anticorrelated transmittances, corresponding to large time separation $\tau\to\infty$, have been analyzed previously in ^[@bohmann2016a].
We focus on the intermediate regime, where the time interval between subsequent pulses $\tau$ is finite.

We consider a two mode squeezed vacuum state as the entangled source. 
The first mode is transmitted through the atmospheric channel at time $t=0$. 
The second mode is stored in a quantum memory and transmitted at a later time $t=\tau$. 
As a result, the two modes experience different but temporally correlated realizations of the atmospheric channel.

For the simulations, we use the same atmospheric channels as defined in ^[sec:timecorr].
Deterministic losses of $0.1\ \mathrm{dB/km}$ are additionally included in the effective transmittances $\eta_0$ and $\eta_\tau$ ^[@losses], together with losses of the optical system.
When measurements are performed using homodyne detection, the local oscillator is transmitted in the same spatial mode as the signal with orthogonal polarization, ensuring a stable phase reference while experiencing the same atmospheric fluctuations.

To analyze entanglement preservation in this scenario, we apply the Simon criterion to the two mode squeezed vacuum state after transmission through the atmospheric channels. 
For the considered model, the Simon certifier $\mathcal W$ takes the form
$$
\begin{split}
\mathcal{W}=&\sinh^2\xi\Big[-\left\langle\sqrt{\eta_0\eta_\tau}\right\rangle^2\cosh^2\xi+\left\langle\eta_0\right\rangle\left\langle\eta_\tau\right\rangle\sinh^2\xi\Big]\nonumber\\
&\times\Big[1-\frac{\left\langle\sqrt{\eta_0\eta_\tau}\right\rangle^2}{4}\sinh^22\xi\nonumber\\
&+\sinh^2\xi\left(\left\langle\eta_0\right\rangle+\left\langle\eta_\tau\right\rangle+\left\langle\eta_0\right\rangle\left\langle\eta_\tau\right\rangle\sinh^2\xi\right)\Big]
\end{split}
$$
According to the Simon criterion, the transmitted state is entangled if and only if $\mathcal W<0$.

The expression for $\mathcal W$ factorizes into two multiplicative terms. 
The second factor is strictly positive for all physically allowed values of the transmittances and the squeezing parameter. 
As a result, it cannot influence the sign of $\mathcal W$ and can be omitted when determining the entanglement condition.
Therefore, the sign of $\mathcal W$ is fully determined by the first factor. 
Importantly, this factor is invariant under a global rescaling of the transmittances $\eta_0$ and $\eta_\tau$. 
This implies that entanglement preservation is independent of deterministic losses, including losses introduced by the quantum memory and the optical system.

^[fig:cvent] shows the regions of entanglement preservation for a TMSV state transmitted through atmospheric channels. 
![[4_entanglement.png-1.png|200]]
The horizontal axis represents the wind-driven shift $s$, which corresponds to the time separation between pulses $\tau = s / v$, where $v$ is the transverse wind speed (see ^[sec:timecorr]).
The vertical axis shows the squeezing parameter $\xi$ of the initial TMSV state.
The shaded regions correspond to $\mathcal W<0$, where the Simon criterion certifies that the received state remains entangled.

The figure reveals a counterintuitive feature: increasing the squeezing parameter $\xi$ reduces the maximum wind-driven shift for which entanglement is preserved. 
As a result, stronger squeezing does not improve entanglement robustness in atmospheric channels. 

For a squeezing parameter of $\xi = 2$ and a turbulence strength of $\sigma_R^2 = 11$, Gaussian entanglement remains for wind-driven shifts up to $s = 6.4\ \mathrm{cm}$, corresponding to a time separation of $\tau = 6.4\ \mathrm{ms}$ for a transverse wind speed of $v = 10\ \mathrm{m/s}$. 
This demonstrates that entanglement between light pulses is highly robust, persisting beyond millisecond time intervals. 
However, losses associated with the quantum memory can significantly reduce the absolute value of the Simon certifier.

In Section ^[sec:timecorr], we introduced the spatial coherence radius $\rho_0$, which characterizes the correlation of transmittances and depends on the receiver aperture radius $R_\mathrm{ap}$. 
![[5_witness_coherence.png-1.png|200]]
The threshold wind-driven shift $s_\mathrm{th}$, defined as the maximum shift for which entanglement is preserved ($\mathcal W < 0$), also depends on $R_\mathrm{ap}$.
^[fig:sthbyrho] shows $s_\mathrm{th}$ as a function of the coherence radius $\rho_0$. 
The figure shows that $s_\mathrm{th}(\rho_0)$ is a monotonically increasing, nonlinear function. 
Larger coherence allows entanglement to survive larger wind-driven shifts. 
At the same time, the threshold decreases with increasing squeezing.
The nonlinear behavior highlights the nontrivial interplay between initial squeezing, channel correlations, and receiver geometry in determining entanglement robustness.

In summary, we have introduced and quantified the time interval over which entanglement between pulses is preserved, and analyzed how it depends on channel aperture, coherence radius, and squeezing. 
Gaussian entanglement is robust against atmospheric turbulence, while stronger squeezing does not improve its survival. 
Deterministic losses affect only the absolute value of the certifier. 
These results provide a practical guideline for maintaining continuous variable entanglement in realistic free-space quantum channels.

 >squeezeing - is reduced below the vacuum noise limit, at the expense of increasing the noise in the conjugate quadrature to satisfy the Heisenberg Uncertainty Principle ($(\Delta X)^2 (\Delta P)^2 \geq \frac{1}{4}$).

## Discrete-variable entanglement between pulses
## Adaptive real-time selection for nonclassical states
## Conclusion