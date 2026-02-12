import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


@app.cell
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
    return gaussian_kde, mo, np, plt, pyatm


@app.cell
def _(pyatm):
    channel = pyatm.Channel(
      grid=pyatm.RectGrid(resolution=2**9, delta=0.0004),
      source=pyatm.GaussianSource(
          wvl=809e-9,
          w0=0.02,
          F0=1.6e3
      ),
      path=pyatm.IdenticalPhaseScreensPath(
        phase_screen=pyatm.SSPhaseScreen(
          model=pyatm.MVKModel(
            Cn2=1.5e-14,
            l0=1e-3,
            L0=1e3,
          ),
          f_grid=pyatm.RandLogPolarGrid(
            points=2**10,
            f_min=1 / 1e3 / 15,
            f_max=1 / 1e-3 * 2
          )
        ),
        length=1.6e3,
        count=10
      ),
      pupil=pyatm.CirclePupil(
        radius=0.04
      ),
    )
    return (channel,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # PDT examples
    """)
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
        LognormalPlotParams,
        TotalProbabilityPlotParams,
    )


@app.cell(hide_code=True)
def _(plt):
    def plot_example(x, y, model):
        _fig, _ax = plt.subplots(1, 1, figsize=(2.5, 1.6))
        plt.plot(x, y, color=model.color, linewidth=2)
        plt.fill_between(x, y, color=model.color, alpha=0.2)


        # Circle labels
        if model.label and model.label:
            # label_pos = model.get('label_pos', np.random.randint(0, len(eta_axis)))
            label_x = x[model.label_pos]
            label_y = y[model.label_pos]
            _ax.scatter([label_x], [label_y], s=100,
                       marker="o", zorder=10, clip_on=False, linewidth=1.2,
                       edgecolor=model.color, facecolor="white")
            _ax.text(label_x + model.label_dx,
                    0.99 * label_y + model.label_dy, model.label,
                    zorder=20, color=model.color, ha="center", va="center",
                    size=8, clip_on=False, weight='bold',
                    fontfamily='sans-serif')

        plt.ylim(0, max(y) * 1.1)
        plt.yticks([])
        plt.xticks([0,1])
        plt.xlabel(r'Transmittance $\eta$', labelpad=-13)
        plt.ylabel('PDT density')
        plt.grid(None)
        plt.tight_layout()
        return _fig, _ax
    return (plot_example,)


@app.cell(hide_code=True)
def _(LognormalPlotParams, np, plot_example):
    def _():
        from scipy.stats import lognorm

        mu = -0.5
        sigma = 0.3
        scale = np.exp(mu)
        x = np.linspace(0.001, 1.1, 300)
        pdf = lognorm.pdf(x, s=sigma, scale=scale)
        truncation_point = 1
        mask = x <= truncation_point
        x_trunc = x[mask]
        pdf_trunc = pdf[mask]
        dx = x_trunc[1] - x_trunc[0]
        pdf_trunc_norm = pdf_trunc / (np.sum(pdf_trunc) * dx)

        fig, ax = plot_example(x_trunc, pdf_trunc_norm, LognormalPlotParams(label_pos=200, label_dy=-0.02, label_dx=0.002))
        ax.axvline(x=1.0, color='k', lw=0.2, linestyle='-')
        ax.set_xlim(0, 1.03)
        fig.savefig(f'tmp/lognorm.png', bbox_inches='tight', pad_inches=1/50, dpi=600, transparent=True)
        return fig

    _()
    return


@app.cell(hide_code=True)
def _(BeamWanderingPlotParams, np, plot_example):
    def _(eta):
        from scipy.special import iv
        EXP_OVERFLOW_THRESHOLD = np.log(np.finfo(np.float64).max)
        def bw_eta_0(a, st2):
            return 1 - np.exp(-2 * a**2 / st2)
        def bw_shape_l(eta_0, a, st2):
            return 8 * a**2 / st2 * (np.exp(-4 * a**2 / st2) * iv(1, 4 * a**2 / st2) / (1 - np.exp(-4 * a**2 / st2) * np.i0(4 * a**2 / st2))) * np.log(2 * eta_0 / (1 - np.exp(-4 * a**2 / st2) * np.i0(4 * a**2 / st2)))**(-1)
        def bw_scale_R(eta_0, a, l, st2):
            return a * np.log(2 * eta_0 / (1 - np.exp(-4 * a**2 / st2) * np.i0(4 * a**2 / st2)))**(-1 / l)
        def bw_pdt(eta, eta_0, R, l, bw2):
            eta = np.asarray(eta)
            pdt = np.zeros_like(eta)
            mask = (0 < eta) & (eta < eta_0)
            eta_less_than_eta0 = eta[mask]
            pdt[mask] = R**2 / (bw2 * eta_less_than_eta0 * l) * np.log(eta_0 / eta_less_than_eta0)**(2 / l - 1) * \
                np.exp(-(R**2 / (2 * bw2)) * np.log(eta_0 / eta_less_than_eta0)**(2 / l))
            return pdt
        def bw_is_clear_transmittance(a, st2):
            # If the aperture is about 13 times larger than the beam width, this leads to an overflow of the i0 (i1).

            return 4 * a**2 / st2 > EXP_OVERFLOW_THRESHOLD
        def beam_wandering_pdt(eta, st2, bw2, aperture_radius, eta_0=None, shape_l=None, scale_R=None):

            # In the case of i0 overflow, approximate with the maximum possible PDT, which is close to a clear channel anyway.
            if bw_is_clear_transmittance(aperture_radius, st2):
                return bw_pdt(eta, eta_0=1, R=aperture_radius * 1.0113920776113101, l=30.454248857822876, bw2=bw2)

            eta_0 = eta_0 or bw_eta_0(aperture_radius, st2)
            shape_l = shape_l or bw_shape_l(eta_0, aperture_radius, st2)
            scale_R = scale_R or bw_scale_R(eta_0, aperture_radius, shape_l, st2)
            return bw_pdt(eta, eta_0, scale_R, shape_l, bw2)
        def get_eta_mean(S_BW, W, aperture_radius):
            return 1 - np.exp(-2 * aperture_radius**2 / (4 * S_BW**2 + W**2))
        def get_eta2_mean(S_BW, W, aperture_radius):
            def F_1_approx(nu, r, sigma):
                x2 = r**2 / sigma**2
                F0 = 1 - np.exp(-x2 / 2)
                if x2 < EXP_OVERFLOW_THRESHOLD:
                    _iv0 = iv(0, x2)
                    _log = np.log(2 * F0 / (1 - _iv0 * np.exp(-x2)))
                    if _log < 1e-7:
                        return 0.0
                    mu_1 = (2 * x2 * (1 / (np.exp(x2) / iv(1, x2) - _iv0 / iv(1, x2))) / _log)
                    D1_1 = sigma / r * _log**(1 / mu_1)
                else:
                    _iv0 = iv(0, EXP_OVERFLOW_THRESHOLD)
                    _log = np.log(2 * F0 / (1 - _iv0 * np.exp(-x2)))
                    mu_1 = (2 * x2 * (iv(1, EXP_OVERFLOW_THRESHOLD) / (np.exp(EXP_OVERFLOW_THRESHOLD) - _iv0)) / _log)
                    D1_1 = sigma / r * _log**(1 / mu_1)
                result = F0 * np.exp(-(D1_1 * nu / sigma)**mu_1)
                return result

            def Q_approx(nu, r, sigma):
                res = 1 - F_1_approx(nu, r, sigma)
                return res

            p = W**2 / 8 / S_BW**2
            d = 2 * aperture_radius / W * np.sqrt(2 * p * (p + 1) / (2 * p**2 + 3 * p + 1))
            b = 1 / (2 * p + 1)
            res = (1 - 2 * np.exp(-2 * aperture_radius**2 / (4 * S_BW**2 + W**2)) + np.exp(-d**2 / 2) *
                    (1 - Q_approx(d, d * b, np.sqrt(1 - b**2)) + Q_approx(d * b, d, np.sqrt(1 - b**2))))
            return res
        return beam_wandering_pdt(eta, 0.07, 0.008, 0.2)

    _eta = np.linspace(0,1,300)
    _pdf = _(_eta)

    _fig, _ax = plot_example(_eta, _pdf, BeamWanderingPlotParams(label_pos=180, label_dy=-0.07))
    _fig.savefig(f'tmp/bw.png', bbox_inches='tight', pad_inches=1/50, dpi=600, transparent=True)
    _fig
    return


@app.cell(hide_code=True)
def _(EllipticalBeamPlotParams, gaussian_kde, np, plot_example):
    def _():
        from typing import Optional, Tuple
        from scipy.special import lambertw, iv


        class EllipticBeamAnalyticalPDT:
            def __init__(self, W0, a, size: int):
                self.W0 = W0
                self.a = a
                self.size = size
                self.bw: Optional[float] = None
                self.theta_mean: Optional[float] = None
                self.theta_cov: Optional[Tuple[float, float]] = None

            def set_params(self, bw: float, theta_mean: float, theta_cov: Tuple[float, float]):
                self.bw = bw
                self.theta_mean = theta_mean
                self.theta_cov = theta_cov
                return self

            def set_params_from_data(self, mean_x, mean_x2, mean_y2):
                bw = np.sqrt((mean_x**2).mean())
                W2_mean, W2_cov = self._get_mean_W(mean_x, mean_x2, mean_y2)
                theta_mean, theta_cov = self._get_mean_theta(W2_mean, W2_cov)
                return self.set_params(bw, theta_mean, theta_cov)

            def _get_mean_W(self, mean_x, mean_x2, mean_y2):
                x2_mean = mean_x2.mean()
                xx_mean = (mean_x**2).mean()
                x2x2_mean = (mean_x2**2).mean()
                x2y2_mean = (mean_x2 * mean_y2).mean()
                W2_mean = 4 * (x2_mean - xx_mean)

                delta_ij = np.asarray([1, 0])
                part_1 = 8 * delta_ij * xx_mean**2
                part_2 = xx_mean * W2_mean
                part_3 = x2x2_mean * (4 * delta_ij - 1) - x2y2_mean * (4 * delta_ij - 3)
                Wi2Wj2_mean = 8 * (-part_1 - part_2 + part_3)
                W2_cov = Wi2Wj2_mean - W2_mean**2
                return W2_mean, W2_cov

            def _get_mean_theta(self, W2_mean, W2_cov):
                theta_mean = np.log(W2_mean / self.W0**2 / np.sqrt(1 + W2_cov[0] / W2_mean**2))
                theta_cov = np.log(1 + W2_cov / W2_mean**2)
                return theta_mean, theta_cov

            def _get_W_eff(self, chi, W1, W2):
                exp_part1 = self.a**2 / W1**2 * (1 + 2 * np.cos(chi)**2)
                exp_part2 = self.a**2 / W2**2 * (1 + 2 * np.sin(chi)**2)
                arg = 4 * self.a**2 / W1 / W2 * np.exp(exp_part1 + exp_part2)
                W2_eff = 4 * self.a**2 / lambertw(arg).real
                return np.sqrt(W2_eff)

            def _get_R_lambda(self, xi) -> Tuple[float, float]:
                if xi == 0:
                    return np.inf, 2
                arg = self.a**2 * xi**2
                exp_bes_part = 1 - np.exp(-arg) * iv(0, arg)
                log_part = np.log(2 * (1 - np.exp(-arg / 2)) / exp_bes_part)

                lmbd_part_1 = np.exp(-arg) * iv(1, arg)
                lmbd = 2 * arg * lmbd_part_1 / exp_bes_part / log_part
                R = log_part**(-1 / lmbd)
                return R, lmbd

            def _get_eta0(self, W1, W2):
                R, lmbd = self._get_R_lambda(1 / W1 - 1 / W2)
                eta0_part1 = iv(0, self.a**2 * (1 / W1**2 - 1 / W2**2))
                eta0_part2 = np.exp(-self.a**2 * (1 / W1**2 + 1 / W2**2))
                if W1 == W2:
                    eta0_part3 = 0
                    eta0_part4 = 0
                else:
                    eta0_part3 = 2 * (1 - np.exp(-self.a**2 / 2 * (1 / W1 - 1 / W2)**2))
                    eta0_part4 = np.exp(-((W1 + W2)**2 / np.abs(W1**2 - W2**2) / R)**lmbd)
                return 1 - eta0_part1 * eta0_part2 - eta0_part3 * eta0_part4

            def eta(self, r_0, varphi_0, theta_1, theta_2, phi):
                W1 = self.W0 * np.exp(theta_1 / 2)
                W2 = self.W0 * np.exp(theta_2 / 2)

                W_eff = self._get_W_eff(phi - varphi_0, W1=W1, W2=W2)
                eta_0 = self._get_eta0(W1=W1, W2=W2)
                R, lmbd = self._get_R_lambda(2 / W_eff)
                return eta_0 * np.exp(-(r_0 / self.a / R)**lmbd)

            def pdt(self):
                if self.bw is None or self.theta_mean is None or self.theta_cov is None:
                    raise ValueError(
                        'The parametes must be setted via .set_params(...) or .set_params_from_data(...).')
                r_0s = np.random.rayleigh(self.bw, size=self.size)
                varphi_0s = np.random.uniform(0, 2 * np.pi, size=self.size)
                thetas = np.random.multivariate_normal(
                    [self.theta_mean, self.theta_mean],
                    [self.theta_cov, self.theta_cov[::-1]],
                    size=self.size).T
                phis = np.random.uniform(0, np.pi / 2, size=self.size)
                params = zip(r_0s, varphi_0s, thetas[0], thetas[1], phis)
                transmittance = []
                for r_0, varphi_0, theta_1, theta_2, phi in params:
                    transmittance.append(self.eta(r_0, varphi_0, theta_1, theta_2, phi))
                return transmittance
        _eb = EllipticBeamAnalyticalPDT(W0=0.05, a=0.038, size=10000)
        _eb.set_params(bw=0.01, theta_mean=0.05, theta_cov=[0.1, 0.008])
        pdt = _eb.pdt()
        pdt = np.asarray(pdt)[~np.isnan(pdt)]


        def get_hist(eta):
            kde = gaussian_kde(eta)
            x = np.linspace(min(eta), max(eta), 200)
            y = kde(x)
            return x, y
        return get_hist(pdt)


    _eta, _pdf = _()
    _fig, _ax = plot_example(_eta, _pdf, EllipticalBeamPlotParams(label_pos=140, label_dy=-0.07))
    _fig.savefig(f'tmp/eb.png', bbox_inches='tight', pad_inches=1/50, dpi=600, transparent=True)
    _fig
    return


@app.cell(hide_code=True)
def _(TotalProbabilityPlotParams, np, plot_example):
    def _():
        from scipy.stats import lognorm
        from scipy.special import i1
        from scipy.integrate import quad

        def bayesian_pdt(eta, eta_mean, eta2_mean, a, st2, bw2, scale_R=None, shape_l=None, r0_size=2000):
            bw = np.sqrt(bw2)

            def bw_eta_0(a, st2):
                return 1 - np.exp(-2 * a**2 / st2)


            def bw_shape_l(eta_0, a, st2):
                return 8 * a**2 / st2 * (np.exp(-4 * a**2 / st2) * i1(4 * a**2 / st2) / (1 - np.exp(-4 * a**2 / st2) * np.i0(4 * a**2 / st2))) * np.log(2 * eta_0 / (1 - np.exp(-4 * a**2 / st2) * np.i0(4 * a**2 / st2)))**(-1)


            def bw_scale_R(eta_0, a, l, st2):
                return a * np.log(2 * eta_0 / (1 - np.exp(-4 * a**2 / st2) * np.i0(4 * a**2 / st2)))**(-1 / l)

            def get_eta0(eta_mean, bw, scale_R, shape_l):
                def under_int(xi):
                    return xi * np.exp(-xi**2 / 2) * np.exp(-(bw / scale_R * xi)**shape_l)
                return eta_mean / quad(under_int, 0, np.inf)[0]

            def get_zeta02(eta2_mean, bw, scale_R, shape_l):
                def under_int(xi):
                    return xi * np.exp(-xi**2 / 2) * np.exp(-2 * (bw / scale_R * xi)**shape_l)
                return eta2_mean / quad(under_int, 0, np.inf)[0]

            eta_0 = bw_eta_0(a, st2)
            shape_l = shape_l or bw_shape_l(eta_0, a, st2)
            scale_R = scale_R or bw_scale_R(eta_0, a, shape_l, st2)
            eta0 = get_eta0(eta_mean, bw, scale_R, shape_l)
            zeta02 = get_zeta02(eta2_mean, bw, scale_R, shape_l)
            sigma_r0 = np.sqrt(np.log(zeta02 / eta0**2))

            total_probability_model = np.zeros_like(eta)
            for r0 in np.random.rayleigh(bw, size=r0_size):
                mu_r0 = -np.log(eta0**2 / np.sqrt(zeta02)) + \
                    (abs(r0) / scale_R)**shape_l
                lognorm_model = lognorm(sigma_r0, scale=np.exp(-mu_r0))
                total_probability_model += lognorm_model.pdf(
                    eta) / lognorm_model.cdf(1)
            return 1 / r0_size * total_probability_model

        _eta = np.linspace(0,1,300)
        return _eta, bayesian_pdt(_eta, eta_mean=0.6, eta2_mean=0.37, a=0.03, st2=0.002, bw2=0.00001, r0_size=1000)


    _eta, _pdf = _()
    _fig, _ax = plot_example(_eta, _pdf, TotalProbabilityPlotParams(label_pos=140, label_dy=-0.07))
    _fig.savefig(f'tmp/tp.png', bbox_inches='tight', pad_inches=1/50, dpi=600, transparent=True)
    _fig
    return


@app.cell
def _(BetaPlotParams, np, plot_example):
    def _():
        from scipy.stats import beta
        def beta_pdt(eta, eta_mean, eta2_mean):
            eta_std2 = eta2_mean - eta_mean**2
            beta_a = (eta_mean**2 - eta_mean**3 - eta_mean * eta_std2) / eta_std2
            beta_b = beta_a * (1 / eta_mean - 1)
            return beta.pdf(eta, beta_a, beta_b)

        _eta = np.linspace(0,1,300)
        return _eta, beta_pdt(_eta, eta_mean=0.6, eta2_mean=0.37)


    _eta, _pdf = _()
    _fig, _ax = plot_example(_eta, _pdf, BetaPlotParams(label_pos=210, label_dy=-0.07))
    _fig.savefig(f'tmp/be.png', bbox_inches='tight', pad_inches=1/50, dpi=600, transparent=True)
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Beam examples
    """)
    return


