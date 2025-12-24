# Application
## Introduction
This chapter investigates the practical application of quantum state transmission through turbulent atmospheric channels.
Understanding the limits of quantum state preservation under realistic conditions is essential for designing robust quantum communication protocols. 
We quantify the effects of channel properties, including temporal correlations, aperture size, and finite detector resolution, on different aspects of quantumness. 
This analysis provides a practical framework for assessing the feasibility of free-space quantum tasks.

We analyze three distinct manifestations of quantumness under these conditions. 
First, we investigate the preservation of Gaussian entanglement between continuous-variable pulses separated by a finite time delay. 
Second, we extend this analysis to discrete-variable systems, focusing on polarization-entangled states. 
Finally, we consider adaptive selection strategies for single-mode nonclassicality, examining the impact of the temporal separation between a classical probe and the quantum state on squeezed vacuum and squeezed coherent states.

A central theme of this discussion is the role of temporal correlations in the channel.
We build on time-dependent transmittance simulations described in the previous chapter ^[sec:timecoh].
Our analysis accounts for realistic conditions, including parametric down-conversion states rather than single-photon Bell states, the interplay between turbulence and quantum memory delay, detector efficiency, and the finite dimensionality of photon-number-resolving detectors.
The results provide a quantitative framework for assessing the feasibility of free-space quantum tasks under realistic atmospheric conditions.

## Gaussian entanglement between pulses
#### Quantum entanglement 
describes correlations between distinct subsystems that cannot be explained by classical physics and that arise from the non separability of the joint quantum state.
The conceptual origin of entanglement can be traced to the Einstein Podolsky Rosen paradox. 
In its original formulation, the EPR argument considers two spatially separated systems prepared in a correlated state. 
If the value of one observable of the first system can be predicted with certainty by measuring the second system, then this observable is considered an element of reality. 
If this holds simultaneously for two non commuting observables, then the quantum mechanical description appears incomplete. 
The EPR paradox was originally presented as a critique of quantum mechanics, but it later became a cornerstone for understanding nonclassical correlations.

In modern quantum information theory, entanglement is no longer viewed as a sign of incompleteness, but as a well defined physical resource.
It is a central resource in quantum information science, where it enables tasks that are impossible or inefficient using classical correlations alone.
In this section, the focus is on continuous variable entanglement realized in optical systems.

#### Continuous variable systems 
are quantum systems whose observables have continuous spectra. 
In quantum optics, such systems arise naturally from bosonic modes of the electromagnetic field. 
Each optical mode can be modeled as a quantum harmonic oscillator, and its physical observables are given by field quadratures.

Continuous variable entanglement appears as nonclassical correlations between the quadratures of different optical modes. 
These correlations can be measured using well-studied homodyne detection^[@10.1364/OL.8.000177] ^[@10.1103/RevModPhys.81.299]. 
As a result, such systems are widely used in optical implementations of quantum communication, quantum key distribution, and quantum enhanced metrology ^[@sbraunstein2005; @sweedbrook2012].

#### The two-mode squeezed vacuum (TMSV) state $\left|\xi\right>$
is the canonical example of a continuous variable entangled state. 
In this state, the quantum noise of two optical modes is strongly correlated. Fluctuations of one quadrature in the first mode are correlated with the corresponding quadrature of the second mode, while the conjugate quadratures are anticorrelated. 
The strength of these correlations increases with the squeezing parameter $\xi$.
In the limit of infinite squeezing, the TMSV approaches the idealized EPR state discussed in the original paradox^[@10.1088/0256-307X/21/10/003] ^[@10.1103/PhysRevLett.68.3663]. 

Two mode squeezed vacuum states can be generated using nondegenerate optical parametric oscillators or by interfering two single mode squeezed states on a balanced beam splitter. 
In the photon number basis, the TMSV state can be written as
$$
\left|\xi\right>=\cosh^{-1}\xi\sum_{n=0}^{\infty}(-\tanh \xi)^n\left|n,n\right>
$$

