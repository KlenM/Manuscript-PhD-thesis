import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import numpy as np
    import scipy
    import pandas as pd
    import dataclasses
    import sys
    import pyatmosphere as pyatm
    import matplotlib.pyplot as plt
    from pathlib import Path
    from scipy.stats import gaussian_kde
    from scipy.ndimage import gaussian_filter1d
    from scipy.interpolate import interp1d


    plt.style.use("../klen.mplstyle")

    _wd = '/mnt/hdd/documents/to_clean/oldphys/article2/sup_arxiv/'
    if _wd not in sys.path:
        sys.path.append(_wd)

    WD = Path(_wd)
    DATA = Path('/mnt/hdd/documents/to_clean/oldphys/article2/article2_data/')

    def get_hist(eta):
        kde = gaussian_kde(eta)
        x = np.linspace(min(eta), max(eta), 200)
        y = kde(x)
        return x, y
    return DATA, gaussian_kde, np, pd, plt, pyatm, scipy


@app.cell
def _(DATA, pd):
    from klen.v1 import myaqc

    from src import utils

    def _load_data(channel_name, aperture_size):
        file_name = "aperture_" + str(aperture_size).replace(".", "_") + '.csv'
        path = DATA / channel_name / file_name
        df = pd.read_csv(path)
        df.columns = [float(c) for c in df.columns]
        return df
    utils.load_data = _load_data

    def _get_apertures(channel_name):
        apertures = []
        for file in (DATA / channel_name).glob('*.csv'):
            if '.raw' in file.name or '.adhoc' in file.name:
                continue
            a = float(file.name[9:-4].replace('_', '.'))
            apertures.append(a)
        apertures.sort()
        return apertures

    utils.get_apertures = _get_apertures

    from src.correlations import get_correlations
    from src.entanglement import GaussianEntanglementPlot, WitnessCoherenceCalculator, WitnessCoherencePlot
    from src.bell import BellCalculator, BellPlot, BellPlotTime
    from src.nonclassicality import NonclassicalityPlot
    return get_correlations, utils


@app.cell
def _():
    FIGSIZE_SOLO = (150/25.4 /5*4, 80/25.4)
    FIGSIZE_DOUBLE = (150/25.4, 80/25.4)
    return FIGSIZE_DOUBLE, FIGSIZE_SOLO


@app.cell
def _(pyatm):
    pyatm.gpu.config['use_gpu'] = True
    return


@app.cell(disabled=True, hide_code=True)
def _(pyatm):
    _ch = pyatm.Channel(
                grid=pyatm.RectGrid(resolution=2**9, delta=0.0003),
                source=pyatm.GaussianSource(wvl=809e-9, w0=0.02, F0=1e3),
                path=pyatm.IdenticalPhaseScreensPath(
                    phase_screen=pyatm.SSPhaseScreen(
                        model=pyatm.MVKModel(Cn2=5e-15, l0=1e-3, L0=80),
                        f_grid=pyatm.RandLogPolarGrid(points=2**10, f_min=1 / 80 / 15, f_max=1 / 1e-3 * 2)
                    ), length=1e3, count=10
                ),
                pupil=pyatm.CirclePupil(radius=0.01),
            )
    res = pyatm.simulations.BeamResult(channel=_ch)
    _sim = pyatm.simulations.Simulation([res])

    lt_w = 1.7e-2
    lt_d2 = 5.2e-1
    lt_s = 7.1e-1
    lt_x15 = 8.4e-1

    # _sim.run(plot_step=100)
    return


@app.cell
def _(utils):
    utils.load_data('strong_d2', 0.2).columns
    return