@app.cell
def _(channel, mean_x, mean_x2, mean_y, np):
    def _():
        import cupy as cp
        np.random.seed(0)
        cp.random.seed(0)
        beam_res = []

        try:
            while True:
                # print('s')
                beam_shape = channel.run(pupil=False)
                x0, y0 = mean_x(channel, output=beam_shape), mean_y(channel, output=beam_shape)
                r0 = np.sqrt(x0**2 + y0**2)
                x2 = mean_x2(channel, output=beam_shape)
                st = np.sqrt(4 * (x2 - x0**2))
                #if r0 > 1.3 * st / 2 and 1/6 < y0 / r0 < 5/6 and 1/6 < x0 / r0 < 5/6:
                # if r0 > 1.3 * st / 2 and 1/6 < y0 / r0 and 1/6 < x0 / r0:
                if r0 > 1.3 * st / 2 and 1/5 < np.abs(y0 / r0) and 1/5 < np.abs(x0 / r0):
                    beam_res.append({'beam_shape': beam_shape, 'x0': x0, 'y0': y0, 'r0': r0, 'x2':  x2, 'st': st})
                    print('#')
                if len(beam_res) > 5:
                    return beam_res
        except KeyboardInterrupt:
            return beam_res

    beam_res = _()
    print(len(beam_res))
    return (beam_res,)


