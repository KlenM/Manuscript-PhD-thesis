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
The EPR paradox was originally presented as a critique of quantum mechanics, but it later became a cornerstone for understanding non classical correlations.

In modern quantum information theory, entanglement is no longer viewed as a sign of incompleteness, but as a well defined physical resource.
It is a central resource in quantum information science, where it enables tasks that are impossible or inefficient using classical correlations alone.
In this section, the focus is on continuous variable entanglement realized in optical systems.

#### Continuous variable systems 
are quantum systems whose observables have continuous spectra. 
In quantum optics, such systems arise naturally from bosonic modes of the electromagnetic field. 
Each optical mode can be modeled as a quantum harmonic oscillator, and its physical observables are given by field quadratures.

Continuous variable entanglement appears as non classical correlations between the quadratures of different optical modes. 
These correlations can be measured using well studied homodyne detection^[@10.1364/OL.8.000177] ^[@10.1103/RevModPhys.81.299]. 
As a result, such systems are widely used in optical implementations of quantum communication, quantum key distribution, and quantum enhanced metrology ^[@sbraunstein2005; @sweedbrook2012].

#### The two-mode squeezed vacuum (TMSV) state $\left|\xi\right>$
is the canonical example of a continuous variable entangled state. 
In this state, the quantum noise of two optical modes is strongly correlated. Fluctuations of one quadrature in the first mode are correlated with the corresponding quadrature of the second mode, while the conjugate quadratures are anticorrelated. 
The strength of these correlations increases with the squeezing parameter $\xi$.
In the limit of infinite squeezing, the TMSV approaches the idealized EPR state discussed in the original paradox^[@10.1088/0256-307X/21/10/003] ^[@10.1103/PhysRevLett.68.3663]. 

Two mode squeezed vacuum states can be generated using non degenerate optical parametric oscillators or by interfering two single mode squeezed states on a balanced beam splitter. 
In the photon number basis, the TMSV state can be written as
$$
\ket{\xi}=\cosh^{-1}\xi\sum_{n=0}^{\infty}(-\tanh \xi)^n\ket{n,n}
$$
>Gaussian entanglement in the turbulent atmosphere has been analyzed in Ref. [57] in the context of fully correlated and anticorrelated transmittances.

- intro
    - entanglement, history ERP, relevance (superficially)
        - The original EPR paradox posits that if you can simultaneously predict the value of two non-commuting observables of one particle by measuring the other particle, then the description of reality given by quantum mechanics is incomplete.
    - cv ent
        - Amplitude and phase natural degrees of freedom of light - CV entanglement
            - continuous range of values. (quadrature amplitudes)
            - is easy to measure?
        - why continuous variable systems matter in quantum information
            - computation, qkd, metrology
    - TMSVS - most canonical
        - kind of gaussian entangl?
        - is EPR ^[@10.1088/0256-307X/21/10/003]
        - In the TMSV state, the quantum noise is correlated between two distinct modes
        - how to creation
            - Non-degenerate Optical Parametric Oscillator (NOPO) or by mixing two single-mode squeezed states on a beam splitter.
    - atmos. quantum channel setup, two time for two modes
        - homodyne or what?
    - cryteria
        - Duan-Simon criterion) are only sufficient, not necessary (for nongauss??)
        - Peres Horodecki criterion conceptually
        - Reid/Duan-Simon Criterion or Logarithmic Negativity.??
        - Present the Simon criterion for Gaussian states.
        - Mention Duan inequality as an experimentally accessible witness.
        - Clarify necessity versus sufficiency.
- W by s
- s threshold by rho (introduced in timecorr)
- conclusion
- further?
    - squeezeing - is reduced below the vacuum noise limit, at the expense of increasing the noise in the conjugate quadrature to satisfy the Heisenberg Uncertainty Principle ($(\Delta X)^2 (\Delta P)^2 \geq \frac{1}{4}$).
---

The two-mode squeezed vacuum state (TMSVS)

$$
\begin{split}
\mathcal{W}=&\sinh^2\xi\Big[-\left\langle\sqrt{\eta_0\eta_\tau}\right\rangle^2\cosh^2\xi+\left\langle\eta_0\right\rangle\left\langle\eta_\tau\right\rangle\sinh^2\xi\Big]\nonumber\\
&\times\Big[1-\frac{\left\langle\sqrt{\eta_0\eta_\tau}\right\rangle^2}{4}\sinh^22\xi\nonumber\\
&+\sinh^2\xi\left(\left\langle\eta_0\right\rangle+\left\langle\eta_\tau\right\rangle+\left\langle\eta_0\right\rangle\left\langle\eta_\tau\right\rangle\sinh^2\xi\right)\Big]
\end{split}
$$

![[4_entanglement.png-1.png|200]]

![[5_witness_coherence.png-1.png|200]]

## Discrete-variable entanglement between pulses
## Adaptive real-time selection for nonclassical states
## Conclusion