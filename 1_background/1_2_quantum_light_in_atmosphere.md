## Quantum light in atmosphere
The study of quantum light propagation through the atmosphere was initially motivated by the task of secure quantum communication, particularly Quantum Key Distribution (QKD). 
Unlike classical encryption, QKD security does not rely on computational hardness but on fundamental quantum laws forbidding perfect cloning of quantum states.
Photons are natural candidates for quantum communication because they interact weakly with the environment, can be transmitted over long distances, and support multiple encoding degrees of freedom -- polarization, phase, time-bin, or orbital angular momentum.
However, the description of light propagation through the atmosphere becomes complicated due to random fluctuations of the refractive index, which cause turbulence-induced effects such as beam wandering, wavefront distortion, and intensity scintillation.

### Experimental contributions
Pioneering experimental efforts soon followed. Buttler et al. demonstrated the first outdoor QKD over a 1 km free-space link, proving that quantum states of light could survive real atmospheric conditions ^[@buttler1998].
Shortly after, Hughes et al. extended this to a 1.6 km urban channel, showing that the combined effects of turbulence and background light could be effectively mitigated ^[@hughes2002].
Entanglement-based experiments pushed the boundaries further. In 2007 Ursin et al. successfully distributed entangled photons over a 144 km free-space channel between the Canary Islands, demonstrating that quantum entanglement could be preserved over unprecedented long distances ^[@ursin2007].
In 2008–2009, experiments involving Earth-based and satellite stations, for both uplinks and downlinks, enabled the analysis of the feasibility of various QKD protocols ^[@villoresi2008,bonato2009].
The launch of the Micius satellite in 2016 enabled quantum communication between cities via satellite, linking ground stations in Beijing and Graz (Austria), separated by 7600 km on Earth^[@liao2018].
This demonstrated that long-distance quantum links can be maintained through the atmosphere despite turbulence, absorption, and background light, opening the way toward a global quantum network.

> [!note]- Options
> - Teleportation: https://www.nature.com/articles/nature11472 , https://www.nature.com/articles/nature23675

### Foundation of classical theory of light in atmosphere
Theory of quantum light propagation in the atmosphere is based on the classical studies of light propagation through turbulent media.
The theoretical roots lie in the statistical theory of turbulence formulated by A. N. Kolmogorov (1941)^[@kolmogorov1941].
Kolmogorov introduced a model for energy transfer in incompressible turbulent flows, where energy cascades from large to small scales.
In the inertial range, this leads to the $\kappa^{-11/3}$ power spectrum of refractive-index fluctuations.

In the early theoretical treatments of wave propagation through random media, the Born approximation was first employed to describe single scattering events, assuming weak refractive-index fluctuations and negligible multiple scattering effects^[@andrews2005].
Later, Tatarskii, based on the Rytov approximation, introduced the second-order perturbation term^[@tatarski1961], and presented a comprehensive theory of wave propagation in a turbulent atmosphere, rigorously connecting the statistical properties of refractive-index fluctuations with the resulting effect on optical waves^[@tatarskii1971].
This method is widely used for analyzing the statistical properties of optical fields propagating through turbulent atmosphere, allowing one to compute quantities such as the log-amplitude and phase variance functions, intensity and phase correlations, and the structure function. 
Nevertheless, this formulation remains valid only under weak turbulence conditions.

Further developments aimed at extending the range of validity beyond weak turbulence have employed alternative frameworks such as the parabolic equation method and extended Rytov theory^[@andrews2005], the phase approximation of the Huygens–Kirchhoff method^[@banakh1977], and the photon distribution function approach^[@baskov2018]. 
In contemporary studies, many approaches are based on the extended Huygens–Fresnel (eHF) principle^[@lutomirski1971]. 
However, it has been pointed out that commonly used variations of this method do not provide significant improvements over traditional methods^[@charnotskii2015].

An alternative and widely used approach for simulating wave propagation through turbulence is the phase screen method. 
In this technique, the turbulent medium is modeled as a series of discrete, statistically independent layers that impose random phase distortions on the wavefront, allowing efficient numerical computation of amplitude and phase fluctuations over long propagation distances. 
The theoretical description and implementation details of this method are discussed in the following ^[@sec:2_0_numsim].

### Probability density function  of the irradiance
Of particular interest is the probability density function  of the irradiance.
It provides a statistical description of the intensity fluctuations, or scintillations. 
In weak fluctuation regimes, assuming a Gaussian refractive-index field and using the Born approximation with first-order perturbation theory, the irradiance is described by the modified Rician distribution. 
However, experimental studies by Parry and Pusey^[@parry1979] showed that the theoretical moments predicted by this model were systematically lower than measured values, even under weak turbulence conditions.
Within the first-order Rytov approximation, the irradiance fluctuations are well described by the lognormal distribution^[*Add description of lonormal*]. 
This model generally agrees well with observations for short propagation paths or weak turbulence but fails to capture the statistics of irradiance under strong turbulence, indicating the need for more sophisticated models in such regimes.

While the irradiance fluctuations are well described by the lognormal distribution in weak turbulence, experiments show that under very strong turbulence, the distribution tends toward a negative exponential. 
To account for strong scintillations, several models have been proposed^[@andrews2005]. 
The K-distribution^[@jakeman1978] is based on a modulation process in which the irradiance follows a conditional negative exponential modulated with the gamma distributed process, providing good agreement with experimental data. 
The lognormal–Rician distribution models the irradiance as Rician, modulated by a lognormal distribution, and has been shown to better fit experimental observations^[@churnside1989], although it does not have a closed-form expression. 
The gamma–gamma distribution^[@al-habash2001] generalizes the K-distribution, with parameters that can be related to atmospheric conditions through models for large-scale and small-scale scintillations, and it offers a closed-form expression for the cumulative distribution function.
Despite their empirical success in describing irradiance fluctuations in strong turbulence, these models remain phenomenological rather than being derived from first principles.

### Probability density function of photocounting
In the studies discussed above, the optical intensity is typically high, resulting in a continuous photocurrent. 
However, when the intensity is on the order of individual photons and the detection time interval is short, the detector registers random discrete pulses. 
The quantity of interest in this regime is the probability density function of photocounting.

In 1970, it was proposed to modulate the photocounting statistics with the previously discussed lognormal distribution of the mean photon count^[@diament1970]. 
While this approach can be useful in certain specific cases^[@milonni2004], the infinite tail of the lognormal distribution implies unphysical photon amplification, making it unsuitable as a general model and requiring further study to establish a description of atmospheric turbulence effects on quantum states.

> entanglement, nonclass, etc in turbulence. 
> adaptive optics, post selection