# Conclusions {.unnumbered}

>- [ ] write intro to conclus as intro

> - intro (Reiterate the "Why" and "What."	Confident & Direct)
>     - why this study was necessary [1p]
>     - main claim or findings [2p]
> - intro
>     - qunatum network, long distance, satellites
>     - existing toolset of models of PDT - applicability unclear
>     - describes ensamble, do not account for correlations between consequnce pulses
>     - A comprehensive numerical framework was required to resolve the applicability of these models and to characterize the temporal correlations

> ## q communication
> ## pdt (gap)
> - the range of validity of these models has remained unclear.
>     - Some of the models were validated with experimental data by fitting, but no compete understanding which model in which regime work better.
> - identify governing parameters, test model assumptions, and resolve temporal structure

 >### Synthesis of findings:
> #### numsim

> This research successfully implemented a Phase Screen Method utilizing a Sparse Spectrum (SS) generation approach. By adopting the Modified Von Karman spectrum, the resulting phase screens achieved an ideal structure function, effectively bypassing the low-frequency sampling errors inherent in traditional FFT-based methods.

> validation, models

>ideas:
>- As an aperture integrated quantity, transmittance depends explicitly on the receiver geometry and aperture size, which makes its statistical behavior more complex than that of the local field amplitude.

We show that transferring assumptions about the light field before aperture directly to the transmittance value distribution is not valid.
Beam wandering is the most pronounced effect in weak turbulence, but this does not imply that beam wandering based PDT models are accurate in this regime.
A good fit of the truncated lognormal distribution in strong turbulence does not justify its universal use across strong turbulence scenarios.
The same limitation applies to approaches that infer transmittance statistics from light field distributions in a point.
Realistic measurements always involve a finite size aperture in contrast to the theoretical descriptions of the light field are typically defined at an infinitesimal point.

We demonstrate that the ratio between the aperture size and the average beam size is the primary parameter shaping the PDT.
Transmittance is bounded on the interval $[0,1]$, which enforces asymmetry that depends on its mean value.
For apertures smaller than the mean beam waist, transmittance values concentrate near the lower bound.
The resulting statistical dispersion produces a strongly positively skewed distribution.
When the average transmittance approaches unity, the distribution becomes negatively skewed.

When the first two moments of transmittance are specified, the central task of a PDT model is to predict higher order moments correctly.
Not all models have sufficient flexibility to account for aperture induced shape changes.
For example, the lognormal distribution is always positively skewed and therefore performs well only for small apertures.
We propose a new empirical model based on the Beta distribution.
It reproduces skewness near both bounds and generally outperforms existing models.
Its analytical simplicity makes it suitable for practical use.

Physically grounded models are typically formulated in terms of beam shape statistics such as beam wandering and beam spreading.
This means that accurately predicting the mean transmittance and variance, in addition to higher moments, falls within their scope of tasks.
In practice, these models often fail to do so.
They often reproduce the qualitative shape of numerically simulated PDTs but exhibit systematic shifts.
To overcome this misspecification bias we proposed a transmittance matching procedure.
Based on this procedure, we construct a new physically grounded model with fewer parameters than the elliptical beam model, while producing unbiased estimates of the first two transmittance moments and outperforming it overall.

> validated model assumptions for further dev of model.

To guide further development of physically grounded models, we validated the key assumptions underlying their construction.
We demonstrated that the beam centroid displacement follows Gaussian statistics across all turbulence regimes.
In contrast, the commonly assumed bivariate Gaussian distribution of beam semi-axis sizes fails systematically.
The joint distribution exhibits strong suppression along the diagonal, which cannot be captured by a Gaussian model.
Further investigation of this effect may benefit from connections to random matrix theory, which could provide a theoretical explanation for the observed structure.

Existing models further assume statistical independence between the beam centroid position and the instantaneous beam size.
We show that this assumption is violated.
The induced correlations are small in the weak to moderate turbulence regime but become significant under strong turbulence.
Neglecting these correlations leads to an underestimation of the PDT spread in this regime.

> time correlations

The PDT models describe either single pulse propagation or pulses separated by times much longer than the atmospheric correlation time.
However, real quantum communication systems operate at high repetition rates.
Consecutive pulses therefore propagate through strongly correlated atmospheric conditions.
The channel transmittance becomes temporally correlated, and this correlation is imprinted on the output quantum states.
Such effects are not captured by existing models.

