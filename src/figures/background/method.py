import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pyatmosphere as pyatm
    import matplotlib.pyplot as plt

    pyatm.gpu.config['use_gpu'] = True
    xp = pyatm.gpu.get_xp()
    plt.style.use("../klen.mplstyle")
    return np, plt


@app.cell
def _(plot_subharmonic_grid, plt):
    _f, _ax = plt.subplots(1, 2, figsize=(150/25.4, 60/25.4))
    plot_subharmonic_grid(_ax[0])
    _f
    return


@app.cell
def _(np, plt):

    def plot_subharmonic_grid(ax):
        # 1. Regular FFT Sampling Grid (Level 0)
        # Represented as a coarse grid across the domain
        fft_range = np.linspace(-1, 1, 7)
        X, Y = np.meshgrid(fft_range, fft_range)
        ax.scatter(X, Y, c='lightgray', s=20, label='Regular FFT Sampling', alpha=0.6)
    
        # 2. Level 1 Subharmonics
        # Sampling the central 3x3 area of the previous level with 3x3 points
        l1_range = np.linspace(-1/3, 1/3, 3)
        X1, Y1 = np.meshgrid(l1_range, l1_range)
        # Filter out the origin to show refinement around it
        ax.scatter(X1, Y1, c='royalblue', s=60, marker='s', edgecolors='black', 
                   label='Subharmonics Level 1')
    
        # 3. Level 2 Subharmonics
        # Sampling the central area of Level 1 with 3x3 points
        l2_range = np.linspace(-1/9, 1/9, 3)
        X2, Y2 = np.meshgrid(l2_range, l2_range)
        ax.scatter(X2, Y2, c='crimson', s=40, marker='o', edgecolors='black', 
                   label='Subharmonics Level 2')

        # Formatting
        # ax.set_title("Subharmonics Phase Screen Grid Structure", fontsize=14, pad=20)
        # ax.set_xlabel("Normalized Spatial Frequency ($f_x$)", fontsize=12)
        # ax.set_ylabel("Normalized Spatial Frequency ($f_y$)", fontsize=12)
        ax.axhline(0, color='black', linewidth=0.8, alpha=0.3)
        ax.axvline(0, color='black', linewidth=0.8, alpha=0.3)
        # ax.legend(loc='upper right', frameon=True, shadow=True)
        ax.set_aspect('equal')
        ax.grid(True, linestyle='--', alpha=0.3)
    
        # Zoom in slightly to see the subharmonics clearly
        ax.set_xlim(-1.1, 1.1)
        ax.set_ylim(-1.1, 1.1)

        plt.tight_layout()
        plt.show()

    return (plot_subharmonic_grid,)


@app.cell
def _(np, plt):

    def plot_log_radial_grid():
        # 1. Create a figure and polar axes
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})

        # 2. Set the radial axis to logarithmic scale
        # Note: Log scale cannot start at exactly 0.
        ax.set_rscale('symlog', linthresh=0.1) 
        # Alternatively, use 'log' if you don't need the center (0,0)
        # ax.set_yscale('log') # Matplotlib often maps radial to 'y' internally

        # 3. Define the radial limits (e.g., from 0.1 to 100)
        rmin, rmax = 0.1, 100
        ax.set_ylim(rmin, rmax)

        # 4. Generate some sample data
        theta = np.linspace(0, 2*np.pi, 500)
        # A spiral that grows exponentially
        r = 0.1 * np.exp(0.1 * theta * 10) 
    
        # 5. Plot the data
        ax.plot(theta, r, color='crimson', lw=2, label='Exponential Spiral')

        # 6. Customize Grid and Ticks
        # Set radial ticks at powers of 10
        rticks = [0.1, 1, 10, 100]
        ax.set_rticks(rticks)
        ax.set_yticklabels([f'$10^{{{int(np.log10(t))}}}$' for t in rticks])
    
        # Enable minor grid lines for the log effect
        ax.grid(True, which='both', linestyle='--', alpha=0.5)

        ax.set_title("Logarithmic Radial Grid Representation", pad=30, fontsize=14)
        ax.legend(loc='lower right')

        plt.show()

    plot_log_radial_grid()
    return


@app.cell
def _(np, plt):

    def generate_log_radial_points(n_rings=10, n_per_ring=12, r_min=0.1, r_max=100):
        # 1. Generate radii uniform in log space
        # This creates 'n_rings' levels between r_min and r_max
        radii = np.logspace(np.log10(r_min), np.log10(r_max), n_rings)
    
        # 2. Generate angles uniform in linear space (0 to 2*pi)
        angles = np.linspace(0, 2*np.pi, n_per_ring, endpoint=False)
    
        # 3. Create the grid
        R, Theta = np.meshgrid(radii, angles)
    
        # Convert to Cartesian for plotting or FFT processing
        X = R * np.cos(Theta)
        Y = R * np.sin(Theta)
    
        return X.flatten(), Y.flatten(), radii

    # Generate the data
    x_pts, y_pts, r_levels = generate_log_radial_points()

    # --- Visualization ---
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot the points
    ax.scatter(x_pts, y_pts, c='royalblue', s=15, alpha=0.7, label='Log-Radial Samples')

    # Draw concentric circles to show the log-spacing
    for r in r_levels:
        circle = plt.Circle((0, 0), r, color='gray', fill=False, linestyle='--', alpha=0.3)
        ax.add_artist(circle)

    # Formatting
    ax.set_aspect('equal')
    ax.set_xlim(-110, 110)
    ax.set_ylim(-110, 110)
    ax.set_title("Uniform Sampling in Log-Radial Scale", fontsize=14)
    ax.set_xlabel("$f_x$ (Frequency)")
    ax.set_ylabel("$f_y$ (Frequency)")
    ax.grid(True, which='both', alpha=0.1)
    ax.legend()

    plt.show()
    return


if __name__ == "__main__":
    app.run()
