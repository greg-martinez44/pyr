import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def plot(x, y, xlab=None, ylab=None, main=None, col=None):
    if xlab:
        plt.xlabel(xlab)
    if ylab:
        plt.ylabel(ylab)
    if main:
        plt.title(main)
    return plt.scatter(x, y, c=col)

def pdf(fig, filename):
    with PdfPages(filename) as pdf:
        pdf.savefig(fig)
        plt.close()
