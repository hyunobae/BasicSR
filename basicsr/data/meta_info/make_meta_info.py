import os

path = "/home/knuvi/Desktop/hyunobae/BasicSR/datasets/vvc/gt"
f = open('meta_info_Compressed_vvc_GT.txt', "w")

flist = os.listdir(path)

for file in flist:
    num = os.listdir(path+'/'+file)
    f.write(f"{file} {len(num)} (544,960,1)\n")
    print(f"{file} {len(num)} (544,960,1)\n")
f.close()
