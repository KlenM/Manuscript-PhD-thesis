## Problem Statement
-  “The analysis conducted above has shown that ... 
    -  classical theory of light propagation through turbulence is studied a lot
    - However, due to the inherent complexity of turbulence, existing theory relies almost entirely on the phenomenological Kolmogorov model.
        - Assumes homogeneous, isotropic turbulence and constant energy cascade rate assumption in the inertial range.
        - Realistic atmospheric conditions include boundary-layer effects, anisotropy, wind gusts, heat flows from human-made machines and other sources of inhomogenity.
        - Consequently, all models based on Kolmogorov description of turbulence can be applied only to limited, idealized conditions like open spaces far from the ground level. 
    - Important quantity of intensity fluctuation at point is verified to follow lognornal distribution for weak turbulence (Rytov regime) and transforms to negative exponential distribution for strong conditions.
        - however in quantum case the relevant quantity isn't just intensity at point, but the transmittance - aperture-integrated intensity
    - Numerous of models proposed for the probability density of transmittance
        - Some of them are derived phenomenologically by analogy with the classical models of irradiance, other are physical motivated, based on beam shape decomposition.
        - In all analytical models parameters are expressed in terms of field correlation functions.
            - These correlation functions are derived under simplifying assumptions, which results in biased estimation of model parameters.
        - Assumptions about beam-shape statistics remain weakly verified experimentally or numerically.
    - Applicability of PDT models is unclear
        - The truncated lognormal model, derived under Rytov approximation of  weak turbulence, is reported to fit well in strong-turbulence regime.
        - Conversely, under weak turbulence, better fits are obtained from beam-wandering or elliptical-beam models -- the models that characterized by the completely different shape of PDT.
        - No consistent mapping exists between atmospheric quantum channel and the best PDT model.
    - The description of atmospheric quantum channels in terms of PDT function provides description of ensemble of quantum state. 
        - Effectively treat independent realizations of the channel (no temporal correlations).
        - Appropriate only when consecutive quantum pulses are separated by intervals much longer than turbulence correlation time.
        - In realistic quantum protocols (MHz–GHz pulse repetition rates), transmittance fluctuations are temporally correlated.
        - No time-domain statistical characterization of transmittance in atmospheric quantum channels has been reported.
- Therefore, it is necessary to develop a comprehensive numerical framework for modeling atmospheric quantum channels that enables consistent validation of existing analytical PDT models and assumptions about beam-shape statistics, supports for formulation of new improved PDT models, and allows quantitative study of temporal correlations of transmittance under realistic turbulence conditions.
- To achieve this goal, the following research tasks are to be addressed:
    - Develop a numerical model for time-dependent transmittance sampling based on the phase-screen approach, enabling realistic simulation of atmospheric quantum channels.
    - Validate existing analytical models of transmittance under a range of turbulence conditions, including verification through the propagation of squeezed quantum states.
    - Investigate the statistical properties of beam-shape parameters and quantify their influence on the probability density of transmittance.
    - Develop and validate new analytical models of atmospheric quantum channels, including the refinement and adaptation of models that account for biased transmittance moments.
    - Analyze time-domain correlations of transmittance and determine their relation to turbulence dynamics and pulse repetition rates relevant to quantum communication systems.
    - Examine the preservation of nonclassical properties by studying discrete-variable (DV) and continuous-variable (CV) entanglement between temporally separated pulses, and assess the role of post-selection in maintaining quantum correlations.

> [!note]+ Ideas to add
> - weak - beam wandering effects; strong - beam spreading (source?..)
> - dependance of $l_0, L_0$. 
> - tracked PDT
