import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import dataclasses
    import pyatmosphere as pyatm
    import matplotlib.pyplot as plt
    from pathlib import Path
    from scipy.stats import gaussian_kde
    from scipy.ndimage import gaussian_filter1d
    from scipy.interpolate import interp1d


    plt.style.use("klen.mplstyle")

    def get_hist(eta):
        kde = gaussian_kde(eta)
        x = np.linspace(min(eta), max(eta), 200)
        y = kde(x)
        return x, y


    def pdf_to_cdf(x, pdf, tol=1e-12):
        x = np.asarray(x)
        pdf = np.asarray(pdf)
        if x.ndim != 1 or pdf.ndim != 1 or x.size != pdf.size:
            raise ValueError("x and pdf must be 1D arrays of the same length")

        dx = np.diff(x)
        if not np.allclose(dx, dx[0]):
            dxs = np.diff(x, prepend=x[0])
        else:
            dxs = np.full_like(x, dx[0])

        support = np.where(pdf > tol)[0]
        if support.size == 0:
            raise ValueError("No nonzero PDF values found (under given tol)")
        i_min, i_max = support[0], support[-1]

        cdf = np.zeros_like(pdf)
        cdf[i_min:i_max+1] = np.cumsum(pdf[i_min:i_max+1] * dxs[i_min:i_max+1])

        cdf[:i_min] = 0.0
        cdf[i_max+1:] = 1.0
        return cdf
    return (
        Path,
        dataclasses,
        gaussian_filter1d,
        gaussian_kde,
        interp1d,
        mo,
        np,
        pd,
        plt,
    )


@app.cell
def _():
    FIGSIZE_SOLO = (150/25.4 /5*4, 80/25.4)
    FIGSIZE_DOUBLE = (150/25.4, 80/25.4)
    return FIGSIZE_DOUBLE, FIGSIZE_SOLO


@app.cell(hide_code=True)
def _():
    from dataclasses import dataclass
    from typing import Optional


    @dataclass
    class PlotParams:
        name: Optional[str] = None
        label: Optional[str] = None
        color: str = "k"
        linestyle: str = "-"
        clip_tails: float = 0.02
        smooth: float = 0
        ks_smooth: float = 0
        label_pos: int = 0
        label_dx: float = 0
        label_dy: float = 0
        zorder: int = 0


    @dataclass
    class NumericalPlotParams(PlotParams):
        name: str = "numerical"
        label: Optional[str] = "N"
        zorder: int = 8


    @dataclass
    class TrackedNumericalPlotParams(PlotParams):
        name: str = "tracked_numerical"
        label: Optional[str] = "R"
        color: str = "#555555"
        linestyle: str = "-."
        zorder: int = 7


    @dataclass
    class LognormalPlotParams(PlotParams):
        name: str = "lognormal"
        label: Optional[str] = "L"
        color: str = "#e53935"
        zorder: int = 4


    @dataclass
    class BeamWanderingPlotParams(PlotParams):
        name: str = "beam_wandering"
        label: Optional[str] = "W"
        color: str = "#21a9ca"
        zorder: int = 1


    @dataclass
    class EllipticalBeamPlotParams(PlotParams):
        name: str = "elliptical_beam"
        label: Optional[str] = "E"
        color: str = "#d81b60"
        zorder: int = 2


    @dataclass
    class TotalProbabilityPlotParams(PlotParams):
        name: str = "total_probability"
        label: Optional[str] = "T"
        color: str = "#e28544"
        zorder: int = 3

    @dataclass
    class BetaPlotParams(PlotParams):
        name: str = "beta"
        label: Optional[str] = "B"
        color: str = "#3949ab"
        zorder: int = 6

    @dataclass
    class BetaTotalProbabilityPlotParams(PlotParams):
        name: str = "beta_total_probability"
        label: Optional[str] = "$\\mathsf{T_B}$"
        color: str = "#00897b"
        zorder: int = 5


    @dataclass
    class NumTotalProbabilityPlotParams(PlotParams):
        name: str = "num_total_probability"
        label: Optional[str] = "$\\mathsf{T_L}$"
        color: str = "#e28544"
        linestyle: str = "--"
        zorder: int = 3

    @dataclass
    class NumBetaTotalProbabilityPlotParams(PlotParams):
        name: str = "num_beta_total_probability"
        label: Optional[str] = "$\\mathsf{T_B}$"
        color: str = "#00897b"
        linestyle: str = "--"
        zorder: int = 5

    @dataclass
    class NumEllipticalBeamPlotParams(PlotParams):
        name: str = "num_elliptical_beam"
        label: Optional[str] = "E"
        color: str = "#d81b60"
        linestyle: str = "--"
        zorder: int = 3

    @dataclass
    class MMPlotParams(PlotParams):
        name: str = "anchored_circular_beam"
        label: Optional[str] = "C"
        linestyle: str = "--"
        color: str = "#000"
        zorder: int = 1

    @dataclass
    class AnchoredBeamWanderingPlotParams(PlotParams):
        name: str = "anchored_beam_wandering"
        label: Optional[str] = "A"
        linestyle: str = "--"
        color: str = "#21a9ca"
        zorder: int = 1
    return (
        BeamWanderingPlotParams,
        BetaPlotParams,
        EllipticalBeamPlotParams,
        MMPlotParams,
        NumericalPlotParams,
        TotalProbabilityPlotParams,
    )


