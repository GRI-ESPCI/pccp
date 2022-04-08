import sys
import os

from pccp import create_app

project = "pccp"

BASE_DIR = os.path.join(os.path.dirname(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

application = create_app()