In this work, we extended the PDT framework by introducing a two time PDT formulation.
The resulting two time PDT provides a complete statistical description of two consecutive pulses with arbitrary temporal separation.
Its properties were studied numerically under Taylor’s frozen turbulence hypothesis.

To quantify temporal correlation properties of atmospheric quantum channels, we introduced the aperture averaged spatial coherence radius $\rho_0$.
It is defined as the temporal separation at which the Pearson correlation coefficient of pulse transmittances decays to $e^{-1}$.
As in the single time PDT, the receiver aperture plays a dominant role.
We showed that the aperture averaged spatial coherence radius increases approximately linearly over a practically relevant range of aperture radii.
The aperture size therefore acts as an effective control parameter for achieving desired levels of transmittance correlation, corresponding to several centimeters of spatial coherence or several milliseconds of temporal coherence.

The transition from ensemble based statistics to explicit two point correlations constitutes the main theoretical advancement of this work.
It closes a gap between idealized single pulse models and realistic high repetition quantum communication scenarios.

> Application

The introduced two time PDT framework enables the analysis of a broad class of quantum communication protocols in turbulent atmospheric channels.
We applied it to study three key quantum properties under realistic operating conditions, including practical source imperfections, deterministic losses in quantum memory storage, finite detector efficiency, and limited detector resolution.
This enables direct assessment of protocol performance beyond idealized assumptions.

We investigated the temporal window over which two entangled systems separated by a time delay $\tau$ preserve entanglement in an atmospheric environment.
For continuous variable systems, entanglement witnesses are robust against constant losses.
As a result, nonclassical correlations can persist for several milliseconds.
In contrast, discrete variable systems are more sensitive to deterministic losses introduced by quantum memory.
These losses reduce entanglement lifetimes from tens of milliseconds for the lossless quantum memory to a few milliseconds with realistic quantum memory losses.
Improving quantum memory efficiency therefore remains a primary technical requirement for extending entanglement preservation times.

We further demonstrated that adaptive selection techniques can enhance the nonclassicality of amplitude squeezed states propagating through the atmosphere, even for pulse separations on the order of tens of milliseconds.
The analysis was performed for both ideal photodetection and on-off array detectors configurations.
In this regime, Bell like inequalities provide a more sensitive probe of nonclassicality criteria.

> how your work moves the field forward.

We showed that the commonly assumed implication from optical field fluctuation mechanisms to transmittance statistics does not hold.
Even when a single physical effect dominates optical field behavior, finite aperture averaging fundamentally reshapes transmittance statistics.
We identify the receiver aperture as the primary parameter controlling the PDT shape.
For example, in a fixed strong turbulence scenario, a small receiver aperture produces a PDT with a log normal shape, consistent with predictions obtained by transferring optical field statistics to transmittance.
However, increasing only the aperture size leads to a negatively skewed PDT, a behavior qualitatively similar to that predicted by beam wandering based models that are commonly assumed to be applicable in weak turbulence.
This demonstrates that apparent agreement with different PDT models arises from aperture size rather than from the dominance of a specific physical mechanism, thereby invalidating such model selection heuristics.
Also, this conclusion is general and applies not only to quantum channels but also to classical optical links, since any detection system involves a finite-sized aperture.

We emphasize that physically grounded PDT models expressed in terms of transmittance moments, rather than beam shape statistics, are more relevant for quantum communication.
Physically grounded models parameterized by beam shape statistics can reproduce the qualitative shape of PDTs, yet systematically bias the most important quantities for quantum protocols: the mean and variance of transmittance.
In addition, validating which assumptions used in physically grounded models are justified provides a clear guide for refining and developing more accurate models in the future.

Finally, we introduce an empirical Beta distribution model for the PDT that generally outperforms existing approaches across the full range of aperture sizes and turbulence conditions.
Some modern studies still use only the average transmittance when evaluating quantum key distribution or other quantum communication protocols, which provides an incomplete and potentially misleading description of the channel.
The simplicity of the analytical Beta model allows these analyses to incorporate the full transmittance statistics, enabling more accurate theoretical predictions and experimental evaluation.

