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
The probability distribution of transmittance (PDT), fully characterizes the statistics of quasi-monochromatic pulse propagation through an atmospheric quantum channel. 
This framework enables explicit input-output relations between the transmitted and received quantum states, forming the basis for protocol performance analysis.

Several analytical models for the PDT have been developed, but their range of validity remains unclear.
Although some models were validated by fitting, this approach lacks rigor and may represent parameters that are biased relative to actual atmospheric conditions.
Furthermore, some assumptions underlying these models have not yet been validated.
The existing framework describes an ensemble of independent single-beam propagation events.
In practice, the turbulence coherence time is on the order of milliseconds, so consecutive pulses propagate through correlated atmospheric conditions.
The probability distribution of transmittance cannot account for this temporal correlation.
Ignoring it discards the exploitable structure that could be used for protocol optimization and introduces vulnerabilities in quantum security protocols that assume independent channel realizations.

> - [ ] Add ground that analyt model applic assumed to be based on turbulence conditions.

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

We analyze the probability distribution of transmittance obtained from numerical simulations for free space optical channels under weak, moderate, and strong turbulence regimes.
The numerical results are compared with several analytical models.
These include two physically motivated beam-shape based models, namely the beam wandering and elliptical beam models, the truncated lognormal model, and a hybrid approach the total probability model.
The agreement between empirical and analytical distributions is quantified using the Kolmogorov-Smirnov statistic.

The numerical distributions are generally unimodal and bell shaped.
In strong turbulence they become broader and flatter.
Since the transmittance is bounded between zero and one, this constraint strongly affects the distribution shape.
The aperture size relative to the average beam size is identified as the dominant control parameter.
For small apertures, transmittance values concentrate near zero, which enforces a positive skew.
For large apertures, the upper bound at unity induces negative skew.
Accurate prediction of the first moments of transmittance is therefore necessary for any analytical model to produce valid distributions.

Our findings reveal that the applicability of a model is predominantly influenced by the ratio of the aperture to the average beam size.
Consequently, the conventional model-selection heuristics based on turbulence strength are seen as inferior.
The truncated lognormal model, which always exhibits positive skew, provides a consistent description for small apertures across all turbulence regimes but its accuracy worsens for larger apertures.
The beam-shape based models mainly exhibit negative skew, which makes them more suitable for large aperture channels, where they provide an accurate match to the shape of the probability distribution of transmittance.
However, these models suffer from misspecification bias because they are parameterized through moments of beam shape variables instead of transmittance itself.
This leads to systematic shifts of the distribution mode and inaccurate estimation of the mean transmittance.
The total probability model, which combines these two approaches, captures the skewness transition induced by changes in the aperture size.
For small apertures, its performance closely follows that of the lognormal model, while for large apertures it yields some improvement in the predicting of the transmittance distribution.

 To mitigate the misspecification bias, we introduce a transmittance matching technique that reformulates beam-shape based models in terms of the first moments of transmittance.
This method is applied to a model with an intermediate description between the beam wandering and elliptical beam models because of the complex, semi-analytical formulation of the latter.
Despite its simpler formulation compared to the elliptical beam model, it generally outperforms it across all turbulence regimes.

We also test key assumptions underlying physically based models.
The beam centroid is confirmed to follow a two dimensional normal distribution, but its statistical independence from beam shape deformations is violated, especially in strong turbulence.
In the elliptical beam model, the logarithms of the semi axes are assumed to follow a bivariate Gaussian distribution. 
Numerical simulations instead reveal a strong suppression of probability density along the diagonal, which indicates that the two axes are rarely equal.
These findings will guide the future development of the beam-shape based models.

Finally, we propose an empirical model of PDT based on the Beta distribution.
Its bounded support naturally matches the physical range of transmittance and it reproduces the skewness transition with aperture size.
This model generally outperforms all other considered analytical models, and its simple analytical formulation makes it well-suited for theoretical predictions and practical application.

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