# Анотація {#sec:annotation_ua .unnumbered}
**Клен М.Д.** Статистичні моделі та часова когерентність квантового світла в турбулентній атмосфері.*---Квалiфiкацiйна наукова праця на правах рукопису.*
*Дисертацiя на здобуття наукового степеня доктора фiлософiї за спецiальнiстю 01.04.02 "Теоретична фiзика" (104--Фiзика та астрономiя).---Iнститут теоретичної фiзики iм. М.М. Боголюбова Нацiональної академiї наук України, Київ, 2026.*

Основою локальних мереж квантового зв'язку є волоконно-оптичні канали, проте вони обмежені експоненційним затуханням сигналу та стаціонарністю інфраструктури.
Оптичні канали у вільному просторі пропонують гнучку альтернативу, дозволяючи створювати бездротові з'єднання між наземними станціями, а також з авіаційними платформами, що є недоступним для стаціонарних волоконних мереж.
На відміну від контрольованих умов при використанні оптичного волокна, канали у вільному просторі піддаються впливу атмосферної турбулентності.
Цей процес спричиняє стохастичні флуктуації показника заломлення та відповідні спотворення променя світла, що проявляється у вигляді блукання променя навколо осі поширення та сцинтиляції (флуктуацій інтенсивності).
Відтак, зазначені ефекти суттєво ускладнюють опис таких каналів для квантової комунікації.

Вплив турбулентності на квантовий стан світла у квазімонохроматичній моді моделюється однією випадковою величиною --- ефективністю проходження, що визначається відношенням інтенсивності, яка потрапила у приймальну апертуру, до загальної інтенсивності променя світла.
Таким чином, розподіл імовірності ефективності проходження (РІЕП) є ключовим для характеристики атмосферних квантових каналів у вільному просторі.
Попри його фундаментальне значення, при моделюванні РІЕП зберігаються суттєві теоретичні прогалини.
По-перше, не визначено чітких критеріїв застосовності наявних у літературі аналітичних моделей РІЕП.
По-друге, сучасні дослідження переважно базуються на описі ансамблю проходжень пучка світла, ігноруючи часові кореляції.
Це унеможливлює динамічну характеристику каналів, необхідну для реалізації практичних квантових протоколів в умовах турбулентності.

Для вирішення цих проблем однією з основних цілей цього дослідження є встановлення меж застосовності існуючих аналітичних моделей шляхом їх порівняння з результатами чисельного моделювання.
Ми також проводимо валідацію фундаментальних припущень, на яких базуються поточні моделі, з метою оцінки їхньої придатності для різних сценаріїв використання.
Крім того, другий компонент цього дослідження присвячений вивченню часової залежності квантових властивостей в умовах атмосферної турбулентності.
Зокрема, ми прагнемо кількісно оцінити ступінь стійкості заплутаності та некласичності до стохастичних флуктуацій, спричинених саме цими умовами.

У цьому дослідженні застосовано чисельний метод фазових екранів, що моделює поширення світла як послідовність тонких фазових модуляторів, розділених ділянками вільного простору.
Щоб уникнути статистичних похибок, властивих традиційним методам генерації фазових екранів, ми використовуємо метод розрідженого спектру, який гарантує, що згенеровані фазові екрани суворо відповідають теоретичним виразам.
Додатково цей підхід дозволяє генерувати довгі фазові екрани, що дає змогу застосувати гіпотезу "замороженої" турбулентності Тейлора.
Цей метод пов'язує часову еволюцію турбулентності з просторовим зміщенням, спричиненим вітром.
Ми оцінюємо точність прогнозів існуючих аналітичних моделей за допомогою статистики Колмогорова-Смирнова, щоб виміряти, наскільки близько передбачення аналітичних моделей відповідають чисельно змодельованим даним.

