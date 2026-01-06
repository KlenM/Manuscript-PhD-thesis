# Conclusions {.unnumbered}

 [[0_1_introduction]]

> - intro (Reiterate the "Why" and "What."	Confident & Direct) 
>     - why this study was necessary [1p]
>     - main claim or findings [2p]
> - intro
>     - qunatum network, long distance, satellites
>     - existing toolset of models of PDT - applicability unclear
>     - describes ensamble, don't account for correlations between consequnce pulses
>     - A comprehensive numerical framework was required to resolve the applicability of these models and to characterize the temporal correlations

## q communication
## pdt (gap)
- the range of validity of these models has remained unclear.
    - Some of the models were validated with experimental data by fitting, but no compete understanding which model in which regime work better.
- identify governing parameters, test model assumptions, and resolve temporal structure

## Synthesis of findings:
### numsim

### valid

We show that transferring assumptions about the light field before aperture directly to the transmittance value distribution is not valid.
Beam wandering is the most pronounced effect in weak turbulence, but this does not imply that beam wandering based PDT models are accurate in this regime.
A good fit of the truncated lognormal distribution in strong turbulence does not justify its universal use across strong turbulence scenarios.
The same limitation applies to approaches that infer transmittance statistics from light field distributions in a point.
Realistic measurements always involve a finite size aperture in contrast to the theoretical descriptions of the light field are typically defined at an infinitesimal point.

We demonstrate that the ratio between the aperture size and the average beam size is the primary parameter shaping the PDT.
Transmittance is bounded on the interval $[0,1]$, which enforces asymmetry that depends on its mean value.
For apertures smaller than the mean beam waist, transmittance values concentrate near the lower bound.
The resulting statistical dispersion produces a strongly positively skewed distribution.
When the average transmittance approaches unity, the distribution becomes negatively skewed.

When the first two moments of transmittance are specified, the central task of a PDT model is to predict higher order moments correctly.
Not all models have sufficient flexibility to account for aperture induced shape changes.
For example, the lognormal distribution is always positively skewed and therefore performs well only for small apertures.
We propose a new empirical model based on the Beta distribution.
It reproduces skewness near both bounds and generally outperforms existing models.
Its analytical simplicity makes it suitable for practical use.

Physically grounded models are typically formulated in terms of beam shape statistics such as beam wandering and beam spreading.
This means that accurately predicting the mean transmittance and variance, in addition to higher moments, falls within their scope of tasks.
In practice, these models often fail to do so.
They often reproduce the qualitative shape of numerically simulated PDTs but exhibit systematic shifts.
To overcome this misspecification bias we proposed a transmittance matching procedure.
Based on this procedure, we construct a new physically grounded model with fewer parameters than the elliptical beam model, while producing unbiased estimates of the first two transmittance moments and outperforming it overall.

> validated model assumptions for further dev of model.

To guide further development of physically grounded models, we validated the key assumptions underlying their construction.
We demonstrated that the beam centroid displacement follows Gaussian statistics across all turbulence regimes.
In contrast, the commonly assumed bivariate Gaussian distribution of beam semi-axis sizes fails systematically.
The joint distribution exhibits strong suppression along the diagonal, which cannot be captured by a Gaussian model.
Further investigation of this effect may benefit from connections to random matrix theory, which could provide a theoretical explanation for the observed structure.

Existing models further assume statistical independence between the beam centroid position and the instantaneous beam size.
We show that this assumption is violated.
The induced correlations are small in the weak to moderate turbulence regime but become significant under strong turbulence.
Neglecting these correlations leads to an underestimation of the PDT spread in this regime.

### Time
- The PDT models are capable to describe only single pulse propagataion or the case of very large time separation between pulse.
    - The practical scenaria involves high repetitve pulse propagation
    - so the quantum state imposed high correlation transmittance.
- In this work, utilizing the Taylors frozen-turbulence hypothesis, we introduced the two-time PDT, which  enables complete description of two consequtive correlated pulses.
- to characterize atmospherical quantum channels correlation property we  introduced the aperture-averaged spatial coherence radius $\rho_0$, which is defined as the time interval between pulses, when the Pearson correlation of transmittances falls to $e^{-1}$.
    - It serves as the measure for the persistence of temporal correlations.
- As in the case of single-time PDT, the aperture plays primary role.
    - We show, that aperture-averaged spatial coherence radius increases almost linearly with the aperture radius, with some small nonlinear deviation.
- The transition from ensemble-based statistics to two-point correlations represents the theoretical advancement of this work.
 
### Application
- The introduced framework of two-time PDT enables the analysis of variaty of qunatum protocols in turbulent atmosphere.
- 

## how your work moves the field forward.
>  - Prove the "So What?" (Argumentative) [1p]
> - understanding: aperture, ...; "practical": ...
> - Theoretical, Methodological, or Practical
> - iideas
>     - there is a sad tendency (but probably down?) to use only avarage value of transmittance for QKD protocols
## Limitations and Future Research

> - Show self-awareness. (Reflective & Objective) [1p]
> - (horizontal, gauss beam - higher order, circular aperture, constant cn2, kolmogorov model, frozen turbulence hypothesis, stationar)
> - many-time pdt, analytical model of moments, qkd

## sense of completion and significance
> - The Global Perspective: matters in the "real world"
> - enduring value - Avoid ending on a limitation
