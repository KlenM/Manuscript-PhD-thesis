<span data-section="1"></span>
# Abstract
This thesis establishes the range of applicability for existing analytical models and resolves their inconsistencies by introducing a corrected description and a robust empirical alternative.

It further develops a two-time framework to characterize temporal correlations and quantify the timescales of quantum properties in the turbulent atmosphere.

<span data-section="1.1"></span>
## Background
### Context
Scalable quantum networks necessitate free-space optical links to overcome the exponential signal attenuation inherent in optical fiber transmission.

<span data-section="1.2"></span>
### Challenge
Atmospheric turbulence introduces stochastic refractive index fluctuations that severely degrade signal integrity through beam wandering and scintillation.

<span data-section="1.3"></span>
### Subject
The atmospheric transmittance, defined as the ratio of the intensity collected by the receiving aperture to the total beam intensity, serves as the critical random variable governing the preservation of the quantum state in quasi-monochromatic modes.

<span data-section="1.4"></span>
### Gaps
Despite the existence of many alternative analytical models of the probability distribution of transmittance (PDT), the field lacks a rigorous selection criterion and relies exclusively on ensemble descriptions that fail to capture time correlations in atmospheric turbulence.

<span data-section="1.5"></span>
## Purpose
### Applicability
To identify the range of applicability for existing analytical models by systematically comparing their predictions against numerical simulations.

<span data-section="1.6"></span>
### Assumptions
To validate the underlying assumptions of the analytical models to evaluate their applicability in different scenarios.

<span data-section="1.7"></span>
### Quantum Properties 
To investigate the temporal dependence of quantum properties, specifically quantifying the resilience of entanglement and nonclassicality against stochastic fluctuations induced by atmospheric turbulence.

<span data-section="1.8"></span>
## Methods
### Simulation Framework
This work employs a numerical simulation of atmospheric quantum channels based on the phase screen method, modeling the propagation path as a sequence of thin, phase-modulated layers separated by free-space vacuum segments.

### Spectrum
To address the statistical discrepancies inherent in traditional phase screen generation techniques, the simulation employs a sparse spectrum approach to ensure that the generated phase screens strictly align with analytical assumptions.

### Validation
The accuracy of the analytical model predictions is rigorously assessed against the simulation data using the Kolmogorov-Smirnov statistic

### Temporal dynamics
Since the temporal dependence of quantum properties is governed by the time-evolution of atmospheric transmittance, this study models the turbulent atmosphere using the Taylor frozen turbulence hypothesis to characterize these temporal correlations.

<span data-section="1.9"></span>
## Results
### Skewness
Simulations demonstrate that the skewness, representing the asymmetry of the distribution, exhibits high variability dependent on the receiving aperture size, while turbulence strength primarily changes the variance without significantly altering the shape.

<span data-section="1.10"></span>
### Misspecification bias
While analytical models parametrized by beam shape moments correctly predict the overall shape of the PDT, numerical simulations reveal a systematic shift in their predicted mode and mean values

<span data-section="1.11"></span>
### Beam assumption
We identified that beam-center can’t be considered independent of shape deformation as well as the Gaussian joint distribution hypothesis of the logarithms of the beam semi-axes doesn’t hold.

<span data-section="1.12"></span>
### Two-time PDT
The two-time PDT framework extends static ensemble descriptions by characterizing joint distribution of transmittances at two distinct times.

<span data-section="1.13"></span>
### Coherence radius
The introduction of an aperture-averaged spatial coherence radius which quantifies the wind-driven displacement at which transmittance correlations decay to exp(-1), scaling linearly with aperture size.

<span data-section="1.14"></span>
### Beta
We introduce a novel empirical Beta-distribution model, parametrized by only the first two moments, which enforces the physical domain [0,1] for transmittance, accurately captures aperture-driven skewness, and outperforms existing analytical models across the majority of tested parameter regimes

<span data-section="1.15"></span>
### transmittance moments matching
the misspecification bias in models parametrized by beam shape moments is addressed by introducing the transmittance moments matching. The circular beam model using this technique shows better agreement compared to other physics based models.

<span data-section="1.16"></span>
### Entanglement
Entanglement between two pulses is preserved for time separation of several to tens milliseconds with quantum memory efficiency acts as limiting parameter.

<span data-section="1.17"></span>
### Nonclassicality
We show that adaptive selection protocols which uses bright classical pulses to probe the channel transmittance establish a practical tool to preserve nonclassicality with time intervals for several milliseconds.

<span data-section="1.18"></span>
## Conclusions
### aperture criterion
While existing models accurately capture mean and variance, their fixed skewness behavior fails to reflect the aperture-driven asymmetry of the actual distribution, necessitating a shift from turbulence-based to aperture-based criteria for model selection.

<span data-section="1.19"></span>
### Models applicability
This thesis establishes definitive selection criteria that resolve the field's current ambiguity regarding model applicability.

<span data-section="1.20"></span>
### Practical Beta
The proposed Beta-distribution model provides a closed analytical expression that offers a robust tool for estimating realistic performance of quantum protocols in atmospheric channels, directly addressing the systematic errors introduced by constant-transmittance approximations.

<span data-section="1.21"></span>
### Model refinement
The identification of a non-negative correlation between beam-centroid displacement and beam deformation, alongside the rejection of the Gaussian joint distribution hypothesis for the logarithms of beam semi-axes, guides the necessary refinement of future theoretical frameworks for transmittance statistics.

<span data-section="1.22"></span>
### Entanglement
quantum correlations persist over long timescales renders the feasibility of time-bin encoding strategies for long-distance quantum networking.