В результаті, чисельне моделювання, що охоплює режими від слабкої до сильної турбулентності, продемонструвало, що інтенсивність атмосферної турбулентності передусім визначає лише дисперсію РІЕП, не змінюючи суттєво форми розподілу.
Натомість асиметрія розподілу виявляє високу варіативність та зміну знака залежно від розміру приймальної апертури.
Зокрема, коли розмір апертури є значно меншим за характерну ширину променя, хвіст розподілу подовжується у напрямку до вищих значень ефективності проходження (позитивна асиметрія); навпаки, збільшення апертури зміщує хвіст у бік нижчих значень ефективності проходження (негативна асиметрія).
Проте більшість аналітичних моделей обмежені жорсткою поведінкою асиметрії та не здатні відтворити цей перехід, зумовлений розміром апертури.

Ми провели систематичний аналіз властивостей та обмежень існуючих аналітичних моделей.
Було встановлено, що відхилення центру променя не можна вважати незалежним від деформації його форми, а гіпотеза гауссового спільного розподілу для логарифмів піввісей променя є хибною.
Іншою проблемою є те, що, хоча аналітичні моделі, параметризовані характеристиками променя, досить точно наближають загальну форму РІЕП, чисельне моделювання виявляє систематичне зміщення їхніх передбачень щодо моди розподілу та середнього значення.
Ця розбіжність зумовлена неправильною специфікацією моделі, оскільки припущення про ідеалізовану кругову або еліптичну форму променя не дозволяє адекватно описати його реальні складні деформації.
Як наслідок, такі моделі вносять систематичні помилки та демонструють гірші показники статистики Колмогорова-Смирнова порівняно з іншими підходами.

Для усунення зміщення через неправильну специфікацію моделі ми впроваджуємо метод узгодження моментів ефективності проходження, який перепараметризує моделі на основі форми променя через перші моменти ефективності проходження.
Застосування цієї методики до моделі кругового променя демонструє кращі значення статистики Колмогорова-Смирнова порівняно з іншими фізично обґрунтованими моделями.
Наша інша емпірична модель на основі Бета-розподілу демонструє вищу узгодженість із даними у більшості протестованих режимів, оскільки вона краще враховує варіації асиметрії, зумовлені розміром апертури.

Для опису часових кореляцій в атмосферних квантових каналах ми розробили концепцію двочасового РІЕП, яка дозволяє вийти за межі статичних описів ансамблів і характеризувати спільні розподіли ефективності проходження як функцію часового інтервалу між двома імпульсами.
На цій основі ми вводимо усереднений за апертурою радіус просторової когерентності, який кількісно визначає зміщення вітру, при якому кореляції ефективності проходження спадають до exp(−1).
Зокрема, визначений радіус просторової когерентності можна апроксимувати лінійною залежністю від розміру приймальної апертури.
Така формалізація забезпечує статистичний фундамент для кількісної оцінки часових кореляцій в атмосферних квантових каналах та аналізу стійкості квантових властивостей.

Спираючись на концепцію двочасового РІЕП, ми кількісно оцінюємо стійкість квантової заплутаності та некласичності в атмосферних каналах.
Хоча квантова заплутаність між двома імпульсами може зберігатися протягом десятків мілісекунд, ефективність квантової пам'яті залишається критичним фактором, що обмежує практичне використання квантової заплутаності в дискретних змінних у часових інтервалах тривалістю кілька мілісекунд.
Крім того, показано, що протоколи адаптивної селекції з використанням яскравих класичних імпульсів для тестування ефективності проходження каналу дозволяють зберігати некласичність протягом часових інтервалів до десятків мілісекунд між тестовим імпульсом та квантовим станом.

Підсумовуючи, у цій дисертації усунуто неоднозначності щодо розуміння та опису атмосферних квантових каналів.
Зокрема, встановлено, що існуючі аналітичні моделі часто не здатні коректно врахувати асиметрію розподілу, залежну від розміру апертури.
Це зумовлює необхідність відмови від інтенсивності турбулентності як єдиного критерію вибору моделі.
Натомість у цій роботі встановлено, що розмір приймальної апертури є визначальним параметром для вибору відповідної моделі.

