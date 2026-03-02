# Introduction
#### Relevance and Motivation.

Free-space quantum channels are a core element of long distance quantum communication.
Optical fibers form the backbone of local and regional networks.
Global scale communication, however, requires satellite-to-ground links, where propagation occurs predominantly in vacuum with near zero absorption.
Several other quantum communication tasks also rely on free-space propagation, including links with moving platforms and mobile ground stations.
In all such scenarios, atmospheric propagation is unavoidable at least over part of the link.

Atmospheric turbulence constitutes a dominant obstacle in these channels.
Its effect arises from stochastic fluctuations of the atmospheric refractive index, which induce random variations of the received optical signal.
The statistical properties of the optical field amplitude after atmospheric propagation have been studied extensively.
Well established concepts describe beam wandering, beam spreading, scintillation, and speckle formation.
These descriptions capture the spatial structure of the optical field at the receiver plane but do not directly address the quantities most relevant for quantum communication.

For practical quantum communication, the relevant quantity is the channel transmittance.
It is defined as the optical intensity integrated over the receiver aperture and normalized to the emitted intensity.
Transmittance is the central random variable that determines the quantum state of a quasi-monochromatic light mode after propagation through the atmosphere.
Therefore, an accurate characterization of the PDT is required for the description of quantum-state propagation in free space.

Despite its importance, transmittance has received less systematic treatment than field amplitude statistics.
Existing analytical models of the PDT are derived either from field statistics at a fixed spatial point or from phenomenological descriptions of first order beam shape parameters at the aperture plane.
However, the applicability range of these models remains unclear.
Several distributions have been validated by fitting experimental data, but this approach does not establish clear criteria for model selection.
Without a clear understanding of their domain of validity, the predictive power of these models is limited.

A further conceptual gap arises from the implicit assumption of statistical independence between pulses in the standard PDT framework.
The PDT provides an ensemble description of a single propagation event and treats successive pulses independently.
This assumption holds only when the time separation between pulses exceeds the atmospheric correlation time.
In modern high repetition rate quantum communication systems, consecutive pulses propagate through strongly correlated turbulence.
In this regime, temporal correlations become significant and must be explicitly accounted for.
Addressing this limitation is essential for realistic modeling of high rate atmospheric quantum channels.

> - [ ] horizontal links with constant Cn2
> - [ ] circular aperture

#### Research Purpose and Objectives.

The purpose of this work is to establish a comprehensive framework for the accurate characterization of atmospheric quantum channels by advancing the modeling of transmittance statistics and temporal correlations in order to determine the quantum properties of light propagating through a turbulent atmosphere.
To achieve this purpose, the following objectives are formulated:
- Develop a robust numerical model of atmospheric quantum channels that enables accurate spatial and temporal sampling of channel transmittance.
- Systematically validate existing analytical PDT models over a wide range of turbulence regimes, including weak, moderate, and strong turbulence, and identify their domains of applicability.
- Investigate the statistical properties of beam-shape parameters in order to test the unverified assumptions underlying physically motivated models.
- Based on the results of the preceding analyses, develop improved analytical models of atmospheric quantum channels.
- Analyze and quantify temporal correlations of transmittance fluctuations.
- Evaluate quantum properties in turbulent media under realistic conditions, including continuous-variable and discrete-variable entanglement between temporally separated pulses, as well as the efficiency of adaptive real time selection techniques for preserving optical nonclassicality.

#### Research Methods.

An analytical description of atmospheric quantum channels is complicated by the complexity of the underlying theoretical framework.
Closed form treatments rely on strong assumptions and do not capture the full statistical variability induced by turbulence.
In this work, the analysis is performed using numerical simulations.
The numerical framework is built around the sparse-spectrum approach of the phase-screen method applied with the modified von Kármán turbulence spectrum.

Standard numerical approaches based on fast Fourier transforms with subharmonic corrections suffer from low frequency undersampling and rigid grid constraints.
These effects lead to biased channel statistics and distorted transmittance distributions.
The sparse-spectrum model avoids these limitations through random sampling of spectral components within a logarithmic spectral domain.
This approach removes grid locking, restores correct low frequency behavior, and provides an accurate representation of turbulence.

One of the objectives of this study is to determine the applicability range of analytical channel models.
For this purpose, the Kolmogorov-Smirnov statistic is used to quantify the statistical distance between model cumulative distributions and empirical distributions obtained from simulations.

