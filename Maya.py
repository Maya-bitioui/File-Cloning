import os, sys, platform

os.system('git pull')

bit = platform.architecture()[0]

if bit == '64bit':
  import maya64

elif bit == '32bit':
	import maya32
