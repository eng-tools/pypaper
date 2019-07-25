import os

initials = "###INITIALS###"

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/"
PUB_PATH = ROOT_DIR + "%s_paper/" % initials
FIG_FOLDER = "%s-figures" % initials
PUB_FIG_PATH = PUB_PATH + FIG_FOLDER + "/"
TEMP_FIG_PATH = ROOT_DIR + "temp/"
MODULE_DATA_PATH = ROOT_DIR + "data/"  # no initials, consistent with python science environment from PyCharm

# add project specific paths here

# import user_paths as up

# import user specific paths here
# if hasattr(up, 'EXTERNAL_DATABASE_PATH'):
#     EXTERNAL_DATABASE_PATH = up.EXTERNAL_DATABASE_PATH
# else:
#     EXTERNAL_DATABASE_PATH = '<set-path-to-EXTERNAL_DATABASE_PATH>'
