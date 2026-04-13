# Анотація {#sec:annotation_ua .unnumbered}
**Клен М.Д.** Статистичні моделі та часова когерентність квантового світла в турбулентній атмосфері.*---Квалiфiкацiйна наукова праця на правах рукопису.*
*Дисертацiя на здобуття наукового степеня доктора фiлософiї за спецiальнiстю 01.04.02 "Теоретична фiзика" (104--Фiзика та астрономiя).---Iнститут теоретичної фiзики iм. М.М. Боголюбова Нацiональної академiї наук України, Київ, 2026.*

Квантові канали у вільному просторі забезпечують квантовий зв'язок на великі відстані в умовах, коли передача по оптичному волокну є недоцільною.
Це охоплює значні дистанції, де експоненціальні втрати на поглинання в оптичному волокні унеможливлюють його використання, а також зв'язок між мобільними платформами, такими як супутниково-наземні канали та авіаційні системи.
Оптичне випромінювання є оптимальним носієм квантової інформації в таких сценаріях, оскільки воно зберігає квантові стани на великих відстанях.
Це дозволяє реалізувати низку протоколів квантового зв'язку, включаючи квантовий розподіл ключів, квантову телепортацію та обмін квантовою заплутаністю.
Ці можливості мають вирішальне значення для глобальної інфраструктури квантових мереж та архітектури квантового інтернету.

В низці розповзюджених застосувань, квантова інформація кодується в квазімонохроматичних оптичних імпульсах, які можна апроксимувати як гаусові моди світла.
При цьому, атмосферна турбулентність становить одну з основних фізичних проблем.
Випадкові коливання показника заломлення викликають блукання променя, спотворення хвильового фронту, сцинтиляцію та розширення променя.
Ці ефекти нелінійно залежать від відстані поширення, інтенсивності турбулентності та довжини хвилі.
Подальші вимірювання передбачають використання оптичної системи з скінченною апертурою, яка обрізає частину спотвореного профілю світла.
Цей процес еквівалентний лінійному каналу з втратами, що характеризується ефективністю проходження $\eta$, яка визначається як частка інтенсивності променя, що уловлюється апертурою приймача.
У протоколах, що розглядається, одна величина $\eta$ узагальнює складну тривимірну фізику поширення, що має значення для передачі квантового стану.

Атмосферна турбулентність є стохастичним процесом, що робить ефективність проходження каналу випадковою величиною.
Розподіл імовірностей ефективності проходження (РІЕП) повністю характеризує статистику поширення квазімонохроматичного імпульсу через атмосферний квантовий канал.
Ця концепція дозволяє встановити чіткі співвідношення між вхідними та вихідними даними для переданих і отриманих квантових станів, що є основою для аналізу ефективності протоколу.

Було розроблено кілька аналітичних моделей для РІЕП, але межі їхньої застосовності залишаються нез'ясованими.
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
Метод фазових екранів,
Розподіл імовірностей ефективності проходження (РІЕП),
Метод узгодження ефективності проходження,
Модель кругового променя,
Двочасовий розподіл імовірностей ефективності проходження (Двочасовий РІЕП),
Часові кореляції в каналах у вільному просторі,
Часове кодування,
Просторовий радіус когерентності,
Квантова заплутаність,
Протоколи адаптивного вибору,
Збереження некласичності,
Квантова пам'ять в атмосфері,
Режим сильної турбулетності.

**Cписок публiкацiй:**
1. M. Klen and A. A. Semenov, "Numerical simulations of atmospheric quantum channels", Phys. Rev. A 108, 033718 (2023).
2. M. Klen, D. Vasylyev, W. Vogel, and A. A. Semenov, "Time correlations in atmospheric quantum channels", Phys. Rev. A 109, 033712 (2024).
3. I. Pechonkin, M. Klen, and A. A. Semenov, "Circular-beam approximation for quantum channels in a turbulent atmosphere", Phys. Rev. A 112, 063716 (2025).
4. A. Semenov, M. Klen, and I. Pechonkin, "Quantum Optics in the Turbulent Atmosphere: Fundamental Issues and Applications", in Quantum Technologies for Defence and Security II, edited by V. Fernandez, G. Sorelli, and S. Schwartz (p. 38). Proceedings of SPIE 13676, 136760H-13 (2025).

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

The impact of turbulence on the quantum state encoded in a quasi-monochromatic light mode can be described by a single random variable---transmittance---defined as the ratio of the intensity captured by the receiving aperture to the total beam intensity.
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
Consequently, the proposed empirical Beta-distribution model emerges as the superior choice for practical implementation, providing a closed-form analytical expression parameterized by only two moments.
This capability is particularly vital for quantum protocol analysis, where current methods often rely on constant-transmittance approximations that systematically ignore the random nature of atmospheric channels and introduce significant estimation errors.
Utilizing the Beta-distribution model directly addresses this limitation, effectively eliminating potential loopholes in performance analysis by  demonstrating robust validity across the majority of parameter regimes.

Ultimately, the analyzed resilience of quantum correlations over practical temporal windows renders time-bin encoding strategies feasible for free-space quantum networking. 
However, the practical realization of discrete variable entanglement protocols remains constrained by quantum memory efficiency. 
This highlights that while atmospheric channels support practical timescales, unlocking their full potential requires addressing storage limitations inherent in current quantum hardware.

**Keywords:**
Free-space quantum channels,
Probability distribution of transmittance (PDT),
Temporal correlations in free-space channels,
Time-bin encoding,
Two-time PDT,
Spatial coherence radius,
Transmittance-moment matching,
Atmospheric turbulence,
Sparse-spectrum phase-screen method
Strong fluctuation regime
Quantum entanglement,
Adaptive selection protocols,
Nonclassicality preservation

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
    \item\label{mypaper4} A. Semenov, M. Klen, and I. Pechonkin, "Quantum Optics in the Turbulent Atmosphere: Fundamental Issues and Applications", in Quantum Technologies for Defence and Security II, edited by V. Fernandez, G. Sorelli, and S. Schwartz (p. 38). Proceedings of SPIE 13676, 136760H-13 (2025). \textbf{(Q1)}
\end{enumerate}
```


>в яких опубліковані основні наукові результати дисертації;
які засвідчують апробацію матеріалів дисертації;
які додатково відображають наукові результати дисертації.

```{=latex}
\clearpage
```