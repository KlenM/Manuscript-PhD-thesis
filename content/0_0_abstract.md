# Анотація {#sec:annotation_ua .unnumbered}
**Клен М.Д.** Статистичні моделі та часова когерентність квантового світла в турбулентній атмосфері. *-- Квалiфiкацiйна наукова праця на правах рукопису.*
*Дисертацiя на здобуття наукового степеня доктора фiлософiї за спецiальнiстю 01.04.02 "Теоретична фiзика" (104 - Фiзика та астрономiя). -- Iнститут теоретичної фiзики iм. М.М. Боголюбова Нацiональної академiї наук України, Київ, 2026.*

Квантові канали у вільному просторі забезпечують квантовий зв'язок на великі відстані в умовах, коли передача по оптичному волокну є недоцільною.
Це охоплює значні дистанції, де експоненціальні втрати на поглинання в оптичному волокні унеможливлюють його використання, а також зв'язок між мобільними платформами, такими як супутниково-наземні канали та авіаційні системи.
Оптичне випромінювання є оптимальним носієм квантової інформації в таких сценаріях, оскільки воно зберігає квантові стани на великих відстанях.
Це дозволяє реалізувати низку протоколів квантового зв'язку, включаючи квантовий розподіл ключів, квантову телепортацію та обмін квантовою заплутаністю.
Ці можливості мають вирішальне значення для глобальної інфраструктури квантових мереж та архітектури квантового інтернету.

Квантова інформація зазвичай кодується в квазімонохроматичних оптичних імпульсах, які можна апроксимувати як гаусові моди променя.
Однак атмосферна турбулентність становить головну фізичну проблему.
Випадкові коливання показника заломлення викликають блукання променя, спотворення хвильового фронту, сцинтиляцію та розширення променя.
Ці ефекти нелінійно залежать від відстані поширення, інтенсивності турбулентності та довжини хвилі.
Подальші вимірювання передбачають використання оптичної системи з скінченною апертурою, яка обрізає частину спотвореного профілю світла.
Цей процес еквівалентний лінійному каналу з втратами, що характеризується ефективністю проходження $\eta$, яка визначається як частка інтенсивності променя, що уловлюється апертурою приймача.
Один скаляр $\eta$ узагальнює складну тривимірну фізику поширення, що має значення для передачі квантового стану.

Атмосферна турбулентність є стохастичним процесом, що робить ефективність проходження каналу випадковою величиною.
Розподіл імовірностей ефективності проходження (РІЕП) повністю характеризує статистику поширення квазімонохроматичного імпульсу через атмосферний квантовий канал.
Ця концепція дозволяє встановити чіткі співвідношення між вхідними та вихідними даними для переданих і отриманих квантових станів, що є основою для аналізу ефективності протоколу.

Було розроблено кілька аналітичних моделей для РІЕП, але межі їхньої застосовності залишаються нез’ясованими.
Хоча деякі моделі були підтверджені шляхом підгонки параметрів, цей підхід не є достатньо точним і може давати параметри, зміщені відносно фактичних атмосферних умов.
Крім того, деякі припущення, що лежать в основі цих моделей, ще не були підтверджені.

Існуюча концепція РІЕП описує сукупність незалежних подій поширення одиничного променя крізь атмосферу.
На практиці час когерентності турбулентності становить близько мілісекунд, тому послідовні імпульси поширюються через корельовані атмосферні умови.
Розподіл імовірностей ефективності проходження не може врахувати цю часову кореляцію.
Ігнорування цього факту відкидає структуру, яку можна використовувати для оптимізації протоколу, і створює вразливі місця в протоколах квантової безпеки, які передбачають незалежність реалізацій каналів.

> 2. Num method

Функція РІЕП визначається через скінченну просторову інтеграцію квадрата амплітуди поля, що підпорядковується стохастичному диференціальному рівнянню в частинних похідних.
Таке формулювання ускладнює аналітичний опис і робить фізичну інтерпретацію складним завданням.
Наближення в аналітичних виразах звужують теорію до конкретних граничних випадків, залишаючи основні режими турбулентності поза межами аналітичного опису.

