import os

initials = "###INITIALS###"

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/"
PUBLICATION_PATH = ROOT_DIR + "%s_paper/" % initials
FIGURE_FOLDER = "%s-figures/" % initials
PUBLICATION_FIGURE_PATH = PUBLICATION_PATH + FIGURE_FOLDER
TEMP_FIGURE_PATH = ROOT_DIR + "temp/"
MODULE_DATA_PATH = ROOT_DIR + "%s_data/" % initials

# add project specific paths here

# import user_paths as up

# import user specific paths here