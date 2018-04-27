import os
import logging as lg

lg.basicConfig(level=lg.DEBUG)

def launch_analysis(data_file):

    directory = os.path.dirname(os.path.dirname(__file__)) # we get the right path.
    path_to_file = os.path.join(directory, "data", data_file) # with this path, we go inside the folder `data` and get the file.

    try:
        with open(path_to_file, "r") as file:
            preview = file.readline()
            lg.debug("Yeah! We managed to read the file. Here is a preview: \n {}".format(preview))
    except FileNotFoundError as e:
        lg.critical('Ow :( The file was not found. Here is the message:\n {}'.format(e))

if __name__ == "__main__":

    launch_analysis('../data/SyceronBrut.xml')