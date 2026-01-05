# Conclusions {.unnumbered}

- [[0_1_introduction]]
- q communication
- pdt (gap)
-  identify governing parameters, test model assumptions, and resolve temporal structure

...
- the range of validity of these models has remained unclear.
    - Some of the models were validated with experimental data by fitting, but no compete understanding which model in which regime work better.

> Synthesis of findings:
- numsim
- we show that mirroring the known assumptions about the light field before aperture to the trasmittance isn't good way
    - while beam wandering is the most pronounce effect in the weak turbulence regime, it doesn't imply that PDT models based on the beam wandering effect good in this regime.
    - from other side the good fit of the truncated lognormal distribution on the channel of strong turbulence doesn't make it good for all strong turbulence channels.
    - ... lognorm mirroring?
- what matters  most is the aperture size, compare to the average beam size.
    - *Aperture enters the scene as a primary parameter that affects the PDT shape*.
    - (HERE)
    - *transmittance naturally bounded on 0,1*
    - When first two moments of transmittance is specified, the main task of such models is to correctly predict the higher moments of transmittance.
        - ~~When aperture is smaller than average beam size the trasmittance values are located close to the left side of the $[0,1]$ interval and the distribution has positive skew. ~~
        - In this case, the models which have mainly 
        - beta
    - moment matching
        - CB [look below]
- As the result - applicability
- We also validated model assumptions for further dev of model.
- Time
- Application





- ~~The PDT models are typically defined using specific combinations of first two moments of transmittance and beam shape.~~




- intro
    - qunatum network, long distance, satellites
    - existing toolset of models of PDT - applicability unclear
    - describes ensamble, don't account for correlations between consequnce pulses
    - A comprehensive numerical framework was required to resolve the applicability of these models and to characterize the temporal correlations
- Synthesis of Findings (simultaniosly) main claim (large): 
    - > statistical properties of transmittance are governed more by receiver aperture geometry and low-order transmittance moments than by the specific phenomenological form of beam-shape distributions
    - Validation of existing PDT models revealed that the empirical Beta distribution generally provides the superior fit to numerical data
    - Physically motivated models, such as the beam-wandering and elliptical-beam models, were found to exhibit biased transmittance moments
        - This study demonstrated that analytical models must be parameterized by transmittance moments rather than beam-shape statistics to maintain predictive accuracy
        - This model incorporates beam-size variability through a log-normal distribution while enforcing consistency with the first two transmittance moments
        - By absorbing higher-order deformations and scintillation into effective beam-size fluctuations, the model provides a tractable and accurate description of the PDT suitable for practical quantum communication tasks.
    - validated several beam shape statistic assumptions used in analy models
    - the spatial coherence radius, which determines the timescale over which successive pulses remain correlated
        - scales almost linerrly with aperture?
    - applications
- how your work moves the field forward.
- Limitations and Future Research
- sense of completion and significance