@app.cell
def _(LinearSegmentedColormap):

    c_red = 1.0
    c_green = 165/255
    c_blue = 0.0

    cdict_pure_orange = {
        # Red is always full
        'red':   ((0.0, c_red, c_red), 
                  (1.0, c_red, c_red)),

        # Green is always at the orange-ratio mid-point
        'green': ((0.0, c_green, c_green), 
                  (1.0, c_green, c_green)),

        # Blue is always zero
        'blue':  ((0.0, c_blue, c_blue), 
                  (1.0, c_blue, c_blue)),

        # Alpha: This is the only thing that moves
        'alpha': ((0.0, 0.0, 0.0),   # Fully transparent at 0%
                  (0.07, 0.2, 0.2),   # Reaches full opacity at 70%
                  (0.2, 0.3, 0.3),   # Reaches full opacity at 70%
                  (0.7, 0.8, 0.8),   # Reaches full opacity at 70%
                  (1.0, 1.0, 1.0))   # Stays opaque until 100%
    }

    ph_orange = LinearSegmentedColormap('phOrange', cdict_pure_orange)
    return (ph_orange,)


@app.cell
def _():
    from matplotlib.colors import LinearSegmentedColormap
    from pyatmosphere.measures import I, mean_x, mean_y, mean_x2
    return I, LinearSegmentedColormap, mean_x, mean_x2, mean_y