@app.cell
def _(FIGSIZE_DOUBLE, gaussian_kde, np, plt, utils):
    import matplotlib.cm as cm

    _f, _ax = plt.subplots(1, 2, figsize=FIGSIZE_DOUBLE)

    def _(axin, channel_name, aperture_size, time):
        df = utils.load_data(channel_name, aperture_size)
    
        kde = gaussian_kde(np.vstack([df[0], df[time]]))
        # xmin, xmax = df[0].min(), df[0].max()
        # ymin, ymax = df[time].min(), df[time].max()
        xmin = ymin = 0
        xmax = ymax = 1
    
        grid_x = np.linspace(xmin, xmax, 100)
        grid_y = np.linspace(ymin, ymax, 100)
        XX, YY = np.meshgrid(grid_x, grid_y)
    
        ZZ = kde(np.vstack([XX.ravel(), YY.ravel()])).reshape(XX.shape)

        # H, xedges, yedges = np.histogram2d(df[0], df[time], bins=100)
        # X, Y = np.meshgrid(xedges[:-1], yedges[:-1])
        # Z = H.T
        CS = axin.contourf(XX, YY, ZZ,
                          levels=np.linspace(ZZ.min(), ZZ.max(), 20), # 15 contour levels
                          # linewidths=1,
                          cmap=cm.plasma
                          ) # 'plasma' or 'hot' are good for density
    
        # plt.colorbar(CS, ax=axin)
        axin.set_xlabel(r'Transmittance $\eta_0$')
        axin.set_aspect('equal')
        axin.text(
        0.95, 0.89, # Position (X, Y)
        rf'$s={time*100:.0f}\text{{ cm}}$', # The text string
            fontsize=10,
        color='black',
        horizontalalignment='right',
        # Define the clean, white background style
        bbox={
            'facecolor': 'white',
            'alpha': 0.8,
            'edgecolor': 'none', # Crucial: removes the default black border
            'boxstyle': 'round,pad=0.6' # Use a rounded corner box
        }
    )

    _(_ax[0], 'strong_d2', 0.2, 0.028)
    _ax[0].set_ylabel(r'Transmittance $\eta_\tau$')
    # _(_ax[0], 'strong', 0.02)
    # _(_ax[0], 'strong_x1_5', 0.02)
    _(_ax[1], 'strong_d2', 0.2, 0.16799999999999998)
    # _(_ax[1], 'strong', 0.2)
    # _(_ax[1], 'strong_x1_5', 0.2)

    _f.tight_layout()
    _f.savefig("plots/twotimepdt.pdf")
    _f
    return


@app.cell
def _(FIGSIZE_DOUBLE, np, plt, utils):
    _f, _ax = plt.subplots(1, 2, figsize=FIGSIZE_DOUBLE)

    def _(axin, channel_name, aperture_size):
        dim_scale = 100
        smooth = 0.01
        df = utils.load_data(channel_name, aperture_size)
        eta_pearson = utils.pearson_df(df)

        # t = np.linspace(0, df.columns[-1], 100)
        # values = scipy.interpolate.interp1d(df.columns, eta_pearson)(t)
        axin.plot(dim_scale * df.columns, eta_pearson, c=utils.LINE_MAIN_COLOR,
                 marker='o', markersize=3)
        y_line = np.exp(-1)
        corrr_length = dim_scale * utils.get_intersect(df.columns, eta_pearson, y_line)
        axin.hlines(y_line, 0, corrr_length, color='k', ls=':')
        axin.vlines(corrr_length, 0, y_line, color='k', ls=':')
        axin.scatter(corrr_length, y_line, s=10, color='k', zorder=10, marker='x')
        axin.text(0.2, y_line + 0.03, r"$e^{-1}$")
        axin.text(7, 0.83, rf"$R_\text{{ap}}={aperture_size * dim_scale:.0f}\text{{ cm}}$")

        axin.set_ylabel("Pearson correlation")
        axin.set_xlabel(r"Wind-driven shift $s$ (cm)")
        axin.set_ylim(0, 1.05)
        axin.set_xlim(0, axin.get_xlim()[1])
        # axin.tick_params(axis='both', which='major')
        axin.xaxis.set_label_coords(0.4, -0.1)
        # axin.yaxis.set_label_coords(-0.18, 0.5)
        axin.text(corrr_length + 0.4, 0.06, r'$\rho_0$')
        return corrr_length

    print(_(_ax[0], 'strong_d2', 0.02))
    # _(_ax[0], 'strong', 0.02)
    # _(_ax[0], 'strong_x1_5', 0.02)
    print(_(_ax[1], 'strong_d2', 0.2))
    # _(_ax[1], 'strong', 0.2)
    # _(_ax[1], 'strong_x1_5', 0.2)
    _ax[0].set_xlim(0,22)
    _f.tight_layout()
    _f.savefig("plots/corr.pdf")
    _f
    return