У цій роботі ми використовуємо чисельне моделювання для отримання розподілу імовірностей ефективності проходження.
Ми застосовуємо метод фазових екрані для поширення хвиль у випадкових середовищах, який широко використовується в класичній оптиці.
Основним обмеженням цього підходу є недостатня дискретизація низькочастотної частини спектра турбулентності.
Щоб подолати це обмеження, ми застосовуємо метод розрідженого спектра, який дозволяє генерувати фазові екрани, чиї статистичні характеристики відповідають заданому теоретичному спектру.

За умови правильного вибору кількості фазових екранів та інших параметрів моделювання, метод фазових екранів із розрідженим спектром усуває розбіжність між результатами чисельного моделювання та аналітичним теоретичним описом атмосферних каналів.
Більше того, можливість генерувати фазові екрани довільного розміру з правильними статистичними властивостями дозволяє досліджувати часову еволюцію атмосферних каналів за гіпотезою "замороженої" турбулентності Тейлора.
Отриманий підхід дозволяє проводити комплексний аналіз атмосферних квантових каналів у вільному просторі та квантових властивостей світла, що поширюється в атмосфері.

> ## 3. Validation of Physical Assumptions

Ми аналізуємо розподіл імовірностей ефективності проходження (РІЕП), отриманий на основі чисельного моделювання для оптичних каналів у вільному просторі в умовах слабкої, помірної та сильної турбулентності.
Чисельні результати порівнюються з декількома аналітичними моделями.
До них належать дві фізично обґрунтовані моделі, що характеризують поведінку промуеня в площині апертури, а саме: моделі блукання променя та еліптичного променя, усічена логнормальна модель та гібридний підхід на основі моделі повної ймовірності.
Збіг між емпіричним та аналітичним розподілами кількісно оцінюється за допомогою статистики Колмогорова-Смирнова.

Чисельні розподіли, як правило, є одномодовими та мають гаусівську форму.
В умовах сильної турбулентності вони стають ширшими та більш плоскими.
Оскільки ефективність проходження обмежена в діапазоні від нуля до одиниці, це обмеження суттєво впливає на форму розподілу.
Розмір апертури відносно середнього розміру променя є домінуючим параметром що впливає на РІЕП.
Для малих апертур значення ефективності проходження концентруються поблизу нуля, що зумовлює позитивну асиметрію.
Для великих апертур верхня межа (одиниця) зумовлює негативну асиметрію.
Тому для будь-якої аналітичної моделі необхідне точне прогнозування перших моментів ефективності проходження для отримання достовірних розподілів.

Наші висновки показують, що на застосовність моделі переважно впливає відношення радіуса апертури до середнього розміру променя.
Отже, традиційні евристичні методи вибору моделі, засновані лише на інтенсивності турбулентності, не є застосовними.
Усічена логнормальна модель, яка завжди демонструє позитивну асиметрію, забезпечує узгоджений опис для малих апертур у всіх режимах турбулентності, але її точність погіршується зі збільшенням розміру апертури.
Моделі, засновані на опису променя, здебільшого демонструють негативну асиметрію, що робить їх більш придатними для каналів з великою апертурою, де вони забезпечують кращу відповідність формі РІЕП.
Однак ці моделі передбачають похибку специфікації, оскільки вони параметризуються через моменти форми променя, а не через моменти ефективність проходження.
Це призводить до систематичних зсувів моди розподілу і неточної оцінки середньої ефективності проходження.
Модель повної ймовірності, яка поєднує ці два підходи, фіксує перехід асиметрії, спричинений змінами розміру апертури.
Для малих апертур її точність близька до логнормальної моделі, тоді як для великих апертур вона забезпечує певне покращення у прогнозуванні РІЕП.

Щоб зменшити похибку специфікації, ми впроваджуємо техніку узгодження ефективності проходження, яка переформулює моделі, засновані на описі форми променя, через перші моменти ефективності проходження.
Цей метод застосовується до моделі з проміжним описом між моделями блукання променя та еліптичного променя через складне напіваналітичне формулювання останньої.
Незважаючи на простіше формулювання порівняно з моделлю еліптичного променя, наша модель загалом перевершує її в усіх режимах турбулентності.

Ми також перевіряємо ключові припущення, що лежать в основі фізично обґрунтованих моделей.
Підтверджено, що центр мас променя описується двовимірним нормальним розподілом, але його статистична незалежність від деформацій форми променя порушується, особливо в умовах сильної турбулентності.
У моделі еліптичного променя було припущенно, що логарифми піввісей підпорядковуються двовимірному гаусовому розподілу.
Натомість чисельне моделювання виявляє сильне зменшення густини ймовірності вздовж діагоналі, що вказує на те, що дві осі рідко бувають рівними.
Ці висновки стануть основою для майбутнього розвитку моделей, заснованих на описі форми променя.

