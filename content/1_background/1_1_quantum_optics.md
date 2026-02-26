## Quantum Optics {#sec:qo}
Classical optics, built on Maxwell’s equations, describes light as a deterministic, smooth electromagnetic wave^[@born2000,jackson1998].
It explains reflection, interference, diffraction, and polarization with remarkable success.
But in the first half of the 20th century, it remained unclear whether light was truly a wave or a collection of quanta.
While theoretical developments anticipated the photon concept, no experiment could prove its necessity^[@scully1972].
The photoelectric effect, often referred to as evidence of photons, can be also described within a semiclassical framework: a continuous electromagnetic field interacting with quantized matter^[@LambScully1969].
Taylor’s double-slit experiment with extremely weak light, performed in 1909^[@taylor1909], later was used as evidence in the debate over whether light behaves as a wave or as discrete quanta^[@slater1925].

>This part must be rewritten

This uncertainty persisted until 1976, when Kimble, Dagenais, and Mandel developed^[@kimble1976] a theory describing the two-time intensity correlations of light emitted by a two-level atom, and then observed photon antibunching effect experimentally in 1977^[@kimble1977].
This phenomenon cannot be explained by any classical electromagnetic field and confirms the quantum nature of light.

Later on, many other quantum features of light were demonstrated^[@mandel1995].
The observation of squeezed states, which demonstrates variance below vacuum noise in one quadrature, was reported by Slusher et al. in 1985^[@slusher1985].
An illustrative counter-intuitive example of multi-photon interference, Hong-Ou-Mandel effect, demonstrated by Hong et al.  in 1987^[@hong1987].
Furthermore, numerous experimental tests of Bell inequalities using entangled photons have been performed in various configurations ^[@aspect1981,tittel1998,weihs1998,hensen2015,brunner2014], highlighting the nonclassical correlations of light.

Despite the late growth of experimental studies, the theoretical framework of quantum optics had already been well established much earlier.
Foundational contributions were made by Glauber^[@glauber1963b], Mandel^[@mandel1965], and other pioneers, who developed the groundwork for understanding the quantum properties of light long before many of the mentioned experiments were conducted.

In the early 1960s, Roy Glauber introduced the idea of representing quantum states of light $\hat\rho$ as a linear expansion over coherent states^[@glauber1963a,sudarshan1963a]
$$
%\label{eq:rho2P}
\hat\rho=\int P(\alpha)\,|\alpha\rangle\langle\alpha|\,\mathrm{d}^{2}\alpha,
$$
where $|\alpha\rangle$ are coherent states---eigenvectors of the annihilation operator---which form an overcomplete basis of the Hilbert space^[@klauder1985], $\mathrm{d}^2\alpha = \mathrm{d}\mathrm{Re}\alpha \mathrm{d}\mathrm{Im}\alpha$ and $P(\alpha)$ is the Glauber-Sudarshan P-function, a quasiprobability distribution over phase space.
If $P(\alpha)$ is a well-behaved, positive function, the quantum state can be interpreted as a classical mixture of coherent fields; if it is negative or singular, the state exhibits some nonclassical features^[@mandel1986,sperling2020].
Later, this idea was formalized and extended into the broader phase-space formalism of quantum mechanics^[@cohen1966] which has become the mainstream framework used today to describe quantum states of light.