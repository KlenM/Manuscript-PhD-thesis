import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import dataclasses
    import sys
    import pyatmosphere as pyatm
    import matplotlib.pyplot as plt
    from pathlib import Path
    from scipy.stats import gaussian_kde
    from scipy.ndimage import gaussian_filter1d
    from scipy.interpolate import interp1d

    ARTICLE1_PATH = "/mnt/hdd/documents/to_clean/oldphys/article1/dev/04-details/"
    if ARTICLE1_PATH not in sys.path:
        sys.path.append(ARTICLE1_PATH)


    plt.style.use("../klen.mplstyle")



    def get_hist(eta):
        kde = gaussian_kde(eta)
        x = np.linspace(min(eta), max(eta), 200)
        y = kde(x)
        return x, y


    return (
        Path,
        dataclasses,
        gaussian_filter1d,
        get_hist,
        interp1d,
        mo,
        np,
        pd,
        plt,
    )


@app.cell
def _():
    import json
    from lib import beam_centroid, r0_w, r0_eta, semiaxis
    import config
    from lib import data
    from scipy.stats import norm, skew, kurtosis


    CHANNELS = ['weak_inf', 'weak_zap', 'moderate_inf', 'moderate_zap', 'strong_inf']
    return CHANNELS, beam_centroid, config, data, norm


@app.cell
def _():
    FIGSIZE_SOLO = (150/25.4 /5*4, 80/25.4)
    FIGSIZE_DOUBLE = (150/25.4, 80/25.4)
    return FIGSIZE_DOUBLE, FIGSIZE_SOLO


