#!/bin/bash
#######################################################################################
#
#    A helper script for fetching and copying tutorials and examples
#    into ~/tutorials
#
#
#######################################################################################

CWD=$(pwd)

TEMP_DIR=$CWD/temp_dir
mkdir -p $TEMP_DIR

cd $TEMP_DIR
# fetching a small/incomplete mangopy repo:
git clone -n https://github.com/astib/MANGO.git --depth 1
cd MANGO
git checkout b25cba78e58197394809cb8323656a1d636c3e3d mangopy_tutorial.ipynb
###############################################################################
# NOTE: If another commit is used as the source to install mango inside       #
# setup_py27_env.sh and setup_py36_env.sh then also change the corresponding  #
# commit in this file                                                         #
###############################################################################
mkdir -p ~/tutorials/mango
mv mangopy_tutorial.ipynb ~/tutorials/mango/.


cd $TEMP_DIR
git clone -n https://github.com/timduly4/pyglow.git --depth 1
cd pyglow
git checkout 83a055dae3aca540d0f862c7589a17fb14064e36 examples/*.py
###############################################################################
# NOTE: If another commit is used as the source to install the pyglow inside  #
# setup_pyglow.sh then also change the corresponding  commit in this file     #
###############################################################################
mkdir -p ~/tutorials/pyglow
mv examples/test_airglow.py ~/tutorials/pyglow/.
mv examples/test_iri12_iri16.py ~/tutorials/pyglow/.
mv examples/test_ne_airglow_profile.py ~/tutorials/pyglow/.
mv examples/test_user_indices.py ~/tutorials/pyglow/.

# cleanup
cd $CWD
rm -r $TEMP_DIR
