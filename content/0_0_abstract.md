# Анотація {#sec:annotation_ua .unnumbered}
**Клен М.Д. Чисельне моделювання квантових каналів в турбулентній атмосфері**. *-- Квалiфiкацiйна наукова праця на правах рукопису.*
*Дисертацiя на здобуття наукового степеня доктора фiлософiї за спецiальнiстю 01.04.02 ”Теоретична фiзика” (104 - Фiзика та астрономiя). - Iнститут теоретичної фiзики iм. М.М. Боголюбова Нацiональної академiї наук України, Київ, 2026.*

**Ключовi слова:** .

**Cписок публiкацiй:**
1. сим
2. тайм кор

```{=latex}
\clearpage
```

> ознайомити зі змістом і результатами дослідження, узагальнено й лаконічно викласти суть наукової праці, позначити новаторство та практичну значимість.
> 5-7 pages

# Abstract {#sec:annotation_en .unnumbered}
**Klen M.D. Numerical simulation of atmospheric quantum channels.** -- *Qualifying scientific work in the form of a manuscript.*
*Dissertation for the degree of Doctor of Philosophy in the specialty 01.04.02 ”Theoretical Physics” (104 - Physics and Astronomy). - Bogolyubov Institute for Theoretical Physics of the National Academy of Sciences of Ukraine, Kyiv, 2025.*

> ## 1. Context and the Problem of Stochastic Transmittance

Free-space quantum channels enable long-distance quantum communication in regimes where optical fiber transmission is impractical. 
This includes very long distances where exponential fiber absorption losses prohibit fiber links, as well as communication between mobile platforms such as satellite-to-ground links and aircraft-based systems.
Optical radiation is the optimal carrier for quantum information in such scenarios because it preserves quantum states over long distances.
This enables a range of quantum communication protocols, including quantum key distribution, quantum teleportation, and entanglement swapping.
These capabilities are critical for global quantum network infrastructure and quantum internet architecture.

Quantum information is typically encoded in quasi-monochromatic optical pulses, which can be approximated as Gaussian beam modes.
However, atmospheric turbulence constitutes the dominant physical challenge.
Random refractive index fluctuations induce beam wander, wavefront distortion, scintillation, and beam spreading.
These effects depend nonlinearly on propagation distance, turbulence strength, and wavelength.
Subsequent measurements involve a finite optical system aperture, which truncates part of the distorted light profile.
This process is equivalent to a linear loss channel characterized by the transmittance $\eta$, defined as the fraction of beam power captured by the receiver aperture.
The single scalar $\eta$ encapsulates the complex three-dimensional propagation physics relevant for quantum state transmission.

Atmospheric turbulence is a stochastic process, making the channel transmittance a random variable. 
The probability distribution of transmittance $\mathcal P(\eta)$, fully characterizes the statistics of quasi-monochromatic pulse propagation through an atmospheric quantum channel. 
This framework enables explicit input-output relations between the transmitted and received quantum states, forming the basis for protocol performance analysis.

Several analytical models for the probability distribution of transmittance have been developed, but their range of validity remains unclear.
Although some models were validated by fitting, this approach lacks rigor and may represent parameters that are biased relative to actual atmospheric conditions.
Furthermore, some assumptions underlying these models have not yet been validated.
The existing framework describes an ensemble of independent single-beam propagation events.
In practice, the turbulence coherence time is on the order of milliseconds, so consecutive pulses propagate through correlated atmospheric conditions.
The probability distribution of transmittance cannot account for this temporal correlation.
Ignoring it discards the exploitable structure that could be used for protocol optimization and introduces vulnerabilities in quantum security protocols that assume independent channel realizations.

> ## 2. Development of a Numerical Framework

