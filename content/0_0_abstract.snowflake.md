# Level 1 
This thesis establishes the range of applicability for existing analytical models and resolves their inconsistencies by introducing a corrected description and a robust empirical alternative.
It further develops a two-time framework to characterize temporal correlations and quantify the timescales of quantum properties in the turbulent atmosphere.

# Level 2
## Background
- **Context**: Scalable quantum networks necessitate free-space optical links to overcome the exponential signal attenuation inherent in optical fiber transmission.
- **Challenge**: Atmospheric turbulence introduces stochastic refractive index fluctuations that severely degrade signal integrity through beam wandering and scintillation.
- **Subject**: The atmospheric transmittance, defined as the ratio of the intensity collected by the receiving aperture to the total beam intensity, serves as the critical random variable governing the preservation of the quantum state in quasi-monochromatic modes.
- **Gaps**: Despite the existence of many alternative analytical models of the probability distribution of transmittance (PDT), the field lacks a rigorous selection criterion and relies exclusively on ensemble descriptions that fail to capture time correlations in atmospheric turbulence.

## Purpose
- **Applicability**: To identify the range of applicability for existing analytical models by systematically comparing their predictions against numerical simulations.
- **Assumptions**: To validate the underlying assumptions of the analytical models to evaluate their applicability in different scenarios.
- **Quantum Properties**: To investigate the temporal dependence of quantum properties, specifically quantifying the resilience of entanglement and nonclassicality against stochastic fluctuations induced by atmospheric turbulence.

## Methods
- **Simulation Framework**: This work employs a numerical simulation of atmospheric quantum channels based on the phase screen method, modeling the propagation path as a sequence of thin, phase-modulated layers separated by free-space vacuum segments.
- **Spectrum**: To address the statistical discrepancies inherent in traditional phase screen generation techniques, the simulation employs a sparse spectrum approach to ensure that the generated phase screens strictly align with analytical assumptions.
- **Validation**: The accuracy of the analytical model predictions is rigorously assessed against the simulation data using the Kolmogorov-Smirnov statistic
- **Temporal dynamics**: Since the temporal dependence of quantum properties is governed by the time-evolution of atmospheric transmittance, this study models the turbulent atmosphere using the Taylor frozen turbulence hypothesis to characterize these temporal correlations.

## Results
- **Skewness**: Simulations demonstrate that the skewness, representing the asymmetry of the distribution, exhibits high variability dependent on the receiving aperture size, while turbulence strength primarily changes the variance without significantly altering the shape.
- **Misspecification bias**: While analytical models parametrized by beam shape moments correctly predict the overall shape of the PDT, numerical simulations reveal a systematic shift in their predicted mode and mean values
- **Beam assumption**: We identified that beam-center can’t be considered independent of shape deformation as well as the Gaussian joint distribution hypothesis of the logarithms of the beam semi-axes doesn’t hold.
- **Two-time PDT**: The two-time PDT framework extends static ensemble descriptions by characterizing joint distribution of transmittances at two distinct times.
- **Coherence radius**: The introduction of an aperture-averaged spatial coherence radius which quantifies the wind-driven displacement at which transmittance correlations decay to exp(-1), scaling linearly with aperture size.

- **Beta**: We introduce a novel empirical Beta-distribution model, parametrized by only the first two moments, which enforces the physical domain [0,1] for transmittance, accurately captures aperture-driven skewness, and outperforms existing analytical models across the majority of tested parameter regimes
- **transmittance moments matching**: the misspecification bias in models parametrized by beam shape moments is addressed by introducing the transmittance moments matching. The circular beam model using this technique shows better agreement compared to other physics based models.

- **Entanglement**: Entanglement between two pulses is preserved for time separation of several to tens milliseconds with quantum memory efficiency acts as limiting parameter.
- **Nonclassicality**: We show that adaptive selection protocols which uses bright classical pulses to probe the channel transmittance establish a practical tool to preserve nonclassicality with time intervals for several milliseconds.

