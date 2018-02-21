import matplotlib.pyplot as plt
from bwplot import cbox
import all_paths as ap
from engformat import plot_tools as efpt
from engformat import plot as efp
from engformat import plot_outputs as efpo

font_prop = {'size': 9}


def create(save=0, show=0):

    bf, subplot = plt.subplots()
    subplot.plot([0], [0], label="", c=cbox(0))

    subplot.set_xlabel('Period [s]')
    # subplot.set_xscale('log')
    subplot.set_ylabel('Disp. Response [m]')
    efp.xy(subplot, x_origin=True, y_origin=True)
    efpt.revamp_legend(subplot, loc="upper left", prop=font_prop)

    bf.tight_layout()
    name = __file__.replace('.py', '')
    name = name.split("figure_")[-1]
    extension = ""
    if save == 1:
        efpo.save_figure(ap, bf, name, save=save, extension=extension)
    elif save == 2:
        print(efpo.save_figure(ap, bf, name, save=save, latex=False))  # publish
    if show:
        plt.show()


if __name__ == '__main__':
    create(save=0, show=1)
