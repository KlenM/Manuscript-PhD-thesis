# Introduction
#### Relevance and Motivation.
> Focuses on the critical analysis of the current state of the field and the definition of the research problem.

> - Free space quantum channels are a central component of long distance quantum communication.
> - fibers a blackbone for local networks, but satellite-to-ground ... becaus vacuum near-zero absorption.
> - "last mile" problem - atmos turb degrades
> - not determenistically but stochastically
> - other tasks Quntum communication with moving parties .. involve propagation in atmosphere.
> 
> - stat props of the field ampitude after propagation through atmos ... was studied extensively^.
> - Defined concepts of the beam shape properties as beam wandering, spreading, speckles,..
> - However the qunatitty of interest transmittance is a derived quantity.
>     - (explain why it's quantity of interest)
> - it's complex because it's defined as integrated intensity over the aperture shape normalized on the emitted intensity
> - the statistical properties of it is not studied as well as .. .
> - current state .. are .. that a toolset of single-time prob dist of transm (PDT) models was esteblished.
> 
> - the range of validity of these models has remained unclear.
>     - Some of the models were validated with experimental data by fitting, but no compete understanding which model in which regime work better.
> - numsim
> 
> - The PDT provides a statistical description of the transmittance ensemble. 
> - It predicts the probability of different outcomes when a single pulse propagates through the atmosphere.
> - ignore correlations between consecutive pulses.
> - *It can be also used for the sequence of pulses when the time intervals between them are very large.*
> 
> - this thesis answers ....
> - to identify governing parameters, test model assumptions, and resolve temporal structure
> 
> - also:
>     - The Significance: Why does this matter right now?
>     - Thesis Map

> - horizontal links with constant Cn2
> - circular aperture

#### Research Purpose and Objectives.

#### Research Methods.

An analytical description of atmospheric quantum channels is complicated by the complexity of the underlying theoretical framework.
Closed form treatments rely on strong assumptions and do not capture the full statistical variability induced by turbulence.
In this work, the analysis is performed using numerical simulations.
The numerical framework is built around the sparse spectrum approach of the phase screen method combined with the modified von Karman turbulence spectrum.

Standard numerical approaches based on fast Fourier transforms with subharmonic corrections suffer from low frequency undersampling and rigid grid constraints.
These effects lead to biased channel statistics and distorted transmittance distributions.
The sparse spectrum model avoids these limitations through random sampling of spectral components within a logarithmic spectral domain.
This approach removes grid locking, restores correct low frequency behavior, and provides an accurate representation of turbulence.

One of the objectives of this study is to determine the applicability range of analytical channel models. 
For this purpose, the Kolmogorov-Smirnov statistic is used to quantify the statistical distance between model cumulative distributions and empirical distributions obtained from simulations.

The temporal dynamics are modeled using Taylor’s frozen turbulence hypothesis, which assumes that refractive index fluctuations are transported by transverse wind while remaining structurally unchanged.
By combining this hypothesis with a sparse spectrum approach, we can generate arbitrarily long phase screens to simulate the channel's temporal evolution.
This enables the consistent simulation of successive optical pulses as they propagate through the turbulent channel.

This framework is suitable for studying time dependent channel effects.
Temporal correlations are quantified using the Pearson correlation coefficient, which yields characteristic times over which transmittance values remain statistically correlated.

The numerical framework is applied to analyze the survival of quantum correlations and nonclassicality in the turbulent atmosphere.
For continuous variable states, Gaussian entanglement is certified using the Simon inseparability criterion.
Discrete variable entanglement is quantified by the Bell parameter in the Clauser-Horne-Shimony-Holt formulation.
Nonclassical photon statistics are characterized by the Mandel Q-parameter for ideal photodetection.
For the arrays of click on-off detectors, the Binomial Q parameter is used with the Bell-like inequalities approach in regimes where standard photocounting criteria become inconclusive.
Collectively, these metrics allow for a direct assessment of nonlocal correlations and nonclassical features in atmospheric quantum channels.

#### Scientific Novelty of the Results.

- *Systematic validation of analytical PDT models* was performed by benchmarking  against the results of numerical simulations. 
  Results show that common assumptions, such as the log-normal model’s validity in strong turbulence and the beam-wandering model’s validity in weak turbulence, are incomplete.
- *Receiver aperture as the dominant parameter shaping transmittance* was demonstrated by analyzing the ratio between aperture radius and beam size. 
  Small apertures yield PDTs skewed positively near zero, while larger apertures produce negative skewness. 
  These findings highlight the importance of accurately predicting the third moment of transmittance and explain why models with positive skew, such as the truncated log-normal, perform better for small apertures, whereas beam-shape–based models capture the negative skew for large apertures.
- *Misspecification bias in physically motivated models* arises when models are parametrized using beam-shape moments rather than transmittance moments. In this case, the resulting PDT exhibits a pronounced shift relative to numerical data, which can compromise quantum protocols that depend on precise mean and variance of transmittance.
- *Validation of statistical assumptions in beam-shape models* shows that while beam-centroid displacement is accurately Gaussian, it is not independent of beam deformations, particularly under strong turbulence. 
  Logarithms of beam semi-axes are not jointly Gaussian as assumed in the elliptic-beam model, exhibiting strong suppression along the diagonal. 
  These results indicate that more advanced statistical descriptions are required for precise transmittance distribution modelling.
- *Transmittance-moment matching method for beam-shape models* is introduced to eliminate the misspecification bias. 
  The parameters of the beam-shape models are expressed through transmittance moments rather than beam-shape parameters. 
  This method preserves physical interpretability while ensuring consistency with the key statistical characteristics of the quantum channel. 
  The resulting analytical model outperforms all previous beam-shape based approaches.
- *Empirical Beta distribution PDT model* provides a flexible alternative with natural support on [0,1]. 
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
For instance, small apertures lead to truncated log normal statistics, while larger apertures produce negatively skewed distributions consistent with beam shape based models.
This criterion allows for the systematic selection of models and replaces previous flawed selection heuristics.

To support practical applications, we introduce an empirical analytical model based on the Beta distribution.
The model is simple and flexible, yet remains fully analytical, and it reproduces the main classes of observed transmittance statistics.
Its parameters can be efficiently estimated from numerical or experimental data, making the model suitable for real time evaluation of quantum protocols under realistic atmospheric conditions.

Existing descriptions of atmospheric quantum channels treat quantum pulses as statistically independent ensembles.
This assumption breaks down in modern systems operating at high repetition rates, where successive pulses propagate through strongly correlated turbulence.
This thesis introduces the two time probability distribution of transmittance to explicitly describe joint statistics of two consecutive pulses.
We also introduce the aperture-averaged spatial coherence radius which provides a practical criterion for choosing pulse repetition rates that either exploit or suppress correlation effects, depending on the protocol objective.
This extension represents a necessary step from idealized single pulse models toward realistic high rate quantum communication.

Numerical simulations show that atmospheric turbulence allows preservation of entanglement over time scales of several milliseconds.
With further development of quantum memories, storage times of tens of milliseconds are expected for discrete variable entanglement.
Taken together, these results demonstrate the feasibility of correlation aware strategies, including adaptive selection techniques, for preserving nonclassicality in realistic atmospheric channels.

#### Statement of Authorship.

The research presented in the papers 1 and 2 was primarily conducted by the candidate. 
The scientific advisor, Andrii Semenov, provided the core conceptual ideas, research direction, and supervisory control throughout the project.
The co-authors -- specifically D. Vasylyev, W. Vogel, and M. Bohmann -- provided assistance through enlightening discussions that helped refine the theoretical results and the interpretation of simulated data.

In the paper 3 my individual contributions to the research included providing the numerical framework utilized for beam shape distribution analysis and performing the extensive model validation. 
Additionally, I proposed the moment matching technique to eliminate the model-misspecification bias found in previous models. 

#### Approbation of Research Results.

The results of the dissertation were presented at seminars of the Bogolyubov Institute for Theoretical Physics of the National Academy of Sciences of Ukraine, as well as at Ukrainian and international conferences, in particular:
1. M. Klen and A. A. Semenov, "Free-space quantum channels: Numerical simulations", US-Ukraine Quantum Forum 2023, August 28-31, 2023
2. M. Klen, "Quantum light in atmospheric turbulence", 25th Symposium on photonics and optics SPO 2024, Kyiv, (Ukraine), November 8, 2024 
3. M. Klen, "Numerical simulations in free-space quantum channels", poster session at Quantum 2025: From Foundations of Quantum Mechanics to Quantum Information and Quantum Metrology & Sensing, Turin, (Italy), May 18-24, 2025

#### Structure and Volume of the Thesis. 

The dissertation consists of an introduction, seven chapters, conclusions, and a list of references (0 titles). 
The total volume of the work is 0 pages, including 0 tables and 0 figures.

#### Relationship of the Work to Scientific Programs and Grants. 

The dissertation was completed at the Bogolyubov Institute for Theoretical Physics of the National Academy of Sciences of Ukraine. 
It is related to the following academic programs, topics, and grants:
1. National Research Foundation of Ukraine through Project No. 2020.02/0111, Nonclassical and hybrid correlations of quantum systems under realistic conditions. 
2. National Research Foundation of Ukraine through Project No. 2023.03/0165, Quantum correlations of electromagnetic radiation. 
3. Simons Foundation “Presidential Discretionary-Ukraine Support grant” 

```{=latex}
\clearpage
```
