#coding=utf-8
import os

allfile = os.listdir('./')

for name in allfile:
	if name[:2].isnumeric():
		os.rename(name, 'F_'+name)
	else:
		os.rename(name, 'F_0'+name)