@app.cell
def _(Path, config):
    config.DATA_PATH = Path('/mnt/hdd/documents/to_clean/oldphys/article1/dev/01-simulation/data')
    config.RESULTS_PATH = Path('/mnt/hdd/documents/to_clean/oldphys/article1/dev/02-analysis/results')
    config.PLOTS_PATH = Path('./plots')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Beam centroid""")
    return


@app.cell
def _(data, get_hist, norm, np):
    def beam_centroid_distribution_plot(ax, channel_name):
        x_axis, numerical = get_hist(data.x_0(channel_name))
        analytical = norm(loc=0, scale=np.sqrt(data.bw2(channel_name)))
        ax.fill_between(x_axis, 0, numerical, label='Simulated data', color='#00baf7')
        ax.plot(x_axis, analytical.pdf(x_axis), lw=1.4, ls=(4, (8, 3)), color='black',
                alpha=0.95, label=r'Normal distribution $N(0, W_{BW}^2$)')
        ax.set_xlabel("Beam-centroid\ncoordinate $x_0$ (m)")
        ax.set_ylabel("Probability density")
        ax.grid(which='major', color='#BBBBBB', linestyle='--')
        return ax
    return (beam_centroid_distribution_plot,)


@app.cell
def _(FIGSIZE_DOUBLE, beam_centroid_distribution_plot, plt):
    _f, _ax = plt.subplots(1, 2, figsize=FIGSIZE_DOUBLE)
    beam_centroid_distribution_plot(_ax[0], 'weak_inf')
    beam_centroid_distribution_plot(_ax[1], 'weak_zap')

    _f.tight_layout()
    _f.savefig(f'plots/bw_weak_inf_zap.svg', bbox_inches='tight', pad_inches=1/50)
    plt.show()
    return


@app.cell
def _(FIGSIZE_DOUBLE, beam_centroid_distribution_plot, plt):
    _f, _ax = plt.subplots(1, 2, figsize=FIGSIZE_DOUBLE)
    beam_centroid_distribution_plot(_ax[0], 'moderate_inf')
    beam_centroid_distribution_plot(_ax[1], 'moderate_zap')

    _f.tight_layout()
    _f.savefig(f'plots/bw_moderate_inf_zap.svg', bbox_inches='tight', pad_inches=1/50)
    plt.show()
    return


@app.cell
def _(FIGSIZE_SOLO, beam_centroid_distribution_plot, plt):
    _f, _ax = plt.subplots(1, 1, figsize=FIGSIZE_SOLO)
    beam_centroid_distribution_plot(_ax, 'strong_inf')

    _f.tight_layout()
    _f.savefig(f'plots/bw_strong_inf.svg', bbox_inches='tight', pad_inches=1/50)
    plt.show()
    return


@app.cell(hide_code=True)
def _(CHANNELS, beam_centroid):
    def generate_latex_tables(data):
        tables = {
            "weak": [
                f'weak\_inf & {data["weak_inf"]["skew"]:.3f} \\\\' if "weak_inf" in data else None,
                f'weak\_inf & {data["weak_inf"]["kurtosis"]:.3f} \\\\' if "weak_inf" in data else None,
                f'weak\_zap & {data["weak_zap"]["skew"]:.3f} \\\\' if "weak_zap" in data else None,
                f'weak\_zap & {data["weak_zap"]["kurtosis"]:.3f} \\\\' if "weak_zap" in data else None
            ],
            "moderate": [
                f'moderate\_inf & {data["moderate_inf"]["skew"]:.3f} \\\\' if "moderate_inf" in data else None,
                f'moderate\_inf & {data["moderate_inf"]["kurtosis"]:.3f} \\\\' if "moderate_inf" in data else None,
                f'moderate\_zap & {data["moderate_zap"]["skew"]:.3f} \\\\' if "moderate_zap" in data else None,
                f'moderate\_zap & {data["moderate_zap"]["kurtosis"]:.3f} \\\\' if "moderate_zap" in data else None
            ],
            "strong": [
                f'strong\_inf & {data["strong_inf"]["skew"]:.3f} \\\\' if "strong_inf" in data else None,
                f'strong\_inf & {data["strong_inf"]["kurtosis"]:.3f} \\\\' if "strong_inf" in data else None
            ]
        }

        # Generate and print each table
        for channel, rows in tables.items():
            print(f"\\begin{{table}}")
            print(f"\\centering")
            print(f"\\caption{{{channel} Channel Statistics}}")
            print(r"\\begin{tabular}{ll}")
            print(r"\\textbf{Channel} & \\textbf{Value} \\\\")
            print(r"\\hline")
            for row in rows:
                if row is not None:
                    print(row)
            print(r"\\end{tabular}")
            print(r"\\end{table}")
            print()


    def generate_markdown_tables(data):
        channels = ["weak", "moderate", "strong"]
        output = []
    
        for channel in channels:
            output.append("| Channel | Skew | Kurtosis |")
            output.append("|:---|:---:|:---:|")
        
            for measure, stats in data.items():
                if measure.startswith(channel + '_'):
                    output.append(f"| {measure} | {stats['skew']:.3f} | {stats['kurtosis']:.3f} |")
        
            output.append("")
    
        return '\n'.join(output)

    _data = {channel_name: beam_centroid.cumulants(channel_name)
               for channel_name in CHANNELS}
    _md_bw = generate_markdown_tables(_data)
    with open('plots/bw.md', 'w') as f:
        f.write(_md_bw)
    print(_md_bw)
    return


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
        label: Optional[str] = "$\\mathsf{T_L}$"
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
    return (
        BeamWanderingPlotParams,
        BetaPlotParams,
        BetaTotalProbabilityPlotParams,
        EllipticalBeamPlotParams,
        LognormalPlotParams,
        NumericalPlotParams,
        TotalProbabilityPlotParams,
    )


@app.cell(hide_code=True)
def _(mo):
    channel_dropdown = mo.ui.dropdown(label='Channel: ', value='weak_inf', options=['weak_inf', 'weak_zap', 'moderate_inf', 'moderate_zap', 'strong_inf'])
    return (channel_dropdown,)


@app.cell(hide_code=True)
def _(Path, channel_dropdown, pd):
    FILE = f"/mnt/hdd/documents/to_clean/oldphys/article1/dev/01-simulation/data/{channel_dropdown.value}/transmittance.csv"
    MODELS_PATH = Path("/mnt/hdd/documents/to_clean/oldphys/article1/dev/02-analysis/results") / channel_dropdown.value

    df = pd.read_csv(FILE)
    return (df,)


@app.cell(hide_code=True)
def _(df, mo):
    aperture_index = mo.ui.slider(0, len(df.columns) - 1, value=10, label='Aperture radius ', show_value=True)
    return (aperture_index,)


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
        channel_path = Path("/mnt/hdd/documents/to_clean/oldphys/article1/dev/02-analysis/results")  / channel_name
        return [loc.name for loc in channel_path.iterdir() if loc.is_dir()]

    CIRCLE_LABEL_SIZE = 100
    CIRCLE_LABEL_TEXTSIZE = 8

    def plot_pdt(ax, channel_name, aperture_radius, models):
        available_models = get_available_models(channel_name)
        channel_path = Path("/mnt/hdd/documents/to_clean/oldphys/article1/dev/02-analysis/results")  / channel_name
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
        channel_path = Path("/mnt/hdd/documents/to_clean/oldphys/article1/dev/02-analysis/results") / channel_name
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
def _(plt):
    plt.rcParams['lines.linewidth'] = 1.4
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Online channel""")
    return


