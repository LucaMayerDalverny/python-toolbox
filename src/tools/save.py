"""
Contains functions for saving data representations
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, ScalarFormatter


def graph(directory, curves, legends,
          abscissa_label, ordinate_label, title=None,
          show_grid=False, abscissa_scale=None, ordinate_scale=None):
    """
    Save a graph containing one or multiple curves as an image.

    Parameters
    ----------
    directory : string
        The directory where the graph will be saved.
    curves : list[list[int or float]]
        The list of curves to plot in the graph.
    legends : list[string]
        The labels corresponding to the curves.
    abscissa_label : string
        The label for the abscissa axis.
    ordinate_label : string
        The label for the ordinate axis.
    title : string
        The main title for the graph.
    show_grid : bool
        To show the grid of the graph.
    abscissa_scale : string
        The scale to use for the abscissa axis.
        ('linear', 'log', 'logit' etc.)
    ordinate_scale : string
        The scale to use for the ordinate axis.
        ('linear', 'log', 'logit' etc.)
    
    Examples
    --------
    >>> import src.tools.save as save
    >>> identity = [ i for i in range(10)]
    >>> square = [ i*i for i in range(10) ]
    >>> save.graph("functions.svg", [identity, square], ["y = x", "y = x²"], "x", "y", "Usual functions")
    """

    # Plotting the curves in the graph
    for curve_idx in range(len(curves)):
        plt.plot(curves[curve_idx])

    # Addition of the labels for the axis
    plt.xlabel(abscissa_label)
    plt.ylabel(ordinate_label)

    # Addition of the graph title
    if title is not None:
        plt.title(title)

    # Setting the scale for the abscissa axis
    if abscissa_scale is not None:
        plt.xscale(abscissa_scale)
        plt.gca().xaxis.set_minor_formatter(NullFormatter())
        plt.gca().xaxis.set_major_formatter(ScalarFormatter())

    # Setting the scale for the ordinate axis
    if ordinate_scale is not None:
        plt.yscale(ordinate_scale)
        plt.gca().yaxis.set_minor_formatter(NullFormatter())
        plt.gca().yaxis.set_major_formatter(ScalarFormatter())

    # Showing the grid on the graph
    plt.grid(True) if show_grid else ""

    # Placing the legend at the best location in the graph
    plt.legend(legends, loc='best')

    # Saving the figure
    plt.savefig(directory)
    plt.close('all')