#### Simon certifier.
Detecting entanglement in continuous variable systems requires criteria that can distinguish separable states from entangled states. 
The fundamental conceptual basis for separability in bipartite quantum systems is given by the Peres Horodecki criterion^[@PH]. 
This criterion states that any separable quantum state must remain a valid physical state after partial transposition with respect to one subsystem.
In general infinite dimensional Hilbert spaces, this condition is necessary but not sufficient for separability.
However Simon showed that for two mode Gaussian states such as the TMSV state the partial transposition criterion is both necessary and sufficient for separability ^[@simon2000] ^[@shchukin2005].
This makes the Simon criterion a useful and complete tool for Gaussian entanglement detection for TMSV states.

The effect of atmospheric turbulence on continuous variable entanglement depends on temporal correlations of the channel transmittance. 
The limiting cases of fully correlated transmittances, corresponding to time separation $\tau\to 0$, and fully anticorrelated transmittances, corresponding to large time separation $\tau\to\infty$, have been analyzed previously in ^[@bohmann2016a].
We focus on the intermediate regime, where the time interval between subsequent pulses $\tau$ is finite.

We consider a two mode squeezed vacuum state as the entangled source. 
The first mode is transmitted through the atmospheric channel at time $t=0$. 
The second mode is stored in a quantum memory and transmitted at a later time $t=\tau$. 
As a result, the two modes experience different but temporally correlated realizations of the atmospheric channel.

For the simulations, we use the same atmospheric channels as defined in ^[sec:timecorr].
Deterministic losses of $0.1\ \mathrm{dB/km}$ are additionally included in the effective transmittances $\eta_0$ and $\eta_\tau$ ^[@losses], together with losses of the optical system.
When measurements are performed using homodyne detection, the local oscillator is transmitted in the same spatial mode as the signal with orthogonal polarization, ensuring a stable phase reference while experiencing the same atmospheric fluctuations.

To analyze entanglement preservation in this scenario, we apply the Simon criterion to the two mode squeezed vacuum state after transmission through the atmospheric channels. 
For the considered model, the Simon certifier $\mathcal W$ takes the form
$$
\begin{split}
\mathcal{W}=&\sinh^2\xi\Big[-\left\langle\sqrt{\eta_0\eta_\tau}\right\rangle^2\cosh^2\xi+\left\langle\eta_0\right\rangle\left\langle\eta_\tau\right\rangle\sinh^2\xi\Big]\nonumber\\
&\times\Big[1-\frac{\left\langle\sqrt{\eta_0\eta_\tau}\right\rangle^2}{4}\sinh^22\xi\nonumber\\
&+\sinh^2\xi\left(\left\langle\eta_0\right\rangle+\left\langle\eta_\tau\right\rangle+\left\langle\eta_0\right\rangle\left\langle\eta_\tau\right\rangle\sinh^2\xi\right)\Big]
\end{split}
$$
According to the Simon criterion, the transmitted state is entangled if and only if $\mathcal W<0$.

The expression for $\mathcal W$ factorizes into two multiplicative terms. 
The second factor is strictly positive for all physically allowed values of the transmittances and the squeezing parameter. 
As a result, it cannot influence the sign of $\mathcal W$ and can be omitted when determining the entanglement condition.
Therefore, the sign of $\mathcal W$ is fully determined by the first factor. 
Importantly, this factor is invariant under a global rescaling of the transmittances $\eta_0$ and $\eta_\tau$. 
This implies that entanglement preservation is independent of deterministic losses, including losses introduced by the quantum memory and the optical system.

^[fig:cvent] shows the regions of entanglement preservation for a TMSV state transmitted through atmospheric channels. 
![[4_entanglement.png-1.png|200]]
The horizontal axis represents the wind-driven shift $s$, which corresponds to the time separation between pulses $\tau = s / v$, where $v$ is the transverse wind speed (see ^[sec:timecorr]).
The vertical axis shows the squeezing parameter $\xi$ of the initial TMSV state.
The shaded regions correspond to $\mathcal W<0$, where the Simon criterion certifies that the received state remains entangled.

The figure reveals a counterintuitive feature: increasing the squeezing parameter $\xi$ reduces the maximum wind-driven shift for which entanglement is preserved. 
As a result, stronger squeezing does not improve entanglement robustness in atmospheric channels. 

For a squeezing parameter of $\xi = 2$ and a turbulence strength of $\sigma_R^2 = 11$, Gaussian entanglement remains for wind-driven shifts up to $s = 6.4\ \mathrm{cm}$, corresponding to a time separation of $\tau = 6.4\ \mathrm{ms}$ for a transverse wind speed of $v = 10\ \mathrm{m/s}$. 
This demonstrates that entanglement between light pulses is highly robust, persisting beyond millisecond time intervals. 
However, losses associated with the quantum memory can significantly reduce the absolute value of the Simon certifier.

