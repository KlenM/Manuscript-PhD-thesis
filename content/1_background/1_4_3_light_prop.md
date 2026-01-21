### Light beam propagation in inhomogeneous media

To obtain the transmittance value of the optical communication channel, we must solve the classical problem of light propagation through stochastic isotropic media. This section defines the fundamental equations governing beam intensity at the aperture plane.

#### Gaussian beam source.
In this work, we restrict the analysis to the Gaussian beam mode at the transmittance plane^[@siegman1986]. Gaussian modes provide an accurate approximation of the output of most laser sources used in free space optical communication. Because of this, they are widely adopted in theoretical modeling and experimental studies of atmospheric optical channels.

The boundary condition at the transmitter plane $z=z_0$ takes the form of a Gaussian beam^[@andrews2005]
$$%\label{eq:gaussbeam}
\boxed{u(\mathbf{r};0)=\sqrt{\frac{2}{\pi W_0^2}}\exp\left[-\frac{\mathbf{r}^2}{W_0^2}-\frac{ik}{2F_0}\mathbf{r}^2\right]}$$
where $W_0$ is the beam waist radius and $F_0$ is the radius of curvature of the wavefront. For collimated beams, $F_0 \to \infty$, while for focused beams, $F_0$ takes finite values.

#### Paraxial wave equation in stochastic media.
> To describe the propagation of gaussian beams through turbulent atmosphere we begin from the general wave equation derived from Maxwell’s equations.

