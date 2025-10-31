# Background
While classical optics provides *a deterministic description of electromagnetic wave propagation*, it fails to capture the inherently probabilistic and nonclassical properties of light observed at the quantum level. 
Quantum optics, developed to describe these effects, offers the theoretical framework for understanding coherence, entanglement, and other features of nonclassical radiation. 
However, most quantum optical studies assume deterministic homogeneous propagation conditions. 
In reality, atmospheric turbulence introduces random fluctuations that destroy coherence and entanglement, turning a deterministic quantum channel into a stochastic one.
Extending this framework to include atmospheric turbulence introduces additional challenges due to the random, time-dependent nature of the propagation channel.

## Quantum Optics
Classical optics, built on Maxwell’s equations, describes light as a deterministic, smooth electromagnetic wave.
It explains reflection, interference, diffraction, and polarization with remarkable success.
But in the first half of the 20th century, it remained unclear whether light was truly a wave or a collection of quanta.
While theoretical developments anticipated the photon concept, no experiment could prove its necessity.
The photoelectric effect, often referred to as evidence of photons, can be also described within a semiclassical framework: a continuous electromagnetic field interacting with quantized matter.
Taylor’s double-slit experiment with extremely weak light, performed in 1909^[@taylor1909], later was used as evidence in the debate over whether light behaves as a wave or as discrete quanta^[@slater1925].^[This part must be rewritten]

This uncertainty persisted until 1976, when Kimble, Dagenais, and Mandel developed^[@kimble1976] a theory describing the two-time intensity correlations of light emitted by a two-level atom, and then observed photon antibunching effect experimentally in 1977^[@kimble1977].
This phenomenon cannot be explained by any classical electromagnetic field and confirms the quantum nature of light.

Later on, many other quantum features of light were demonstrated.
The observation of squeezed states, which demonstrates variance below vacuum noise in one quadrature, was reported by Slusher et al. in 1985^[@slusher1985].
An illustrative counter-intuitive example of multi-photon interference, Hong-Ou-Mandel effect, demonstrated by Hong et al.  in 1987^[hong1987].
Furthermore, numerous experimental tests of Bell inequalities using entangled photons have been performed in various configurations ^[@aspect1981,tittel1998,weihs1998,hensen2015,brunner2014], highlighting the nonclassical correlations of light.

Despite the late growth of experimental studies, the theoretical framework of quantum optics had already been well established much earlier. 
Foundational contributions were made by Glauber^[@glauber1963b], Mandel^[@mandel1965], and other pioneers, who developed the groundwork for understanding the quantum properties of light long before many of the mentioned experiments were conducted. 

In the early 1960s, Roy Glauber introduced the idea of representing quantum states of light $\hat\rho$ as a linear expansion over coherent states^[@glauber1963a,sudarshan1963a]
$$\hat\rho=\int P(\alpha)\,|\alpha\rangle\langle\alpha|\,\mathrm{d}^{2}\alpha$$
where $|\alpha\rangle$ are coherent states -- eigenvectors of the annihilation operator -- which form an overcomplete basis of the Hilbert space, $\mathrm{d}^2\alpha = \mathrm{d}\mathrm{Re}\alpha \mathrm{d}\mathrm{Im}\alpha$ and $P(\alpha)$ is the Glauber-Sudarshan P-function, a quasiprobability distribution over phase space. 
If $P(\alpha)$ is a well-behaved, positive function, the quantum state can be interpreted as a classical mixture of coherent fields; if it is negative or singular, the state exhibits some nonclassical features^[@mandel1986,sperling2020].
Later, this idea was formalized and extended into the broader phase-space formalism of quantum mechanics^[@cohen1966] which has become the mainstream framework used today to describe quantum states of light.
 
## Quantum light in atmosphere
- motivated mainly from secure Quantum Communication
    - Photons are preferred due to low interaction with the environment and ability to encode quantum information (qubits).
    - But Free-space propagation introduces turbulence, scattering, absorption, and background noise.
    - Pionering works: Buttler et al. demonstrated QKD over 1 km free-space channel in the open air^[@buttler1998]. Hughes et al., transmission of single photons over 1.6 km urban free-space channel, showing atmospheric turbulence and background light can be managed^[@hughes2002].
    - Entanglement: 2007–2008: Experiments by Ursin et al. in Vienna, distributing entangled photons over 144 km between Canary Islands, achieving long-distance free-space entanglement distribution.
    - Moving Platforms, ground to satellite channels: 2012–2013: Experiments transmitting single photons from moving aircraft and high-altitude platforms, simulating satellite-to-ground channels.
    - Satellite-Based Quantum Communication Milestones: 2017: Chinese Micius satellite demonstrates satellite-to-ground QKD over 1,200 km, establishing feasibility of global quantum communication.
- Theory: 
    - Classical: Kolmogorov, Tatarskii,  
    - Quantum case
        - energy (photon number) conservation problem
        -  degradation of entanglement, nonclass, etc under turbulence. 

adaptive optics, post selection

## Quantum channel modeling
- PDT
    - Most models focus on single-parameter descriptions (e.g., average loss), often ignoring higher-order correlations (examples? :) )

### Truncated Log-normal distribution model

### Beam wandering model

### Total probability law model

### Elliptical beam model

## Unresolved issues
- Lot of approximation limits analytical approaches
- Validation/Applicability of models is unclear
- No time dependence study

> - longnormal - strong; weak - beam wandering
> - weak - beam wandering effects; strong - beam spreading (source?..)

## Problem Statement

> Note – Conclusions and Formulation of Research Tasks
>
> * “The analysis conducted above has shown that there exist ... (methods, models, tools, devices, structures, technologies, etc.), but they have many shortcomings, such as: ...
> * Therefore, it is necessary to develop ... (state the research goal — often expanded — emphasizing advantages that address the shortcomings of existing scientific and technical achievements).
> * To achieve this goal, the following research tasks should be solved (listed below as a numbered list, taken from the Introduction, except for the first one, which typically concerns reviewing and analyzing literature and current scientific and technical progress).”

1. —
2. —
3. —