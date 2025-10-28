## Theory of turbulent atmosphere
Turbulence is widely recognized as one of the most complex and challenging phenomena in nature.
The complexity are rooted in the Navier-Stokes equations, which results in  the non-linear, multi-scale, and intrinsically chaotic behavior of the system, making precise prediction impossible over extended periods. 
Thus the atmospheric study mostly relies on statistical descriptions and the main object for sdescription is the wind velocity random field.

### Energy cascade model of turbulence {#sec:turb_cascade}
There are various sources that creates turbulence like wind shear, thermal convection, buoyancy effects, obstacles, but the statistical properties of the resulting flow tend to show similar universal behavior.

We assume that turbulent atmosphere is stationary, homogeneous, and isotropic. 
Stationarity implies that the statistical properties of the flow do not change over time. 
Homogeneity means that no particular location in the space is special. Isotropy requires that no direction is privileged. 
This assumption forms a workable starting point for studying the statistical properties of turbulence.

>"By making one further assumption of incompressible turbulence, that is, g. v = 0 (Batchelor [2.4]), we can write D, in terms of Dr,," ([“Laser Beam Propagation in the Atmosphere”, 1978, p. 23](zotero://select/library/items/6VHCHVKG)) ([pdf](zotero://open-pdf/library/items/4WBAA526?page=23&annotation=VDDGJIX8))
>"Clifford [-2.52] also showed that the depolarization effects of the atmosphere are negligible even when the wavelength 2 is greater than the inner scale Io" ([“Laser Beam Propagation in the Atmosphere”, 1978, p. 39](zotero://select/library/items/6VHCHVKG)) ([pdf](zotero://open-pdf/library/items/4WBAA526?page=39&annotation=BFRJZMRA))

Let's consider the structure function of the velocity field -- ensemble average over turbulent atmosphere realizations of the square of longitudinal velocity difference at two points in space. 
$$%\label{eq:kolmStructFunc}
D_v(r) = \left<|v(x) - v(x+r)|^2\right> \equiv  v_r^2$$
Since we assume homogeneous and isotropic turbulence, the statistics of fluctuations do not depend on the direction.
We can define two time scales: the "inertial" time $T_I \sim r/v_r$ at which the structure of velocity difference deforms, and the "viscous" time $T_\nu \sim r^2/\nu$ at which the structure of velocity difference is smoothed by viscosity ^[@jimenez2004].
Here $\nu$ is the kinematic viscosity (momentum diffusivity).
The ratio of these two time scales defines the Reynolds number $\mathcal R_r=T_\nu/T_I = v_r r/\nu$.
When $\mathcal R_r \gg 1$ the viscous time is much longer than inertial time, so the structure of velocity difference deforms into other (smaller) structures before its energy dissipates by viscosity.  
For $\mathcal R_r < 1$ the structure dissipates their energy rapidly due to viscosity.

It's widely used in the literature to associate these structures with turbulent eddies of diameter $r$ and linear velocity difference $v_r$. Then, inertial time corresponds to the time it takes for an eddy to complete one rotation. Although turbulent eddies are not well defined, they can be valuable for illustrating the intuition about turbulence dynamics.

We can define two characteristic lengths that play important role in turbulent atmosphere theory.
The outer scale of turbulence $L_0$ can be considered as the typical size of the largest eddies or characteristic size of the system, like the altitude of laser beam propagation ^[@??], with typical values of $L_0 \approx 80\mathrm{m} - 1\mathrm{km}$.
The inner scale or turbulence $l_0$ can be considered as the scale at which $\mathcal R_{l_0} \approx 1$, with typical value of $l_0 \approx 1\mathrm{mm} - 1\mathrm{cm}$. 
The interval of scales between $l_0$ and $L_0$ is called as the inertial range.

#### Structure function of the velocity field
In the 1940s Kolmogorov assumed that energy enters the turbulent system at large scales $L_0$, cascades through inertial range scales without energy loss, and finally dissipates at the $l_0$ scale due to the viscosity.  
This is so called energy cascade model of turbulence.
In this case the energy flux from a scale to another by unit mass defined as the kinetic energy divided by deformation time must be a constant:
$$\varepsilon \sim \frac{v_r^2}{T_I}=\frac{v_r^3}{r}=\mathrm{const}$$
The dimensional analysis implies that the structure function ^[eq:kolmStructFunc] must be proportional to
$$D_v(r)\sim\left(\varepsilon\, r\right)^{2/3}\equiv C_v^2 r^{2/3}\,,\quad l_0\ll r\ll L_0$$
where $C_v^2$ is the velocity structure constant (units of $\mathrm m^{4/3}\mathrm s^{-2}$). 

#### Structure function of the index of refraction
As can be seen from ^[eq:parax], the refractive index $n$ is the single parameter of the medium that affects light propagation. 
It, in turn, depends on temperature, pressure, humidity, and other atmospheric variables.
The dominant contribution arises from temperature fluctuations, since temperature relaxes much more slowly than the other parameters.
In the inertial range of turbulence, the advective transport strongly dominates over diffusion, so temperature behaves as a passive scalar transported by the turbulent velocity field. 
Consequently, the structure functions of the refractive index, temperature, and velocity fields exhibit the same scaling behavior $D_n(r) \sim D_T(r) \sim D_v(r)$, and therefore
$$D_n(r) = C_n^2 r^{2/3}\,,\quad l_0\ll r\ll L_0$$
where $C_n^2$ is the refractive-index structure constant -- the parameter the primarily determines the turbulence strength.

It is also very common to define the Kolmogorov turbulence model with the power spectral density function, which can be obtained using ^[eq:DtoPhi] as
$$\Phi(k)=0.033 C_n^2 \kappa^{-11/3}\,\quad 2\pi/L_0 \ll \kappa \ll 2\pi/l_0$$
where $\kappa = 2\pi/l$ is the spatial frequency and $C_n^2$ is the refractive index structure constant. 
Near ground level, $C_n^2$ ranges from around $10^{-17}$ m$^{-2/3}$ (weak turbulence) to $10^{-13}$ m$^{-2/3}$ (strong turbulence).

The Kolmogorov power-law spectrum model, because of its simple expression, is mostly used in analytical calculations. 
However the $-11/3$ power introduce some challenges when used under integrals over $\kappa$.
Other problem with this model arises when we take look at the low spectrum region. 
We can see that this model yields infinite value of power density as $L_0 \to \infty$ which is sometimes used to simplify calculation.  
Such unphysical condition can be fixed by  introducing models that behaves the same in the internal region but smoothly fall-off in the energy and viscosity ranges.
One of such models is modified von Karman model which introduce decay of power spectral density at the $l_0$ and $L_0$ values
$$\boxed{\Phi_n(\kappa) = 0.033 C_n^2 \frac{\exp(-\kappa^2/\kappa_m^2)}{(\kappa^2 + \kappa_0^2)^{11/6}}}$$
where $\kappa_0 = 2\pi/L_0$ and $\kappa_m = 5.92/l_0$ represent the outer and inner scale cutoffs, respectively.

It is worth emphasizing that when this turbulence theory was first proposed, it consisted entirely of theoretical predictions.
Its experimental confirmation came nearly a decade later and showed the first clear validation of the theory.
After some time, more sophisticated numerical and analytical approaches based directly on the Navier–Stokes equations were conducted
These studies validated the $-5/3$ power-law dependence of the energy spectrum in the inertial subrange. 
However, they also revealed additional fine structures, such as a small bump in the high-frequency (viscous) range of the spectrum. 
But overall, while the refined models introduced deeper physical insights, they largely supported the fundamental scaling laws established by Kolmogorov and the modified von Karman spectrum.

>- "the amount of supporting experimental evidence is amazing ( M y r u p [2.9] and K a i m a l et al. [2.10])," ([“Laser Beam Propagation in the Atmosphere”, 1978, p. 24](zotero://select/library/items/6VHCHVKG)) ([pdf](zotero://open-pdf/library/items/4WBAA526?page=24&annotation=UBIAQ3SV))

>When choosing MVK in [[2_5_ps]] say why not Andrews spectrum: 
>"While these advanced spectral models reflect the intimate details of atmospheric turbulence, the author believes that the details of the turbulence spectrum behavior at the highfrequency (inner scale) cutoff and low-frequency (outer scale) domain are irrelevant for the majority of the optical propagation problems. This is evident in the substantial uncertainty in the definitions of the inner and outer scales found in the literature, and in the somewhat loose relations between these scales and the spectral parameters κm and κ0 f"
> by Charnotski 10.1364/JOSAA.30.002455
>This question can be one of the further problems to study, after maturity of the current level of study of atmospheric quantum channels.

![\label{fig:psd_scales}The model of turbulent atmosphere and its power spectral density for Kolmogorov model blue and Modified von Karmal model green](file:///home/klen/syncthing/desktop/physics/phd/thesis/src/generated/psd_scales.svg)

The Figure ^[fig:psd_scales] summarizes the model of atmospheric turbulence. 
It depicts the energy flow through scales starting from large scales of energy injection, going through inertial range where the turbulent motion is predominant process and to the region of energy dissipation by viscosity.

>[!danger] Add 
>- [ ] Add paragraph that turb atm can be assumed as Gaussian process. We rely on this in PS section.

>Sources: [pdf](https://oa.upm.es/88590/1/5480314.pdf) eddy concept try. Here v to n [source](https://subarutelescope.org/staff/guyon/15teaching.web/05AstrOptics2016.web/wdir.web/AstrOpt2016_11atmosphericturbulence.pdf)
>- [ ] we need some words about what is gaussian turbulence - why we use complex normal distr for phase screens generation

### Frozen turbulence hypothesis
The Kolmogorov model, along with its modifications like the Von Karman spectrum, provides a strong theoretical basis for understanding the ensemble averaged statistics of turbulence. 
However, these models do not directly address the temporal statistics of the turbulent field. 
This lack of a temporal description is critical for several reasons. 
It is required for studying the temporal properties of the impact of the turbulent atmosphere on phenomena like light propagation. 
For experimental atmosphere study, most atmospheric experiments rely on small number of fixed in space sensors to record fluctuations over time because this setup is significantly easier to realize in practice than true spatial sampling. 
The answer to the question how to compare the temporal data with the spatial statistics provided by G. I. Taylor in 1937 with the Frozen Turbulence Hypothesis.

The hypothesis is based on the difference between two atmospheric time scales. 
The first is the advection time, which can be defined as the duration required for the mean wind of speed $v$ to carry turbulent structure of size $r$ across the observation point, so $T_v = r/v$.
The second is the mentioned above the inertial time $T_I \sim r/v_r$ ^[sec:turb_cascade]. 
Typical values for mean wind speed is  $v \sim 5-20\,\mathrm{m/s}$ in moderate to strong wind condition and $v_r \sim 0.1-2\,\mathrm{m/s}$ for the root mean squared velocity fluctuation.
Then in the case when the advection time is much smaller than inertial time $T_v/T_I = v_r/v \ll 1$  we can assume that the index of refraction field is effectively frozen and evolve in time by moving with constant wind speed $\mathbf{v}: |\mathbf{v}|=v$ as a whole:
$$n(\mathbf{r},\,t)=n(\mathbf{r}-\mathbf{v}\,t,\,0)$$
The intuition behind this can be supported by looking at clouds, which seem to keep their shape for a long time while drifting steadily with the wind.
This phenomenon is known as the Taylor frozen turbulence hypothesis.

The Taylor frozen turbulence hypothesis is subject to several restrictions. 
As in the general Kolmogorov model of turbulence, it assumes that the turbulence is roughly homogeneous and isotropic.
A key requirement of the hypothesis is that the advection time is much smaller than the inertial (or evolution) time of the turbulent structures, so that changes in the turbulence during transport are negligible. 
The hypothesis also assumes a constant wind speed in both magnitude and direction; near obstacles, the ground, or in the presence of gusts, deviations from this assumption may occur. 
Despite these limitations, the frozen turbulence approximation is widely used in practice and provides a useful framework for modeling time-dependent turbulent fields.

> link to adaptive optics as a proof of use

>In general, this makes some limits on the observation times, however, for a small region of interest -- such as an optical aperture -- it can often be applied over sufficiently long timescales. 

>## Turbulence strength $C_n^2$ parameter estimation
