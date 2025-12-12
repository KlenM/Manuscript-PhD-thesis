import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pyatmosphere as pyatm
    import matplotlib.pyplot as plt

    plt.style.use("klen.mplstyle")
    return mo, np, plt, pyatm


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    I need to make plot in matplotlib and edit in inkscape.

    With `text.usetex: True` we can't change fonts at all for some reasons.
    Export to .pdf breaks `cmmi10` font greek letters. 
    Export to .pgf just useless trash for this task.

    Anyway you can't change latex expression in inkspace - you can rasterize them. You can do the same with the text - just recreate in inkscape from scratch if needed. Moreover, `.svg` preserves text, which you can edit in inkscape XML editor. So, use `.svg`.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Examples for PSD scales (`fig:psd_scales`)""")
    return


@app.cell
def _(np, pyatm):
    from pyatmosphere.gpu import get_xp

    class AndrewsModel(pyatm.theory.models.Model):
        def psd_n(self, kappa):
            xp = get_xp()
            kl = 3.3 / self.l0
            k0 = (2 * np.pi) / self.L0
            k_per_kl = kappa / kl
            return 0.033 * self.Cn2 * (1 + 1.802 * k_per_kl - 0.254 * k_per_kl**(7/6)) * \
                xp.exp(-(k_per_kl)**2) / (kappa**2 + k0**2)**(11/6)


    class KolmogorovModel(pyatm.theory.models.Model):
        def psd_n(self, kappa):
            return 0.033 * self.Cn2 * kappa**(-11/3)
    return AndrewsModel, KolmogorovModel


@app.cell
def _(AndrewsModel, KolmogorovModel, np, plt, pyatm):
    _x = np.unique(np.concatenate([
        np.logspace(np.log10(4e-5), np.log10(2 * 1e-3), 40, endpoint=False), 
        np.logspace(np.log10(2 * 1e-3), np.log10(80/2), 20, endpoint=False), 
        np.logspace(np.log10(80/2), np.log10(1000), 40, endpoint=False), 
        ]))
    _k = 2 * np.pi / _x
    _E_K = KolmogorovModel(Cn2=1e-14, l0=3e-3, L0=80).psd_n(_k)
    _E_MVK = pyatm.theory.models.MVKModel(Cn2=1e-14, l0=3e-3, L0=80).psd_n(_k)
    _E_Andr = AndrewsModel(Cn2=1e-14, l0=3e-3, L0=80).psd_n(_k)

    _f, _ax = plt.subplots(figsize=(150/25.4, 60/25.4))
    _ax.plot(_k, _E_K)
    _ax.plot(_k, _E_MVK)
    # _ax.plot(_k, _E_Andr, c='red')
    _ax.tick_params(axis='y', left=False, labelleft=False)

    _ax.axvline(2*np.pi / 1e-3, color='black', lw=1, ls='--')
    _ax.axvline(2*np.pi / 80, color='black', lw=1, ls='--')

    _ax.text(2*np.pi / 80 - 4.2e-2, 1e-44, r'$\frac{2\pi}{L_0}$')
    _ax.text(2*np.pi / 1e-3 - 3500, 1e-44, r'$\frac{2\pi}{l_0}$')

    _top = 1e-3
    _ax.text(6e-3, _top, 'Energy', fontsize=12)
    _ax.text(2, _top, 'Inertial range', fontsize=12)
    _ax.text(1.2e4, _top, 'Dissipation', fontsize=12)
    _ax.annotate('', 
        xy=(0.85, 0.82), xycoords='axes fraction',    # end
        xytext=(0.11, 0.82), textcoords='axes fraction',  # start
        arrowprops=dict(arrowstyle='->', linewidth=1, color='black', mutation_scale=20)
    )

    _ax.set_ylim(1e-50, 1000)
    _ax.set_xscale('log')
    _ax.set_yscale('log')
    _ax.set_xlabel(r"$\mathrm{log}\,k$")
    _ax.set_ylabel(r"PSD $\mathrm{log}\,\Phi(k)$")

    _f.tight_layout()
    # _f.savefig('generated/psd_scales.svg')
    _f
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Misc libs""")
    return


@app.cell
def _():
    def plt_fonts(query):
        import matplotlib.font_manager as fm

        for f in fm.findSystemFonts():
            if query in f:
                prop = fm.FontProperties(fname=f)
                print(f, "->", prop.get_name())

    plt_fonts('latin')
    return


if __name__ == "__main__":
    app.run()
