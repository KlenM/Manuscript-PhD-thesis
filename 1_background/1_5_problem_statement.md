## Problem Statement
The analysis above shows that the classical theory of light propagation through turbulence has been extensively studied over the past decades.
However, due to the intrinsic complexity of turbulence, the existing theoretical framework relies almost entirely on the phenomenological Kolmogorov model.
This model assumes homogeneous and isotropic turbulence with a constant energy cascade rate within the inertial range. 
In reality, atmospheric conditions deviate substantially from these assumptions.
The presence of boundary-layer effects, wind gusts, heat flows from both natural and human-made sources introduces strong inhomogeneities and anisotropy in the refractive index field.
Consequently, all models based on the Kolmogorov description of turbulence are applicable only to limited, idealized conditions, such as propagation in open spaces far from the ground or other perturbing sources.

An important quantity in the classical analysis of optical wave propagation through turbulence is the intensity fluctuation at a single point. 
Under weak turbulence (the Rytov regime), it is established that this quantity follows a lognormal distribution, while under very strong turbulence conditions, it transforms into a negative exponential distribution. 
However, for the atmospheric quantum channels, the relevant quantity is not the intensity at a single point, but rather the transmittance, which is the intensity integrated over the aperture.

A number of models for the probability density of transmittance have been proposed.
Some of them are phenomenological, constructed by analogy with classical irradiance distributions. 
Others are physically motivated, relying on beam-shape decomposition at the aperture plane. 
In all analytical models, parameters are expressed in terms of field correlation functions.
However, these functions are derived under simplifying assumptions that inevitably lead to biased parameter estimates.
Additionally, the assumptions about beam-shape statistics remain weakly verified by experimental or numerical studies.

The applicability of PDT models remains unclear.
The truncated lognormal model, which was introduced by analogy with the classical model derived from the Rytov approximation that is valid under weak turbulence, has been reported to fit experimental data well under strong turbulence.
Conversely, under weak turbulence, better fits are typically obtained from beam-wandering or elliptical-beam models, which exhibit probability density functions of significantly different shapes.
Thus, a consistent correspondence between the parameters of an atmospheric quantum channel and a suitable PDT model has not yet been established.

The PDT-based description of atmospheric quantum channels effectively represents an ensemble of single quantum states propagated through atmospheric turbulence.
Such a model is valid only if consecutive quantum pulses are separated by time intervals much longer than the turbulence correlation time. 
In practice, however, pulse repetition rates typically lie in the MHz–GHz range, meaning that transmittance values are temporally correlated over many consecutive pulses.
Despite its practical relevance, a comprehensive time-domain statistical characterization of transmittance in atmospheric quantum channels has not yet been established.

These gaps highlight the need to develop a numerical framework for modeling atmospheric quantum channels. 
Such a framework would enable the consistent validation of existing analytical PDT models and assumptions about beam-shape statistics. 
It would also support developing improved PDT models and enable quantitatively studying temporal transmittance correlations under realistic turbulence conditions.

To achieve this goal, the following research tasks are to be addressed:
1. Develop a numerical model of atmospheric quantum channels capable of temporal sampling of transmittance.
2. Validate existing analytical PDT models under a range of turbulence conditions, including a comparative analysis of the models' ability to represent the transmission and degradation of squeezed quantum states.
3. Investigate the statistical properties of beam-shape parameters^[what].
4. Develop and validate new analytical models of atmospheric quantum channels, including the adaptation of models that account for biased transmittance moments.
5. Analyze time-domain correlations of transmittance.
6. Study the quantum properties of light in a turbulent atmosphere, such as discrete-variable (DV) and continuous-variable (CV) entanglement between temporally separated pulses and the preservation of nonclassicality with adaptive selection techniques.

> [!attention] The tasks must be refined after writing the main chapters
> Also, no background about q props of light in turb.


> [!note]+ Ideas to add
> - weak - beam wandering effects; strong - beam spreading (source?..)
> - dependance of $l_0, L_0$. 
> - tracked PDT
