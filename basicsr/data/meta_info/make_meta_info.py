import os

path = "/home/knuvi/Desktop/hyunobae/BasicSR/datasets/val/gt"
f = open('meta_info_Compressed_test_GT.txt', "w")

flist = os.listdir(path)

for file in flist:
    num = os.listdir(path+'/'+file)
    f.write(f"{file} {len(num)} (540,960,3)\n")
    print(f"{file} {len(num)} (540,960,3)\n")
f.close()
