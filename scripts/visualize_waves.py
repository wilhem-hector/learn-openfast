"""Plot wave elevation from OpenFAST output using the shared figure settings."""

import matplotlib.pyplot as plt

if __package__:
    from . import figureSettings
else:
    import figureSettings


def plot_wave_elevation(time, elevation):
    """Plot time in seconds against Wave1Elev in metres; return the figure."""
    fig, ax = plt.subplots(figsize=(12, 4), layout="constrained")
    ax.plot(time, elevation)
    ax.set_xlabel("Simulation time [s]")
    ax.set_ylabel("Wave elevation [m]")
    ax.grid(True, alpha=0.3)
    ax.margins(x=0)
    return fig