## Conclusions
- **aperture criterion**: While existing models accurately capture mean and variance, their fixed skewness behavior fails to reflect the aperture-driven asymmetry of the actual distribution, necessitating a shift from turbulence-based to aperture-based criteria for model selection.
- **Models applicability**: This thesis establishes definitive selection criteria that resolve the field's current ambiguity regarding model applicability.
- **Practical Beta**: The proposed Beta-distribution model provides a closed analytical expression that offers a robust tool for estimating realistic performance of quantum protocols in atmospheric channels, directly addressing the systematic errors introduced by constant-transmittance approximations.
- **Model refinement**: The identification of a non-negative correlation between beam-centroid displacement and beam deformation, alongside the rejection of the Gaussian joint distribution hypothesis for the logarithms of beam semi-axes, guides the necessary refinement of future theoretical frameworks for transmittance statistics.
- **Entanglement**: quantum correlations persist over long timescales renders the feasibility of time-bin encoding strategies for long-distance quantum networking.

# Level 3
## Background
### Context
Fiber links form the foundation of local quantum communication networks over short distances. 
However, as transmission distances increase, the exponential signal attenuation inherent in optical fibers becomes a prohibitive barrier that limits the size of quantum networks. 
To overcome this physical limitation and enable a scalable quantum network that spans continents or connects to orbiting satellites, free-space optical links with satellite-based platforms offer an essential alternative. 
By transmitting quantum states primarily through the vacuum space, these links effectively bypass the material-induced light loss inherent in glass fibers. 
Additionally, the free-space approach allows for connections between moving ground stations, aircraft, and satellites, which fixed fiber infrastructure cannot establish.

However, unlike the controlled environment of optical fibers, free-space links are subject to atmospheric turbulence that induces stochastic fluctuations in the refractive index and severely distorts the propagating beam.
These perturbations manifest as beam wandering from the propagation axis and intensity fluctuations known as scintillation.
Consequently, these effects introduce significant complexity in characterizing the channel statistics for free-space optical communication.

### Subject

The impact of turbulence on the quantum state encoded in the quasi-monochromatic mode of light can be described by a single random variable---transmittance---which is defined as the ratio of intensity captured by the receiving aperture to the total beam intensity.
Thus, the probability distribution of transmittance (PDT) is central to the characterization of atmospheric quantum channels.
Despite its fundamental role, significant theoretical gaps persist regarding how this variable is modeled and utilized.
First, there remains no clear understanding regarding model selection among the various analytical models for PDT modeling.
Second, current literature relies on static ensemble descriptions that neglect time correlations.
This approach fails to provide the dynamic characterization required by many practical quantum protocols in turbulent atmosphere.

## Purpose

To address these challenges, one of the primary objectives of this research is to establish the range of applicability for existing analytical models by comparing their predictions against numerical simulations.
We also validate the underlying assumptions of current models in order to evaluate their suitability for different scenarios.
Furthermore, the second component of this study investigates the temporal dependence of quantum properties in atmospheric turbulence.
Specifically, we seek to quantify the resilience of entanglement and nonclassicality against stochastic fluctuations induced in these conditions.
## Methods

This study employs a numerical approach to simulate atmospheric channels based on the phase screen method, modeling the propagation path as a sequence of thin, phase-modulated layers separated by free-space vacuum segments.
To address statistical discrepancies inherent in traditional generation techniques, we utilize the sparse spectrum approach that ensures generated phase screens strictly align with theoretical requirements.
Additionally, this approach facilitates the generation of extended phase screens, enabling the application of the Taylor frozen turbulence hypothesis. 
This method links the time-evolution of atmospheric transmittance to wind-driven displacements.
We assess the predictive accuracy of existing analytical models against this data using the Kolmogorov-Smirnov statistic to measure how closely the analytical model predictions match the simulated data.

## Results
### Skewness

