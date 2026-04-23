### Light beam propagation in inhomogeneous media {#sec:light_in_turb}
To obtain the transmittance of the atmospheric quantum channel, we must solve the classical problem of light propagation through stochastic isotropic media.
This process involves characterizing how random fluctuations in the medium alter the beam's power distribution.
To that end, this section defines the fundamental equations governing the evolution of the complex field amplitude and the resulting intensity at the aperture plane.

#### Paraxial wave equation in stochastic media.
> To describe the propagation of gaussian beams through turbulent atmosphere we begin from the general wave equation derived from Maxwell's equations.

>- scalar wave, polarization or only one of 6 components.
>- "smoothly varying stochastic refractive index" ([Andrews and Phillips, 2005, p. 137](zotero://select/library/items/IJGQ3J8A)) ([pdf](zotero://open-pdf/library/items/VGHZA9HX?page=161&annotation=XM7K93SD))
>- "set of fundamental assumptions on the propagating wave" ([Andrews and Phillips, 2005, p. 137](zotero://select/library/items/IJGQ3J8A)) ([pdf](zotero://open-pdf/library/items/VGHZA9HX?page=161&annotation=E4LAXLAC))
>- "J. W. Strohbehn, ed., Laser Beam Propagation in the Atmosphere (Springer, New York, 1978)" ([Andrews and Phillips, 2005, p. 177](zotero://select/library/items/IJGQ3J8A)) ([pdf](zotero://open-pdf/library/items/VGHZA9HX?page=201&annotation=WV4N9T75))
>- [ ] n is real

The propagation of electromagnetic fields in the atmosphere is described by the scalar wave equation^[@strohbehn1968,siegman1986].
Separating temporal and spatial variables yields the Helmholtz equation
$$\nabla^{2}E+k^{2}n^{2}(\mathbf{r},z)E=0,$$
where $\nabla^2$ is the Laplacian operator, $k$ is the vacuum wave number and $E$ is the complex spatial amplitude.
For Gaussian beams propagating along the z-axis over long distances, the paraxial approximation becomes valid^[@siegman1986].
We express the complex amplitude in terms of a slowly varying complex envelope as $E(\mathbf r;z)=u(\mathbf r; z) e^{ikz}$.
Under the paraxial approximation the envelope $u(\mathbf r; z)$ is a slowly varying function of $z$, satisfying the condition $\left| \frac{\partial ^{2}u}{\partial z^{2}} \right| \ll \left| k \frac{\partial u}{\partial z} \right|$.
We also assume that $\delta n(\mathbf r, z)^2 \approx 0$, where $\delta n(\mathbf{r},z) = n(\mathbf{r},z) - 1$ represents the refractive index perturbation.
By neglecting second-order terms in the refractive index perturbation $\delta n^2 \approx 0$, where $\delta n(\mathbf{r},z) = n(\mathbf{r},z) - 1$, the equation reduces to the paraxial scalar wave equation in a medium with spatially varying refractive index
$$
%\label{eq:parax}
\boxed{2ik\frac{\partial u(\mathbf{r};z)}{\partial z}+\Delta_\mathbf{r} u(\mathbf{r};z)+2k^2\delta n(\mathbf{r},z) u(\mathbf{r};z)=0},$$
where $\Delta_\mathbf{r}$ represents the transverse Laplacian operator.

#### Gaussian beam source.
In this work, we restrict the analysis to the Gaussian beam mode at the transmitter plane^[@siegman1986].
Gaussian modes provide an accurate approximation of the output of most laser sources used in free space optical communication.
Because of this, they are widely adopted in theoretical modeling and experimental studies of atmospheric optical channels.
The boundary condition at the transmitter plane $z=0$ is given by the Gaussian beam^[@andrews2005]
$$%\label{eq:gaussbeam}
\boxed{u(\mathbf{r};0)=\sqrt{\frac{2}{\pi W_0^2}}\exp\left[-\frac{\mathbf{r}^2}{W_0^2}-\frac{ik}{2F_0}\mathbf{r}^2\right]},$$
where $W_0$ is the beam waist radius and $F_0$ is the radius of curvature of the wavefront. For collimated beams, $F_0 \to \infty$, while for focused beams, $F_0$ takes finite values.

#### Vacuum propagation.
For the case $\delta n = 0$ (homogeneous medium), the solution becomes straightforward. 
The Fresnel diffraction integral^[@goodman2017] describes the field evolution
$$u(x,y,z)=\frac{e^{ikz}}{i\lambda z}\iint_{-\infty}^{\infty}u(x',y',0)e^{i\frac{k}{2z}[(x-x')^{2}+(y-y')^{2}]}dx'dy'.$$
This integral represents a convolution with the propagation kernel, based on the Huygens-Fresnel principle where each wavefront point acts as a source of secondary spherical wavelets.
In the spatial frequency domain, this convolution becomes multiplication with the transfer function $H(f_{x},f_{y},z)=e^{ikz}e^{-i\pi\lambda z(f_{x}^{2}+f_{y}^{2})}$, known as the angular spectrum method^[@goodman2017]. 
This formulation enables efficient numerical implementation using Fast Fourier Transform algorithms.

#### Transmittance of channel.
To simulate the PDT, we must first calculate the transmittance value at the aperture plane $z=z_\mathrm{ap}$ for various channel realizations.
This is achieved by integrating the squared magnitude of the optical field over the entire receiving aperture $\mathcal{A}$ as follows
$$%\label{eq:eta}
\boxed{\eta = \int_\mathcal{A} d^2\mathbf{r} |u(\mathbf{r}; z_\mathrm{ap})|^2}.$$
Specifically, the integration domain $\mathcal{A}$ represents the circular region of the pupil with radius $R_\mathrm{ap}$, and $d^2\mathbf{r}=dxdy$.

#### Statistical properties of a light beam in turbulence.
In the absence of refractive index fluctuations, a Gaussian beam (see ^[eq:gaussbeam]) propagating in free space keeps its deterministic Gaussian profile at the aperture plane, as it represents the exact solution of the paraxial wave equation^[@siegman1986].
When the beam travels through a turbulent atmosphere, random changes in the refractive index make the optical field at the aperture plane a stochastic quantity.
To efficiently compress the vast amount of information required to describe the optical field distorted by turbulence, it is convenient to characterize the random fluctuations of the complex amplitude in terms of its second- and fourth-order correlation functions^[@andrews2005]
$$
\begin{split}
\Gamma_2(\mathbf{r};z) &= \left< |u(\mathbf{r};z_\mathrm{ap})|^2 \right>,\\
\Gamma_4(\mathbf{r}_1,\mathbf{r}_2;z_\mathrm{ap}) &= \left< |u(\mathbf{r}_1;z_\mathrm{ap})|^2 |u(\mathbf{r}_2;z_\mathrm{ap})|^2 \right>,
\end{split}
$$
where $\langle \cdot \rangle$ denotes ensemble averaging over turbulence realizations.

These correlation functions enable the calculation of several statistical quantities that are essential for parametrizing analytical models of atmospheric channels.
The average transmittance of the atmospheric channel, according to ^[eq:eta], is given by
$$\langle\eta\rangle  =
\left<\int_{\mathcal{A}} d^2\boldsymbol{r} |u(\boldsymbol{r}, z_\mathrm{ap})|^2\right>=
\int_{\mathcal{A}} d^2\boldsymbol{r} \, \Gamma_2(\boldsymbol{r}, z_{\mathrm{ap}})$$
and can be seen as the primary characteristic of channel effectiveness.
The second moment of the transmittance
$$\begin{split}
\langle\eta^2\rangle =
\left<\int_{\mathcal{A}} d^2\boldsymbol{r}_1 |u(\boldsymbol{r}_1, z_\mathrm{ap})|^2\int_{\mathcal{A}} d^2\boldsymbol{r}_2 |u(\boldsymbol{r}_2, z_\mathrm{ap})|^2\right> = \\ =
\int_{\mathcal{A}}\int_{\mathcal{A}}  d^2\boldsymbol{r}_1  d^2\boldsymbol{r}_2 \, \Gamma_4(\boldsymbol{r}_1, \boldsymbol{r}_2, z_\mathrm{ap})
\end{split}$$
requires the fourth-order correlation function and characterizes the variability of the atmospheric channel transmittance.

Let us consider the statistical properties of the beam-spot at the aperture plane^[@andrews2005].
The simplest property is the beam centroid, which is defined for a single realization of turbulent atmosphere as
$$
%\label{eq:x0}
x_0 = \int_{\mathbb{R}^2} d^2\boldsymbol{r} \, x\, |u(\boldsymbol{r}, z_\mathrm{ap})|^2.$$
While it is obvious that under the assumption of isotropic turbulence (see ^[sec:turb_cascade]) the average value of the beam centroid $\left<x_0\right>=0$, it remains an open question whether its distribution is Gaussian.
In particular, for strong turbulence the distribution can deviate, for example by exhibiting heavy tails.
The second moment is referred to as the long-term beam-spot radius. It is defined as
$$
%\label{eq:WLT2}
W_\mathrm{LT}^2 = 4\int_{\mathbb{R}^2} d^2\boldsymbol{r} \, x^2\, \Gamma_2(\boldsymbol{r}, z_{\mathrm{ap}})$$
and represents the effective spatial extent of the beam after propagation through turbulence, incorporating both diffraction and spreading due to turbulence effects.
The variance of the beam-centroid coordinate, often referred to as beam wandering, characterizes the random displacement of the beam centroid
$$
%\label{eq:SBW2}
\sigma_\mathrm{BW}^2=\left<x_0^2\right>=
\int_{\mathbb{R}^4} d^2\boldsymbol{r}_1  d^2\boldsymbol{r}_2 \, x_1 x_2 \,\Gamma_4(\boldsymbol{r}_1, \boldsymbol{r}_2, z_\mathrm{ap}).
$$
Complementary to these two quantities is the squared beam-spot radius, which is also referred to as the short-term beam-spot radius, defined as
$$
%\label{eq:Sshort_term}
S=
4\int_{\mathbb{R}^2} d^2\boldsymbol{r} \, (x - x_0)^2\, \Gamma_2(\boldsymbol{r}, z_{\mathrm{ap}})=
W_\mathrm{LT}^2 - 4 \sigma_\mathrm{BW}^2,
$$
which characterizes the average instantaneous width of the beam, excluding the contribution from beam wandering.

> conclusion

>- describe why 4 in longterm
>- examples of analyt expressions of gamma2 and 4. refs to articles
>- delta correlated n: discussed and justifies and refs: [charnotsk](https://sci-hub.se/10.1364/JOSAA.32.001357)