In Section ^[sec:timecorr], we introduced the spatial coherence radius $\rho_0$, which characterizes the correlation of transmittances and depends on the receiver aperture radius $R_\mathrm{ap}$. 
![[5_witness_coherence.png-1.png|200]]
The threshold wind-driven shift $s_\mathrm{th}$, defined as the maximum shift for which entanglement is preserved ($\mathcal W < 0$), also depends on $R_\mathrm{ap}$.
^[fig:sthbyrho] shows $s_\mathrm{th}$ as a function of the coherence radius $\rho_0$. 
The figure shows that $s_\mathrm{th}(\rho_0)$ is a monotonically increasing, nonlinear function. 
Larger coherence allows entanglement to survive larger wind-driven shifts. 
At the same time, the threshold decreases with increasing squeezing.
The nonlinear behavior highlights the nontrivial interplay between initial squeezing, channel correlations, and receiver geometry in determining entanglement robustness.

In summary, we have introduced and quantified the time interval over which entanglement between pulses is preserved, and analyzed how it depends on channel aperture, coherence radius, and squeezing. 
Gaussian entanglement is robust against atmospheric turbulence, while stronger squeezing does not improve its survival. 
Deterministic losses affect only the absolute value of the certifier. 
These results provide a practical guideline for maintaining continuous variable entanglement in realistic free-space quantum channels.

## Discrete-variable entanglement between pulses

In the previous section, entanglement was discussed in the continuous variable regime. 
This description is natural for Gaussian states and homodyne based measurements. 
However, many experimentally relevant sources and protocols operate in a finite-dimensional Hilbert space, where entanglement can be encoded in discrete degrees of freedom. 
This motivates a separate treatment of discrete variable entanglement.

We consider a maximally entangled two qubit system corresponding to a Bell state. 
Each qubit is encoded in the polarization degree of freedom of a single photon occupying a well defined temporal mode. 
The horizontal polarization $\mathrm{h}$ defines the logical zero state, while the vertical polarization $\mathrm{v}$ defines the logical one. 
Using two temporal modes $t = 0$ and $t = \tau$, the system spans four optical modes, namely $\mathrm{h}0$, $\mathrm{v}0$, $\mathrm{h}\tau$, and $\mathrm{v}\tau$. 
The corresponding Bell state is written as
$$
\begin{split}
\left| \mathcal{B} \right\rangle &= \frac{1}{\sqrt{2}} \Big( \left| \mathrm{h} \right\rangle_0 \left| \mathrm{v} \right\rangle_\tau - \left| \mathrm{v} \right\rangle_0 \left| \mathrm{h} \right\rangle_\tau \Big) \\
&= \frac{1}{\sqrt{2}} \Big( \left| 1 \right\rangle_{\mathrm{h0}} \left| 0 \right\rangle_{\mathrm{v0}} \left| 0 \right\rangle_{\mathrm{h\tau}} \left| 1 \right\rangle_{\mathrm{v\tau}} - \left| 0 \right\rangle_{\mathrm{h0}} \left| 1 \right\rangle_{\mathrm{v0}} \left| 1 \right\rangle_{\mathrm{h\tau}} \left| 0 \right\rangle_{\mathrm{v\tau}} \Big)
\end{split}
$$

In optical implementations, entangled photon pairs are often generated through a nonlinear light matter interaction such as spontaneous parametric down conversion (PDC) ^[@pdcent]. 
A PDC source produces a superposition of photon number states. 
In the relevant polarization and temporal modes, this superposition can be written as
$$\left| \mathrm{PDC} \right\rangle = (\cosh\xi)^{-2} \sum\limits_{n=0}^{+\infty} \sqrt{n+1} \tanh^n \xi \left| \Phi_n \right\rangle$$
with
$$
\left| \Phi_n \right\rangle = \frac{1}{\sqrt{n+1}} \sum\limits_{m=0}^{n} (-1)^m \left| n-m \right\rangle_{\mathrm{h0}} \left| m \right\rangle_{\mathrm{v0}} \left| m \right\rangle_{\mathrm{h\tau}} \left| n-m \right\rangle_{\mathrm{v\tau}}
$$
The parameter $\xi$ is determined by the pump power and the nonlinear coupling strength. 
The term with $n = 1$ corresponds to a polarization Bell state occupying the two temporal modes, while higher order terms describe the simultaneous emission of multiple photon pairs.
In this section, we analyze the entanglement between optical pulses separated by a time interval $\tau$ for both the ideal Bell state and the PDC state.

