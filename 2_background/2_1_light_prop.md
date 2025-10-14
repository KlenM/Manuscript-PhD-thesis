# Light beam propagation in media

To obtain the transmittance value of the optical communication channel, we must solve the classical problem of light propagation through stochastic isotropic media. This section defines the fundamental equations governing beam intensity at the aperture plane.

## Gaussian beam source
- in this work we consider only the gaussian beam mode at the trasmittance plane. 
- such modes are highly used because they approximate laser source output well.

The boundary condition at the transmitter plane $z=z_0$ takes the form of a Gaussian beam:
$$u(\mathbf{r};0)=\sqrt{\frac{2}{\pi W_0^2}}\exp\left[-\frac{\mathbf{r}^2}{W_0^2}-\frac{ik}{2F_0}\mathbf{r}^2\right]$$
where $W_0$ is the beam waist radius and $F_0$ is the radius of curvature of the wavefront. For collimated beams, $F_0 \to \infty$, while for focused beams, $F_0$ takes finite values.

## Paraxial wave equation in stochastic media
To describe the propagation of gaussian beams through turbulent atmosphere we begin from the general wave equation derived from Maxwell’s equations.

- scalar wave, polarization or only one of 6 components.

The electromagnetic field propagation in atmosphere is described with the scalar wave equation. Separating temporal and spatial variables yields the Helmholtz equation:
$$\nabla^{2}E+k^{2}n^{2}E=0$$
where $\nabla^2$ is the Laplacian operator and $k$ is the vacuum wave number.

For Gaussian beams propagating along the z-axis over long distances, the paraxial approximation becomes valid. 
We express the complex amplitude as $E(x,y,z)=u(x,y,z) e^{ikz}$.
Under paraxial approximation the assumption that the $z$ derivative of the amplitude function u is a slowly varying function of z reads as $\left| \frac{\partial ^{2}u}{\partial z^{2}} \right| \ll \left| k \frac{\partial u}{\partial z} \right|$ is valid. 

This leads to the paraxial scalar wave equation in a medium with spatially varying refractive index:
$$2ik\frac{\partial u(\mathbf{r};z)}{\partial z}+\Delta_\mathbf{r} u(\mathbf{r};z)+2k^2\delta n(\mathbf{r},z) u(\mathbf{r};z)=0$$
where $\delta n(\mathbf{r},z) = n(\mathbf{r},z) - 1$ represents the refractive index perturbation from vacuum.

- [ ] The paraxial equation uses $\Delta r\Delta_\mathbf{r} \delta r$​ notation but should clarify this represents the transverse Laplacian

## Transmittance calculation

To quantify the optical power collected by the receiver, we calculate the transmittance at the aperture plane $z=z_\mathcal{A}$:

$$\eta = \int_\mathcal{A} d^2\boldsymbol{r} |u(\boldsymbol{r}, z_\mathcal{A})|^2$$

where $\mathcal{A}$ represents the circular aperture area with radius $R_A$.

## Vacuum propagation

For the case $\delta n = 0$ (homogeneous medium), the solution becomes straightforward. The Fresnel diffraction integral describes the field evolution:

$$U(x,y,z)=\frac{e^{ikz}}{i\lambda z}\iint_{-\infty}^{\infty}U(x',y',0)e^{i\frac{k}{2z}[(x-x')^{2}+(y-y')^{2}]}dx'dy'$$

This integral represents a convolution with the propagation kernel, based on the Huygens-Fresnel principle where each wavefront point acts as a source of secondary spherical wavelets.

In the spatial frequency domain, this convolution becomes multiplication with the transfer function $H(f_{x},f_{y},z)=e^{ikz}e^{-i\pi\lambda z(f_{x}^{2}+f_{y}^{2})}$, known as the angular spectrum method. This formulation enables efficient numerical implementation using Fast Fourier Transform algorithms.

- [ ] some words about analytical approaches to atmos propagation