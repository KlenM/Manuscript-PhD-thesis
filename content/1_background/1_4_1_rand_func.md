### Preliminaries on random functions theory

> - One support point for a dedicated section is to add a bit of math vibe to the thesis
> - Also, in the case of including of random processes paper - here is the place for background

When studying light propagation through random media, it is essential to introduce the minimal framework of random functions. In our problem, randomness enters through spatial variations of the refractive index, which in turn induces randomness in most derived quantities like beam properties at the aperture plane or the transmittance values. By treating these quantities as random functions, we can systematically describe their statistical properties, characterize correlations, study ergodicity property markov property, etc ^[@kampen2011,andrews2005,mandel1995].

Let us consider a function $\xi$ of two parameters:
$$\xi: T \times \Omega \to \xi(t, \omega)$$
where $t \in T$ is the domain parameter (time, space, etc.) and $\omega \in \Omega$ is an outcome, which can be usefully interpreted as a specific realization of a universe from the set of all possible parallel worlds.
This form allows us to adopt two complementary perspectives.
If we fix the outcome $\omega$---i.e., select one specific universe---then we obtain a deterministic function $\xi^{(\omega)}(t)$.
This is referred to as a sample path or realization of the random function.
Examples of two sample paths as functions of $t$ are shown in ^[fig:sample_paths].

![\label{fig:sample_paths}Examples of two sample paths of the random function $\xi(t, \omega)$. In this context, the random function represents atmospheric channel transmittance $\eta$. The pink line corresponds to the realization $\xi^{(\omega_1)}(t)$, while the blue line corresponds to $\xi^{(\omega_2)}(t)$. Each path illustrates the deterministic evolution of the channel transmittance over time $t$ for a fixed outcome $\omega$.](background/eta_process.pdf)

>~~The function $\xi$ is what we call a random function~~.

If we fix the domain parameter $t$---i.e., look at all possible universes at a single time---then we obtain a random variable $\xi_t$.
In this view, the random function can be seen as a family of random variables $\{\xi_t\}_{t\in T}$ indexed by $t \in T$.

We can define some random function by specifying all distribution functions of the form ^[@yaglom2004]:
$$
\begin{split}
%\label{eq:randProcDef}
F_{t}(x) &= \mathbb{P}[\xi_t < x], \quad \forall t \in T\\
F_{t_1,t_2}(x_1,x_2) &= \mathbb{P}[\xi_{t_1} < x_1, \xi_{t_2} < x_2], \quad \forall t_1, t_2\\
&\dots\\
F_{t_1,\dots,t_n}(x_1,\dots,x_n) &= \mathbb{P}[\xi_{t_1} < x_1,\dots \xi_{t_n} < x_n], \quad \forall t_i, \ i \in [1\dots n], \ \forall n \\
\end{split}
$$
Other convenient way to specify a random function is using some analytic formula containing parameters which are random variables.