To quantify discrete-variable entanglement, we use the Bell parameter $\mathcal{B}$, defined in the Clauser-Horne-Shimony-Holt form^[@CHSH]. 
It is constructed from correlations between measurements on two parts in different bases. 
A value of $\mathcal{B} > 2$ signals a violation of local realism and confirms the presence of entanglement.

Several studies have investigated the distribution of discrete variable entanglement through turbulent free space channels. 
A theoretical framework describing the propagation of polarization entanglement through atmospheric turbulence was developed in ^[@SemenovVogel2010] for both Bell states and PDC states. 
In that work, the entanglement degradation was described in terms of statistical moments of the transmittance.

The role of temporal correlations in the atmospheric channel was further analyzed in ^[@gumb], where two limiting propagation scenarios were considered. 
The case of copropagation corresponds to perfectly correlated transmittance fluctuations and is observed in the limit $\tau \to 0$. 
The opposite limit of counterpropagation corresponds to statistically independent fluctuations and is obtained for $\tau \to \infty$. 
These two regimes provide useful benchmarks but do not describe intermediate situations where correlations are only partial.

Experimental feasibility of distributing polarization entanglement through strong turbulence channels was demonstrated in ^[@Fedrizzi2009]. 
That experiment confirmed that polarization entanglement can survive high loss free space propagation. 
However, the temporal separation between consecutive pulses was on the order of $50\mathrm{ns}$, which is much shorter than the atmospheric correlation time. 
As a result, the corresponding transmittance fluctuations were almost perfectly correlated between the two pulses.

In realistic free space quantum communication scenarios, the temporal separation between entangled pulses may become comparable to or larger than the atmospheric correlation time. 
In this regime, transmittance fluctuations are neither fully correlated nor fully independent. 
Consequently, the measured Bell parameter becomes a nontrivial function of the pulse separation time $\tau$.
Determining this dependence is essential for understanding entanglement distribution under realistic channel conditions and for assessing the robustness of Bell inequality violations in random media.

> For theta (...). Derivation for Bell (Sem, Gumb) and PDC

For the numerical simulations, we employ the same atmospheric channel model as defined in Section ^[sec:timecorr]. 
The first mode is transmitted through the atmospheric channel at time $t = 0$. The second mode is stored in a quantum memory and is transmitted at a later time $t = \tau$ ^[@qmem]. 

In contrast to the continuous variable case, the discrete variable description requires an explicit account of all deterministic losses. 
Losses directly affect the detection probabilities and therefore enter the evaluation of the Bell parameters. 
As a result, each optical and detection component must be included in the channel model.

The total deterministic loss amounts to $9.42\,\mathrm{dB}$ and consists of:
- atmospheric attenuation of $0.1\,\mathrm{dB}/\mathrm{km}$ over a propagation distance of $50\,\mathrm{km}$, resulting in a loss of $5\,\mathrm{dB}$
- a $50{:}50$ beam splitter, introducing a loss of $10 \log_{10}(1/2) = 3\,\mathrm{dB}$
- detector efficiency of $0.85$, corresponding to a loss of $10 \log_{10}(0.85) = 0.71\,\mathrm{dB}$
- quantum memory writing efficiency of $0.85$, corresponding to a loss of $10 \log_{10}(0.85) = 0.71\,\mathrm{dB}$

In addition to these static contributions, the quantum memory readout exhibits a time dependent loss. 
It is modeled as an effective attenuation of $3\,\mathrm{dB}/\mathrm{ms}$ of storage time, which directly depends on the pulse separation time $\tau$.
Noise counts originating from detector dark counts and stray light are included in the simulation $\nu=3 \times 10^{-4}$.

> More details about QMemory are possible 

