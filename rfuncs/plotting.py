import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def plot(x, y, xlab:str=None, ylab:str=None, main:str=None, col:str=None):
    """Creates a scatter plot from data points."""
    if xlab:
        plt.xlabel(xlab)
    if ylab:
        plt.ylabel(ylab)
    if main:
        plt.title(main)
    return plt.scatter(x, y, c=col)

def pdf(fig, filename:str) -> None:
    """Saves a figure as a pdf."""
    with PdfPages(filename) as pdf:
        pdf.savefig(fig)
        plt.close()