Також ми пропонуємо емпіричну модель РІЕП, засновану на бета-розподілі.
Її обмежений носій природно відповідає фізичному діапазону ефективності проходження і відтворює перехід асиметрії залежно від розміру апертури.
Ця модель загалом перевершує всі інші розглянуті аналітичні моделі, а її проста аналітична формула робить її зручною для теоретичних прогнозів і практичного застосування.

> ## 5 temp corr

Ми розширюємо концепцію розподілу імовірностей ефективності проходження, щоб врахувати часові кореляції в атмосферних квантових каналах.
Існуючі моделі описують одиночні імпульси або імпульси, розділені інтервалом, що перевищує час кореляцій в атмосфері.
Натомість реальні системи працюють з високою частотою імпульсів, тому послідовні імпульси поширюються через корельовану турбулентність, що впливає на вихідні квантові стани.
Ці ефекти не враховуються одночасовими моделями РІЕП.
Ми вводимо і аналізуємо двочасовий РІЕП, який забезпечує повний статистичний опис двох послідовних імпульсів з довільним часовим інтервалом.
Його властивості досліджуються чисельно за гіпотезою "замороженої" турбулентності Тейлора.

Для кількісної оцінки часових кореляцій ми вводимо усереднений за апертурою радіус когерентності як часовий інтервал, при якому коефіцієнт кореляції Пірсона ефективності проходження спадає до $e^{-1}$.
Отримані характерні масштаби усередненого за апертурою радіуса когерентності відповідають декільком сантиметрам просторової когерентності або декільком мілісекундам часової когерентності.

Як і у випадку одночасового РІЕП, апертура приймача визначає поведінку усередненого за апертурою радіуса когерентності.
Просторовий радіус когерентності збільшується приблизно лінійно з розміром апертури в практично значущому діапазоні.
Це підкреслює роль розміру апертури як ефективного параметра для керування величиною кореляцій в атмосферних квантових каналах.

> ## 6. Applications and Practical Significance

Практична значущість цієї моделі продемонстрована на прикладі її застосування до декількох квантових протоколів у реалістичних атмосферних умовах.
Спочатку ми аналізуємо збереження гауссової заплутаності у  неперервних змінних між імпульсами, розділеними в часі.
Для визначення збереження заплутаності використовується критерій сепарабельності Саймона.
Ми виявили, що пороговий час збереження заплутаності становить декілька мілісекунд.
Цей поріг залежить від апертури приймача і закономірно виражається через просторовий радіус когерентності, який монотонно, проте нелінійно збільшується з розміром апертури.

Для систем з дискретними змінними ми вивчаємо стійкість поляризаційно-заплутаних станів Белла та станів, отриманих шляхом спонтанного параметричного розсіяння.
Результати показують, що атмосферна турбулентність сама по собі дозволяє квантовим кореляціям зберігатися протягом десятків мілісекунд.
Однак на практиці досяжний часовий масштаб суттєво обмежений залежними від часу втратами на зберігання і зчитування в квантовій пам'яті, що скорочує час збереження заплутаності до декількох мілісекунд.
Стійкість квантових кореляцій протягом таких часових інтервалів вказує на те, що використання двох або більше розділених у часі квантових станів може збільшити ефективну розмірність Гільбертового простору.

**Ключовi слова:**
Квантові канали у вільному просторі,
Квантовий зв'язок,
Атмосферна турбулентність,
Квантова оптика,
Чисельне моделювання методом фазових екранів,
Розподіл імовірностей ефективності проходження (РІЕП),
Метод узгодження ефективності проходження,
Модель кругового променя,
Двочасовий розподіл імовірностей ефективності проходження (Двочасовий РІЕП),
Часові кореляції в каналах у вільному просторі,
Часове кодування,
Просторовий радіус когерентності,
Заплутаність неперервних та дискретних змінних,
Протоколи адаптивного вибору,
Збереження некласичності,
Квантова пам'ять в атмосфері,
Режим сильної турбулетності.

