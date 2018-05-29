#
# Module automatically generated by Updater v1.0
# @author Daniel J. Finnegan
#

import os
from subprocess import call

UPDATER_CMAKE_ARGS = ['-DBUILD_INSTALLER=OFF'] # Turn this on to build the installer
UPDATER_BUILD_CUSTOM = True # Set this to True if your project has a custom build function

# Default implementation just calls cmake
# Reimplement as you see fit
def build_full_package(project_root):
	if not os.path.isdir(os.path.join(project_root, 'bin')):
		os.mkdir(os.path.join(project_root, 'bin'))

	os.chdir(os.path.join(project_root, 'bin'))
	call(['cmake'] + UPDATER_CMAKE_ARGS + ['..'])
	call(['cmake', '--build', '.'])

####################################################################
