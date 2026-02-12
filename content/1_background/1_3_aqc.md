## Quantum channels in turbulent atmosphere {#sec:aqc}
In the work of Semenov and Vogel (2009)^[@semenov2009], a more general problem of quantum state of light transformation after propagation through a turbulent atmosphere was considered.
Taking into account the size of the collecting telescope and the fact that the total intensity after propagation cannot exceed the total intensity of the initial state, they derived the input-output relation of a quantum channel in a turbulent atmosphere.
They showed that a light beam distorted by atmospheric turbulence, when passing through a finite aperture, can be modeled as a linear-loss quantum channel.
The channel is characterized by an effective transmittance coefficient $\eta \in [0,1]$.
This coefficient represents the fraction of the total beam intensity that passes through the aperture.

While linear-loss channels can be specified in the density-operator formalism, a particularly elegant and tractable representation is obtained when quantum states are described in the Glauber-Sudarshan $P$-function representation^[eq:rho2P] ^[@glauber1963,sudarshan1963a].
Then, the input-output relation for linear-loss channels can be expressed as:
$$
%\label{eq:PoutPin}
P_{out}(\alpha) = \frac{1}{\eta} P_{in}\left(\frac{\alpha}{\sqrt{\eta}}\right)$$

However, in the atmospheric case, the effective transmittance $\eta$ is not a fixed constant. Since the refractive index $n(\boldsymbol{r}, t)$ is a random field, every realization of turbulence corresponds to a different value of $\eta$. Consequently, the atmospheric quantum channel is a statistical mixture of lossy channels, described by averaging over all possible transmittance values:
$$%\label{eq:PDTdef}
P_{out}(\alpha) = \int_0^1 d \eta \mathcal{P}(\eta) \frac{1}{\eta} P_{in}\left(\frac{\alpha}{\sqrt{\eta}}\right)$$
where $P(\eta)$ is the probability density of transmittance (PDT).
The PDT encodes the statistics of turbulence and depends on multiple parameters: the source beam properties (e.g., waist size, wavelength), the atmospheric channel (e.g., turbulence strength, path length, model), and the aperture geometry.
The probability density of transmittance (PDT) is the primary defining characteristic of atmospheric quantum channels, as it fully captures the stochastic effects of turbulence on the output quantum state.

Direct experimental reconstruction of PDT is possible either via homodyne detection of quantum states^[@semenov2009] or via classical intensity measurements at the receiver with a photodiode.
However, experimental studies are  generally complicated.
They require expensive setups with two synchronized sites separated by large distances.
Measurements must be carried out under uncontrolled atmospheric conditions, which complicates the study, and temporal fluctuations further hinder precise characterization.
These difficulties highlight the importance of studying atmospheric quantum channels in controlled and well-characterized way.

>- pdt is eta over ensamble of turb realisations
>- many authors (sources) studying qunatum protocols in AQC use only average transmitance, which can be too rough approximation.
>- PDT
>    - Most models focus on single-parameter descriptions (e.g., average loss), often ignoring higher-order correlations (examples? :) )

> - in our work we consider the following channel:
> - We consider the pulse as a superposition of Gaussian beams [21] with different wave numbers k, propagating along the Z axis onto the aperture plane at distance zap from the source.
> - qunatum state is prepared in a single mode of light at the transmittance plane.
> - it propagates along $z$-axis in turbulent atmosphere undergo some disturbance.
> - at the aperture plane, limited size of the aperture leads to truncation of some part of the light, *leaving us with the output quantum state*.

>When the quantum state propagates in atmosphere, as opposed to ideal vacuum propagation, it undergoes several perturbations.
These include attenuation of intensity, beam shape distortion, and phase distortions due to random refractive index fluctuations in the turbulent medium, which are characterized by the stochastic refractive index field $n(\boldsymbol{r},t)$.
We will discuss the precise mechanism of these perturbations in the next subsection.
>
>By the time the beam reaches the receiving aperture, its transverse intensity distribution is distorted by turbulence-induced scattering and diffraction effects.
>
>Quantum channels are linear maps that transform one quantum state to another and satisfy the completely positive and trace-preserving (CPTP) conditions.

### Analytical models of PDT {#sec:pdt}
Several analytical models of the probability distribution of transmittance were developed between 2009 and 2018 to describe the statistical properties of atmospheric quantum channels.
These models are typically formulated in terms of parameters derived from the field correlation function, such as the average transmittance, transmittance variance, or beam-spot parameters at the aperture plane, including the mean beam-spot radius and the variance of the beam-center position.

The truncated lognormal distribution model^[@semenov2009] originates based on the lognormal model of irradiance^[sec:pdf_irradiance] but introduces an additional truncation condition at the point $\eta=1$.  Despite being derived under the Rytov approximation in classical optics, this model was reported to yield reasonable agreement under strong turbulence conditions^[@capraro2012,vasylyev2016].

The beam-wandering model^[@vasylyev2012] accounts for random deflection of the beam’s center of mass from the propagation axis while neglecting beam-shape deformation.
It assumes a normally distributed beam-center position in the aperture plane, resulting in a log-negative Weibull distribution for the PDT.
The model depends only on the beam-shape parameters, and it's supposed to be applicable under weak turbulence conditions.

The elliptical-beam model^[@vasylyev2016] extends the beam-wandering approach by incorporating elliptical shape distortions, thereby capturing additional contributions to the cumulative beam decomposition of the intensity at the aperture plane.
This added complexity requires numerical evaluation of the model parameters.
This model was also proposed for weak or weak-to-moderate turbulence^[@vasylyev2016,vasylyev2018].

Finally, the total probability law model^[@vasylyev2018] separates the effects of beam wandering and beam-shape distortion.
It assumes that the shape distortion can be described by a truncated lognormal distribution.
The advantage of this model is that it provides accurate values of the mean transmittance; however, the model parameters must be determined numerically.

As a conclusion, various models exist based on both phenomenological approaches and physically grounded formulations.
However, the further development of purely analytical, physically justified models is limited by the difficulty of expressing their parameters in closed analytical form.
In addition, all analytical models are formulated in terms of field correlation functions, which themselves involve significant approximations.
It also remains an open question under which conditions each model should be applied.

> #### Truncated Log-normal distribution model.
> $\mathcal{P}(\eta; \left<\eta\right>, \left<\eta^2\right>)$
> origin, assumptions, key formula, and expected regime of validity.
>
> #### Beam wandering model.
> $\mathcal{P}(\eta; W^2_\text{ST}, \sigma_\text{BW}^2)$
>
> #### Elliptical beam model.
>
> #### Total probability law model.
>  $\mathcal{P}(\eta; \left<\eta\right>, \left<\eta^2\right>, W^2_\text{ST}, \sigma_\text{BW}^2)$
>

> - [ ] Where is the single-photon propagation introduced for the transmittance value?