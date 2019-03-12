"""
A script executor.

This is an executer of scripts.
It's intended to install all the requirements and run a script.
"""
import sys
import re
import subprocess


def install_requirements():
    """Look for and install the software requirements."""
    script_name = input("Insert the script file name ")
    requirement_file = input("Insert the requirements file name ")
    installed_packages = subprocess.check_output(
        [sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [re.findall("[a-zA-Z-]+", e.decode("utf-8"))
                          for e in installed_packages.split()]
    try:
        with open(requirement_file, 'r') as r:
            requirements = r.readlines()
            for line in requirements:
                line = re.findall("[a-zA-Z-]+", line)
                if line not in installed_packages:
                    subprocess.call([sys.executable, '-m', 'pip',
                                     'install', '--upgrade', line])
                    installed_packages.append(line)
        r.close()
        subprocess.call(
            [sys.executable, script_name])
    except Exception as e:
        print("There isn't an existent requirement file called "
              + requirement_file)
        print(e)
        return


if __name__ == '__main__':
    subprocess.call(
        [sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    install_requirements()