@app.cell
def _(I, channel, ph_orange, plt):
    def _():
        plt.figure(dpi=110, figsize=(3.4, 3.4))
        plt.imshow(
          I(channel, output=channel.source.output()), 
          cmap=ph_orange, 
          vmin=0, vmax=1100, 
          extent=channel.grid.extent
        )
        # plt.plot([0, x0], [0, y0], lw=0.5, c='k', ls='--')
        # plt.plot([0, x0], [y0, y0], lw=1, c='k', ls=':')
        # plt.plot([x0, x0], [0, y0], lw=1, c='k', ls=':')
        # circle1 = plt.Circle((x0, y0), st/2, color='k', ls=(0, (14,11)), fill=False, zorder=10)
        # plt.gca().add_patch(circle1)

        # angle = Arc((0, 0), 0.012, 0.012, angle=0, theta1=0.0, theta2=np.arcsin(y0/r0) / 2 / np.pi * 360 )
        # plt.gca().add_patch(angle)
        # plt.annotate("", xy=(x0 - st/2*x0/r0, y0 - st/2*y0/r0), xytext=(x0 + st/2*x0/r0, y0 + st/2*y0/r0), arrowprops=dict(arrowstyle="<->", color='k'))

        # plt.annotate("$W_r$", xy=(x0*0.67, y0*1.3), c='k')
        # plt.annotate("$(0,0)$", xy=(-0.01, -0.004), c='k')
        # plt.annotate("$y_0$", xy=(-0.008, y0*1.1), c='k')
        # plt.annotate("$x_0$", xy=(x0*1.1, -0.008), c='k')
        # plt.annotate("$\chi$", xy=(0.007, 0.002), c='k')

        # plt.axhline(0,color='k', lw=0.5)
        # plt.axvline(0,color='k', lw=0.5) 
        plt.xticks([]);
        plt.yticks([]);
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        # plt.xlim(-0.057, 0.057)
        # plt.ylim(-0.057, 0.057)
        plt.xlim(-0.04, 0.04)
        plt.ylim(-0.04, 0.04)
        plt.gca().axis('off')
        # plt.gca().set_facecolor('#e9ebe8')
        # plt.gca().figure.patch.set_facecolor('#e9ebe8')
        plt.savefig('tmp/beam_g.png', bbox_inches='tight', pad_inches=1/50, dpi=600, transparent=True)
        # plt.savefig(config.PLOTS_PATH / ('beam_profile.pdf'), **{
        #     "format": "pdf",
        #     "dpi": 300,
        #     "bbox_inches": "tight",
        #     "pad_inches": 0.005
        #     }
        # )
        plt.show()

    _()
    return