The dependence of the Bell parameter $\mathcal{B}$ on the temporal separation between pulses $\tau$ is shown in Figure ^[fig:bell] for both the ideal Bell state and the parametric down conversion state. 

![[bell.png|200]]

For the PDC state, the Bell parameter additionally depends on the source parameter $\xi$.
In the simulations, we optimize over $\xi$ by choosing the value that maximizes $\mathcal{B}$ for each separation $\tau$.

Because of time-dependent losses in the channel, the wind-driven shift $s$ cannot be treated as interchangeable with the pulses time separation $\tau$. 
To account for this effect, we consider two wind speeds, $v = 10$ and $v = 5$. 
To isolate the impact of time-dependent quantum memory losses from atmospheric effects, we also show results for an ideal quantum memory with perfect readout efficiency of $0\,\mathrm{dB}/\mathrm{ms}$.

From the results, it is apparent that atmospheric turbulence alone allows discrete-variable entanglement to survive over pulse separations of tens of milliseconds. 
Quantum correlations persisting over such long times indicate that using two or more time-separated quantum states makes it possible to increase the effective dimensionality of the Hilbert space ^[@80].
However, the introduction of quantum memory losses strongly reduces the Bell parameter to a few milliseconds.

These findings indicate that the feasibility of the protocol is currently limited by hardware efficiency. 
They emphasize that developing high-performance quantum memories is important for practical implementation.

> - [ ] ensure links to Sem, Gum, 2009 exp

> In this subsection, we have analyzed discrete-variable entanglement between temporally separated optical pulses. Both ideal Bell states and parametric down conversion states were considered. The analysis accounted for atmospheric turbulence, deterministic losses, quantum memory inefficiencies, and background noise.

## Threshold-based selection for nonclassical states

Nonclassicality is a broader concept than entanglement. 
Entanglement refers to quantum correlations between subsystems, while nonclassicality can arise even in a single mode optical field. 
It characterizes states that cannot be described within a classical theory of electromagnetic radiation. 

Classical optical states admit a description in terms of solutions of Maxwell equations with stochastic amplitudes and phases. 
Coherent states form a prominent subset of this class. 
They minimize the Heisenberg uncertainty relation
$$
%\label{eq:heis}
(\Delta X)^2 (\Delta P)^2 \geq \frac{1}{4}
$$
and therefore exhibit the smallest allowed quadrature noise. 
Despite this property, coherent states remain classical since their fluctuations can be reproduced by classical stochastic models.

A systematic characterization of nonclassicality is provided by the Glauber Sudarshan $P$ function^[eq:Pfunc]. 
This function represents a quantum state as a statistical mixture of coherent states. 
If the $P$ function is positive and regular, the state is considered classical. 
The absence of such a representation is a necessary and sufficient criterion for nonclassicality. 
Nonclassical states exhibit either negativity of the $P$ function or singularities that are stronger than those of a classical probability distribution. 
These features indicate the failure of any classical stochastic description.

The negativity of the $P$ function provides a clear qualitative criterion but it is not unique as a quantitative measure. 
Several nonclassicality measures have been proposed that capture different operational aspects of this property ^[@ge2020]. Their relevance depends on the task under consideration.

>Mandel param
>Q param array
>Bell like ineq

Historically, the first unambiguous experimental signature of nonclassical light was photon antibunching ^[sec:QO]. 
This effect cannot be explained by classical intensity fluctuations and directly contradicts classical field theories. 
Squeezed states represent another important class of nonclassical states. 
In these states, the noise of one quadrature is reduced below the vacuum level, while the noise of the conjugate quadrature increases to satisfy the uncertainty relation^[eq:heis]. 
Such noise reduction has no classical analog, since classical stochastic electromagnetic fields cannot suppress quadrature fluctuations below the vacuum limit.

> Where and how to define squeezed states??

In this section, we study the propagation of squeezed states through an atmospheric channel.
We consider the threshold selection of the transmittance as a method to improve the preservation of nonclassical properties in atmospheric channels. 
This approach exploits fluctuations of the channel transmittance $\eta_t$ to conditionally enhance nonclassical features of the transmitted light.

In the first subsection, we analyze the propagation of a squeezed vacuum state and study the dependence of the output squeezing on the transmittance threshold. 
We consider the limiting case of the adaptive selection method discussed in ^[sec:timecoh], corresponding to a vanishing time interval between the classical probe pulse and the quantum pulse, $\tau \to 0$. 
This scenario can be described using the one-time PDT function ^[eq:pdt], which allows comparison of the predictions of the analytical models discussed in ^[sec:validation] with the results of numerical simulations.

