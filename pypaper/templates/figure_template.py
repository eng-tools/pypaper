import matplotlib.pyplot as plt
from bwplot import cbox
import all_paths as ap
import engformat as ef
import settings as ops

font_prop = {'size': 9}


def create(save=0, show=0):

    bf, subplot = plt.subplots()
    subplot.plot([0], [0], label="", c=cbox(0))

    subplot.set_xlabel('Period [s]')
    # subplot.set_xscale('log')
    subplot.set_ylabel('Disp. Response [m]')
    ef.xy(subplot, x_origin=True, y_origin=True)
    ef.revamp_legend(subplot, loc="upper left", prop=font_prop)

    bf.tight_layout()
    name = __file__.replace('.py', '')
    name = name.split("figure_")[-1]
    extension = ""
    if save == 2:
        ef.save_figure(ap, bf, name, publish=True, name_ext=extension, ftype=ops.PUBLICATION_FILE_TYPE,
                       latex=False, dpi=ops.PUBLICATION_DPI)
    elif save == 1:
        ef.save_figure(ap, bf, name, name_ext="")
    if show:
        plt.show()


if __name__ == '__main__':
    create(save=0, show=1)