@app.cell(hide_code=True)
def _(
    NumericalPlotParams,
    Path,
    dataclasses,
    gaussian_filter1d,
    interp1d,
    np,
    pd,
):
    def get_available_models(channel_name):
        channel_path = Path("/home/klen/syncthing/desktop/physics/circular_beam/03_validation/article1_sup/04_src/02-analysis/results")  / channel_name
        return [loc.name for loc in channel_path.iterdir() if loc.is_dir()]

    CIRCLE_LABEL_SIZE = 100
    CIRCLE_LABEL_TEXTSIZE = 8

    def plot_pdt(ax, channel_name, aperture_radius, models):
        available_models = get_available_models(channel_name)
        channel_path = Path("/home/klen/syncthing/desktop/physics/circular_beam/03_validation/article1_sup/04_src/02-analysis/results")  / channel_name
        file_name = str(aperture_radius).replace('.', '_') + '.csv'
        for model in models:
            model = dataclasses.asdict(model)
            if model['name'] not in available_models:
                print("ERROR: '%s' model for the '%s' channel not found" %
                      (model['name'], channel_name))
                continue
            df = pd.read_csv(channel_path / model['name'] / file_name)

            # Smooth data
            if model['smooth'] != 0:
                df['probability_density'] = gaussian_filter1d(
                    df['probability_density'], model['smooth'])

            # Clip tails
            tails_mask = df['probability_density'] > model['clip_tails']
            eta_axis = df['transmittance'][tails_mask].tolist()
            data = df['probability_density'][tails_mask].tolist()
            if model['name'] == 'beam_wandering':
                eta_axis = list(eta_axis) + [eta_axis[-1]]
                data = list(data) + [0]

            ax.plot(eta_axis, data, label=model['name'], c=model['color'],
                    ls=model['linestyle'], zorder=model['zorder'])

            # Circle labels
            if model['label'] and model['label_pos']:
                color = model['color']
                # label_pos = model.get('label_pos', np.random.randint(0, len(eta_axis)))
                label_x = df['transmittance'][model['label_pos']]
                label_y = df['probability_density'][model['label_pos']]
                ax.scatter([label_x], [label_y], s=CIRCLE_LABEL_SIZE,
                           marker="o", zorder=10, clip_on=False, linewidth=1.2,
                           edgecolor=color, facecolor="white")
                ax.text(label_x + model['label_dx'],
                        0.99 * label_y + model['label_dy'], model['label'],
                        zorder=20, color=color, ha="center", va="center",
                        size=CIRCLE_LABEL_TEXTSIZE, clip_on=False, weight='bold',
                        fontfamily='sans-serif')

        ax.grid(which='major', color='#BBBBBB', linestyle='--')
        ax.set_ylabel("Probability distribution")
        ax.set_xlabel("Transmittance $\\eta$")
        plot_file_name = (channel_name + '_pdt_' +
                          str(aperture_radius).replace('.', '_'))
        return plot_file_name


    def plot_ks_values(ax, channel_name, models, apertures=None):
        models = [m for m in models if not isinstance(m, NumericalPlotParams)]
        available_models = get_available_models(channel_name)
        # if any(isinstance(m, MMPlotParams) for m in models):        
        channel_path = Path("/home/klen/syncthing/desktop/physics/circular_beam/03_validation/article1_sup/04_src/02-analysis/results") / channel_name
        # else:
            # channel_path = Path("/mnt/hdd/documents/to_clean/oldphys/article1/dev/02-analysis/results") / channel_name
        ks_values_df = pd.read_csv(channel_path / 'ks_values.csv')
        beam_df = pd.read_csv(channel_path / 'beam_params.csv')
        lt2 = beam_df['lt2'][0]

        for model in models:
            model = dataclasses.asdict(model)
            if model['name'] not in available_models:
                print("ERROR: '%s' model for the '%s' channel not found" %
                      (model['name'], channel_name))
                continue

            _normed_x = (ks_values_df['aperture_radius'] / np.sqrt(lt2)).tolist()

            # Smooth data
            if model['ks_smooth'] != 0:
                normed_x = np.linspace(min(_normed_x), max(_normed_x), 200)
                func = interp1d(_normed_x, ks_values_df[model['name']])
                data = gaussian_filter1d(func(normed_x), model['ks_smooth'])
            else:
                data = ks_values_df[model['name']]
                normed_x = _normed_x

            data[data > 1] = 1
            data = data.tolist()
            ax.plot(normed_x, data, label=model['name'], c=model['color'],
                    ls=model['linestyle'], zorder=model['zorder'])

            # Circle labels
            if model['label']:
                # label_pos = model.get('label_pos', np.random.randint(0, len(normed_x)))
                label_x = _normed_x[model['label_pos']]
                label_y = ks_values_df[model['name']][model['label_pos']]
                ax.scatter([label_x], [label_y], s=CIRCLE_LABEL_SIZE,
                           marker="o", zorder=10, clip_on=False, linewidth=1.2,
                           edgecolor=model['color'], facecolor="white")
                ax.text(label_x + model['label_dx'],
                        0.985 * label_y + model['label_dy'], model['label'],
                        zorder=20, color=model['color'], ha="center", va="center",
                        size=CIRCLE_LABEL_TEXTSIZE,clip_on=False, weight='bold',
                        fontfamily='sans-serif')

        if apertures is not None:
            for a in apertures:
                ax.axvline(a / np.sqrt(lt2), zorder=-5, lw=1, c='k')

        secax = ax.secondary_xaxis(
            1, functions=(lambda x: x * np.sqrt(lt2) * 100, lambda r: r)
        )
        secax.set_xlabel("Aperture radius $R_{{\\mathrm{{ap}}}}$ (cm)", labelpad=4)
        ax.grid(which='major', color='#BBBBBB', linestyle='-')
        ax.set_yscale('log')
        ax.set_ylabel("KS statistic $D_M$")
        ax.set_xlabel("Normalized aperture radius "
                      "$R_{{\\mathrm{{ap}}}} / W_{{\\mathrm{{LT}}}}$", labelpad=3)
        ax.set_xlim(left=0, right=ax.get_xlim()[1] * 0.98)
        ax.set_xticks(np.arange(0, ax.get_xlim()[1], 0.25))
    return plot_ks_values, plot_pdt