@app.cell
def _(FIGSIZE_SOLO, get_correlations, np, plt, scipy, utils):
    class SpatialCoherencePlot():
        def __init__(self, dim_scale=(100, 100)):
            fig, ax = plt.subplots(1, 1, figsize=FIGSIZE_SOLO)
            ax.set_xlabel(r'Aperture radius $R_\mathrm{ap}$ (cm)')
            ax.set_ylabel("Spatial coherence \nradius $\\rho_0$ (cm)")
            self.dim_scale = dim_scale
            self.fig = fig
            self.ax = ax
            self.line_color_id = 1

        def plot(self, channel_name, label=None, lt=None, **kwargs):
            apertures, spatial_coherence = get_correlations(channel_name)
            scaled_apertures = self.dim_scale[0] * np.asarray(apertures)
            if lt:
                scaled_apertures /= (self.dim_scale[0] * lt)
            scaled_spatial_coherence = self.dim_scale[1] * np.asarray(spatial_coherence)
            kwargs = {'color': utils.LINE_COLORS[self.line_color_id], 'marker': 'o', 'markersize': 3, **kwargs}
            self.ax.plot(scaled_apertures, scaled_spatial_coherence, label=label, **kwargs)
            self.line_color_id += 1

        def plot_example(self, channel_name, aperture_size, pos=(0.51, 0.16, 0.47, 0.4)):
            smooth = 1
            axin = self.ax.inset_axes(pos)
            df = utils.load_data(channel_name, aperture_size)
            eta_pearson = utils.pearson_df(df)

            t = np.linspace(0, df.columns[-1], 100)
            values = scipy.interpolate.interp1d(df.columns, eta_pearson)(t)
            axin.plot(self.dim_scale[0] * t, scipy.ndimage.gaussian_filter1d(values, smooth), c=utils.LINE_MAIN_COLOR)
            y_line = np.exp(-1)
            corrr_length = self.dim_scale[0] * utils.get_intersect(df.columns, eta_pearson, y_line)
            axin.hlines(y_line, 0, corrr_length, color='k', ls=':')
            axin.vlines(corrr_length, 0, y_line, color='k', ls=':')
            axin.scatter(corrr_length, y_line, s=10, color='k', zorder=10)
            axin.text(0.2, y_line + 0.03, r"$e^{-1}$", fontsize='x-small')

            axin.set_ylabel("Pearson\ncorrelation", fontsize='x-small')
            axin.set_xlabel(r"Wind-driven shift $s$ (cm)", fontsize='x-small')
            axin.set_ylim(0, 1.05)
            axin.set_xlim(0, axin.get_xlim()[1])
            axin.tick_params(axis='both', which='major', labelsize='x-small')
            axin.xaxis.set_label_coords(0.5, -0.22)
            axin.yaxis.set_label_coords(-0.18, 0.5)
            axin.text(9.2, 0.06, r'$\rho_0$', fontsize='x-small')
            self.axin = axin

        def savefig(self, file_path, **kwargs):
            self.fig.tight_layout()
            kwargs = {**utils.SAVE_KWARGS, **kwargs}
            self.fig.savefig(file_path, **kwargs)
    return (SpatialCoherencePlot,)


@app.cell
def _(SpatialCoherencePlot):
    scp = SpatialCoherencePlot()
    # scp.plot("weak", color='black')
    # scp.plot("moderate", color='green')
    scp.plot("strong_d2", color='black', label=r"$\sigma_\mathrm{R}^2=5.5$")
    scp.plot("strong", ls='--', color='black', label=r"$\sigma_\mathrm{R}^2=11$")
    scp.plot("strong_x1_5", ls='-.', color='black', label=r"$\sigma_\mathrm{R}^2=16.5$")
    scp.ax.set_xlim(0,26)
    scp.ax.set_ylim(0,15.5)


    # scp.plot_example('strong', aperture_size=0.2)
    scp.ax.legend(handlelength=3.5)
    # scp.ax.set_ylim(bottom=0)
    # scp.savefig("plots/3_corr_length.pdf")
    scp.ax.grid(which='major', color='#BBBBBB', linestyle='--')
    scp.fig.tight_layout()
    scp.savefig("plots/corr_length.pdf")
    scp.fig
    return


