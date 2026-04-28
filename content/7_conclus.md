\phantomsection
# Conclusions{#sec:conclusions .unnumbered}

># intro

This thesis addressed the statistical modeling of quantum optical channels in the turbulent atmosphere, including a study of corresponding temporal correlations.
We established a numerical framework based on the sparse-spectrum phase-screen method to simulate beam propagation through a turbulent atmosphere.
This approach mitigates low-frequency undersampling inherent in standard techniques, thereby enabling comprehensive analysis of stochastic wave propagation dynamics.
This framework allowed us to investigate transmittance statistics across weak, moderate, and strong turbulence regimes, including model validation and assessment of quantum entanglement preservation limits in a turbulent atmosphere.
Its code is publicly available and has attracted interest from the community.

># validation

\textbf{Systematic validation} revealed that receiver aperture size relative to the average beam radius dictates model accuracy more strongly than turbulence strength alone.
Small apertures induce positive skewness favoring the truncated lognormal model, whereas large apertures produce negative skewness described by beam-wandering or elliptical-beam approximations.
The empirical Beta distribution generally outperformed analytical alternatives due to its bounded support on $[0,1]$ and flexibility in capturing skewness transitions.
This finding clarifies an important aspect of PDT statistical behavior and establishes the aperture-to-beam ratio as the primary design criterion for optical links.

># assumptions

\textbf{Underlying  assumptions.} Numerical results indicate that while the beam centroid follows a two-dimensional Gaussian distribution in weak and moderate turbulence, it exhibits slightly platykurtic characteristics under strong conditions.
Furthermore, the assumption of statistical independence between the beam centroid and shape fluctuations is violated, especially in strong turbulence regimes.
Logarithms of the beam semi-axes also deviate from bivariate Gaussian distributions, showing suppression along the diagonal where axes are equal.
These deviations indicate that analytical models relying on these simplified assumptions introduce systematic errors in transmittance prediction.
This necessitates explicit correction in subsequent analytical frameworks.

># transmittance-matching technique.

\textbf{ Transmittance-matching technique.} We identified a fundamental flaw in beam-shape-based models such as beam-wandering and elliptical-beam approximations.
Standard geometric assumptions about the beam shape cannot account for complex shape evolution after propagation through the turbulent atmosphere, leading to the misspecification bias inherent in such models.
This deficiency manifests as systematic biases in predicted average transmittance moments.
To resolve this issue, we introduced a Transmittance-Moment Matching technique applied specifically to the circular-beam approximation.
The corrected model significantly improved agreement with numerical simulations compared to standard beam-based alternatives.
Consequently, this correction represents a significant advancement in physically grounded modeling for atmospheric channels.

># 2-time pdt

\textbf{Temporal correlations.} The existing framework of the PDT is insufficient for describing high-repetition-rate systems where temporal correlations persist between consecutive pulses.
Therefore, we introduced a Two-Time PDT framework $\mathcal{P}(\eta_0,\eta_\tau)$ to capture the joint statistics of transmittance values at different times.
A key parameter defined within this framework is the aperture-averaged spatial coherence radius $\rho_0$, marking the wind-shift displacement where the Pearson correlation decays to $e^{-1}$.
This spatial coherence radius scales linearly with aperture size, serving as a practical criterion for determining optimal pulse repetition rates.

># qunatum properties in atmosphere

\textbf{Quantum properties.} Applications to continuous-variable quantum protocols demonstrated that Gaussian entanglement persists over millisecond timescales.
Discrete-variable entanglement survives atmospheric turbulence for tens of milliseconds, though practical limits reduce this to a few milliseconds due to quantum memory readout losses.
Adaptive selection using classical probe pulses improves the preservation of nonclassicality over pulse separations of tens of milliseconds.
These results quantify the temporal resources available for time-bin encoding and correlation-aware communication strategies.

># limitations

\textbf{Limitations.} Atmospheric quantum channels depend on numerous physical parameters, making a fully comprehensive description impractical.
Consequently, we restricted our attention to a minimal set sufficient to isolate core effects, prioritizing physical understanding over system-specific details.
For example, the transmitter optical field is modeled as a Gaussian beam without explicitly considering higher-order spatial modes, and the receiver aperture is assumed to be circular, rather than accounting for specific optical configurations (e.g., Cassegrain).
Turbulence parameters are treated as constant along horizontal propagation paths.
These constraints are necessary for the systematic analysic conducted in this work.
For any subsequent developments, the simulation framework can be readily adapted to incorporate more intricate channel properties.

A second category of limitations arises from the intrinsic complexity of the real turbulent atmosphere.
Unlike the stationary Kolmogorov-based descriptions employed here, actual atmospheric dynamics are non-stationary and exhibit intermittency, characterized by abrupt fluctuations separated by variable intervals.
These features impose fundamental constraints on modeling accuracy that apply universally to all Kolmogorov-based theoretical frameworks.

># the end

Ultimately, this thesis establishes a rigorous framework for evaluating long-distance atmospheric communication under controlled conditions.
While restricted to a minimal set of physical parameters, this approach isolates core stochastic effects critical for system design.
This capability is essential for engineering robust quantum protocols where fiber transmission is prohibitive.
Consequently, the work provides a theoretical foundation for designing robust atmospheric quantum channels under varying turbulence conditions.
