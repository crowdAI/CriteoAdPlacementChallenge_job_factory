import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

from rq.cli import worker
if __name__ == '__main__':
    #TODO: Enable passing config information here
    sys.exit(worker())
