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
- we will consider two types of source beam collimated -- F = infty -- and focused -- F = z_ap.
    - this will have significant differece in some aspects.
- note logarithmic scale. we recall the the same visual distance between for example 10-3 to 10-2 and 10-2 to 10-1 corresponds to 10 times different actual distance.
#### Collimated beam


![\label{fig:ks_weak_inf}Weak zap](images/validation/weak_inf_ks_values.svg)
- bw and ellipt "the worst agreement" despite physical based nature
    - elliptic beam minima, of fig 2
- truncated lognormal has descend coinsidence for small apertures, but getting worse for larger apertures, when the sign of skewness (assymentry) of numerical pdt  .. while lognormal pdt has positive for all aperture parameters
- total probability models almost the same as their counterparts for this channel
- The beta model shows best agreement. It has minima at around $\langle\eta\rangle=0.5$ , where the numerical pdt has symmetrical shape.
- the example of modesl for aperture = x which coresponds to the minima of elliptical beam model is shown in the fig 2.

![\label{fig:pdt_weak_inf}Weak inf](images/validation/weak_inf_pdt_0_03.svg)

- We see that this minimum correponds to the case when the mode of the elliptical beam model distribution mathes the numerical PDT.
    - not the case for other apertures
- the BW assumes fixed shape of the beam, so the transmittance can't be bigger then the trasmittance of the coaxial circular beam of coresponding width.
- for weak turbulence we generally have small variance of transmittance, so the PDT looks similar to gaussian shape especially if 0 << avg eta << 1

#### Focused beam


![\label{fig:ks_weak_zap}Weak zap](images/validation/weak_zap_ks_values.svg)

- in general poorer .. than collimated 
    - We want to emphisise that this shoudn't be confused and considered that focused beam is worse.
    - Focused beam is typically characterized by smaller beam spot size at the aperture plane, which results in better average transmittance for the same aperture radius those in general in better efficiency of protocols.
    - The figure shows poorer performance of analytical models compared to numerical simulation results.
- for focused beam the total probability models shows best performance.
- However for $R_\text{ap} \gtrsim W_\text{LT}$  the models don't work.
    - In this domain the beta model still produce best performance.

![\label{fig:pdt_weak_zap}Weak zap](images/validation/weak_zap_pdt_0_015.svg)

- mismatch skewness of lognormal; also the visible that truncated tail of lognormal distribution is big, having unphysical finite probability at $\eta=1$
- elliptic beam model have biased mean transmittance 
- beta model despite being parameterized with first two moments of transmittance, shows underestimate of absolute values of skewness and kurtosis in this range.
- But the beta model combined with the beam wandering model -- total probability model -- shows perfect match with the numerical PDT.  
### Moderate channel

- "is 1.6 km. Such a channel has been implemented in Erlangen, Germany"
#### moderate_inf
- beta model is better for small apertures
- However, for small apertures beta total probability model performs even worse than than simple beta model.
- As can be seen on fig X, beta model perfectly match the shape
    - But lognormal, despite being defined with first two moments of trasmittance, have biased variance -- the model is much narrower than numerical PDT.
    - This can explained by the fact, that parameters of the truncated lognormal model actually defines the first two moment of the full lognormal pdf and after truncation the moments are different.
- The figure X demonstrates PDT when aperture ~ W_LT - total probability is superior.
    - We also can see that at this point the beam wander model mode match the numeriical PDT mode, which results in minima of KS statistic of this mode'l.

![\label{fig:pdt_moderate_inf}Moderate inf](images/validation/moderate_inf_ks_values.svg)



![\label{fig:ks_moderate_inf}Moderate inf](images/validation/moderate_inf_pdt_0_05.svg)

#### moderate_zap

![\label{fig:pdt_moderate_zap}Moderate zap](images/validation/moderate_zap_ks_values.svg)

- like in weak channel, general performance is worse than moderate_inf
- generally beta mode is better
- total prob models 'shines' at <~1 until they work
- When the modes of beam wandering and elliptic beam modes match numerical PDT at ~1 they shows best performance. 
- in the fig X we can see the reason of generally wors performance

![\label{fig:ks_moderate_zap}Moderate zap](images/validation/moderate_zap_pdt_0_012.svg)

- The numerical PDT has highly non-gaussian shape with almost constant probability density on some interval. 
- And any models can not capture this feature.

### Strong channel

![\label{fig:pdt_moderate_inf}Moderate inf](images/validation/strong_inf_ks_values.svg)

- interestingly  33 rytov channel ~~ moderate zap of sigma_rytov2 = 5 channel.
- only at very small apertures ~0.1 R_ap the lognormal model performs better, what can be seen of fig X

![\label{fig:ks_strong_inf}Strong inf](images/validation/strong_inf_pdt_0_1.svg)

- For the trasmittance moment in this region changes its shape to the $(1-\eta)^{\beta-1}$ - like shape when the shape of the numerical PDT still resembles the lognormal shape.

## Statistics of beam shape parameters
- gaussianity of x0

## Discussion
- num sim is the origin to be able to compare modes
- can models be extended or corrected? Speckles are important in bw models
- discuss previous assumption

## Conclusion

> uncertainty treatment: statistical convergence, noise, numerical errors.
