# Validation of existing models
 - why pdf study matters - repeat the problem statement idea of "lognomal for strong or weak"
 - (goal) validate analytical models of PDT against numerical simulations and to identify their ranges of applicability across three system conditions.
 - description of parameters
 - evaluation metric
     - pros: in many task excidance is important - CDF. So the KS shows the difference between CDFs. 
 - structure

## Type of parameters
- (Nature -) Experiment - Kolmogorov theory - Correlation function - Model parameters ??..
- Cn2 parameters and Gamma2 parameters 
- table of models (there are a lot so the reader need visual aid)

## Beta distribution model
- before we conduct validation, we..

## Results: Models Validation
### Weak channel
- Rytov parameter $\sigma_\mathrm{R}^2=0.2$ 
- Overview
    - channel length $z_\mathrm{ap}=1\text{ km}$
    - structure constant for the index of refraction $C_n^2=5\times10^{-15}$ (m$^{-2/3}$)
    - initial beam-spot radius at the transmitter, $W_0=2$~(cm)
    - wavelength $\lambda=2\pi/k=809$~(nm) 
    - outer scale $L_0=80$~(m)
    - inner scale $\ell_0=10^{-3}$~(m)
- "For $F_0=+\infty$, the Rayleigh length is $z_\mathrm{R}=kW_0^2/2\approx1.553~\mathrm{km}$, which is greater than the channel length $z_\mathrm{ap}{=}1~\mathrm{km}$."
- Simulation parameters:
    -  spatial grid with 512 points along one axis
    - spatial grid steps are 0.3 mm
    - The number of spectral rings is $N=1024$
    - "The inner and outer bounds of the spectrum are $K_\mathrm{min}=1/15 L_0$ and $K_\mathrm{max}=2/\ell_0$, respectively"
    - "The number of phase screens is chosen from the condition that the Rytov parameter for the interscreen distance does not exceed $0.1$ (cf.~Refs.~\cite{Schmidt_book,Martin1988}). It is equal to 10" 
        - the Rytov parameter for the interscreen distances in these cases are $3\times10^{-3}$ 
    - The number of samples $M=10^5$ for all channels

> [PDT: a<LT | a~LT | a>LT ]

qualitative

> [KS: a<LT | a~LT | a>LT ]

quantitative

- Comparison plots
- Quantitative metrics
- Discussion of discrepancies
### Moderate channel
- Overview
- Comparison plots
- Quantitative metrics
- Discussion of discrepancies
### Strong channel
- Overview
- Comparison plots
- Quantitative metrics
- Discussion of discrepancies

## Statistics of beam shape parameters
- gaussianity of x0

## Discussion
- num sim is the origin to be able to compare modes
- can models be extended or corrected? Speckles are important in bw models
- discuss previous assumption

## Conclusion

> uncertainty treatment: statistical convergence, noise, numerical errors.
