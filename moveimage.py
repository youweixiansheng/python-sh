import os,shutil,glob

os.mkdir('CVT')
os.mkdir('DTCWT')
os.mkdir('DTMDCT')
os.mkdir('FPDE')
os.mkdir('GFF')
os.mkdir('GTF')
os.mkdir('HMSD')
os.mkdir('LEPLC')
os.mkdir('LP')
os.mkdir('LPSR')
os.mkdir('MSVD')
os.mkdir('NSCT')
os.mkdir('OIPCNN')
os.mkdir('RP')
os.mkdir('Wavelet')

for file_name in glob.glob('resultimage/*CVT*'):
	shutil.move(file_name,'CVT/') 
for file_name in glob.glob('resultimage/*DTCWT*'):
	shutil.move(file_name,'DTCWT/') 
for file_name in glob.glob('resultimage/*DTMDCT*'):
	shutil.move(file_name,'DTMDCT/') 
for file_name in glob.glob('resultimage/*FPDE*'):
	shutil.move(file_name,'FPDE/') 
for file_name in glob.glob('resultimage/*GFF*'):
	shutil.move(file_name,'GFF/') 
for file_name in glob.glob('resultimage/*GTF*'):
	shutil.move(file_name,'GTF/') 
for file_name in glob.glob('resultimage/*HMSD*'):
	shutil.move(file_name,'HMSD/') 
for file_name in glob.glob('resultimage/*LEPLC*'):
	shutil.move(file_name,'LEPLC/') 
for file_name in glob.glob('resultimage/*LP*'):
	shutil.move(file_name,'LP/') 
for file_name in glob.glob('resultimage/*LPSR*'):
	shutil.move(file_name,'LPSR/') 
for file_name in glob.glob('resultimage/*MSVD*'):
	shutil.move(file_name,'MSVD/') 
for file_name in glob.glob('resultimage/*NSCT*'):
	shutil.move(file_name,'NSCT/') 
for file_name in glob.glob('resultimage/*OIPCNN*'):
	shutil.move(file_name,'OIPCNN/') 
for file_name in glob.glob('resultimage/*RP*'):
	shutil.move(file_name,'RP/')
for file_name in glob.glob('resultimage/*Wavelet*'):
	shutil.move(file_name,'Wavelet/') 
# shutil.move('resultimage/*DTCWT*','DTCWT/')
# shutil.move('resultimage/*DTMDCT*','DTMDCT/')
# shutil.move('resultimage/*FPDE*','FPDE/')
# shutil.move('resultimage/*GFF*','GFF/')
# shutil.move('resultimage/*GTF*','GTF/')
# shutil.move('resultimage/*HMSD*','HMSD/')
# shutil.move('resultimage/*LEPLC*','LEPLC/')
# shutil.move('resultimage/*LP*','LP/')
# shutil.move('resultimage/*LPSR*','LPSR/')
# shutil.move('resultimage/*MSVD*','MSVD/')
# shutil.move('resultimage/*NSCT*','NSCT/')
# shutil.move('resultimage/*OIPCNN*','OIPCNN/')
# shutil.move('resultimage/*RP*','RP/')
# shutil.move('resultimage/*Wavelet*','Wavelet/')
