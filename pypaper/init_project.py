import shutil
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/"

manage_ffp = ROOT_DIR + "manage.py"
shutil.copy(manage_ffp, "manage.py")


