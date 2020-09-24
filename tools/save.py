"""
This module contains functions for saving data representations.
"""
import matplotlib
matplotlib.use('Agg')                                           # Necessary to remove a tkinter issue
import matplotlib.pyplot as plt                                 # Used for plotting data
from matplotlib.ticker import NullFormatter, ScalarFormatter    # Used for the graph axis scale modifications
import numpy as np                                              # Used for reshaping images before saving them
from numpy import ndarray


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
    Saving a graph containing two functions
    >>> import tools.save as save
    >>> identity = [ i for i in range(10)]
    >>> square = [ i*i for i in range(10) ]
    >>> save.graph("usual-functions.svg", [identity, square],
    >>>            ["y = x", "y = x²"], "x", "y", "Usual functions")

    Saving two graphs containing the same homographic function but using different scales for the ordinate axis
    >>> import tools.save as save
    >>> function = [ 1 - (1 / i) for i in range(1, 100) ]
    >>>
    >>> save.graph("homographic-function.png", [function], ["f"],
    >>>            "x", "y", "Homographic function", show_grid=True)
    >>>
    >>> save.graph("homographic-function-logit.png", [function], ["f"],
    >>>            "x", "y", "Homographic function", show_grid=True,
    >>>            ordinate_scale='logit')
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


def images(directory, image_data, label_data=None, gray_levels=False):
    """
    Save a 2D array of images as one png file.

    Parameters
    ----------
    directory : string
        The directory where the image will be saved.
    image_data : ndarray
        The 2D array of images to save.
    label_data : ndarray
        The 2D array of labels corresponding to the images.
    gray_levels : bool
        Save the images in gray levels.

    Examples
    --------
    >>> import tools.save as save
    >>> images_data = np.random.rand(5, 5, 32, 32)
    >>> labels = np.random.randint(0, 10, (5, 5))
    >>> save.images("images.png", images_data, labels, gray_levels=False)

    References
    ----------

    The code is adapted from the following page :
    https://medium.com/@mrdatascience/how-to-plot-mnist-digits-using-matplotlib-65a2e0cc068
    """

    col_number = image_data.shape[1]
    row_number = image_data.shape[0]

    fig, axes = plt.subplots(row_number, col_number, figsize=(1.5 * col_number, 2 * row_number))

    if (col_number == 1 and row_number != 1) or (col_number != 1 and row_number == 1):
        axes = np.reshape(axes, (row_number, col_number))
    elif col_number == 1 and row_number == 1:
        axes = np.array([[axes]])

    for col in range(col_number):
        for row in range(row_number):
            ax = axes[row, col]

            # Plot the images in gray if the parameters indicates it
            if gray_levels:
                ax.imshow(image_data[row, col], cmap='gray')
            else:
                ax.imshow(image_data[row, col])

            # If there is a label array, the label are displayed
            if label_data is not None:
                ax.set_title('Label : {}'.format(label_data[row, col]))

            # Removing the axis
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)

    plt.savefig(directory)
    plt.close('all')
