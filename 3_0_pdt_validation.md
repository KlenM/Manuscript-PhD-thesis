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

## Results and discussion
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
- Despite the physically motivated nature of the beam wandering and elliptical beam models they show the worst agreement with the numerical PDT.
    - elliptic beam minima, of fig 2
- The truncated lognormal model reproduces the numerical PDT fairly well for small apertures, but its accuracy degrades for larger apertures. 
- The reason is the change of skewness in the numerical PDT—from positive to negative—as the aperture increases, while the truncated lognormal distribution remains positively skewed for any parameters.
- The total probability models show performance nearly identical to their base distributions. 
    - ?since beam wander effects are weak?.
- The beta distribution provides the best overall agreement, with its KS statistic reaching a minimum around $\langle\eta\rangle=0.5$, where the numerical PDT is nearly symmetric.

![\label{fig:pdt_weak_inf}Weak inf](images/validation/weak_inf_pdt_0_03.svg)

- At the aperture corresponding to the elliptical beam model’s KS minimum, the mode of the distribution coincides with the mode of the numerical PDT, which can be seen in the fig X. 
    - At other aperture sizes this model has biased mode and transmittance modes.
- the BW assumes fixed shape of the beam, so the transmittance can't be bigger then the trasmittance of the coaxial circular beam of coresponding width.
    - this is reflected in the distinct shape of the beam wandering model, which can't catch the right tail of the numerical distribution.
- Overall, for weak turbulence the transmittance fluctuations are small, and the PDT tends to a quasi-Gaussian shape whenever $0 \ll \langle\eta\rangle \ll 1$.

#### Focused beam


![\label{fig:ks_weak_zap}Weak zap](images/validation/weak_zap_ks_values.svg)

For the focused beam, all analytical models show poorer agreement with numerical PDTs than in the collimated case. 
This should not be misinterpreted as a degradation of channel performance. 
A focused beam typically produces a smaller spot at the aperture plane and thus achieves a higher average transmittance for the same aperture radius, improving overall link efficiency. 
The lower KS scores here simply indicate that existing analytical PDT models fail to capture the more complex field statistics in this focusing regime.

Among all models, the total probability models demonstrate the best performance, especially for small to moderate aperture sizes.

- However, when the aperture radius $R_\text{ap} \gtrsim W_\text{LT}$  the total probility models can't be defined.
    - In this domain the beta model produce best performance.

![\label{fig:pdt_weak_zap}Weak zap](images/validation/weak_zap_pdt_0_015.svg)

- The truncated lognormal model shows mismatched skewness and a physically unrealistic finite probability density at $\eta \to 1$ due to truncation.
- elliptic beam model have biased mean transmittance 
- The beta model, while based on matching the first two moments, underestimates higher-order moments (skewness and kurtosis).
    - When combined with the beam wandering statistics in the total probability model, however, the resulting PDT matches the numerical distribution almost perfectly in both shape and position.
### Moderate channel

- "is 1.6 km. Such a channel has been implemented in Erlangen, Germany"
#### Collimated Beam
- For small apertures, the beta model provides the best fit to the numerical PDT.
    - However, for small apertures beta total probability model performs even worse than than simple beta model.
- As shown in Fig. X, the beta model reproduces the overall shape and width of the numerical PDT accurately.
    - In contrast, the truncated lognormal model—although defined via the first two moments—produces a narrower distribution and underestimates the variance.
    - This bias originates from the fact that truncation changes the actual moments of the distribution; the fitted parameters correspond to the full (untruncated) lognormal rather than the truncated one.
- At apertures $R_\text{ap}\approx W_\text{LT}$, the total probability models outperform all others. 
    - Here, also, the modes of the beam wandering  and elliptical beam models coincide with the mode of the numerical PDT, resulting in the KS minima for these models.

![\label{fig:pdt_moderate_inf}Moderate inf](images/validation/moderate_inf_ks_values.svg)



![\label{fig:ks_moderate_inf}Moderate inf](images/validation/moderate_inf_pdt_0_05.svg)

#### Focused Beam

![\label{fig:pdt_moderate_zap}Moderate zap](images/validation/moderate_zap_ks_values.svg)

- As in the weak channel, the focused beam results in generally worse agreement between analytical and numerical models than the collimated beam.
- The beta model again performs best, outperformed a bit by the total probability models when the aperture is around $R_\text{ap}\approx W_\text{LT}$.
- When the modes of beam wandering and elliptic beam modes match numerical PDT at ~1 they shows best performance. 
- in the fig X we can see the reason of generally worse performance

![\label{fig:ks_moderate_zap}Moderate zap](images/validation/moderate_zap_pdt_0_012.svg)

- The numerical PDT in this regime develops a highly non-Gaussian plateau, with nearly constant probability density over a finite interval of η.
- This feature cannot be reproduced by any of the studied parametric models, all of which assume unimodal, smoothly decaying distributions.

### Strong channel

![\label{fig:pdt_moderate_inf}Moderate inf](images/validation/strong_inf_ks_values.svg)