Numerical simulations spanning weak-to-strong turbulence regimes demonstrated that atmospheric turbulence strength primarily governs the variance of the PDT without significantly altering its fundamental shape. 
Conversely, the skewness---representing the distribution’s asymmetry---exhibits high variability and sign reversals contingent upon the receiving aperture size. 
Specifically, when the aperture is much smaller than the beam width, the distribution tail extends toward higher transmittance values (positive skewness); in contrast, larger apertures shift the tail toward lower transmittance values (negative skewness). 
However, most analytical models are constrained by rigid skewness behaviour and fail to capture this aperture-driven transition.

### Systematic errors

We systematically analyzed the properties and limitations of existing analytical models.
We identified that the beam-center cannot be considered independent of shape deformation, nor does the Gaussian joint distribution hypothesis hold for the logarithms of the beam semi-axes.
Another issue is that, although analytical models parameterized by beam shape moments accurately approximate the overall PDT shape, numerical simulations reveal a systematic shift in their predicted mode and mean values.
This discrepancy arises due to misspecification bias, as idealized circular or elliptical beam shapes cannot fully describe the beam shape deformations. 
Consequently, such models introduce systematic errors and exhibit inferior Kolmogorov-Smirnov statistics compared to other models.

### Models

To address the misspecification bias, we introduce the transmittance-moments-matching technique, which reparametrizes beam-shape based models in term of first transmittance moments.
The circular beam model using this technique shows better values of the Kolmogorov-Smirnov statistics compared to other physics-based models.
Our other empirical Beta-distribution model shows superior performance across the majority of tested regimes because it better accounts for aperture-driven skewness variations.

### Two-time PDT

To describe time correlations is atmospheric quantum channels, we develop a two-time PDT framework that moves beyond static ensemble descriptions to characterize joint transmittance distributions as a function of the time separation between two pulses. 
Building on this, we introduce an aperture-averaged spatial coherence radius which quantifies the wind-driven displacement at which transmittance correlations decay to exp(-1). 
Specifically, the defined coherence radius exhibits a linear scaling behavior relative to the receiving aperture size.
This formalization provides a statistical foundation for quantifying temporal correlations in atmospheric quantum channels and analysing the resilience of quantum properties.

### Protocols

Building upon the two-time PDT, we quantify the resilience of entanglement and nonclassicality in atmospheric channels. 
While entanglement between two pulses persists for time separations up to tens of milliseconds, quantum memory efficiency currently restricts practical discrete-variable entanglement to several milliseconds.
Furthermore, adaptive selection protocols utilizing bright classical pulses to probe channel transmittance are established as a practical tool capable of preserving nonclassicality within tens of millisecond time intervals between the probe pulse and the quantum state.

## Conclusions

In conclusion, this thesis resolves ambiguities regarding the understanding and characterization of atmospheric quantum channels.
Specifically, existing analytical models often fail to reflect the aperture-dependent asymmetry observed in actual distributions.
This necessitates a departure from using turbulence strength as the primary selection criterion, as this is insufficient for accurate modeling.
Instead, this work establishes the size of the receiving aperture as the governing parameter for selecting the appropriate model.

While the circular-beam model  with the developed transmittance-moments-matching approach demonstrates superior performance among physics-based models, its reliance on numerical integration limits broad application.
Consequently, the proposed empirical Beta-distribution model emerges as the superior choice for practical implementation, providing a closed-form analytical expression parameterized by only two moments.
This capability is particularly vital for quantum protocol analysis, where current methods often rely on constant-transmittance approximations that systematically ignore the random nature of atmospheric channels and introduce significant estimation errors.
Utilizing the Beta-distribution model directly addresses this limitation, effectively eliminating potential loopholes in performance analysis by  demonstrating robust validity across the majority of parameter regimes.

Ultimately, the analyzed resilience of quantum correlations over practical temporal windows renders time-bin encoding strategies feasible for free-space quantum networking. 
However, the practical realization of discrete variable entanglement protocols remains constrained by quantum memory efficiency. 
This highlights that while atmospheric channels support practical timescales, unlocking their full potential requires addressing storage limitations inherent in current quantum hardware.