@app.cell(hide_code=True)
def _(aperture_index, channel_dropdown, df, mo):
    aperture = df.columns[aperture_index.value]
    aperture_file = aperture.replace('.', '_')
    aperture = float(aperture)
    channel_dropdown,\
    mo.hstack([aperture_index, mo.md(rf'$R_\mathbf{{A}}={aperture}$ m')], justify='start')
    return (aperture,)


@app.cell
def _(
    BeamWanderingPlotParams,
    BetaPlotParams,
    BetaTotalProbabilityPlotParams,
    EllipticalBeamPlotParams,
    LognormalPlotParams,
    NumericalPlotParams,
    TotalProbabilityPlotParams,
    aperture,
    channel_dropdown,
    plot_ks_values,
    plot_pdt,
    plt,
):
    def _():
        models = [
            NumericalPlotParams(smooth=1.8, label_dy=0.04, label_dx=0.001),
            # BeamWanderingPlotParams(),
            # LognormalPlotParams(ks_smooth=0, label_dy=0.04),
            # BetaPlotParams(ks_smooth=0, label_dy=0.005, label_dx=0.001),
            # EllipticalBeamPlotParams(smooth=0, label_dy=0.025),
            # NumEllipticalBeamPlotParams(smooth=0, ks_smooth=4, label_pos=125, label_dy=0.025),
            TotalProbabilityPlotParams(),
            BetaTotalProbabilityPlotParams(),
        ]

        _f, _ax = plt.subplots(1, 2, figsize=(150/25.4, 60/25.4))
        plot_pdt(_ax[0], channel_dropdown.value, aperture_radius=aperture, models=models)
        # _ax[0].set_xlim(0, .05)
        # _ax[0].set_ylim(0, 15)

        models=[
            LognormalPlotParams(label_pos=18),
            BeamWanderingPlotParams(label_pos=17, ks_smooth=4.5),
            BetaPlotParams(label_pos=13, label_dx=0.003),
            EllipticalBeamPlotParams(label_pos=23, ks_smooth=4),
            TotalProbabilityPlotParams(label_pos=14, ks_smooth=1),
            BetaTotalProbabilityPlotParams(label_pos=16, ks_smooth=2),
            # NumEllipticalBeamPlotParams(label_pos=30, ks_smooth=1),
            # NumTotalProbabilityPlotParams(label_pos=26, ks_smooth=4),
            # NumBetaTotalProbabilityPlotParams(label_pos=34, ks_smooth=4),
            ]
        plot_ks_values(ax=_ax[1], channel_name=channel_dropdown.value, models=models, apertures=[float(aperture)])
        return _f

    _f = _()
    # _f.savefig('generated/psd_scales.svg')
    _f.tight_layout()
    _f
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# weak_inf""")
    return


@app.cell
def _():
    aperture_weak_inf = 0.03
    return (aperture_weak_inf,)