@app.cell
def _(I, beam_res, channel, ph_orange, plt):
    def _(beam_shape, x0, y0, r0, x2, st):
        plt.figure(dpi=110, figsize=(3.4, 3.4))
        plt.imshow(
          I(channel, output=beam_shape), 
          cmap=ph_orange, 
          vmin=0, vmax=1100, 
          extent=channel.grid.extent
        )
        # plt.plot([0, x0], [0, y0], lw=0.5, c='k', ls='--')
        # plt.plot([0, x0], [y0, y0], lw=1, c='k', ls=':')
        # plt.plot([x0, x0], [0, y0], lw=1, c='k', ls=':')
        # circle1 = plt.Circle((x0, y0), st/2, color='k', ls=(0, (14,11)), fill=False, zorder=10)
        # plt.gca().add_patch(circle1)

        # angle = Arc((0, 0), 0.012, 0.012, angle=0, theta1=0.0, theta2=np.arcsin(y0/r0) / 2 / np.pi * 360 )
        # plt.gca().add_patch(angle)
        # plt.annotate("", xy=(x0 - st/2*x0/r0, y0 - st/2*y0/r0), xytext=(x0 + st/2*x0/r0, y0 + st/2*y0/r0), arrowprops=dict(arrowstyle="<->", color='k'))

        # plt.annotate("$W_r$", xy=(x0*0.67, y0*1.3), c='k')
        # plt.annotate("$(0,0)$", xy=(-0.01, -0.004), c='k')
        # plt.annotate("$y_0$", xy=(-0.008, y0*1.1), c='k')
        # plt.annotate("$x_0$", xy=(x0*1.1, -0.008), c='k')
        # plt.annotate("$\chi$", xy=(0.007, 0.002), c='k')

        # plt.axhline(0,color='k', lw=0.5)
        # plt.axvline(0,color='k', lw=0.5) 
        plt.xticks([]);
        plt.yticks([]);
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        # plt.xlim(-0.057, 0.057)
        # plt.ylim(-0.057, 0.057)
        _d = 0.05
        plt.xlim(x0-_d, x0+_d)
        plt.ylim(y0-_d, y0+_d)
        plt.gca().axis('off')
        # plt.gca().set_facecolor('#e9ebe8')
        # plt.gca().figure.patch.set_facecolor('#e9ebe8')
        plt.savefig('tmp/beam_example.png', bbox_inches='tight', pad_inches=1/50, dpi=600, transparent=True)
        # plt.savefig(config.PLOTS_PATH / ('beam_profile.pdf'), **{
        #     "format": "pdf",
        #     "dpi": 300,
        #     "bbox_inches": "tight",
        #     "pad_inches": 0.005
        #     }
        # )
        plt.show()

    _(**beam_res[1])
    return


@app.cell(hide_code=True)
def _(I, beam_res, channel, ph_orange, plt):
    def _(beam_shape, x0, y0, r0, x2, st):
        plt.figure(dpi=110, figsize=(3.4, 3.4))
        plt.imshow(
          I(channel, output=beam_shape), 
          cmap=ph_orange, 
          vmin=0, vmax=1100, 
          extent=channel.grid.extent
        )
        plt.plot([0, x0], [0, y0], lw=0.5, c='k', ls='--')
        plt.plot([0, x0], [y0, y0], lw=1, c='k', ls=':')
        plt.plot([x0, x0], [0, y0], lw=1, c='k', ls=':')
        circle1 = plt.Circle((x0, y0), st/2, color='k', ls=(0, (14,11)), fill=False, zorder=10)
        plt.gca().add_patch(circle1)

        # angle = Arc((0, 0), 0.012, 0.012, angle=0, theta1=0.0, theta2=np.arcsin(y0/r0) / 2 / np.pi * 360 )
        # plt.gca().add_patch(angle)
        plt.annotate("", xy=(x0 - st/2*x0/r0, y0 - st/2*y0/r0), xytext=(x0 + st/2*x0/r0, y0 + st/2*y0/r0), arrowprops=dict(arrowstyle="<->", color='k'))

        plt.annotate("$W_r$", xy=(x0*0.67, y0*1.3), c='k')
        plt.annotate("$(0,0)$", xy=(-0.01, -0.004), c='k')
        plt.annotate("$y_0$", xy=(-0.008, y0*1.1), c='k')
        plt.annotate("$x_0$", xy=(x0*1.1, -0.008), c='k')
        # plt.annotate("$\chi$", xy=(0.007, 0.002), c='k')

        plt.axhline(0,color='k', lw=0.5)
        plt.axvline(0,color='k', lw=0.5) 
        plt.xticks([]);
        plt.yticks([]);
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        # plt.xlim(-0.057, 0.057)
        # plt.ylim(-0.057, 0.057)
        plt.xlim(-0.015, 0.0415)
        plt.ylim(-0.01, 0.042)
        plt.gca().axis('off')
        # plt.gca().set_facecolor('#e9ebe8')
        # plt.gca().figure.patch.set_facecolor('#e9ebe8')
        plt.savefig('tmp/beam0.png', bbox_inches='tight', pad_inches=1/50, dpi=600, transparent=True)
        # plt.savefig(config.PLOTS_PATH / ('beam_profile.pdf'), **{
        #     "format": "pdf",
        #     "dpi": 300,
        #     "bbox_inches": "tight",
        #     "pad_inches": 0.005
        #     }
        # )
        plt.show()

    for _br in [beam_res[2]]:
        _(**_br)
    return


