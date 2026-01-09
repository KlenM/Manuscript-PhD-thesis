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

## 1. Context and the Problem of Stochastic Transmittance
Free-space quantum channels enable long-distance quantum communication in regimes where optical fiber transmission is impractical. 
This includes very long distances where exponential fiber absorption losses prohibit fiber links, as well as communication between mobile platforms such as satellite-to-ground links and aircraft-based systems.
Optical radiation is the optimal carrier for quantum information in such scenarios because it preserves quantum states over long distances.
This enables a range of quantum communication protocols, including quantum key distribution, quantum teleportation, and entanglement swapping.
These capabilities are critical for global quantum network infrastructure and quantum internet architecture.

Quantum information is typically encoded in quasi-monochromatic optical pulses, which can be approximated as Gaussian beam modes.
However, turbulent atmospheric turbulence constitutes the dominant physical obstacle.
Random refractive index fluctuations induce beam wander, wavefront distortion, scintillation, and beam spreading.
These effects depend nonlinearly on propagation distance, turbulence strength, and wavelength.
Subsequent measurements involve a finite optical system aperture, which truncates part of the distorted light profile.
This process is equivalent to a linear loss channel characterized by the transmittance $\eta$, defined as the fraction of beam power captured by the receiver aperture.
The single scalar $\eta$ encapsulates the complex three-dimensional propagation physics relevant for quantum state transmission.

Atmospheric turbulence is a stochastic process, making the channel transmittance a random variable. 
The probability distribution of transmittance $\mathcal P(\eta)$, fully characterizes the statistics of quasi-monochromatic pulse propagation through an atmospheric quantum channel. 
This framework enables explicit input-output relations between the transmitted and received quantum states, forming the basis for protocol performance analysis.

Several analytical models for the probability distribution of transmittance have been developed, but their range of validity remains unclear.
Several models were validated by fitting, but this approach lacks rigor and can yield parameters biased relative to actual atmospheric conditions.
Furthermore, some assumptions underlying these models have not yet been validated.
The developed framework describes an ensemble of independent single-beam propagation events.
In practice, the turbulence coherence time is on the order of milliseconds, so consecutive pulses propagate through correlated atmospheric conditions.
Existing framework cannot account for this temporal correlation.
Ignoring it discards the exploitable structure that could be used for protocol optimization and introduces vulnerabilities in quantum security protocols that assume independent channel realizations.

## 2. Development of a Numerical Framework

- such us description of aqc involve stochastic diferent eq with finited intgration of solution the analysical approaches are limited and involves huge approx.
- This limits discovery and understanding.
- In this thesis, we develop a comprehensive numerical framework based on the sparse-spectrum model of the phase-screen method to systematically evaluate atmospheric quantum channels and validate existing PDT models. 
## 3. Validation of Physical Assumptions
## 4. Introduction of New Analytical Models

- We introduce a highly applicable empirical model based on the Beta distribution and propose a simplified circular-beam approximation that utilizes a transmittance-moment matching technique to eliminate inherent biases. 
## 5. Analysis of Temporal Correlations

- Additionally, we extend our analysis beyond ensemble-averaging by investigating temporal correlations between consecutive pulses, introducing the two-time PDT to characterize the effects of atmospheric time-coherence on nonclassical state transfer.
## 6. Applications and Practical Significance

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