Хоча модель кругового променя з використанням розробленого методу узгодження моментів ефективності проходження демонструє найкращі результати серед фізично обґрунтованих моделей, необхідність чисельного інтегрування обмежує її широке практичне застосування.
Відтак, емпірична модель на основі Бета-розподілу є оптимальною для практичного застосування завдяки наявності аналітичного виразу в замкнутій формі та параметризації лише двома моментами ефективності проходження.
Ця модель є особливо корисною для аналізу квантових протоколів, у яких сучасні методи часто не враховують флуктуації ефективності проходження, що призводить до систематичного ігнорування випадкової природи каналу та суттєвих помилок в оцінюванні характеристик.
Застосування моделі Бета-розподілу дозволяє подолати ці обмеження, забезпечуючи коректність аналізу захищеності в тих випадках, де ігнорування стохастичності каналу призводить до хибних результатів.

Зрештою, підтверджена стійкість квантових кореляцій у реальних часових діапазонах обґрунтовує доцільність застосування методів часового кодування в мережах квантового зв'язку у вільному просторі.
Водночас практична реалізація протоколів з використанням квантової заплутаності в дискретних змінних залишається обмеженою ефективністю квантової пам'яті.
Це підкреслює, що хоча атмосферні канали забезпечують значні часові вікна для реалізації протоколів, повне розкриття їхнього потенціалу потребує подолання технологічних бар'єрів у зберіганні квантової інформації.

**Ключовi слова:**
Квантові канали у вільному просторі,
розподіл імовірностей ефективності проходження (РІЕП),
часові кореляції в каналах у вільному просторі,
часове кодування,
двочасовий РІЕП,
просторовий радіус когерентності,
метод узгодження ефективності проходження,
атмосферна турбулентність,
метод фазових екранів,
квантова заплутаність,
протоколи адаптивної селекції,
збереження некласичності.

>Квантовий зв'язок,
>Квантова оптика,
>Модель кругового променя,
>Квантова пам'ять в атмосфері,
>Режим сильної турбулетності.

**Cписок публiкацiй:**
```{=latex}
\begin{enumerate}[label={[\Roman*]}]
    \item M. Klen and A. A. Semenov, "Numerical simulations of atmospheric quantum channels", Phys. Rev. A 108, 033718 (2023). \textbf{(Q1)}
    \item M. Klen, D. Vasylyev, W. Vogel, and A. A. Semenov, "Time correlations in atmospheric quantum channels", Phys. Rev. A 109, 033712 (2024). \textbf{(Q1)}
    \item I. Pechonkin, M. Klen, and A. A. Semenov, "Circular-beam approximation for quantum channels in a turbulent atmosphere", Phys. Rev. A 112, 063716 (2025). \textbf{(Q1)}
    \item A. Semenov, M. Klen, and I. Pechonkin, "Quantum Optics in the Turbulent Atmosphere: Fundamental Issues and Applications", in Quantum Technologies for Defence and Security II, edited by V. Fernandez, G. Sorelli, and S. Schwartz (p. 38). Proceedings of SPIE 13676, 136760H-13 (2025).
\end{enumerate}
```


```{=latex}
\clearpage
```

> ознайомити зі змістом і результатами дослідження, узагальнено й лаконічно викласти суть наукової праці, позначити новаторство та практичну значимість.
> 5-7 pages

# Abstract {#sec:annotation_en .unnumbered}
**Klen M.D.** Statistical models and temporal coherence of quantum light in the turbulent atmosphere.---*Manuscript. Thesis for the degree of Doctor of Philosophy in the specialty 01.04.02
"Theoretical Physics" (104--Physics and Astronomy).---Bogolyubov Institute for
Theoretical Physics of National Academy of Sciences of Ukraine, Kyiv, 2025.*

>## Background
>### Context

Fiber links form the foundation of local quantum communication networks. 
However, they are constrained by inherent signal attenuation and the rigidity of stationary infrastructure. 
Free-space optical links offer a scalable alternative for expanding these networks through wireless connections. 
Furthermore, they enable connections between moving ground-based stations and airborne platforms, which fixed fiber infrastructure cannot establish.

Unlike the controlled environment of optical fibers, free-space links are subject to atmospheric turbulence that induces stochastic fluctuations in the refractive index and distorts the propagating beam.
These perturbations manifest as beam wandering from the propagation axis and intensity fluctuations known as scintillation.
Consequently, these effects introduce significant complexity in characterizing the channel statistics for free-space quantum communication.