- Interestingly, the behavior of the 33 Rytov channel resembles that of the moderate focused channel with sigma_rytov2 = 5.
- The only difference is that for very small apertures $R_\text{ap} \lesssim 0.1W_\text{LT}$ the truncated lognormal model shows slightly better performance (see Fig. X).

![\label{fig:ks_strong_inf}Strong inf](images/validation/strong_inf_pdt_0_1.svg)

- In this range, the beta model changes its shape to the $(1-\eta)^{\beta-1}$ - like shape when the shape of the numerical PDT still resembles the lognormal shape.
### Conclusion
For both weak turbulence channels and the moderate-turbulence collimated beam channel, the numerically obtained probability density of transmittance (PDT) exhibits a bell-like, unimodal, and relatively narrow distribution, with noticeable asymmetry near the boundaries of its support, $\eta \in [0,1]$.
For the moderate-turbulence focused beam and strong turbulence channels, a similar overall tendency is observed, though the distributions become broader and tend toward a flattened shape, indicating an increased spread of transmittance values caused by the more complex spatial structure of the beam.

The first important observation is that the two physically motivated models—the beam wandering model and the elliptical beam model—being defined in terms of beam shape statistics, exhibit biased transmittance moments.
In some cases, these models reproduce the overall shape of the numerical PDT quite well (see Fig. ^[fig:pdt_weak_zap]), although their peaks are shifted relative to the numerical result.
The best agreement in terms of the KS-statistic is obtained when the peaks of the analytical and numerical PDTs coincide, as illustrated in ^[fig:ks_moderate_inf].
Thus, because of the inability to fully account for all orders of the beam shape decomposition, it is more appropriate to parameterize analytical models in terms of transmittance moments rather than beam shape statistics.

The second important observation concerns the dominant role of the aperture size in determining the applicability of different PDT models.
The KS-statistics results show that the models’ relative performance is similar across different turbulence strengths. 
In contrast, variations in the aperture radius cause significant changes in the KS-statistic, indicating a strong dependence of model accuracy on the aperture parameter.

Physically, increasing the turbulence strength primarily leads to a broader PDT (i.e., increased variance), which is captured reasonably well by all the analytical models.
However, changing the aperture size mainly affects the skewness of the numerical PDT, and many analytical models fail to reproduce this asymmetry accurately.
In particular, the lognormal model always yields positively skewed distributions, whereas the beam wandering model consistently produces negatively skewed ones.
The elliptical beam model generally yields negative skewness, with only a minor positive skew for small apertures, which remains insufficient to reproduce the numerical PDT.
Among the considered models, the total probability models and the Beta model most successfully reproduce the skewness of the numerical PDT.

- overall (indicate this is overall of entire section, not last paragraph)
    - the empirical beta model generally shows best KS statistics performance due to its' naturally bounded on $[0,1]$ support, and skewness behavior at edges. 
    - lognorm - shows descent performance, but worse than beta model. Only for small apertures and strong turbulence when the the numerical PDT is wide and higly skewed so the estimated beta parameters reflects the unphysical L-shaped form of PDT, the lognormal model outperforms. 
    - while total probability model combines the positive skewed lognormal and negative skewed beam wandering model, for small apertures it performance is of order of based lognormal model. However, when the aperture becames of order of the average beam spot width  $R_\text{ap} \lesssim W_\text{LT}$,  it capable to capture the high kurtosis of the numerical PDT, allows it to outperform all other models in some narrow region.
    - the physical grounded beam wandering model and elliptical beam model strongly suffer from from biased first transmittance moment estimation (average transmittance and variance). This is the reason why it performs well when the parameters are fitted using the method of least squares^[@expfit], but bad when the beam shape parameters are estimated with the numerical simulation.
- conclusion

3d observation about tot prob:
> near 1 PDT is more heavy tailor (than beta and other (ellipt?)

overall:
> - generally beta, totprob for big aperture, bw and elliptic if moment matched, 

To be able to capture the primary feature of the probability distribution of transmittance function, analytical models must have negative skewness when the aperture is much smaller than the average beam width and positive skewness when the aperture is of order or bigger than the average beam width.
The truncated lognormal model always have positive skewness which 
    - when ap ~ WLT the 

- moments bias; skewness (3d moment models?); curtosis for moderate-strong when aperture is 0.5; totprob for focused (why??); beta good; 
- due to the bounded nature of the transmittance $\eta \in [0,1]$ the PDT inherently have highly positive skewnes when the aperture is small and highly negative skewness when the aperture is large compared to the average beam size.
    - The strictly positive skew of lognormal distribution limits their region of applicability to sma
    - However, any of the existing before analytical models be able to change the sign of the skewness 
- the KS statistics of models behaves similalrly independent on the turbulence strength in general, but highly depends on the aperture radius.
    - highlight the importance of aperture dependence for atmos quant channel
- 
    - 
## Statistics of beam shape parameters
- gaussianity of x0

## Discussion
- num sim is the origin to be able to compare modes
- can models be extended or corrected? Speckles are important in bw models
- discuss previous assumption

## Conclusion

> uncertainty treatment: statistical convergence, noise, numerical errors.