>". In the absence of such a family of probability distributions, it is customary to describe the random field in terms of its lowerorder statistical moments." ([Andrews and Phillips, 2005, p. 45](zotero://select/library/items/IJGQ3J8A)) ([pdf](zotero://open-pdf/library/items/VGHZA9HX?page=69&annotation=537H37EL))

We will call random processes time-indexed random functions, and random fields random functions indexed by multidimensional (2D or 3D) spatial variables.

#### Stationary random functions.
The common class of random functions in physics is stationary random functions.
A random function is stationary if all of its final-dimensional distribution functions ^[eq:randProcDef] are invariant under the parameter shifts
$$
F_{t_1 + \tau, \dots, t_n+\tau}(x_1, \dots, x_n) = F_{t_1, \dots, t_n}(x_1, \dots, x_n)\,, \quad \forall t_i\,, \ i \in [1\dots n]\,, \ \forall n
$$
This simplifies the process, such as all functions $F_t(x) \ \forall t \in T$ are identical, so we need only one $F_{t_0}(x)$; and instead of considering  $F_{t_1, t_2}(x_1, x_2) \ \forall t_1,t_2$ we need only the family of joint distributions indexed by the time difference $\tau=t_2-t_1$, and so on.

We can characterize random functions with moments.
The first moment $\mu(t)=\mathbb E\, \xi_t = \int_{-\infty}^\infty x dF_t(x)$ is the mean value.
For the stationary random function it is constant $\mu=\mu(t)$, so it is often useful to redefine our random process with a new random process $\xi_t - \mu$. The second moment is the correlation function, which gives more precise characteristic of the random function:
$$B(t_1, t_2) = \mathbb E\, \xi_{t_1}\overline{\xi_{t_2}} = \int_{-\infty}^\infty\int_{-\infty}^\infty x_1 x_2 dF_{t_1,t_2}(x_1,x_2)$$
For the stationary random function it only depends on the time difference $\mathbb E\, \xi_{t}\overline{\xi_{t+\tau}} = B(\tau)$.

>  as we did with the refractive index random field ^[eq:deltan

While correlation function characterize how similar the values at distance $r$, sometimes it is useful to consider how different the values at distance $r$, which is possible with the structure function
$$
%\label{eq:struct_func}
D(t_1,t_2)=\mathbb E|\xi_{t_1}-\xi_{t_2}|^2=\int_{-\infty}^\infty\int_{-\infty}^\infty |x_1 - x_2|^2 dF_{t_1,t_2}(x_1,x_2)$$
The structure function is a powerful tool in the theory of random function with stationary increment^[@kolmogorov1941], but in the case of stationary functions it also depends only on the time difference $\tau$ and it simply relates to the correlation function as $D(\tau) = 2 \left(B(0) - \mathrm{Re}\, B(\tau)\right)$.

In turbulent atmosphere science it is also common to characterize random fields with the complimentary to correlation function power spectral density function $\Phi(k)$, defined as Fourier transformation^[@wiener1930,khintchine1934]:
$$
%\label{eq:psd_theory}
\Phi(\lambda) = \frac{1}{2\pi}\int e^{-i\lambda\tau} B(\tau)\, d\tau$$
In one of the next subsection we will explicitly present several models for refractive index random field using power spectral density function formalism.

>- know avg mean square difference
>    - корисно для функцій зі стаціонарним приростом
>- easy to show through corr
>- to complete the triade of eq through spectrum
>- img

#### Spectral representation.
As in the case of regular functions, it can be very useful to represent random functions in the form of Fourier transform. It was shown, that any stationary random function can be arbitrarily closely represented on some interval $-T < t < T$ as a linear combination of finite number independent harmonic oscillators of the form $\xi_k e^{i\lambda_k t}$, where $\xi_k$ are some complex random variables with mean zero values and $\lambda_k$ are some real constants.

In the limit we get the spectral representation theorem (Cramer-Karhunen), which states that any stationary process $\xi(t)$ can be represented in the form of the Fourier-Stieltjes integral:
$$
%\label{eq:FSint}
\xi(t) = \int_{-\infty}^\infty e^{i\lambda t} dZ(\lambda)
$$
where $dZ(\lambda)$ is a random increment, which associates a random variable for each interval $[\lambda, \lambda + d\lambda]$, with the following properties:
$$
\mathbb E\left[dZ(\lambda)\right]=0\,,\quad
\mathbb E\left[dZ(\lambda_1)\overline{dZ(\lambda_2)}\right]=0\,,\quad
\mathbb E\left[\left|dZ(\lambda)\right|^2\right]=\Phi(\lambda)\,d\lambda
$$
where $\lambda_1 \neq \lambda_2$, and $\Phi(\lambda)$ power spectral density function of the process (given it is absolutely continuous).

> Moreover, if the process is Gaussian, then the random variables Zk are Gaussian and stochastically independent. This result generalizes the Karhunen–Loève transform.
The spectral representation theorem provides a framework for numerical generation of random functions, which forms the basis of the phase screen generation method which we will describe in one of the next sections.

>[Fourier-Stieltjes integral] ([pdf](zotero://open-pdf/library/items/AUHJNVFF?page=49&annotation=QFIE8QQV)) ([Yaglom, 2004, p. 49](zotero://select/library/items/NVY3HWQW))
> Kolmog K10, K12 + [image] ([pdf](zotero://open-pdf/library/items/AUHJNVFF?page=67&annotation=RYT8TWV4)) ([Yaglom, 2004, p. 67](zotero://select/library/items/NVY3HWQW))
>
> *Markov property, Ergodicity property*