**Cписок публiкацiй:**
1. Klen, M., & Semenov, A. A. (2023). Numerical simulations of atmospheric quantum channels. Physical Review A, 108(3). https://doi.org/10.1103/physreva.108.033718
2. Klen, M., Vasylyev, D., Vogel, W., & Semenov, A. A. (2024). Time correlations in atmospheric quantum channels. Physical Review A, 109(3). https://doi.org/10.1103/physreva.109.033712
3. Pechonkin, I., Klen, M., & Semenov, A. A. (2025). Circular-beam approximation for quantum channels in a turbulent atmosphere. Physical Review A, 112(6). https://doi.org/10.1103/pv7j-4zpf
4. Semenov, A., Klen, M., & Pechonkin, I. (2025). Quantum optics in the turbulent atmosphere: fundamental issues and applications. Quantum Technologies for Defence and Security II (p. 38). SPIE. https://doi.org/10.1117/12.3069599

```{=latex}
\clearpage
```

> ознайомити зі змістом і результатами дослідження, узагальнено й лаконічно викласти суть наукової праці, позначити новаторство та практичну значимість.
> 5-7 pages

# Abstract {#sec:annotation_en .unnumbered}
**Klen M.D.** Statistical models and temporal coherence of quantum light in the turbulent atmosphere. -- *Qualifying scientific work in the form of a manuscript.*
*Dissertation for the degree of Doctor of Philosophy in the specialty 01.04.02 "Theoretical Physics" (104 - Physics and Astronomy). -- Bogolyubov Institute for Theoretical Physics of the National Academy of Sciences of Ukraine, Kyiv, 2025.*

> ## 1. Context and the Problem of Stochastic Transmittance

Free-space quantum channels enable long-distance quantum communication in regimes where optical fiber transmission is impractical.
This includes very long distances where exponential fiber absorption losses prohibit fiber links, as well as communication between mobile platforms such as satellite-to-ground links and aircraft-based systems.
Optical radiation is the optimal carrier for quantum information in such scenarios because it preserves quantum states over long distances.
This enables a range of quantum communication protocols, including quantum key distribution, quantum teleportation, and entanglement swapping.
These capabilities are critical for global quantum network infrastructure and quantum internet architecture.

Quantum information is typically encoded in quasi-monochromatic optical pulses, which can be approximated as Gaussian beam modes.
However, atmospheric turbulence constitutes the dominant physical challenge.
Random refractive index fluctuations induce beam wander, wavefront distortion, scintillation, and beam spreading.
These effects depend nonlinearly on propagation distance, turbulence strength, and wavelength.
Subsequent measurements involve a finite optical system aperture, which truncates part of the distorted light profile.
This process is equivalent to a linear loss channel characterized by the transmittance $\eta$, defined as the fraction of beam power captured by the receiver aperture.
The single scalar $\eta$ encapsulates the complex three-dimensional propagation physics relevant for quantum state transmission.

Atmospheric turbulence is a stochastic process, making the channel transmittance a random variable.
The probability distribution of transmittance (PDT), fully characterizes the statistics of quasi-monochromatic pulse propagation through an atmospheric quantum channel.
This framework enables explicit input-output relations between the transmitted and received quantum states, forming the basis for protocol performance analysis.

Several analytical models for the PDT have been developed, but their range of validity remains unclear.
Although some models were validated by fitting, this approach lacks rigor and may represent parameters that are biased relative to actual atmospheric conditions.
Furthermore, some assumptions underlying these models have not yet been validated.

The existing framework describes an ensemble of independent single-beam propagation events.
In practice, the turbulence coherence time is on the order of milliseconds, so consecutive pulses propagate through correlated atmospheric conditions.
The probability distribution of transmittance cannot account for this temporal correlation.
Ignoring it discards the exploitable structure that could be used for protocol optimization and introduces vulnerabilities in quantum security protocols that assume independent channel realizations.

> ## 2. Development of a Numerical Framework
> Numerical simulations were performed using the open-source Python library `pyatmosphere`, developed as part of this work to implement ...

The description of atmospheric quantum channels involves finite spatial integration of the squared magnitude of a field governed by a stochastic partial differential equation.
This formulation hinders analytical progress and makes physical interpretation challenging.
Restrictive assumptions limit existing theory to specific limiting cases, leaving broader turbulence regimes beyond the reach of analytical characterization.
This creates a gap between theoretical description and characterization of transmittance statistics.