>### Subject

The impact of turbulence on the quantum state of light prepared in a quasi-monochromatic mode can be described by a single random variable---transmittance---defined as the ratio of the intensity captured by the receiving aperture to the total beam intensity.
Thus, the probability distribution of transmittance (PDT) is central to the characterization of atmospheric quantum channels.
Despite its fundamental role, significant theoretical gaps persist regarding how this variable is modeled and utilized.
First, there remains no clear understanding regarding model selection among the various analytical models of the PDT.
Second, current literature relies on static ensemble descriptions that neglect time correlations.
This approach fails to provide the dynamic characterization required by many practical quantum protocols in turbulent atmosphere.

>## Purpose

To address these challenges, one of the primary objectives of this research is to establish the range of applicability for existing analytical models by comparing their predictions against numerical simulations.
We also validate the underlying assumptions of current models in order to evaluate their suitability for different scenarios.
Furthermore, the second component of this study investigates the temporal dependence of quantum properties in atmospheric turbulence.
Specifically, we seek to quantify the resilience of entanglement and nonclassicality against stochastic fluctuations induced in these conditions.

>## Methods

This study employs a numerical approach to simulate atmospheric channels based on the phase screen method, modeling the propagation path as a sequence of thin, phase-modulated layers separated by free-space vacuum segments.
To address statistical discrepancies inherent in traditional generation techniques, we utilize the sparse spectrum approach that ensures generated phase screens strictly align with theoretical requirements.
Additionally, this approach facilitates the generation of extended phase screens, enabling the application of the Taylor frozen turbulence hypothesis. 
This method links the time-evolution of atmospheric transmittance to wind-driven displacements.
We assess the predictive accuracy of existing analytical models against this data using the Kolmogorov-Smirnov statistic to measure how closely the analytical model predictions match the simulated data.

>## Results
>### Skewness

Numerical simulations spanning weak-to-strong turbulence regimes demonstrated that atmospheric turbulence strength primarily governs the variance of the PDT without significantly altering its fundamental shape. 
Conversely, the skewness---representing the distribution's asymmetry---exhibits high variability and sign reversals contingent upon the receiving aperture size. 
Specifically, when the aperture is much smaller than the beam width, the distribution tail extends toward higher transmittance values (positive skewness); in contrast, larger apertures shift the tail toward lower transmittance values (negative skewness). 
However, most analytical models are constrained by rigid skewness behaviour and fail to capture this aperture-driven transition.

>### Systematic errors

We systematically analyzed the properties and limitations of existing analytical models.
We identified that the beam-center cannot be considered independent of shape deformation, nor does the Gaussian joint distribution hypothesis hold for the logarithms of the beam semi-axes.
Another issue is that, although analytical models parameterized by beam shape moments accurately approximate the overall PDT shape, numerical simulations reveal a systematic shift in their predicted mode and mean values.
This discrepancy arises due to a model misspecification bias, as idealized circular or elliptical beam shapes cannot fully describe the beam shape deformations. 
Consequently, such models introduce systematic errors and exhibit inferior Kolmogorov-Smirnov statistics compared to other models.

>### Models

To eliminate the model misspecification bias, we introduce the transmittance-moments-matching technique, which reparametrizes beam-shape based models in terms of first transmittance moments.
The circular beam model using this technique shows better values of the Kolmogorov-Smirnov statistics compared to other physics-based models.
Our other empirical Beta-distribution model shows superior performance across the majority of tested regimes because it better accounts for aperture-driven skewness variations.

>### Two-time PDT

To describe time correlations is atmospheric quantum channels, we develop a two-time PDT framework that moves beyond static ensemble descriptions to characterize joint transmittance distributions as a function of the time separation between two pulses. 
Building on this, we introduce an aperture-averaged spatial coherence radius which quantifies the wind-driven displacement at which transmittance correlations decay to exp(-1). 
Specifically, the defined coherence radius exhibits a linear scaling behavior relative to the receiving aperture size.
This formalization provides a statistical foundation for quantifying temporal correlations in atmospheric quantum channels and analysing the resilience of quantum properties.