In the second subsection, we extend the analysis to a more general and realistic scenario. 
We consider amplitude squeezed coherent states and quantify nonclassicality using the Mandel parameter^[@mandel], the Binomial $Q$ parameter[^@vogel], and Bell-like inequality criteria^[@vadym]. 
The Binomial $Q$ parameter generalizes the Mandel parameter to account for realistic detectors, such as arrays of on/off detectors, while Bell-like inequality criteria enable testing nonclassicality in situations where standard photocounting-based approaches fail.
Nonclassicality is studied as a function of the time interval between the classical probe pulse and the quantum pulse, $\tau$, using the results of ^[sec:condProb].

### Squeezed vacuum state with postselection

The protocol is defined as follows. 
A single mode squeezed vacuum state $|\xi\rangle = \hat S(\xi)|0\rangle$ is prepared at the transmitter. 
Here $\hat S(\xi)$ denotes the squeezing operator. 
The strong reference local oscillator is sent through the turbulent atmospheric channel in the same spatial mode as the quantum state but with orthogonal polarisation.
This classical pulse allows reliable estimation of the channel transmittance $\eta$ due to negligible atmospheric depolarisation and thereby enables postselection, in which events with $\eta < \eta_{\mathrm{min}}$ are discarded.
This procedure is equivalent to the adaptive selection in the limit $\tau \to 0$ as discussed in ^[sec:condpdt].

For the selected events the normal ordered quadrature variance $\langle :\Delta \hat x^2: \rangle$ is estimated using balanced homodyne detection. 
The measured quadrature variance satisfies
$$\left\langle\Delta \hat{x}^2 \right\rangle=\frac{1}{2}+\left\langle:\Delta \hat{x}^2: \right\rangle$$
where $1/2$ corresponds to the quadrature variance of the vacuum state. Negative values of $\langle :\Delta \hat x^2: \rangle$ therefore indicate quadrature squeezing and indicates nonclassicality of the transmitted state.

Numerical simulations are performed for a channel of moderate strength of turbulence with $F_0 = z_{\mathrm{ap}}$ as specified in ^[tab:moderate].
For a strong local oscillator the transformation of the normal ordered quadrature variance through a fluctuating loss channel is given by ^[@semenov2012]
$$\left\langle:\Delta\hat{x}^2:\right\rangle_\mathrm{out} = \left\langle\eta\right\rangle \left\langle:\Delta\hat{x}^2:\right\rangle_\mathrm{in} + \left\langle\Delta T^2\right\rangle \left\langle\hat{x}\right\rangle_\mathrm{in}^2$$
where $T = \sqrt{\eta}$. 
For a squeezed vacuum state $\langle \hat x \rangle_{\mathrm{in}} = 0$, so the second term vanishes and only the first moment of $\eta$ contributes.

In the limit of adaptive selection with $\tau \to 0$ the channel is described by a one-time PDT as discussed in ^[eq:2PDTtoPDT]. 
The effective mean transmittance after postselection is
$$\left<\eta\right>= \frac{1}{\overline{\mathcal{F}}(\eta_\mathrm{min})} \int_{\eta_\mathrm{min}}^{1}\! \mathrm{d}\eta\, \eta\, \mathcal{P}(\eta)$$
where $\overline{\mathcal{F}}(\eta_\mathrm{min}) = \int_{\eta_\mathrm{min}}^{1} \!\mathrm{d}\eta\, \mathcal{P}(\eta)$. 
The analytical models defined through the first two moments of the transmittance reproduce these moments by definition. 
In contrast the postselection protocol depends explicitly on the full probability distribution $\mathcal P(\eta)$. 
Accurate predictions therefore require correct modelling of the entire distribution or equivalently of all higher moments. 
This difference motivates a direct comparison between analytical model predictions and numerical results under postselection.

^[fig:sq_thr] shows the output quadrature squeezing as a function of the postselection threshold $\eta_{\mathrm{min}}$. 
Numerical results are compared with predictions of the analytical models.

![[nonclass_1_1.png]]