In this thesis, we employ numerical simulations to gain quantitative insight into the resulting transmittance statistics.
We employ the split step method for wave propagation in random media, which is widely used in classical optics and commonly referred to as the phase screen method.
A central limitation of this approach is undersampling of the low frequency part of the turbulence spectrum.
To overcome this limitation, we adopt the sparse spectrum method, which generates phase screens whose statistics match the prescribed theoretical spectrum.

With a proper choice of the number of phase screens and other simulation parameters, the sparse spectrum phase screen approach closes the gap between numerical simulation results and the underlying theoretical description.
Moreover, the ability to generate phase screens of arbitrary size with correct statistical properties enables the study of temporal evolution of atmospheric channels under Taylor frozen turbulence hypothesis.
The resulting framework enables a comprehensive analysis of free space optical channels and quantum properties of light propagating through the atmosphere.

> ## 3. Validation of Physical Assumptions

We analyze the probability distribution of transmittance obtained from numerical simulations for free space optical channels under weak, moderate, and strong turbulence regimes.
The numerical results are compared with several analytical models.
These include two physically motivated beam-shape based models, namely the beam wandering and elliptical beam models, the truncated lognormal model, and a hybrid approach the total probability model.
The agreement between empirical and analytical distributions is quantified using the Kolmogorov-Smirnov statistic.

The numerical distributions are generally unimodal and bell shaped.
In strong turbulence they become broader and flatter.
Since the transmittance is bounded between zero and one, this constraint strongly affects the distribution shape.
The aperture size relative to the average beam size is identified as the dominant control parameter.
For small apertures, transmittance values concentrate near zero, which enforces a positive skew.
For large apertures, the upper bound at unity induces negative skew.
Accurate prediction of the first moments of transmittance is therefore necessary for any analytical model to produce valid distributions.

Our findings reveal that the applicability of a model is predominantly influenced by the ratio of the aperture to the average beam size.
Consequently, the conventional model-selection heuristics based on turbulence strength are seen as inferior.
The truncated lognormal model, which always exhibits positive skew, provides a consistent description for small apertures across all turbulence regimes but its accuracy worsens for larger apertures.
The beam-shape based models mainly exhibit negative skew, which makes them more suitable for large aperture channels, where they provide an accurate match to the shape of the probability distribution of transmittance.
However, these models suffer from misspecification bias because they are parameterized through moments of beam shape variables instead of transmittance itself.
This leads to systematic shifts of the distribution mode and inaccurate estimation of the mean transmittance.
The total probability model, which combines these two approaches, captures the skewness transition induced by changes in the aperture size.
For small apertures, its performance closely follows that of the lognormal model, while for large apertures it yields some improvement in the predicting of the transmittance distribution.

To mitigate the misspecification bias, we introduce a transmittance matching technique that reformulates beam-shape based models in terms of the first moments of transmittance.
This method is applied to a model with an intermediate description between the beam wandering and elliptical beam models because of the complex, semi-analytical formulation of the latter.
Despite its simpler formulation compared to the elliptical beam model, it generally outperforms it across all turbulence regimes.

We also test key assumptions underlying physically based models.
The beam centroid is confirmed to follow a two dimensional normal distribution, but its statistical independence from beam shape deformations is violated, especially in strong turbulence.
In the elliptical beam model, the logarithms of the semi axes are assumed to follow a bivariate Gaussian distribution.
Numerical simulations instead reveal a strong suppression of probability density along the diagonal, which indicates that the two axes are rarely equal.
These findings will guide the future development of the beam-shape based models.

Finally, we propose an empirical model of PDT based on the Beta distribution.
Its bounded support naturally matches the physical range of transmittance and it reproduces the skewness transition with aperture size.
This model generally outperforms all other considered analytical models, and its simple analytical formulation makes it well-suited for theoretical predictions and practical application.

> ## 5. Analysis of Temporal Correlations

We extend the probability distribution of transmittance framework to account for temporal correlations in atmospheric quantum channels.
Existing models describe isolated pulses or pulses separated by times exceeding the atmospheric correlation time, whereas realistic systems operate with high repetition rates, so consecutive pulses propagate through correlated turbulence that imprints on the output quantum states.
These effects are not captured by single time PDT models.
We introduce a two time PDT that provides a complete statistical description of two consecutive pulses with arbitrary temporal separation.
Its properties are studied numerically under Taylor’s frozen turbulence hypothesis.