@app.cell
def _(FIGSIZE_SOLO, np, plt, utils):

    class ConditionalPDTPlot():
        def __init__(self, eta_min):
            fig, ax = plt.subplots(1, 1, figsize=FIGSIZE_SOLO)
            ax.set_xlabel(r"Transmittance $\eta$")
            ax.set_ylabel(r"Conditional PDT $\mathcal{P}(\eta_\tau|\eta_0 > \eta_\mathrm{min})$")
            self.fig = fig
            self.ax = ax
            self.line_color_id = 0
            self.eta_min = eta_min

            self.ax.axvline(x=eta_min, c='k', lw=0.7)
            self.ax.text(eta_min, 0.15, f"$\eta_\mathrm{{min}}={eta_min}$")

        def _plot_0(self, channel_name, aperture_radius, **kwargs):
            df = utils.load_data(channel_name, aperture_radius)
            _eta, _pdt = utils.hist(df[0][df[0] > self.eta_min], smooth=13, restore_scale=(1e4, 1e4))
            eta = [self.eta_min, *_eta]
            pdt = [0, *_pdt]
            kwargs = {'color': 'k',#utils.LINE_COLORS[self.line_color_id], 
                      'label': f"$s = 0$ cm", **kwargs}
            self.ax.plot(eta, pdt, **kwargs)
            self.line_color_id += 1

        def _plot_inf(self, channel_name, aperture_radius, **kwargs):
            df = utils.load_data(channel_name, aperture_radius)
            eta, pdt = utils.hist(df[0], smooth=5, restore_scale=(2e2, 1e4))
            kwargs = {'color': utils.LINE_MAIN_COLOR, 'label': f"$s = \infty$", **kwargs}
            self.ax.plot(eta, pdt, **kwargs)

        def plot(self, channel_name, aperture_radius, wind_shift, smooth=5, **kwargs):
            if wind_shift == 0:
                return self._plot_0(channel_name, aperture_radius, **kwargs)
            if wind_shift == np.inf:
                return self._plot_inf(channel_name, aperture_radius, **kwargs)

            df = utils.load_data(channel_name, aperture_radius)
            eta, pdt = utils.hist(df[wind_shift][df[0] > self.eta_min], smooth=smooth, restore_scale=(1e4, 1e4))
            kwargs = {'color': 'k',#utils.LINE_COLORS[self.line_color_id], 
                      'label': f"$s = {utils.round_n(wind_shift * 100, 3)}$ cm", **kwargs}
            self.ax.plot(eta, pdt, **kwargs);
            self.line_color_id += 1

        def legend(self):
            self.ax.set_ylim(bottom=0)
            self.ax.legend()

        def savefig(self, file_path, **kwargs):
            self.fig.tight_layout()
            kwargs = {**utils.SAVE_KWARGS, **kwargs}
            self.fig.savefig(file_path, **kwargs)

    return (ConditionalPDTPlot,)


@app.cell
def _(ConditionalPDTPlot, np):
    cpdtp = ConditionalPDTPlot(eta_min=0.45)
    cpdtp.plot("strong", aperture_radius=0.3, wind_shift=np.inf)
    cpdtp.plot("strong", aperture_radius=0.3, wind_shift=0.196, ls=(5, (10, 3)))
    cpdtp.plot("strong", aperture_radius=0.3, wind_shift=0.056, ls='-.')
    cpdtp.plot("strong_adhoc", aperture_radius=0.3, wind_shift=0.01, ls='--', smooth=10)
    cpdtp.plot("strong", aperture_radius=0.3, wind_shift=0, ls=':')
    cpdtp.legend()
    cpdtp.savefig("plots/cond_pdt.pdf")
    cpdtp.fig
    return


if __name__ == "__main__":
    app.run()