@app.cell
def _():
    aperture_weak_inf = 0.0045
    return (aperture_weak_inf,)


@app.cell
def _(
    BeamWanderingPlotParams,
    BetaPlotParams,
    EllipticalBeamPlotParams,
    FIGSIZE_SOLO,
    MMPlotParams,
    NumericalPlotParams,
    aperture_weak_inf,
    mo,
    plot_pdt,
    plt,
):
    def _():
        models = [
            NumericalPlotParams(smooth=1.8, label_pos=101, label_dy=0.04, label_dx=0.001),
            BeamWanderingPlotParams(label_pos=68),
            # LognormalPlotParams(ks_smooth=1, label_pos=152, label_dy=0.04),
            BetaPlotParams(ks_smooth=1, label_pos=70, label_dy=0.005, label_dx=0.001),
            EllipticalBeamPlotParams(smooth=2.5, ks_smooth=4, label_pos=78, label_dy=0.025),
            MMPlotParams(smooth=2.5, ks_smooth=4, label_pos=103, label_dy=0.025),
            # NumEllipticalBeamPlotParams(smooth=2.5, ks_smooth=4, label_pos=125, label_dy=0.025),
            # TotalProbabilityPlotParams(label_pos=150),
            # BetaTotalProbabilityPlotParams(label_pos=161),
        ]

        _f, _ax = plt.subplots(1, 1, figsize=FIGSIZE_SOLO)
        _name = plot_pdt(_ax, 'weak_zap', aperture_radius=aperture_weak_inf, models=models)
        _ax.set_ylim(0, 18)
        _ax.set_xlim(0.02, 0.3)
        _f.tight_layout()
        _f.savefig(f'tmp/MM_{_name}.pdf', bbox_inches='tight', pad_inches=1/50)
        return _f

    mo.hstack([_(), "", ""], widths=[2,2,1])
    return