>- scalar wave, polarization or only one of 6 components.
>- "smoothly varying stochastic refractive index" ([Andrews and Phillips, 2005, p. 137](zotero://select/library/items/IJGQ3J8A)) ([pdf](zotero://open-pdf/library/items/VGHZA9HX?page=161&annotation=XM7K93SD))
>- "set of fundamental assumptions on the propagating wave" ([Andrews and Phillips, 2005, p. 137](zotero://select/library/items/IJGQ3J8A)) ([pdf](zotero://open-pdf/library/items/VGHZA9HX?page=161&annotation=E4LAXLAC))
>- "J. W. Strohbehn, ed., Laser Beam Propagation in the Atmosphere (Springer, New York, 1978)" ([Andrews and Phillips, 2005, p. 177](zotero://select/library/items/IJGQ3J8A)) ([pdf](zotero://open-pdf/library/items/VGHZA9HX?page=201&annotation=WV4N9T75))
>- [ ] n is real

The electromagnetic field propagation in atmosphere is described with the scalar wave equation^[@strohbehn1968,siegman1986]. Separating temporal and spatial variables yields the Helmholtz equation
$$\nabla^{2}E+k^{2}n^{2}E=0$$
where $\nabla^2$ is the Laplacian operator and $k$ is the vacuum wave number.

For Gaussian beams propagating along the z-axis over long distances, the paraxial approximation becomes valid^[@siegman1986].
We express the complex amplitude as $E(x,y,z)=u(x,y,z) e^{ikz}$.
Under paraxial approximation the assumption that the $z$ derivative of the amplitude function u is a slowly varying function of z reads as $\left| \frac{\partial ^{2}u}{\partial z^{2}} \right| \ll \left| k \frac{\partial u}{\partial z} \right|$ is valid.

This leads to the paraxial scalar wave equation in a medium with spatially varying refractive index:
$$\boxed{2ik\frac{\partial u(\mathbf{r};z)}{\partial z}+\Delta_\mathbf{r} u(\mathbf{r};z)+2k^2\delta n(\mathbf{r},z) u(\mathbf{r};z)=0}$$
where $\delta n(\mathbf{r},z) = n(\mathbf{r},z) - 1$ represents the refractive index perturbation.

>- [ ] The paraxial equation uses $\Delta r\Delta_\mathbf{r} \delta r$​ notation but should clarify this represents the transverse Laplacian
>- Discussion on the single realization of δn(r) leading to a single channel realization.

>- [ ] some words about analytical approaches to atmos propagation
>- the requirenes of statistical description of n

#### Transmittance of channel.
To quantify the optical power collected by the receiver, we calculate the transmittance at the aperture plane $z=z_\mathrm{ap}$:

$$%\label{eq:eta}
\boxed{\eta = \int_{S_\mathrm{ap}} d^2\boldsymbol{r} |u(\boldsymbol{r}, z_\mathrm{ap})|^2}$$

where $S_\mathrm{ap}$ defines the circular region of integration over aperture pupil of radius $R_\mathrm{ap}$ and $d^2\boldsymbol{r}=dxdy$.

#### Vacuum propagation.
For the case $\delta n = 0$ (homogeneous medium), the solution becomes straightforward. The Fresnel diffraction integral describes the field evolution^[@goodman2017]

$$U(x,y,z)=\frac{e^{ikz}}{i\lambda z}\iint_{-\infty}^{\infty}U(x',y',0)e^{i\frac{k}{2z}[(x-x')^{2}+(y-y')^{2}]}dx'dy'$$

This integral represents a convolution with the propagation kernel, based on the Huygens-Fresnel principle where each wavefront point acts as a source of secondary spherical wavelets.

In the spatial frequency domain, this convolution becomes multiplication with the transfer function $H(f_{x},f_{y},z)=e^{ikz}e^{-i\pi\lambda z(f_{x}^{2}+f_{y}^{2})}$, known as the angular spectrum method. This formulation enables efficient numerical implementation using Fast Fourier Transform algorithms.

#### Statistical properties of a light beam in turbulence.
In the absence of refractive index fluctuations, a Gaussian beam ^[eq:gaussbeam] propagating in free space keeps its deterministic Gaussian profile at the aperture plane, as it represents the exact solution of the paraxial wave equation^[@siegman1986].
When the beam travels through a turbulent atmosphere, random changes in the refractive index make the optical field at the aperture plane a stochastic quantity.
To efficiently compress the vast amount of information required to describe the optical field distorted by turbulence, it is convenient to characterize the random fluctuations of the complex amplitude in terms of its second- and fourth-order correlation functions^[@andrews2005]
$$\Gamma_2(\mathbf{r};z) = \left< |u(\mathbf{r};z_\mathrm{ap})|^2 \right>$$
$$\Gamma_4(\mathbf{r}_1,\mathbf{r}_2;z_\mathrm{ap}) = \left< |u(\mathbf{r}_1;z_\mathrm{ap})|^2 |u(\mathbf{r}_2;z_\mathrm{ap})|^2 \right>$$
where $\langle \cdot \rangle$ denotes ensemble averaging over turbulence realizations.

These correlation functions enable the calculation of several statistical quantities that are essential for parametrizing analytical models of atmospheric channels.
Average transmittance of the atmospheric channel according to ^[eq:eta] equals to
$$\langle\eta\rangle  =
\left<\int_{S_\mathrm{ap}} d^2\boldsymbol{r} |u(\boldsymbol{r}, z_\mathrm{ap})|^2\right>=
\int_{S_\mathrm{ap}} d^2\boldsymbol{r} \, \Gamma_2(\boldsymbol{r}, z_{\mathrm{ap}})$$
and can be seen as the primary characteristic of channel effectiveness.
Second moment of the transmittance
$$\begin{split}
\langle\eta^2\rangle =
\left<\int_{S_\mathrm{ap}} d^2\boldsymbol{r}_1 |u(\boldsymbol{r}_1, z_\mathrm{ap})|^2\int_{S_\mathrm{ap}} d^2\boldsymbol{r}_2 |u(\boldsymbol{r}_2, z_\mathrm{ap})|^2\right> = \\ =
\int_{S_\mathrm{ap}}\int_{S_\mathrm{ap}}  d^2\boldsymbol{r}_1  d^2\boldsymbol{r}_2 \, \Gamma_4(\boldsymbol{r}_1, \boldsymbol{r}_2, z_\mathrm{ap})
\end{split}$$
requires the fourth order correlation function and characterizes the variability of the atmospheric channel transmittance.

Let's consider statistical properties of the beam-spot at the aperture plane^[@andrews2005].
The simplest property is the beam's center of gravity, which defined for a single realization of turbulent atmosphere as
$$x_0 = \int_{\mathbb{R}^2} d^2\boldsymbol{r} \, x\, |u(\boldsymbol{r}, z_\mathrm{ap})|^2$$
While it is obvious that under the assumption of isotropic turbulence ^[sec:turb_cascade] average value of the beam centroid $\left<x_0\right>=0$, it remains an open question whether its distribution is Gaussian.
In particular, for strong turbulence the distribution can deviate, for example by exhibiting heavy tails.
The second moment is referred to as the long-term beam-spot radius. It defined as
$$W_\mathrm{LT}^2 = 4\int_{\mathbb{R}^2} d^2\boldsymbol{r} \, x^2\, \Gamma_2(\boldsymbol{r}, z_{\mathrm{ap}})$$
and represents the effective spatial extent of the beam after propagation through turbulence, incorporating both diffraction and spreading due to the turbulence effects.
The variance of the beam-centroid coordinate, often referred to as beam wandering, characterizes the random displacement of the beam’s center of gravity
$$\sigma_\mathrm{BW}^2=\left<x_0^2\right>=
\int_{\mathbb{R}^4} d^2\boldsymbol{r}_1  d^2\boldsymbol{r}_2 \, x_1 x_2 \,\Gamma_4(\boldsymbol{r}_1, \boldsymbol{r}_2, z_\mathrm{ap})
$$
And complementary to these two quantities the short-term beam-spot radius is defined as
$$W_\mathrm{ST}^2=
4\int_{\mathbb{R}^2} d^2\boldsymbol{r} \, (x - x_0)^2\, \Gamma_2(\boldsymbol{r}, z_{\mathrm{ap}})=
W_\mathrm{LT}^2 - 4 \sigma_\mathrm{BW}^2$$
which characterizes the average instantaneous width of the beam, excluding the contribution from beam wandering.

> conclusion

>- describe why 4 in longterm
>- examples of analyt expressions of gamma2 and 4. refs to articles
>- delta correlated n: discussed and justifies and refs: [charnotsk](https://sci-hub.se/10.1364/JOSAA.32.001357)