>### Protocols

Building upon the two-time PDT, we quantify the resilience of entanglement and nonclassicality in atmospheric channels. 
While entanglement between two pulses persists for time separations up to tens of milliseconds, quantum memory efficiency currently restricts practical discrete-variable entanglement to several milliseconds.
Furthermore, adaptive selection protocols utilizing bright classical pulses to probe channel transmittance are established as a practical tool capable of preserving nonclassicality within tens of millisecond time intervals between the probe pulse and the quantum state.

>## Conclusions

In conclusion, this thesis resolves ambiguities regarding the understanding and characterization of atmospheric quantum channels.
Specifically, existing analytical models often fail to reflect the aperture-dependent asymmetry observed in actual distributions.
This necessitates a departure from using turbulence strength as the primary selection criterion, as this is insufficient for accurate modeling.
Instead, this work establishes the size of the receiving aperture as the governing parameter for selecting the appropriate model.

While the circular-beam model  with the developed transmittance-moments-matching approach demonstrates superior performance among physics-based models, its reliance on numerical integration limits broad application.
Consequently, the empirical Beta-distribution model emerges as the superior choice for practical implementation, providing a closed-form analytical expression parameterized by only two moments.
This capability is particularly vital for quantum protocol analysis, where current methods often rely on constant-transmittance approximations that systematically ignore the random nature of atmospheric channels and introduce significant estimation errors.
Utilizing the Beta-distribution model directly addresses this limitation, effectively eliminating potential loopholes in performance analysis by  demonstrating robust validity across the majority of parameter regimes.

Ultimately, the analyzed resilience of quantum correlations over practical temporal windows renders time-bin encoding strategies feasible for free-space quantum networking. 
However, the practical realization of discrete variable entanglement protocols remains constrained by quantum memory efficiency. 
This highlights that while atmospheric channels support practical timescales, unlocking their full potential requires addressing storage limitations inherent in current quantum hardware.

**Keywords:**
Free-space quantum channels,
probability distribution of transmittance (PDT),
temporal correlations in free-space channels,
time-bin encoding,
two-time PDT,
spatial coherence radius,
transmittance-moment matching,
atmospheric turbulence,
sparse-spectrum phase-screen method
strong fluctuation regime
quantum entanglement,
adaptive selection protocols,
nonclassicality preservation.

> від 5 до 15.

> To .pdf metadata:
>Truncated lognormal model,
>Beam-wandering model,
>Elliptical-beam model,
>Total probability model,
>Beta distribution model,

>Target Research Community:
>- Information Theorists & Channel Modelers
>- Computational Physicists & Atmospheric Scientists
>- Pure Quantum Optics Researchers
>- Quantum Engineers & Experimentalists

**List of publications:**

```{=latex}
\begin{enumerate}[label={[\Roman*]}]
    \item\label{mypaper1} M. Klen and A. A. Semenov, "Numerical simulations of atmospheric quantum channels", Phys. Rev. A 108, 033718 (2023). \textbf{(Q1)}
    \item\label{mypaper2} M. Klen, D. Vasylyev, W. Vogel, and A. A. Semenov, "Time correlations in atmospheric quantum channels", Phys. Rev. A 109, 033712 (2024). \textbf{(Q1)}
    \item\label{mypaper3} I. Pechonkin, M. Klen, and A. A. Semenov, "Circular-beam approximation for quantum channels in a turbulent atmosphere", Phys. Rev. A 112, 063716 (2025). \textbf{(Q1)}
    \item\label{mypaper4} A. Semenov, M. Klen, and I. Pechonkin, "Quantum Optics in the Turbulent Atmosphere: Fundamental Issues and Applications", in Quantum Technologies for Defence and Security II, edited by V. Fernandez, G. Sorelli, and S. Schwartz (p. 38). Proceedings of SPIE 13676, 136760H-13 (2025).
\end{enumerate}
```


>в яких опубліковані основні наукові результати дисертації;
які засвідчують апробацію матеріалів дисертації;
які додатково відображають наукові результати дисертації.

```{=latex}
\clearpage
```