@app.cell
def _(
    BeamWanderingPlotParams,
    BetaPlotParams,
    EllipticalBeamPlotParams,
    FIGSIZE_DOUBLE,
    MMPlotParams,
    TotalProbabilityPlotParams,
    aperture_weak_inf,
    mo,
    plot_ks_values,
    plt,
):
    def _():
        _f, _ax = plt.subplots(1, 2, figsize=FIGSIZE_DOUBLE, constrained_layout=True)
        models=[
            # LognormalPlotParams(label_pos=21),
            BeamWanderingPlotParams(label_pos=17, ks_smooth=4.5),
            BetaPlotParams(label_pos=11, label_dx=0.003, ks_smooth=4),
            EllipticalBeamPlotParams(label_pos=23, ks_smooth=4),
            TotalProbabilityPlotParams(label_pos=17, ks_smooth=1),
            MMPlotParams(label_pos=13, ks_smooth=3.3),
            # AnchoredBeamWanderingPlotParams(label_pos=14),
            # BetaTotalProbabilityPlotParams(label_pos=16, ks_smooth=5),
            # NumEllipticalBeamPlotParams(label_pos=30, ks_smooth=1),
            # NumTotalProbabilityPlotParams(label_pos=26, ks_smooth=4),
            # NumBetaTotalProbabilityPlotParams(label_pos=34, ks_smooth=4),
            ]
        filename = plot_ks_values(ax=_ax[0], channel_name='weak_zap', models=models, apertures=[aperture_weak_inf])
        _ax[0].set_ylim(7e-3, 1)
        _ax[0].set_xlim(0.03, 1.5)
        _ax[0].set_xlabel("Normalized aperture radius "
                      "$R_{{\\mathrm{{ap}}}} / W_{{\\mathrm{{LT}}}}$", labelpad=3, fontsize=12)

        models=[
            # LognormalPlotParams(label_pos=21),
            # LognormalPlotParams(label_pos=25),
            BeamWanderingPlotParams(label_pos=14, ks_smooth=4.5),
            BetaPlotParams(label_pos=11, label_dx=0.003, ks_smooth=4),
            EllipticalBeamPlotParams(label_pos=18, ks_smooth=4),
            # TotalProbabilityPlotParams(label_pos=16, ks_smooth=1),
            MMPlotParams(label_pos=13, ks_smooth=3.3),
            # AnchoredBeamWanderingPlotParams(label_pos=14),
            # BetaTotalProbabilityPlotParams(label_pos=16, ks_smooth=5),
            # NumEllipticalBeamPlotParams(label_pos=30, ks_smooth=1),
            # NumTotalProbabilityPlotParams(label_pos=26, ks_smooth=4),
            # NumBetaTotalProbabilityPlotParams(label_pos=34, ks_smooth=4),
            ]
        filename = plot_ks_values(ax=_ax[1], channel_name='strong_inf', models=models, apertures=[aperture_weak_inf])
        _ax[1].set_ylim(7e-3, 1)
        _ax[1].set_xlim(0.03, 1.2)
        _ax[1].set_ylabel(None)
        _ax[1].set_xlabel("Normalized aperture radius "
                      "$R_{{\\mathrm{{ap}}}} / W_{{\\mathrm{{LT}}}}$", labelpad=3, fontsize=12)


        # _f.tight_layout()
        _f.savefig(f'tmp/MM_ks_values.pdf', bbox_inches='tight', pad_inches=1/25.4)
        return _f

    mo.hstack([_(), "", ""], widths=[2,2,1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # S distribution
    """)
    return


@app.cell
def _(FIGSIZE_SOLO, gaussian_kde, np, pd, plt):
    import scipy
    from klen.v1 import mymath

    moderate_zap = pd.read_csv('/home/klen/syncthing/desktop/physics/circular_beam/01_analytical_model/01_w2_disribution/data/moderate_zap_beam.csv')
    def fit_lognormal(data):
        data = np.asarray(data)
        x_mean = data.mean()
        x2_mean = (data**2).mean()
        mu = np.log(x_mean**2 / np.sqrt(x2_mean))
        s2 = np.log(x2_mean / x_mean**2)
        return scipy.stats.lognorm(s=np.sqrt(s2), scale=np.exp(mu)), mu, s2

    def plot_lognorm_fit(ax, data, title):
        dx2_mean = 4 * (data['mean_x2'] - data['mean_x']**2)
        # ax.set_title(title)
        ax.set_xlabel(r"Squared beam-spot radius $S$ [cm$^2$]")


        kde = gaussian_kde(dx2_mean)
        x = np.linspace(min(dx2_mean), max(dx2_mean), 200)
        y = kde(x)
        ax.fill_between(x * 10000, 0, y, label='Simulated data', color='#00baf7')

        # ax.hist(dx2_mean, bins=100, density=True);
        # _x = np.linspace(*ax.get_xlim(), 100)
        log_model, mu, s2 = fit_lognormal(dx2_mean)
        sbw = (data['mean_x']**2).mean()
        ax.plot(x * 10000, log_model.pdf(x), c='k', ls='--')
        print(mu, s2)
        ax.annotate(f'$\mu={mymath.round(mu, 2)}$\n$\sigma^2={mymath.round(s2, 2)}$', xy=(0.7, 0.65), xycoords='axes fraction')
        # ax.annotate(f'$\sigma^2_{{BW}}={mymath.round(sbw, 2)}$', xy=(0.6, 0.25), xycoords='axes fraction')
        # ax.annotate(f'$\mu={mu}$ $\sigma^2={s2}$', xy=(0.5, 0.9), xycoords='axes fraction')
        return ax

    _f, _ax = plt.subplots(1, 1, figsize=FIGSIZE_SOLO)
    plot_lognorm_fit(_ax, moderate_zap, "Moderate_zap")
    _ax.set_ylabel('Probability density')
    plt.tight_layout()
    _f.savefig(f'tmp/MM_Spdf.pdf', bbox_inches='tight', pad_inches=1/50)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Presentation
    """)
    return


@app.cell(hide_code=True)
def _(
    BeamWanderingPlotParams,
    EllipticalBeamPlotParams,
    FIGSIZE_SOLO,
    NumericalPlotParams,
    mo,
    plot_pdt,
    plt,
):
    def _():
        models = [
            NumericalPlotParams(smooth=1.8, label_pos=178, label_dy=-0.04, label_dx=0.00),
            BeamWanderingPlotParams(label_pos=145),
            # LognormalPlotParams(ks_smooth=1, label_pos=152, label_dy=0.04),
            # BetaPlotParams(ks_smooth=1, label_pos=70, label_dy=0.005, label_dx=0.001),
            EllipticalBeamPlotParams(smooth=2.5, ks_smooth=4, label_pos=160, label_dy=0.025),
            # MMPlotParams(smooth=2.5, ks_smooth=4, label_pos=103, label_dy=0.025),
            # NumEllipticalBeamPlotParams(smooth=2.5, ks_smooth=4, label_pos=125, label_dy=0.025),
            # TotalProbabilityPlotParams(label_pos=150),
            # BetaTotalProbabilityPlotParams(label_pos=161),
        ]

        _f, _ax = plt.subplots(1, 1, figsize=FIGSIZE_SOLO)
        _name = plot_pdt(_ax, 'weak_zap', aperture_radius=0.015, models=models)
        _ax.set_ylim(0, 11)
        _ax.set_xlim(0.5, 1)
        _f.tight_layout()
        _f.savefig(f'tmp/pres_MM_{_name}.png', bbox_inches='tight', pad_inches=1/50, dpi=400)
        return _f

    mo.hstack([_(), "", ""], widths=[2,2,1])
    return


@app.cell
def _(
    BeamWanderingPlotParams,
    EllipticalBeamPlotParams,
    FIGSIZE_SOLO,
    NumericalPlotParams,
    mo,
    plot_pdt,
    plt,
):
    def _():
        models = [
            NumericalPlotParams(smooth=1.8, label_pos=178, label_dy=-0.04, label_dx=0.00),
            BeamWanderingPlotParams(label_pos=183),
            # LognormalPlotParams(ks_smooth=1, label_pos=152, label_dy=0.04),
            # BetaPlotParams(ks_smooth=1, label_pos=70, label_dy=0.005, label_dx=0.001),
            EllipticalBeamPlotParams(smooth=2.5, ks_smooth=4, label_pos=182, label_dy=0.025),
            # MMPlotParams(smooth=2.5, ks_smooth=4, label_pos=103, label_dy=0.025),
            # NumEllipticalBeamPlotParams(smooth=2.5, ks_smooth=4, label_pos=125, label_dy=0.025),
            # TotalProbabilityPlotParams(label_pos=150),
            # BetaTotalProbabilityPlotParams(label_pos=161),
        ]

        _f, _ax = plt.subplots(1, 1, figsize=FIGSIZE_SOLO)
        _name = plot_pdt(_ax, 'weak_zap', aperture_radius=0.021, models=models)
        _ax.set_ylim(0, 38)
        _ax.set_xlim(0.88, 1)
        _f.tight_layout()
        _f.savefig(f'tmp/pres_MM_{_name}.png', bbox_inches='tight', pad_inches=1/50, dpi=400)
        return _f

    mo.hstack([_(), "", ""], widths=[2,2,1])
    return


if __name__ == "__main__":
    app.run()