The temporal dynamics are modeled using Taylor's frozen turbulence hypothesis, which assumes that refractive index fluctuations are transported by transverse wind while remaining structurally unchanged.
By combining this hypothesis with a sparse-spectrum approach, we can generate arbitrarily long phase screens to simulate the temporal evolution of the channel.
This enables the consistent simulation of successive optical pulses as they propagate through the turbulent channel.

This framework is suitable for studying time dependent channel effects.
Temporal correlations are quantified using the Pearson correlation coefficient, which yields characteristic times over which transmittance values remain statistically correlated.

The numerical framework is applied to analyze the survival of quantum correlations and nonclassicality in the turbulent atmosphere.
For continuous variable states, Gaussian entanglement is certified using the Simon inseparability criterion.
Discrete variable entanglement is quantified by the Bell parameter in the Clauser-Horne-Shimony-Holt formulation.
Nonclassical photon statistics are characterized by the Mandel Q-parameter for ideal photodetection.
For the arrays of click on-off detectors, the Binomial Q parameter is used with the Bell-like inequalities approach in regimes where standard photocounting criteria become inconclusive.
Collectively, these metrics allow for a direct assessment of entanglement and nonclassical features in atmospheric quantum channels.

#### Scientific Novelty of the Results.

- *Systematic validation of analytical PDT models* was performed by benchmarking  against the results of numerical simulations.
  Results show that common assumptions, such as the validity of the lognormal model in strong turbulence and the validity of the beam-wandering model in weak turbulence, are incomplete
- *Receiver aperture as the dominant parameter shaping transmittance* was demonstrated by analyzing the ratio between aperture radius and beam size.
  Small apertures yield PDTs skewed positively near zero, while larger apertures produce negative skewness.
  These findings highlight the importance of accurately predicting the third moment of transmittance and explain why models with positive skew, such as the truncated lognormal, perform better for small apertures, whereas beam-shape based models capture the negative skew for large apertures.
- *Misspecification bias in physically motivated models* arises when models are parametrized using beam-shape moments rather than transmittance moments. In this case, the resulting PDT exhibits a pronounced shift relative to numerical data, which can compromise quantum protocols that depend on precise mean and variance of transmittance.
- *Validation of statistical assumptions in beam-shape models* shows that while beam-centroid displacement is accurately Gaussian, it is not independent of beam deformations, particularly under strong turbulence.
  Logarithms of beam semi-axes are not jointly Gaussian as assumed in the elliptic-beam model, exhibiting strong suppression along the diagonal.
  These results indicate that more advanced statistical descriptions are required for precise transmittance distribution modelling.
- *Transmittance-moment matching method for beam-shape models* is introduced to eliminate the model misspecification bias.
  The parameters of the beam-shape models are expressed through transmittance moments rather than beam-shape parameters.
  This method preserves physical interpretability while ensuring consistency with the key statistical characteristics of the quantum channel.
  The resulting analytical model outperforms all previous beam-shape based approaches.
- *Empirical Beta distribution PDT model* provides a flexible alternative to existing heuristic models with the natural support on [0,1].
  Parameterized by the first two transmittance moments, allowing it to capture a highly variable range of distribution shapes, it captures the transition from positive to negative skewness with changing aperture size.
  It generally outperforms existing analytical models across turbulence regimes and aperture sizes.
- *Two-Time PDT framework* generalizes the channel description from static ensemble averages by introducing the joint transmittance distribution at two times. This captures temporal correlations between pulses in high-repetition-rate systems and enables analysis of time-bin encoded protocols.
- *Introduction of aperture-averaged spatial coherence radius* $\rho_0$ defines the wind-driven displacement at which transmittance correlations decay to $e^{-1}$.
  It scales approximately linearly with aperture radius, quantifying temporal coherence and guiding optimal pulse separation or repetition rates for quantum protocols.
- *Quantification of temporal resources in atmospheric channels for quantum protocols* demonstrates that entanglement can be preserved over millisecond timescales.
  The main limiting factor for discrete-variable entanglement is quantum memory; under ideal memory conditions, preservation extends to tens of milliseconds.
  Adaptive selection using bright classical pulses is analyzed under realistic constraints, providing quantitative bounds for exploiting temporal correlations to maintain nonclassicality.
  These results indicate substantial potential to enlarge the effective Hilbert-space dimensionality.

#### Practical Significance.

A central difficulty in current practice is the absence of clear criteria for selecting analytical models of the PDT in a given scenario.
Here, we resolve this ambiguity by establishing a correspondence between the ratio of the receiver aperture radius to the averaged beam radius and the analytical models that perform accurately in the corresponding regime.
For instance, small apertures lead to truncated lognormal statistics, while larger apertures produce negatively skewed distributions consistent with beam shape based models.
This criterion allows for the systematic selection of models and replaces previous flawed selection heuristics.