The description of atmospheric quantum channels involves finite spatial integration of the squared magnitude of a field governed by a stochastic partial differential equation.
This formulation hinders analytical progress and makes physical interpretation challenging.
Restrictive assumptions limit existing theory to specific limiting cases, leaving broader turbulence regimes beyond the reach of analytical characterization.
This creates a gap between theoretical description and characterization of transmittance statistics.

In this thesis, we employ numerical simulations to gain quantitative insight into the resulting transmittance statistics.
We employ the split step method for wave propagation in random media, which is widely used in classical optics and commonly referred to as the phase screen method.
To address the main limitation of this method, namely undersampling of the low frequency components of the turbulence spectrum, we adopt the sparse spectrum method for phase screen generation.

A central limitation of this approach is undersampling of the low frequency part of the turbulence spectrum. 
To overcome this limitation, we adopt the sparse spectrum method, which generates phase screens whose statistics match the prescribed theoretical spectrum.
With a proper choice of the number of phase screens and other simulation parameters, the sparse spectrum phase screen approach closes the gap between numerical simulation results and the underlying theoretical description.
Moreover, the ability to generate phase screens of arbitrary size with correct statistical properties enables the study of temporal evolution of atmospheric channels under Taylor frozen turbulence hypothesis. 
The resulting framework enables a comprehensive analysis of free space optical channels and quantum properties of light propagating through the atmosphere.

> ## 3. Validation of Physical Assumptions

We analyze the probability distribution of transmittance obtained from numerical simulations across three turbulence regimes and compare the results with analytical models.
For weak and moderate turbulence, the numerical distributions are bell-shaped and unimodal, while in the strong turbulence regime they become broader and flatter.
All distributions exhibit characteristic asymmetry near the transmittance boundaries at zero and one.
Using the Kolmogorov–Smirnov statistic, we quantify the difference between the empirical distributions and the analytical models.
We examine two physically motivated models, the beam-wandering and elliptical-beam models, alongside the truncated lognormal approach and a hybrid total-probability model.

- validation
    - we begin analysis by validation.
    - undertand the behaviour, properties
    - 

- tasks
    - the simulation of transmittance value through aperture enables validation of the existing analytical PDT models.
    - 
    - The existed analytical PDT models will be validated compared to the numerical simulation empirical PDT.
    - By analyzing the results of light propagation the unjustified assumptions used in analytical models is 
    - this approach allows the generation of phase scree which perfectly represent the theoretical equations ever for large size of phase screens.
- 
> ## 4. Introduction of New Analytical Models

- We introduce a highly applicable empirical model based on the Beta distribution and propose a simplified circular-beam approximation that utilizes a transmittance-moment matching technique to eliminate inherent biases. 
> ## 5. Analysis of Temporal Correlations

- Additionally, we extend our analysis beyond ensemble-averaging by investigating temporal correlations between consecutive pulses, introducing the two-time PDT to characterize the effects of atmospheric time-coherence on nonclassical state transfer.
> ## 6. Applications and Practical Significance

> від 5 до 15.

**Keywords:** 
Quantum Optics, 
Atmospheric Turbulence, 
Numerical Simulation, 
Probability Density of Transmittance, 
Entanglement, 
Phase Screens.

>в яких опубліковані основні наукові результати дисертації;
які засвідчують апробацію матеріалів дисертації;
які додатково відображають наукові результати дисертації.

**List of publications:**
1. Klen, M., & Semenov, A. A. (2023). Numerical simulations of atmospheric quantum channels. Physical Review A, 108(3). https://doi.org/10.1103/physreva.108.033718
2. Klen, M., Vasylyev, D., Vogel, W., & Semenov, A. A. (2024). Time correlations in atmospheric quantum channels. Physical Review A, 109(3). https://doi.org/10.1103/physreva.109.033712
3. Pechonkin, I., Klen, M., & Semenov, A. A. (2025). Circular-beam approximation for quantum channels in a turbulent atmosphere. Physical Review A, 112(6). https://doi.org/10.1103/pv7j-4zpf


```{=latex}
\clearpage
```