In the limit $\eta_{\mathrm{min}} \to 0$ the postselection is omitted and the protocol depends only on the transmittance moments of the full probability distribution.
Analytical models parameterised by transmittance moments therefore reproduce the numerical results.
However, as discussed in ^[sec:validation], truncation of the lognormal model results in a slight mismatch with the numerical results.
In contrast, the elliptic beam model, which is parameterised through moments of the beam shape parameters rather than the transmittance, exhibits a large discrepancy. 
This underscores the statement (see ^[sec:validation]) that turbulence models should be parameterised directly in terms of transmittance statistics.

For finite thresholds $\eta_{\mathrm{min}} > 0$ the discrepancies generally increase. 
Among the models, the beta distribution model provides the closest agreement with the numerical results over the full range of $\eta_{\mathrm{min}}$. 
This confirms that accurate modelling of the PDT is essential when postselection is applied.

In the previous sections ^[sec:validation], ^[sec:timecoher] the aperture size was identified as the primary factor influencing the output results. 
^[fig:sq_rap] illustrates the dependence of the output squeezing on the aperture radius for different postselection thresholds $\eta_{\mathrm{min}}$. 

![[nonclass_1_2.png]]

Increasing the aperture size within a reasonable range generally has a larger effect on the output squeezing than adjusting the postselection threshold $\eta_{\mathrm{min}}$.
 ^[sec:timecoher].
Its influence, however, is less pronounced than in other cases discussed previously ^[sec:validation], ^[sec:timecoher].
It should also be noted that postselection completely discards states for low-transmittance events. 
This implies that when the rate of quantum states is an important quantity, adjusting the aperture size provides a more effective strategy to optimize squeezing.

>[!danger] Losses aren't mentioned

### Amplitude squeezed coherent state with adaptive selection
In this section we address a more realistic and more general scenario than in the previous section. 
We study an amplitude squeezed coherent state which is defined as a squeezed vacuum displaced by a real amplitude $\alpha_0$ in phase space, $\left|\alpha_0,\xi\right>=\hat D(\alpha_0)\hat S(\xi)\left|0\right>$.
Amplitude squeezed states exhibit reduced photon number fluctuations compared to a classical coherent state with the same mean intensity. 
While a coherent state shows a Poissonian photon number distribution, amplitude squeezing leads to a narrower distribution. 
This reduction of photon number fluctuations is a direct signature of nonclassicality.
This means that nonclassicality can be assessed using photon number statistics, avoiding balanced homodyne detection with its requirement of phase stable reference fields and complex measurement setups.

Nonclassicality in such situations is commonly characterized by the Mandel parameter
$$Q=\frac{\left\langle \Delta \hat n^2\right\rangle}{\left\langle \hat n\right\rangle}-1$$
Negative values of $Q$ correspond to sub Poissonian photon number statistics and therefore to nonclassical light. 
This criterion relies on ideal photon number resolving detection and is therefore of limited applicability in realistic measurement scenarios.

A more realistic detection model is based on an array of $N$ on-off detectors. 
Each detector can only discriminate between the absence and presence of photons. 
For a classical coherent state with complex amplitude $\alpha$, the resulting click statistics are binomial. 
The corresponding response function for registering $m$ clicks, described by a positive operator valued measure (POVM) ^[@povb], is given by
$$\Pi(m|\alpha)=\binom{N}{m}\left(1-e^{-|\alpha|^2/N}\right)^m e^{-(N-m)|\alpha|^2/N}$$
This measurement captures the finite resolution of practical photon counting devices and reduces to ideal photon number resolving detection in the limit $N\to\infty$.
In this setting, nonclassicality can be detected via sub binomial click statistics. 
The corresponding parameter for such measurement is^[@vogelQN]
$$Q_{N}=N\frac{\left\langle\Delta c^2\right\rangle}{\left\langle c\right\rangle(N-\left\langle c\right\rangle)}-1$$where $c$ denotes the number of clicks. 
Negative values of $Q_N$ indicate nonclassical light.

The described criteria provide sufficient but not necessary conditions for nonclassicality. 
There exist nonclassical states whose click statistics remain classical.