To support practical applications, we introduce an empirical analytical model based on the Beta distribution.
The model is simple and flexible, yet remains fully analytical, and it reproduces the main classes of observed transmittance statistics.
Its parameters can be efficiently estimated from numerical or experimental data, making the model suitable for real time evaluation of quantum protocols under realistic atmospheric conditions.

Existing descriptions of atmospheric quantum channels treat quantum pulses as statistically independent ensembles.
This assumption breaks down in modern systems operating at high repetition rates, where successive pulses propagate through strongly correlated turbulence.
This thesis introduces the two-time PDT to explicitly describe joint statistics of two consecutive pulses.
We also introduce the aperture-averaged spatial coherence radius which provides a practical criterion for choosing pulse repetition rates that either exploit or suppress correlation effects, depending on the protocol objective.
This extension represents a necessary step from idealized single pulse models toward realistic high rate quantum communication.

Numerical simulations show that atmospheric turbulence allows preservation of entanglement over time scales of several milliseconds.
With further development of quantum memories, storage times of tens of milliseconds are expected for discrete variable entanglement.
Taken together, these results demonstrate the feasibility of correlation aware strategies, including adaptive selection techniques, for preserving nonclassicality in realistic atmospheric channels.

#### Statement of Authorship.

The research presented in the papers 1 and 2 was primarily conducted by the candidate.
The scientific advisor, A. A. Semenov, provided the core conceptual ideas, research direction, and supervisory control throughout the project.
The co-authors---specifically D. Vasylyev and W. Vogel---provided assistance through enlightening discussions that helped refine the theoretical results and the interpretation of simulated data.

In the paper 3 my individual contributions to the research included providing the numerical framework utilized for beam shape distribution analysis and performing the extensive model validation.
Additionally, I proposed the moment matching technique to eliminate the model-misspecification bias found in previous models.

In the paper 4 my individual contribution consisted of conducting numerical modeling, analyzing the obtained data, and preparing representative visualization materials, which constituted the basis of the presented materials.

#### Approbation of Research Results.

The results of the dissertation were presented at seminars of the Bogolyubov Institute for Theoretical Physics of the National Academy of Sciences of Ukraine, as well as at Ukrainian and international conferences, in particular:
1. M. Klen and A. A. Semenov, "Free-space quantum channels: Numerical simulations", US-Ukraine Quantum Forum 2023, August 28-31, 2023
2. M. Klen, "Quantum light in atmospheric turbulence", 25th Symposium on photonics and optics SPO 2024, Kyiv, (Ukraine), November 8, 2024
3. M. Klen, "Numerical simulations in free-space quantum channels", poster session at Quantum 2025: From Foundations of Quantum Mechanics to Quantum Information and Quantum Metrology & Sensing, Turin, (Italy), May 18-24, 2025
4. A. Semenov, M. Klen, I. Pechonkin, "Quantum optics in the turbulent atmosphere: fundamental issues and applications": invited talk at the SPIE Sensors+Imaging Meeting. Quantum Technologies for Defense and Security II. Madrid, Spain. September 15–18, 2025.

#### Structure and Volume of the Thesis.

The dissertation consists of an introduction, seven chapters, conclusions, and a list of references (122 references).
The total volume of the work is 152 pages, including 90 equations, 9 tables and 31 figures.

#### Relationship of the Work to Scientific Programs and Grants.

The dissertation was completed at the Bogolyubov Institute for Theoretical Physics of the National Academy of Sciences of Ukraine.
It is related to the following academic programs, topics, and grants:
1. Відомча тема відділення фізики та астрономії НАН України “Індуковані шумом динаміка та кореляції в нерівноважних системах”, Р/К 0120U101347.
2. Відомча тема відділення фізики та астрономії НАН України “Стохастичні процеси в конденсованих середовищах, біологічних системах та полях випромінювання”, Р/К  0125U000031.
3. Project of National Research Foundation of Ukraine No. 2020.02/0111, “Nonclassical and hybrid correlations of quantum systems under realistic conditions”.
4. Project of National Research Foundation of Ukraine No. 2023.03/0165 “Quantum correlations of electromagnetic radiation”.
5. Project Simons Foundation International SFI-PD-Ukraine-00014573, PI LB.


```{=latex}
\clearpage
```
