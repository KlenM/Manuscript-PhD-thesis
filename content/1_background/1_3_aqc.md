## Quantum channels in turbulent atmosphere {#sec:aqc}
In the work of Semenov and Vogel (2009)^[@semenov2009], a more general problem of quantum state of light transformation after propagation through a turbulent atmosphere was considered.
They showed that a light beam distorted by atmospheric turbulence, when passing through a finite aperture, can be modeled as a linear-loss quantum channel.
The channel is characterized by an effective transmittance $\eta \in [0,1]$.
This quantity represents the fraction of the total beam intensity that passes through the aperture.

While linear-loss channels can be specified in the density-operator formalism, a particularly elegant and tractable representation is obtained when quantum states are described in the Glauber-Sudarshan $P$-function representation (see ^[eq:rho2P]) ^[@glauber1963,sudarshan1963a].
Then, the input-output relation for linear-loss channels can be expressed as
$$
%\label{eq:PoutPin}
P_\mathrm{out}(\alpha) = \frac{1}{\eta} P_\mathrm{in}\left(\frac{\alpha}{\sqrt{\eta}}\right).
$$
However, in the atmospheric case, the effective transmittance $\eta$ is not a fixed constant. Since the refractive index $n(\boldsymbol{r}, t)$ is a random field, every realization of turbulence corresponds to a different value of $\eta$. Consequently, the atmospheric quantum channel is a statistical mixture of lossy channels, described by averaging over all possible transmittance values
$$%\label{eq:PDTdef}
P_\mathrm{out}(\alpha) = \int_0^1 d \eta \mathcal{P}(\eta) \frac{1}{\eta} P_\mathrm{in}\left(\frac{\alpha}{\sqrt{\eta}}\right),
$$
where $\mathcal{P}(\eta)$ is the probability density of transmittance (PDT).
The PDT encodes the statistics of turbulence and depends on multiple parameters: the source beam properties (e.g., waist size, wavelength), the atmospheric channel (e.g., turbulence strength, path length, model), and the aperture geometry.
The probability density of transmittance (PDT) is the primary defining characteristic of atmospheric quantum channels, as it fully captures the stochastic effects of turbulence on the output quantum state.

The input-output relation ^[eq:PDTdef] holds for both classical and quantum fields since the PDT $\mathcal{P}(\eta)$ is identical in both regimes. 
This correspondence is evident when considering an input coherent state $|\alpha_0\rangle$, characterized by the $P$-function $\delta^{(2)}(\alpha - \alpha_0)$, which results in an output state represented as a statistical mixture of attenuated coherent states. 
Consequently, the task of determining the PDT for an atmospheric quantum channel is equivalent to solving the corresponding classical stochastic propagation problem.

Direct experimental reconstruction of the PDT is possible with classical intensity measurements at the receiver side with a photodiode.
However, experimental studies of PDT properties are generally complicated.
Measurements must be carried out under uncontrolled atmospheric conditions, which complicates the study, and temporal fluctuations further hinder precise characterization.
These difficulties highlight the importance of studying atmospheric quantum channels in a controlled and well-characterized way.

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
Several analytical models of the PDT were developed between 2009 and 2018 to describe the statistical properties of atmospheric quantum channels.
These models are typically formulated in terms of parameters derived from the field correlation function.
The first group consists of models defined by transmittance moments, such as average transmittance and transmittance variance.

The truncated lognormal distribution model^[@semenov2009] is based on the lognormal model of irradiance (see ^[sec:pdf_irradiance]).
Since the lognormal distribution has an infinite bound but the PDT requires values between 0 and 1, an additional truncation condition is introduced at $\eta=1$.
Despite being derived under the Rytov approximation in classical optics, this model was reported to yield reasonable agreement under strong turbulence conditions^[@capraro2012,vasylyev2016].

Alternatively, an empirical approach based on the Beta distribution^[@johnson1995] was introduced in our work \ref{mypaper1}.
In this model, the PDT is defined using the first two transmittance moments as
$$
\mathcal{P}\!\left(\eta\,; \left<\eta\right>, \left<\eta^2\right>\right) = \frac{1}{B(a, b)} \eta^{a-1} (1-\eta)^{b-1},
$$
where $B(a,b)$ is the Beta function and the parameters $a$ and $b$ are expressed through the first two moments as
$$
a = \frac{\langle\eta\rangle - \langle\eta^2\rangle}{ \langle\eta^2\rangle- \langle\eta\rangle^2}\langle \eta \rangle \quad \text{and} \quad
b =  \frac{\langle\eta\rangle - \langle\eta^2\rangle}{ \langle\eta^2\rangle- \langle\eta\rangle^2} \left( 1 - \langle\eta\rangle \right).
$$
This model is particularly convenient because it has a natural support on the interval $[0,1]$ and provides a simple analytical expression that closely resembles numerically obtained distributions across a wide range of turbulence conditions.

The second group comprises models defined by beam-spot parameters at the aperture plane, such as the mean beam-spot radius, the variance of the beam-centroid position, and higher moments.
The beam-wandering model^[@vasylyev2012] accounts for the random deflection of the beam centroid from the propagation axis while neglecting beam-shape deformation.
It assumes a normally distributed beam-centroid position in the aperture plane, resulting in a log-negative Weibull distribution for the PDT.
The model depends only on the beam-shape parameters, and it is assumed to be applicable under weak turbulence conditions.

The elliptical-beam model^[@vasylyev2016] extends the beam-wandering approach by incorporating elliptical shape distortions, thereby capturing additional contributions to the cumulative beam decomposition of the intensity at the aperture plane.
This added complexity requires numerical evaluation of the model parameters.
This model was also proposed for weak or weak-to-moderate turbulence^[@vasylyev2016,vasylyev2018].

Finally, the total probability law model^[@vasylyev2018] separates the effects of beam wandering and beam-shape distortion.
It assumes that the shape distortion can be described by a truncated lognormal distribution.
The advantage of this model is that it provides accurate values of the mean transmittance; however, the model parameters must be determined numerically.

In conclusion, various models exist based on both phenomenological approaches and physically grounded formulations.
However, the further development of purely analytical, physically justified models is limited by the difficulty of expressing their parameters in closed analytical form.
In addition, all analytical models are formulated in terms of field correlation functions, which themselves involve significant approximations.
It also remains an open question under which conditions each model should be applied.


> #### Truncated lognormal distribution model.
> $\mathcal{P}(\eta; \left<\eta\right>, \left<\eta^2\right>)$
> origin, assumptions, key formula, and expected regime of validity.
>
> #### Beam-wandering model.
> $\mathcal{P}(\eta; W^2_\mathrm{ST}, \sigma_\mathrm{BW}^2)$
>
> #### Elliptical-beam model.
>
> #### Total probability law model.
>  $\mathcal{P}(\eta; \left<\eta\right>, \left<\eta^2\right>, W^2_\mathrm{ST}, \sigma_\mathrm{BW}^2)$
>

> - [ ] Where is the single-photon propagation introduced for the transmittance value?