@app.cell(hide_code=True)
def _(I, beam_res, channel, np, ph_orange, plt):
    def _(beam_shape, x0, y0, r0, x2, st):
        plt.figure(dpi=110, figsize=(3.4, 3.4))

        sigma = 0.033
        mask = np.exp(-channel.grid.get_rho2() / (2 * sigma**2))

        plt.imshow(
          I(channel, output=beam_shape)* mask, 
          cmap=ph_orange, 
          vmin=0, vmax=1100, 
          extent=channel.grid.extent
        )
        plt.plot([0, x0], [0, y0], lw=0.5, c='k', ls='--')
        plt.plot([0, x0], [y0, y0], lw=1, c='k', ls=':')
        plt.plot([x0, x0], [0, y0], lw=1, c='k', ls=':')
        circle1 = plt.Circle((x0, y0), st/2, color='k', ls=(0, (14,11)), fill=False, zorder=10)
        plt.gca().add_patch(circle1)

        # angle = Arc((0, 0), 0.012, 0.012, angle=0, theta1=0.0, theta2=np.arcsin(y0/r0) / 2 / np.pi * 360 )
        # plt.gca().add_patch(angle)
        plt.annotate("", xy=(x0 - st/2*x0/r0, y0 - st/2*y0/r0), xytext=(x0 + st/2*x0/r0, y0 + st/2*y0/r0), arrowprops=dict(arrowstyle="<->", color='k'))

        plt.annotate("$W_r$", xy=(x0*1.9, y0*0.7), c='k')
        plt.annotate("$(0,0)$", xy=(0.002, -0.008), c='k')
        plt.annotate("$y_0$", xy=(0.007, y0*1.1), c='k')
        plt.annotate("$x_0$", xy=(x0*1.1, -0.007), c='k')
        # plt.annotate("$\chi$", xy=(0.007, 0.002), c='k')

        plt.axhline(0,color='k', lw=0.5)
        plt.axvline(0,color='k', lw=0.5) 
        plt.xticks([]);
        plt.yticks([]);
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        plt.xlim(-0.05, 0.023)
        plt.ylim(-0.013, 0.057)
        plt.gca().axis('off')
        # plt.gca().set_facecolor('#e9ebe8')
        # plt.gca().figure.patch.set_facecolor('#e9ebe8')
        plt.savefig('tmp/beam1.png', bbox_inches='tight', pad_inches=1/50, dpi=600, transparent=True)
        # plt.savefig(config.PLOTS_PATH / ('beam_profile.pdf'), **{
        #     "format": "pdf",
        #     "dpi": 300,
        #     "bbox_inches": "tight",
        #     "pad_inches": 0.005
        #     }
        # )
        plt.show()

    for _br in [beam_res[5]]:
        _(**_br)
    return


@app.cell(hide_code=True)
def _(I, beam_res, channel, ph_orange, plt):
    def _(beam_shape, x0, y0, r0, x2, st):
        plt.figure(dpi=110, figsize=(3.4, 3.4))
        plt.imshow(
          I(channel, output=beam_shape), 
          cmap=ph_orange, 
          vmin=0, vmax=1100, 
          extent=channel.grid.extent
        )
        plt.plot([0, x0], [0, y0], lw=0.5, c='k', ls='--')
        plt.plot([0, x0], [y0, y0], lw=1, c='k', ls=':')
        plt.plot([x0, x0], [0, y0], lw=1, c='k', ls=':')
        circle1 = plt.Circle((x0, y0), st/2, color='k', ls=(0, (14,11)), fill=False, zorder=10)
        plt.gca().add_patch(circle1)

        # angle = Arc((0, 0), 0.012, 0.012, angle=0, theta1=0.0, theta2=np.arcsin(y0/r0) / 2 / np.pi * 360 )
        # plt.gca().add_patch(angle)
        plt.annotate("", xy=(x0 - st/2*x0/r0, y0 - st/2*y0/r0), xytext=(x0 + st/2*x0/r0, y0 + st/2*y0/r0), arrowprops=dict(arrowstyle="<->", color='k'))

        plt.annotate("$W_r$", xy=(x0*0.8, y0*1.7), c='k')
        plt.annotate("$(0,0)$", xy=(-0.02, 0.004), c='k')
        plt.annotate("$y_0$", xy=(-0.008, y0*1.1), c='k')
        plt.annotate("$x_0$", xy=(x0*1.1, 0.005), c='k')
        # plt.annotate("$\chi$", xy=(0.007, 0.002), c='k')

        plt.axhline(0,color='k', lw=0.5)
        plt.axvline(0,color='k', lw=0.5) 
        plt.xticks([]);
        plt.yticks([]);
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        plt.xlim(-0.057, 0.057)
        plt.ylim(-0.057, 0.057)
        plt.gca().set_facecolor('#e9ebe8')
        plt.gca().figure.patch.set_facecolor('#e9ebe8')
        plt.savefig('tmp/beam2.png', bbox_inches='tight', pad_inches=1/50, dpi=600, transparent=False)
        # plt.savefig(config.PLOTS_PATH / ('beam_profile.pdf'), **{
        #     "format": "pdf",
        #     "dpi": 300,
        #     "bbox_inches": "tight",
        #     "pad_inches": 0.005
        #     }
        # )
        plt.show()

    for _br in [beam_res[3]]:
        _(**_br)
    return


@app.cell(hide_code=True)
def _(I, beam_res, channel, np, ph_orange, plt):
    def _(beam_shape, x0, y0, r0, x2, st):
        plt.figure(dpi=110, figsize=(3.4, 3.4))
    
        sigma = 0.03
        mask = np.exp(-channel.grid.get_rho2() / (2 * sigma**2))

        plt.imshow(
          I(channel, output=beam_shape) * mask, 
          cmap=ph_orange, 
          vmin=0, vmax=1100, 
          extent=channel.grid.extent
        )
        plt.plot([0, x0], [0, y0], lw=0.5, c='k', ls='--')
        # plt.plot([0, x0], [y0, y0], lw=1, c='k', ls=':')
        plt.plot([x0, x0], [0, y0], lw=1, c='k', ls=':')
        plt.scatter([x0], [y0], c='k')
        # circle1 = plt.Circle((x0, y0), st/2, color='k', ls=(0, (14,11)), fill=False, zorder=10)
        # plt.gca().add_patch(circle1)

        # angle = Arc((0, 0), 0.012, 0.012, angle=0, theta1=0.0, theta2=np.arcsin(y0/r0) / 2 / np.pi * 360 )
        # plt.gca().add_patch(angle)
        # plt.annotate("", xy=(x0 - st/2*x0/r0, y0 - st/2*y0/r0), xytext=(x0 + st/2*x0/r0, y0 + st/2*y0/r0), arrowprops=dict(arrowstyle="<->", color='k'))

        # plt.annotate("$W_r$", xy=(x0*0.67, y0*1.3), c='k')
        # plt.annotate("$(0,0)$", xy=(-0.01, -0.004), c='k')
        # plt.annotate("$y_0$", xy=(-0.008, y0*1.1), c='k')
        plt.annotate("$x_0$", xy=(x0*1.1, 0.004), c='k')
        # plt.annotate("$\chi$", xy=(0.007, 0.002), c='k')

        plt.axhline(0,color='k', lw=0.5)
        plt.axvline(0,color='k', lw=0.5) 
        plt.xticks([]);
        plt.yticks([]);
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        plt.xlim(-0.057, 0.057)
        plt.ylim(-0.057, 0.057)
        # plt.xlim(-0.015, 0.0415)
        # plt.ylim(-0.01, 0.042)
        plt.gca().axis('off')
        # plt.gca().set_facecolor('#e9ebe8')
        # plt.gca().figure.patch.set_facecolor('#e9ebe8')
        plt.savefig('tmp/bw.png', bbox_inches='tight', pad_inches=1/50, dpi=600, transparent=True)
        # plt.savefig(config.PLOTS_PATH / ('beam_profile.pdf'), **{
        #     "format": "pdf",
        #     "dpi": 300,
        #     "bbox_inches": "tight",
        #     "pad_inches": 0.005
        #     }
        # )
        plt.show()

    for _br in [beam_res[3]]:
        _(**_br)
    return