@app.cell
def _(
    BeamWanderingPlotParams,
    BetaPlotParams,
    EllipticalBeamPlotParams,
    FIGSIZE_SOLO,
    LognormalPlotParams,
    NumericalPlotParams,
    aperture_weak_inf,
    mo,
    plot_pdt,
    plt,
):
    def _():
        models = [
            NumericalPlotParams(smooth=1.8, label_pos=169, label_dy=0.04, label_dx=0.001),
            BeamWanderingPlotParams(label_pos=153),
            LognormalPlotParams(ks_smooth=1, label_pos=152, label_dy=0.04),
            BetaPlotParams(ks_smooth=1, label_pos=170, label_dy=0.005, label_dx=0.001),
            EllipticalBeamPlotParams(smooth=2.5, ks_smooth=4, label_pos=161, label_dy=0.025),
            # NumEllipticalBeamPlotParams(smooth=2.5, ks_smooth=4, label_pos=125, label_dy=0.025),
            # TotalProbabilityPlotParams(label_pos=150),
            # BetaTotalProbabilityPlotParams(label_pos=161),
        ]

        _f, _ax = plt.subplots(1, 1, figsize=FIGSIZE_SOLO)
        _name = plot_pdt(_ax, 'weak_inf', aperture_radius=aperture_weak_inf, models=models)
        _ax.set_ylim(0, 24)
        _f.tight_layout()
        _f.savefig(f'plots/{_name}.svg', bbox_inches='tight', pad_inches=1/50)
        return _f

    mo.hstack([_(), "", ""], widths=[2,2,1])
    return