To quantify temporal correlations, we define the aperture averaged spatial coherence radius as the temporal separation at which the Pearson correlation coefficient of transmittance decays to $e^{-1}$.
The resulting characteristic scale of aperture averaged coherence radius corresponds to several centimeters of spatial coherence or several milliseconds of temporal coherence.

As in the case of single time PDT, the receiver aperture dominates the behavior of correlation properties.
The spatial coherence radius increases approximately linearly with aperture size over a practically relevant range.
This highlights the role of aperture size as an effective control parameter for engineering transmittance correlations in atmospheric quantum communication protocols.

> ## 6. Applications and Practical Significance

The practical relevance of the framework is demonstrated through its application to several quantum protocols under realistic atmospheric conditions.
We first analyze the preservation of continuous variable Gaussian entanglement between time separated pulses.
The Simon inseparability criterion is used to determine the entanglement survival.
We find that the threshold time for entanglement preservation is on the order of several milliseconds.
This threshold depends on the receiver aperture and is naturally expressed in terms of the spatial coherence radius, which increases monotonically with aperture size but in a nonlinear manner.

For discrete variable systems, we study the robustness of polarization entangled Bell states and parametric down conversion states.
The results show that atmospheric turbulence alone allows quantum correlations to persist for tens of milliseconds.
In practice, however, the achievable timescale is strongly limited by time dependent readout losses in quantum memory, which reduce the preservation time to a few milliseconds.
The persistence of quantum correlations over these timescales indicates that employing two or more time-separated quantum states can increase the effective dimensionality of the Hilbert space.

We further investigate adaptive real time selection protocols, in which bright classical pulses probe the channel transmittance prior to quantum transmission.
This approach enhances the preservation of nonclassical properties of amplitude squeezed states by exploiting the nonvanishing correlations between consecutive pulses.
Analyzing the Mandel parameter and its realistic counterpart for an array of on-off click detectors, we demonstrate an increase in the time over which nonclassicality is preserved, which extends across pulse separations of tens of milliseconds.
These results demonstrate that temporal correlations in atmospheric channels can be leveraged as a practical resource for optimizing free-space quantum communication protocols.

> - [ ] Final words, "Innovation and practical significance."

**Keywords:**
Free-space quantum channels,
Quantum communication,
Atmospheric turbulence,
Quantum optics,
Phase-screens numerical simulation,
Split-step with sparse spectrum method,
pyatmosphere (Python library),
Probability distribution of transmittance (PDT),
Transmittance matching method,
Circular beam model,
Two-time Probability Distribution of Transmittance (Two-time PDT),
Temporal correlations in free-space channels,
Time-bin encoding,
Spatial coherence radius,
CV and DV entanglement,
Adaptive selection protocols,
Nonclassicality preservation,
Quantum memory in atmosphere,
Strong fluctuation regime

> від 5 до 15.

> To .pdf metadata:
>Truncated lognormal model,
>Beam wandering model,
>Elliptical beam model,
>Total probability model,
>Beta distribution model,

>Target Research Community:
>- Information Theorists & Channel Modelers
>- Computational Physicists & Atmospheric Scientists
>- Pure Quantum Optics Researchers
>- Quantum Engineers & Experimentalists

**List of publications:**
1. Klen, M., & Semenov, A. A. (2023). Numerical simulations of atmospheric quantum channels. Physical Review A, 108(3). https://doi.org/10.1103/physreva.108.033718
2. Klen, M., Vasylyev, D., Vogel, W., & Semenov, A. A. (2024). Time correlations in atmospheric quantum channels. Physical Review A, 109(3). https://doi.org/10.1103/physreva.109.033712
3. Pechonkin, I., Klen, M., & Semenov, A. A. (2025). Circular-beam approximation for quantum channels in a turbulent atmosphere. Physical Review A, 112(6). https://doi.org/10.1103/pv7j-4zpf
4. Semenov, A., Klen, M., & Pechonkin, I. (2025). Quantum optics in the turbulent atmosphere: fundamental issues and applications. Quantum Technologies for Defence and Security II (p. 38). SPIE. https://doi.org/10.1117/12.3069599

>в яких опубліковані основні наукові результати дисертації;
які засвідчують апробацію матеріалів дисертації;
які додатково відображають наукові результати дисертації.

```{=latex}
\clearpage
```