@app.cell
def _(I, beam_res, channel, np, ph_orange, plt):
    def _(beam_shape, x0, y0, r0, x2, st):
        plt.figure(dpi=110, figsize=(3.4, 3.4))
    
        sigma = 0.03
        mask = np.exp(-channel.grid.get_rho2() / (2 * sigma**2))

        plt.imshow(
          I(channel, output=beam_shape) * mask, 
          cmap=ph_orange, 
          vmin=0, vmax=1100, 
          extent=channel.grid.extent
        )
        # plt.plot([0, x0], [0, y0], lw=0.5, c='k', ls='--')
        # plt.plot([0, x0], [y0, y0], lw=1, c='k', ls=':')
        # plt.plot([x0, x0], [0, y0], lw=1, c='k', ls=':')
        plt.scatter([x0], [y0], c='k', s=5)
        # circle1 = plt.Circle((x0, y0), st/2, color='k', ls=(0, (14,11)), fill=False, zorder=10)
        # plt.gca().add_patch(circle1)

        # angle = Arc((0, 0), 0.012, 0.012, angle=0, theta1=0.0, theta2=np.arcsin(y0/r0) / 2 / np.pi * 360 )
        # plt.gca().add_patch(angle)
        # plt.annotate("", xy=(x0 - st/2*x0/r0, y0 - st/2*y0/r0), xytext=(x0 + st/2*x0/r0, y0 + st/2*y0/r0), arrowprops=dict(arrowstyle="<->", color='k'))

        # plt.annotate("$W_r$", xy=(x0*0.67, y0*1.3), c='k')
        # plt.annotate("$(0,0)$", xy=(-0.01, -0.004), c='k')
        # plt.annotate("$y_0$", xy=(-0.008, y0*1.1), c='k')
        # plt.annotate("$x_0$", xy=(x0*1.1, 0.004), c='k')
        # plt.annotate("$\chi$", xy=(0.007, 0.002), c='k')

        plt.axhline(0,color='k', lw=0.5)
        plt.axvline(0,color='k', lw=0.5) 
        plt.xticks([]);
        plt.yticks([]);
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        # plt.xlim(-0.015, 0.0415)
        # plt.ylim(-0.01, 0.042)
        plt.gca().axis('off')
        # plt.gca().set_facecolor('#e9ebe8')
        # plt.gca().figure.patch.set_facecolor('#e9ebe8')
        from matplotlib.patches import Ellipse
        angle_deg = 70
        angle_rad = np.deg2rad(angle_deg)
        a = (1.3 * st) / 2
        b = st / 2
        ell = Ellipse(xy=(x0, y0), width=a*2, height=b*2, angle=angle_deg, ec='black', fill=False, ls='--')
        plt.gca().add_patch(ell)

        # W_1: Major Axis Line (along the width/angle)
        x_w1 = x0 + a * np.cos(angle_rad)
        y_w1 = y0 + a * np.sin(angle_rad)
        plt.plot([x0, x_w1], [y0, y_w1], color='black', ls=':', lw=1, label='$W_1$ (Major)')
    
        # W_2: Minor Axis Line (perpendicular to W_1, angle + 90 deg)
        x_w2 = x0 + b * np.cos(angle_rad + np.pi/2)
        y_w2 = y0 + b * np.sin(angle_rad + np.pi/2)
        plt.plot([x0, x_w2], [y0, y_w2], color='black', ls=':', lw=1, label='$W_2$ (Minor)')
        plt.xlim(-0.04, 0.057)
        plt.ylim(-0.057, 0.04)
    
        plt.annotate("$W_1$", xy=(x0*1.2, y0*0.8), c='k')
        plt.annotate("$W_2$", xy=(x0*0.25, y0*1.4), c='k')
        plt.savefig('tmp/eb.png', bbox_inches='tight', pad_inches=1/50, dpi=600, transparent=True)
        # plt.savefig(config.PLOTS_PATH / ('beam_profile.pdf'), **{
        #     "format": "pdf",
        #     "dpi": 300,
        #     "bbox_inches": "tight",
        #     "pad_inches": 0.005
        #     }
        # )
        plt.show()

    for _br in [beam_res[3]]:
        _(**_br)
    return


@app.cell
def _():
    import matplotlib.image as mpimg
    return (mpimg,)


