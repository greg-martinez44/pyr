import os

import pytest
from matplotlib.testing.decorators import check_figures_equal

from rfuncs import *

@pytest.fixture
def tearDown():
    yield
    if os.path.exists("test_plot.pdf"):
        os.remove("test_plot.pdf")

@check_figures_equal(extensions=["png"])
def test_plot_builds_scatterplot_by_default(fig_test, fig_ref):
    x = rnorm(100)
    y = rnorm(100)

    test_ax = fig_test.subplots()
    plt.sca(test_ax)
    plot(x,y)

    fig_ref.subplots().scatter(x, y)

@check_figures_equal(extensions=["png"])
def test_plot_builds_scatterplot_with_different_labels(fig_test, fig_ref):
    x = rnorm(100)
    y = rnorm(100)

    test_ax = fig_test.subplots()
    plt.sca(test_ax)
    plot(x, y, xlab="X label", ylab="Y label", main="Plot Title")

    ref_ax = fig_ref.subplots()
    plt.sca(ref_ax)
    plt.scatter(x, y)
    ref_ax.set_xlabel("X label")
    ref_ax.set_ylabel("Y label")
    plt.title("Plot Title")

@check_figures_equal(extensions=["png"])
def test_plot_builds_scatterplot_with_color(fig_test, fig_ref):
    x = rnorm(100)
    y = rnorm(100)

    test_ax = fig_test.subplots()
    plt.sca(test_ax)
    plot(x, y, col="green")

    ref_ax = fig_ref.subplots()
    plt.sca(ref_ax)
    plt.scatter(x, y, c="green")

def test_pdf_saves_figures_as_pdfs(tearDown):
    x = rnorm(100)
    y = rnorm(100)

    fig = plt.figure()
    ax = fig.subplots()
    plt.sca(ax)
    test_plot = plot(x, y, col="green")

    pdf(fig, "test_plot.pdf")

    assert "test_plot.pdf" in os.listdir(".")