> Limitations and Future Research

Atmospheric quantum channels depend on a large number of physical parameters.
A fully comprehensive description is therefore impractical.
In this work, attention was restricted to a minimal set of parameters sufficient to pinpoint the core physical effects.
This choice enabled systematic analysis and clearer interpretation.

One class of limitations arises from simplified modeling assumptions.
The transmitter optical field was modeled as a Gaussian beam, while higher order spatial modes are of significant interest in the literature.
The receiver aperture was assumed to be circular, whereas realistic systems often employ more complex geometries such as Cassegrain apertures.
Turbulence parameters, including the refractive index structure constant $C_n^2$ and the inner and outer scales $l_0$ and $L_0$, were taken to be constant along the propagation path. Only horizontal links were considered, while ground to satellite channels with altitude dependent $C_n^2$ profiles are of practical interest.
These assumptions were adopted to focus on physical understanding rather than system specific details.
All of these effects can be readily incorporated into the simulation framework developed in this thesis.

A second class of limitations is associated with the intrinsic complexity of the real turbulent atmosphere.
Real atmospheric turbulence is non stationary.
Conditions evolve between day and night, across seasons, and over multi year time scales.
The parameters $C_n^2$, $l_0$, and $L_0$ vary in time and space, whereas Kolmogorov based turbulence description assumes stationarity.
Turbulence exhibits intermittency, with abrupt fluctuations separated by relatively stable intervals.
Additional effects, such as spatial inhomogeneity in urban environments, boundary effects and aerosol scattering introduce fluctuations that are difficult to represent within theoretical models.
These features constrain both modeling accuracy and direct comparison with theory.

These properties of the atmosphere limit experimental validation.
Controlled experiments under stable and well characterized conditions are challenging to realize.
Further experimental studies are therefore required, including the development of measurement setups specifically designed for quantum channel characterization.
In previous studies, analytical models have been validated in certain regimes, typically by fitting transmittance histograms to experimental data.
Such validation provides partial support but does not fully capture model performance,  given the previously discussed misspecification bias.
Future validation efforts should combine high resolution intensity measurements with independent characterization of deterministic attenuation.

> many time pdt
> frozen turbulence hypothesis

> sense of completion and significance

This thesis provides a consistent and practically usable description of atmospheric quantum channels beyond idealized assumptions.
It resolves long standing ambiguities in the interpretation and applicability of probability distributions of transmittance.
It establishes the receiver aperture as the dominant control parameter shaping transmittance statistics and temporal correlations, a conclusion that applies not only to quantum channels but also to classical free space optical links.

This thesis provides a consistent and practically usable description of atmospheric quantum channels beyond idealized assumptions.
It resolves long standing ambiguities in the interpretation and applicability of probability distributions of transmittance.
It establishes the receiver aperture as the dominant control parameter shaping transmittance statistics and temporal correlations, with equal relevance for quantum channels and classical free space optical links.

By combining high fidelity numerical simulation, systematic model testing, and explicit validation of physical assumptions, this work clarifies which elements of existing approaches are justified and which require revision.
The introduced two time PDT framework extends ensemble based channel models to explicitly include correlations between consecutive pulses.
The results demonstrate that temporal correlations induced by atmospheric time coherence increase the effective Hilbert space available for encoding and transferring quantum states of light.

The provided simulation framework employs a phase screen method with Sparse Spectrum generation, reproducing the correct structure function and avoiding low frequency sampling errors inherent in FFT based methods.
The framework has value for both theoretical analysis and system design.
Its code is publicly available and has attracted interest from the community.

Together, these contributions establish a reliable foundation for evaluating and optimizing long distance atmospheric communication under realistic condition, which is essential for designing robust quantum communication protocols.

> - [ ] is key statement for class fso that integrated instensity is limited instead of field presented here?
> - [ ] allows for the generation of arbitrarily long phase screens, !!!
>     - [ ] gpu? x20
> - [ ] numsim limits:
>     - [ ] Markov approx - delta correlated atmosphere, but we often have Deltaz >> L_0
>     - [ ] Paraxial Approximation (no need to account),
>     - [ ] Vacuum Approximation (Split-Step) converged by big number of PS (numerical convergence?)