@app.cell
def _(
    BeamWanderingPlotParams,
    BetaPlotParams,
    BetaTotalProbabilityPlotParams,
    EllipticalBeamPlotParams,
    FIGSIZE_SOLO,
    LognormalPlotParams,
    TotalProbabilityPlotParams,
    aperture_weak_inf,
    mo,
    plot_ks_values,
    plt,
):
    def _():
        models=[
            LognormalPlotParams(label_pos=21),
            BeamWanderingPlotParams(label_pos=17, ks_smooth=4.5),
            BetaPlotParams(label_pos=11, label_dx=0.003, ks_smooth=4),
            EllipticalBeamPlotParams(label_pos=23, ks_smooth=4),
            TotalProbabilityPlotParams(label_pos=14, ks_smooth=1),
            BetaTotalProbabilityPlotParams(label_pos=16, ks_smooth=5),
            # NumEllipticalBeamPlotParams(label_pos=30, ks_smooth=1),
            # NumTotalProbabilityPlotParams(label_pos=26, ks_smooth=4),
            # NumBetaTotalProbabilityPlotParams(label_pos=34, ks_smooth=4),
            ]
        _f, _ax = plt.subplots(1, 1, figsize=FIGSIZE_SOLO)
        filename = plot_ks_values(ax=_ax, channel_name='weak_inf', models=models, apertures=[aperture_weak_inf])
        _ax.set_ylim(1e-3, 1)
        _f.tight_layout()
        _f.savefig(f'plots/weak_inf_ks_values.svg', bbox_inches='tight', pad_inches=1/25.4)
        return _f

    mo.hstack([_(), "", ""], widths=[2,2,1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# weak_zap""")
    return


@app.cell(hide_code=True)
def _():
    aperture_weak_zap = 0.015
    return (aperture_weak_zap,)


@app.cell
def _(
    BetaPlotParams,
    BetaTotalProbabilityPlotParams,
    EllipticalBeamPlotParams,
    FIGSIZE_SOLO,
    LognormalPlotParams,
    NumericalPlotParams,
    aperture_weak_zap,
    mo,
    plot_pdt,
    plt,
):
    def _():
        models = [
            NumericalPlotParams(smooth=1.8, label_pos=170, label_dy=0.04, label_dx=0.001),
            LognormalPlotParams(ks_smooth=1, label_pos=140, label_dy=0.04),
            BetaPlotParams(ks_smooth=1, label_pos=168, label_dy=0.005, label_dx=0.001),
            EllipticalBeamPlotParams(smooth=2.5, ks_smooth=4, label_pos=140, label_dy=0.025),
            # NumEllipticalBeamPlotParams(smooth=2.5, ks_smooth=4, label_pos=125, label_dy=0.025),
            # TotalProbabilityPlotParams(label_pos=150),
            BetaTotalProbabilityPlotParams(label_pos=161),
        ]

        _f, _ax = plt.subplots(1, 1, figsize=FIGSIZE_SOLO)
        _name = plot_pdt(_ax, 'weak_zap', aperture_radius=aperture_weak_zap, models=models)
        _f.tight_layout()
        _f.savefig(f'plots/{_name}.svg', bbox_inches='tight', pad_inches=1/50)
        return _f

    mo.hstack([_(), "", ""], widths=[2,2,1])
    return


@app.cell
def _(
    BeamWanderingPlotParams,
    BetaPlotParams,
    BetaTotalProbabilityPlotParams,
    EllipticalBeamPlotParams,
    FIGSIZE_SOLO,
    LognormalPlotParams,
    TotalProbabilityPlotParams,
    aperture_weak_zap,
    mo,
    plot_ks_values,
    plt,
):
    def _():
        models=[
            LognormalPlotParams(label_pos=21),
            BeamWanderingPlotParams(label_pos=17, ks_smooth=4.5),
            BetaPlotParams(label_pos=13, label_dx=0.003),
            EllipticalBeamPlotParams(label_pos=23, ks_smooth=4),
            TotalProbabilityPlotParams(label_pos=14, ks_smooth=1),
            BetaTotalProbabilityPlotParams(label_pos=16, ks_smooth=2),
            # NumEllipticalBeamPlotParams(label_pos=30, ks_smooth=1),
            # NumTotalProbabilityPlotParams(label_pos=26, ks_smooth=4),
            # NumBetaTotalProbabilityPlotParams(label_pos=34, ks_smooth=4),
            ]
        _f, _ax = plt.subplots(1, 1, figsize=FIGSIZE_SOLO)
        filename = plot_ks_values(ax=_ax, channel_name='weak_zap', models=models, apertures=[aperture_weak_zap])
        _ax.set_ylim(1e-3, 1)
        _f.tight_layout()
        _f.savefig(f'plots/weak_zap_ks_values.svg', bbox_inches='tight', pad_inches=1/25.4)
        return _f

    mo.hstack([_(), "", ""], widths=[2,2,1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# moderate_inf""")
    return


@app.cell(hide_code=True)
def _():
    aperture_moderate_inf = 0.009
    aperture_moderate_inf_2 = 0.05
    return aperture_moderate_inf, aperture_moderate_inf_2


@app.cell(hide_code=True)
def _(
    BeamWanderingPlotParams,
    BetaPlotParams,
    EllipticalBeamPlotParams,
    FIGSIZE_DOUBLE,
    LognormalPlotParams,
    NumericalPlotParams,
    TotalProbabilityPlotParams,
    aperture_moderate_inf,
    aperture_moderate_inf_2,
    mo,
    plot_pdt,
    plt,
):
    def _():
        models = [
            NumericalPlotParams(smooth=1.8, label_dy=0.04, label_dx=0.001, label_pos=25),
            BeamWanderingPlotParams(label_pos=22),
            LognormalPlotParams(ks_smooth=1, label_dy=0.04, label_pos=13),
            BetaPlotParams(ks_smooth=1, label_dy=0.005, label_dx=0.001, label_pos=19),
            EllipticalBeamPlotParams(smooth=2.5, label_dy=0.025, label_pos=27),
            TotalProbabilityPlotParams(label_pos=6),
            # BetaTotalProbabilityPlotParams(),
        ]
        models_2 = [
            NumericalPlotParams(smooth=1.8, label_dy=0.04, label_dx=0.001, label_pos=185),
            BeamWanderingPlotParams(label_pos=182),
            LognormalPlotParams(ks_smooth=1, label_dy=0.04, label_pos=167),
            BetaPlotParams(ks_smooth=1, label_dy=0.005, label_dx=0.001, label_pos=180),
            EllipticalBeamPlotParams(smooth=2.5, label_dy=0.025, label_pos=176),
            TotalProbabilityPlotParams(label_pos=185),
            # BetaTotalProbabilityPlotParams(),
        ]

        _f, _ax = plt.subplots(1, 2, figsize=FIGSIZE_DOUBLE, constrained_layout=True)
        _name = plot_pdt(_ax[0], 'moderate_inf', aperture_radius=aperture_moderate_inf, models=models)
        _ax[0].set_xlim(0, 0.21)
        _ax[0].set_ylim(0, 20)
        _name = plot_pdt(_ax[1], 'moderate_inf', aperture_radius=aperture_moderate_inf_2, models=models_2)
        _ax[1].set_xlim(0.74, 1)
        _ax[1].set_ylim(0, 15)
        _ax[1].set_ylabel(None)
        # _f.tight_layout()
        _f.savefig(f'plots/{_name}.svg', bbox_inches='tight', pad_inches=1/50)
        return _f

    mo.hstack([_(), ""], widths=[2,1])
    return


@app.cell(hide_code=True)
def _(
    BeamWanderingPlotParams,
    BetaPlotParams,
    BetaTotalProbabilityPlotParams,
    EllipticalBeamPlotParams,
    FIGSIZE_SOLO,
    LognormalPlotParams,
    TotalProbabilityPlotParams,
    aperture_moderate_inf,
    aperture_moderate_inf_2,
    mo,
    plot_ks_values,
    plt,
):
    def _():
        models=[
            LognormalPlotParams(label_pos=28),
            BeamWanderingPlotParams(label_pos=17, ks_smooth=4.5),
            BetaPlotParams(label_pos=11, label_dx=0.003, ks_smooth=4),
            EllipticalBeamPlotParams(label_pos=23, ks_smooth=4),
            TotalProbabilityPlotParams(label_pos=12, ks_smooth=1),
            BetaTotalProbabilityPlotParams(label_pos=20, ks_smooth=5),
            # NumEllipticalBeamPlotParams(label_pos=30, ks_smooth=1),
            # NumTotalProbabilityPlotParams(label_pos=26, ks_smooth=4),
            # NumBetaTotalProbabilityPlotParams(label_pos=34, ks_smooth=4),
            ]
        _f, _ax = plt.subplots(1, 1, figsize=FIGSIZE_SOLO)
        filename = plot_ks_values(ax=_ax, channel_name='moderate_inf', models=models, apertures=[aperture_moderate_inf, aperture_moderate_inf_2])
        _ax.set_ylim(4e-3, 1)
        _f.tight_layout()
        _f.savefig(f'plots/moderate_inf_ks_values.svg', bbox_inches='tight', pad_inches=1/25.4)
        return _f

    mo.hstack([_(), "", ""], widths=[2,2,1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# moderate_zap""")
    return


@app.cell
def _():
    aperture_moderate_zap = 0.012
    return (aperture_moderate_zap,)


@app.cell(hide_code=True)
def _(
    BeamWanderingPlotParams,
    BetaPlotParams,
    BetaTotalProbabilityPlotParams,
    EllipticalBeamPlotParams,
    FIGSIZE_SOLO,
    LognormalPlotParams,
    NumericalPlotParams,
    TotalProbabilityPlotParams,
    aperture_moderate_zap,
    mo,
    plot_pdt,
    plt,
):
    def _():
        models = [
            NumericalPlotParams(smooth=2.8, label_pos=26, label_dy=0.04, label_dx=0.001),
            BeamWanderingPlotParams(label_pos=38),
            LognormalPlotParams(ks_smooth=1, label_pos=40, label_dy=0.04),
            BetaPlotParams(ks_smooth=1, label_pos=36, label_dy=0.005, label_dx=0.001),
            EllipticalBeamPlotParams(smooth=2.5, ks_smooth=4, label_pos=46, label_dy=0.025),
            TotalProbabilityPlotParams(label_pos=30),
            BetaTotalProbabilityPlotParams(label_pos=27),
        ]

        _f, _ax = plt.subplots(1, 1, figsize=FIGSIZE_SOLO)
        _name = plot_pdt(_ax, 'moderate_zap', aperture_radius=aperture_moderate_zap, models=models)
        _ax.set_xlim(0, 0.46)
        _ax.set_ylim(0, 8.9)
        _f.tight_layout()
        _f.savefig(f'plots/{_name}.svg', bbox_inches='tight', pad_inches=1/50)
        return _f

    mo.hstack([_(), "", ""], widths=[2,2,1])
    return


@app.cell
def _(
    BeamWanderingPlotParams,
    BetaPlotParams,
    BetaTotalProbabilityPlotParams,
    EllipticalBeamPlotParams,
    FIGSIZE_SOLO,
    LognormalPlotParams,
    TotalProbabilityPlotParams,
    aperture_moderate_zap,
    mo,
    plot_ks_values,
    plt,
):
    def _():
        models=[
            LognormalPlotParams(label_pos=28),
            BeamWanderingPlotParams(label_pos=17, ks_smooth=4),
            BetaPlotParams(label_pos=11, label_dx=0.003, ks_smooth=4),
            EllipticalBeamPlotParams(label_pos=23, ks_smooth=0),
            TotalProbabilityPlotParams(label_pos=12, ks_smooth=1),
            BetaTotalProbabilityPlotParams(label_pos=20, ks_smooth=1),
            # NumEllipticalBeamPlotParams(label_pos=30, ks_smooth=1),
            # NumTotalProbabilityPlotParams(label_pos=26, ks_smooth=4),
            # NumBetaTotalProbabilityPlotParams(label_pos=34, ks_smooth=4),
            ]
        _f, _ax = plt.subplots(1, 1, figsize=FIGSIZE_SOLO)
        filename = plot_ks_values(ax=_ax, channel_name='moderate_zap', models=models, apertures=[aperture_moderate_zap])
        _ax.set_ylim(4e-3, 1)
        _f.tight_layout()
        _f.savefig(f'plots/moderate_zap_ks_values.svg', bbox_inches='tight', pad_inches=1/25.4)
        return _f

    mo.hstack([_(), "", ""], widths=[2,2,1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# strong_inf""")
    return


@app.cell
def _():
    aperture_strong_inf = 0.1
    return (aperture_strong_inf,)


@app.cell
def _(
    BetaPlotParams,
    EllipticalBeamPlotParams,
    FIGSIZE_SOLO,
    LognormalPlotParams,
    NumericalPlotParams,
    aperture_strong_inf,
    mo,
    plot_pdt,
    plt,
):
    def _():
        models = [
            NumericalPlotParams(smooth=2.8, label_pos=7, label_dy=0.01, label_dx=-0.0001),
            # BeamWanderingPlotParams(label_pos=32),
            LognormalPlotParams(ks_smooth=1, label_pos=4, label_dy=0.04),
            BetaPlotParams(ks_smooth=1, label_pos=6, label_dy=0.005, label_dx=-0.00001),
            EllipticalBeamPlotParams(smooth=2.5, ks_smooth=4, label_pos=12, label_dy=0.025),
            # TotalProbabilityPlotParams(label_pos=30),
            # BetaTotalProbabilityPlotParams(label_pos=27),
        ]

        _f, _ax = plt.subplots(1, 1, figsize=FIGSIZE_SOLO)
        _name = plot_pdt(_ax, 'strong_inf', aperture_radius=aperture_strong_inf, models=models)
        _ax.set_xlim(0, 0.05)
        # _ax.set_ylim(0, 15.4)
        _f.tight_layout()
        _f.savefig(f'plots/{_name}.svg', bbox_inches='tight', pad_inches=1/50)
        return _f

    mo.hstack([_(), "", ""], widths=[2,2,1])
    return


@app.cell
def _(
    BeamWanderingPlotParams,
    BetaPlotParams,
    BetaTotalProbabilityPlotParams,
    EllipticalBeamPlotParams,
    FIGSIZE_SOLO,
    LognormalPlotParams,
    TotalProbabilityPlotParams,
    aperture_strong_inf,
    mo,
    plot_ks_values,
    plt,
):
    def _():
        models=[
            LognormalPlotParams(label_pos=28),
            BeamWanderingPlotParams(label_pos=17, ks_smooth=4.5),
            BetaPlotParams(label_pos=11, label_dx=0.003, ks_smooth=4),
            EllipticalBeamPlotParams(label_pos=23, ks_smooth=4),
            TotalProbabilityPlotParams(label_pos=12, ks_smooth=1),
            BetaTotalProbabilityPlotParams(label_pos=20, ks_smooth=5),
            # NumEllipticalBeamPlotParams(label_pos=30, ks_smooth=1),
            # NumTotalProbabilityPlotParams(label_pos=26, ks_smooth=4),
            # NumBetaTotalProbabilityPlotParams(label_pos=34, ks_smooth=4),
            ]
        _f, _ax = plt.subplots(1, 1, figsize=FIGSIZE_SOLO)
        filename = plot_ks_values(ax=_ax, channel_name='strong_inf', models=models, apertures=[aperture_strong_inf])
        _ax.set_ylim(4e-3, 1)
        _f.tight_layout()
        _f.savefig(f'plots/strong_inf_ks_values.svg', bbox_inches='tight', pad_inches=1/25.4)
        return _f

    mo.hstack([_(), "", ""], widths=[2,2,1])
    return


if __name__ == "__main__":
    app.run()
