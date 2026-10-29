"""
Adaption of the standalone script to read an ASCII OpenFAST output and plot some channels.

Contact: Wilhem Hector
Initially written by: E Branlard
"""
import matplotlib.pyplot as plt
from openfast_toolbox.io import FASTOutputFile

# Apply the shared style for both package imports and standalone use.
if __package__:
    from . import figureSettings
else:
    import figureSettings

# --- Example Parameters
# outfile      = 'Main.out'
# plotChannels = ['OoPDefl1','IPDefl1','TTDspFA','TTDspSS']

def plot_couple_channels(outfile, plotChannels):
    """
    outfile: str
        Relative to the output file from the openfast run
    plotChannels: list of str
        List of channels to plot
    """
    fastout = FASTOutputFile(str(outfile))# the toolbox expects a string filename
    data = fastout.toDataFrame().values
    channels = fastout.channels
    units = fastout.units
    print('Available channels:', channels)

    # --- Plot list of selected channels
    nPlots = len(plotChannels)
    time = data[:,0]

    fig,axes = plt.subplots(
        nPlots, 1, sharex=True, squeeze=False,
        figsize=(12, 3.5 * nPlots), layout="constrained"
    )

    for ax, chan in zip(axes[:, 0], plotChannels):
        # Find index of plot channel within data
        id = channels.index(chan)
        ax.plot(time, data[:,id])
        ax.set_xlabel('Time (s)')
        ax.set_ylabel(channels[id] + ' ' + units[id])
        ax.grid()
    plt.show()
    return fig, axes[:, 0]
