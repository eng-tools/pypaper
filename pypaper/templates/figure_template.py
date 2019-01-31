import matplotlib.pyplot as plt
from bwplot import cbox
import engformat as ef

from ###INITIALS###_scripts.tools import fig_functions as ff
import all_paths as ap

import settings as ops


def create(save=0, show=0):

    bf, subplot = plt.subplots(figsize=(ops.TWO_COL, 4))
    subplot.plot([0], [0], label="", c=cbox(0))

    subplot.set_xlabel('Period [s]')
    # subplot.set_xscale('log')
    subplot.set_ylabel('Disp. Response [m]')
    ef.xy(subplot, x_origin=True, y_origin=True)
    ef.revamp_legend(subplot, loc="upper left", prop={'size': 9})

    bf.tight_layout()
    name = __file__.replace('.py', '')
    name = name.split("figure_")[-1]
    extension = ""
    if save:
        bf.savefig(ap.PUB_FIG_PATH + name + extension + ops.PUB_FIG_FILE_TYPE, dpi=ops.PUB_FIG_DPI)
        if ops.PUB_DOCUMENT_TYPE == "latex":
            para = ef.latex_for_figure(ap.FIG_FOLDER, name=ap.PUB_FIG_PATH + name + extension, ftype=ops.PUB_FIG_FILE_TYPE)
            print(para)
    if show:
        plt.show()


if __name__ == '__main__':
    create(save=0, show=1)