@app.cell(hide_code=True)
def _(I, beam_res, channel, mpimg, np, ph_orange, plt):
    def _(beam_shape, x0, y0, r0, x2, st):
        plt.figure(dpi=110, figsize=(3.4, 3.4))

        img = mpimg.imread("/home/klen/Desktop/thesis/tmp/aperture.png")
        _w = 0.1024 * 0.37
        plt.imshow(img, extent=[-_w,  _w, -_w,  _w])
    
        sigma = 0.03
        mask = np.exp(-channel.grid.get_rho2() / (2 * sigma**2))

        plt.imshow(
          I(channel, output=beam_shape) * mask, 
          cmap=ph_orange, 
          vmin=0, vmax=1100, 
          extent=channel.grid.extent
        )
        plt.plot([0, x0], [0, y0], lw=0.5, c='k', ls='--')
        # plt.plot([0, x0], [y0, y0], lw=1, c='k', ls=':')
        # plt.plot([x0, x0], [0, y0], lw=1, c='k', ls=':')
        # plt.scatter([x0], [y0], c='k', s=2)
        plt.annotate("", xy=(0,0), xytext=(x0, y0), arrowprops=dict(arrowstyle="<-", color='k'))
        # circle1 = plt.Circle((x0, y0), st/2, color='k', ls=(0, (14,11)), fill=False, zorder=10)
        # plt.gca().add_patch(circle1)

        # angle = Arc((0, 0), 0.012, 0.012, angle=0, theta1=0.0, theta2=np.arcsin(y0/r0) / 2 / np.pi * 360 )
        # plt.gca().add_patch(angle)
        # plt.annotate("", xy=(x0 - st/2*x0/r0, y0 - st/2*y0/r0), xytext=(x0 + st/2*x0/r0, y0 + st/2*y0/r0), arrowprops=dict(arrowstyle="<->", color='k'))

        plt.annotate("$r_0$", xy=(x0*0.67, y0*1), c='k')
        # plt.annotate("$(0,0)$", xy=(-0.01, -0.004), c='k')
        # plt.annotate("$y_0$", xy=(-0.008, y0*1.1), c='k')
        # plt.annotate("$x_0$", xy=(x0*1.1, 0.004), c='k')
        # plt.annotate("$\chi$", xy=(0.007, 0.002), c='k')

        plt.axhline(0,color='k', lw=0.5)
        plt.axvline(0,color='k', lw=0.5) 
        plt.xticks([]);
        plt.yticks([]);
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        plt.xlim(-0.043, 0.043)
        plt.ylim(-0.043, 0.043)
        # plt.xlim(-0.015, 0.0415)
        # plt.ylim(-0.01, 0.042)
        plt.gca().axis('off')
        # plt.gca().set_facecolor('#e9ebe8')
        # plt.gca().figure.patch.set_facecolor('#e9ebe8')
        plt.savefig('tmp/bw_eta.png', bbox_inches='tight', pad_inches=1/50, dpi=600, transparent=True)
        # plt.savefig(config.PLOTS_PATH / ('beam_profile.pdf'), **{
        #     "format": "pdf",
        #     "dpi": 300,
        #     "bbox_inches": "tight",
        #     "pad_inches": 0.005
        #     }
        # )
        plt.show()

    for _br in [beam_res[5]]:
        _(**_br)
    return


@app.cell
def _(I, beam_res, channel, mpimg, np, ph_orange, plt):
    def _(beam_shape, x0, y0, r0, x2, st):
        plt.figure(dpi=110, figsize=(3.4, 3.4))

        img = mpimg.imread("/home/klen/Desktop/thesis/tmp/aperture.png")
        _w = 0.1024 * 0.37
        plt.imshow(img, alpha=0.2, extent=[-_w,  _w, -_w,  _w])
    
        sigma = 0.03
        mask = np.exp(-channel.grid.get_rho2() / (2 * sigma**2))

        plt.imshow(
          I(channel, output=beam_shape) * mask, 
          cmap=ph_orange, 
          vmin=0, vmax=1100, 
          extent=channel.grid.extent
        )
        plt.plot([0, x0], [0, y0], lw=0.5, c='k', ls='--')
        # plt.plot([0, x0], [y0, y0], lw=1, c='k', ls=':')
        # plt.plot([x0, x0], [0, y0], lw=1, c='k', ls=':')
        # plt.scatter([x0], [y0], c='k', s=2)
        plt.annotate("", xy=(0,0), xytext=(x0, y0), arrowprops=dict(arrowstyle="<-", color='k'))
        # circle1 = plt.Circle((x0, y0), st/2, color='k', ls=(0, (14,11)), fill=False, zorder=10)
        # plt.gca().add_patch(circle1)

        # angle = Arc((0, 0), 0.012, 0.012, angle=0, theta1=0.0, theta2=np.arcsin(y0/r0) / 2 / np.pi * 360 )
        # plt.gca().add_patch(angle)
        # plt.annotate("", xy=(x0 - st/2*x0/r0, y0 - st/2*y0/r0), xytext=(x0 + st/2*x0/r0, y0 + st/2*y0/r0), arrowprops=dict(arrowstyle="<->", color='k'))

        plt.annotate("$r_0$", xy=(x0*0.67, y0*1), c='k')
        # plt.annotate("$(0,0)$", xy=(-0.01, -0.004), c='k')
        # plt.annotate("$y_0$", xy=(-0.008, y0*1.1), c='k')
        # plt.annotate("$x_0$", xy=(x0*1.1, 0.004), c='k')
        # plt.annotate("$\chi$", xy=(0.007, 0.002), c='k')

        plt.axhline(0,color='k', lw=0.5)
        plt.axvline(0,color='k', lw=0.5) 
        plt.xticks([]);
        plt.yticks([]);
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        plt.xlim(-0.043, 0.043)
        plt.ylim(-0.043, 0.043)
        # plt.xlim(-0.015, 0.0415)
        # plt.ylim(-0.01, 0.042)
        plt.gca().axis('off')
        # plt.gca().set_facecolor('#e9ebe8')
        # plt.gca().figure.patch.set_facecolor('#e9ebe8')
        plt.savefig('tmp/bw_eta_c.png', bbox_inches='tight', pad_inches=1/50, dpi=600, transparent=True)
        # plt.savefig(config.PLOTS_PATH / ('beam_profile.pdf'), **{
        #     "format": "pdf",
        #     "dpi": 300,
        #     "bbox_inches": "tight",
        #     "pad_inches": 0.005
        #     }
        # )
        plt.show()

    for _br in [beam_res[5]]:
        _(**_br)
    return


if __name__ == "__main__":
    app.run()
