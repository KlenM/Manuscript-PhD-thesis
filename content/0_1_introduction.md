# Introduction
> - Motivation, Relevance of the topic
> - Aim and objectives of the research
> - Research methods
> - Scientific novelty of the obtained results
> - Practical significance of the obtained results
> - Personal contribution of the researcher
> - List of publications
> - Approval/validation of the results
> - Acknowledgements


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

#### Statement of Authorship.

#### Approbation of Research Results.

#### Structure and Volume of the Thesis. 

The dissertation consists of an introduction, fourXXX chapters, conclusions, a list of references (xxx titles), and x appendices. The total volume of the work is xxx pages, including xx tables and xx figures.
> corresponding to logically completed stages of research

#### Relationship of the Work to Scientific Programs, Plans, Themes, and Grants. 
