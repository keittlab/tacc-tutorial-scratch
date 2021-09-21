#INTRO

# tacc-tutorial-scratch

#First Login to TACC
```
/usr/local/etc/taccinfo
```

look around

```
ls
cd /scratch
pwd
cds
ls
pwd
$SCRATCH
cd /
pwd
cd $SCRATCH
ls
mkdir learning
cd learning
pwd
ls
```

get project files

```
module list 
```

see that git is already present?

```
git clone https://github.com/keittlab/tacc-tutorial-scratch.git

```
You'll probably need to go to https://github.com/settings/tokens and generate a personal access token
enable REPO, ADMIN:REPO_HOOK and DELETE_REPO
update token and use as your github login

note that we already have some form of python:

```
module list
```
and that python already has pip, as well as a lot of useful packages:

```
pip list
```

let's look at what we're going to run

```
vim hexbin.py
```

change output filename to something distinct
to do so, go to the location and press 'i' to enter text editing mode
then esc to exit that mode, followed by :wq to save and exit
someone (maybe not everyone) push it back to git so we can actually see the image

```
python hexbin.py
ls
git add .
git commit -m "new hexbin"
```

what if we know we'll need a newer version of python?

```
module load python3
pip list
python hexbin.py
```

#error!

```
python3 hexbin.py
```
what if we want to start installing packages?
for example, if we want to work with audio data, librosa is useful

```
vim audio_manipulations.py 
```

add line "import librosa"
feel free to add other functions such as librosa.load("Soundscape_2.wav")
exit

```
python3 audio_manipulations.py 
```

#error!

```
pip install librosa
```

#error!
Permission denied: '/opt/apps/intel18/python3/3.7.0/bin/pip'

```
cd /
# look around, not OUR home directory
cd $SCRATCH/learning
```

#Solution 1: virtualenv, a python library

```
virtualenv --python=/opt/apps/intel18/python3/3.7.0/bin/python3 .testvenv
ls
ls -a
source .testvenv/bin/activate
pip list
pip install librosa
pip list
python3 audio_manipulations.py 
```


next step would be to create a requirements.txt file and then pip install the whole batch at once

Virtual environments are great within python, but you can have 'dependency hell'
at any level of software, all the way up to the interaction between a particular version of linux
and the code you are running. In addition, unexpected interactions between layers of software or 
changes across versions of software don't always fail catastrophically: sometimes the only way you know it's 
happening is because the same  scientific calculations lead to different results (perhaps the algorithm in some 
computational library is made more efficient in a newer version, but different methods of approximation
happen to compound in a way that causes notably different results in your code. This itself is catastrophic
for replication and science in general.

So, let's abstract everything into containers!

# CONTAINERS

We first need to enter an interactive session, then load the singularity module

```
idev -m 40
module spider singularity
module load tacc-singularity
module list
singularity help
```

Immediately we can do stuff

```
singularity run docker://godlovedc/lolcow

git clone https://github.com/kahst/BirdNET.git
cd BirdNET
singularity pull docker://breallis/birdnet:cpu
singularity run birdnet_cpu.sif --i Soundscape_1.wav
singularity shell birdnet_cpu.sif
pip list
python which

```

Still within Singularity, look around your filesystem. Everything should be as normal