A more general method based on a Bell-like inequalities for detecting nonclassicality was recently introduced ^[@klimovS]. If there exists a choice of  $\lambda(m)$ such that the inequality
$$\sum_{m=0}^{N-1} \lambda(m) P(m) \leq \sup_{\alpha \in \mathbb{C}} \sum_{m=0}^{N-1} \lambda(m) \Pi(m|\alpha)$$
is violated, the statistics are necessarily nonclassical. 
Here $P(m)$ is the measured click distribution. 
We use the optimal sets of $\lambda(m)$ determined for array detectors with $N=2,3,5$ ^[@vady], which provide a practical tool for reliably detecting nonclassicality in realistic measurement setups.

Using the results of the channel simulations obtained in ^[sec:timecorrr] for different values of time between classical probe and quantum pulse, we apply an adaptive selection strategy to preserve nonclassicality in atmospheric conditions. 
We study the maximal time interval for a given threshold transmittance $\eta_\text{min}$ during which the click statistics remain nonclassical.

>[!note] Mention losses and sim params.

Figure ^[fig:nonclass] shows the wind-driven spatial shift $s$, corresponding to a temporal delay $\tau=s/v$ between the classical probe and the quantum pulse, at which different nonclassicality criteria no longer indicate nonclassicality.

![[nonclass_2.png|200]]

The Mandel parameter $Q$ reaches zero at $s = 7.2~\text{cm}$, indicating the limit of sub-Poissonian photon statistics for an ideal photon number resolving detector. 
For arrays of on-off detectors, the sub-binomial parameters $Q_N$ reach zero at larger shifts: $Q_5 = 9.7~\text{cm}$, $Q_3 = 11.4~\text{cm}$, and $Q_2 = 14.2~\text{cm}$. 
While $Q_N$ approaches $Q$ as $N$ increases, in the considered case smaller detector arrays detect nonclassicality for longer time intervals. 
However, for other state parameters ($\xi=0.16$ and $\alpha_0=1.4$), the trend reverses, and larger detector arrays maintain nonclassicality over longer times.

The figure also shows the difference between the left- and right-hand sides of the Bell-like inequalities ^[eq:vady], which quantifies the distance of the click statistics from the convex hull of coherent state click statistics.
When this difference reaches zero, the click statistics can no longer be considered nonclassical.
The inequalities reach zero at $s = 14.2~\text{cm}$ for $N=2$, $s = 19.6~\text{cm}$ for $N=3$, and exceed $s = 28~\text{cm}$ for $N=5$, which is the maximal value covered by the simulations.
Notably, for $N=2$ the sub-binomial parameter $Q_2$ reaches zero at the same spatial shift as the Bell-like inequality, indicating a deeper connection between these two nonclassicality criteria for small detector arrays.
Overall, these results show that the Bell-like criteria provide a robust detection of nonclassicality over extended time delays.

## Conclusion

The analysis presented in this section characterizes the robustness of quantum correlations and nonclassicality in atmospheric channels. 
We demonstrated that Gaussian entanglement between light pulses persists over millisecond timescales. 
Its preservation increases monotonically with the spatial coherence radius, although nonlinear features are observed.

Discrete-variable entanglement exhibits a distinct behavior, depending on both temporal correlations and deterministic losses. 
Time-dependent losses in current quantum memories significantly restrict the viable pulse separation. 
Simulations indicate that atmospheric coherence alone allows delays of tens of milliseconds, whereas memory decay reduces this to a few milliseconds. 
This discrepancy highlights the need for high-efficiency storage components.

The study of single-mode nonclassicality emphasizes the utility of adaptive selection techniques. 
By monitoring a classical probe pulse, quantum transmission events can be conditionally selected during periods of high transmittance. 
The beta-distribution model accurately predicts the nonclassicality of squeezed states under postselection in the limit of instantaneous adaptive selection ($\tau \to 0$).
For finite $\tau$, two-time PDT models are required, but such models are currently lacking. 
Numerical studies of amplitude-squeezed states show that adaptive selection improves nonclassicality even for pulse separations of tens of milliseconds. 
Bell-like inequalities provide a more sensitive measure of nonclassicality in this context.

In conclusion, temporal correlations in atmospheric quantum channels provide a window for effective quantum communication. 
Exploiting these correlations increases the effective Hilbert-space dimensionality and allows adaptive selection strategies to significantly improve nonclassicality preservation. 
Future work can include experimental validation of the reported findings in time-dependent atmospheric channels.