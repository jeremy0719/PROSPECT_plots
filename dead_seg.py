import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


listDec = np.array([0,1,2,3,5,6,8,9,10,11,12,13,16,18,21,23,27,28,29,31,32,34,36,38,41,42,43,44,46,47,48,50,52,56,60,61,66,69,70,71,72,73,79,83,86,87,97,98,102,103,115,121,122,123,124,126,127,128,136,139,141,144,146,152],dtype=np.int32)
listApr = np.array([0,1,2,3,6,9,11,13,18,21,23,27,32,44,79,86,139],dtype=np.int32)
listAug = np.array([0, 1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 18, 21, 23, 27, 31, 32, 34, 41, 43, 44, 46, 47, 48, 50, 52, 55, 56, 60, 63, 69, 73, 79, 83, 86, 87, 115, 122, 126, 127, 133, 139],dtype=np.int32)

flag = 'Dec'

if flag == 'Apr':
    list_select = listApr
elif flag == 'Aug':
    list_select = listAug
elif flag == 'Dec':
    list_select = listDec


x = list_select % 14 
y = list_select // 14



a, dx, dy, image = plt.hist2d(x,y,bins=(14,11),range=[[-0.5,13.5],[-0.5,10.5]])
for i in range(len(list_select)):
    plt.text(x[i],y[i],list_select[i],fontsize=12,horizontalalignment='center',verticalalignment='center')
for dd in dx:
    plt.vlines(x=dd, ymin=-0.5, ymax=10.5, linestyles='--', linewidth=1)
for dd in dy:
    plt.hlines(y=dd, xmin=-0.5, xmax=13.5, linestyles='--', linewidth=1)
# plt.show()
plt.savefig("figs/dead_seg"+ flag + ".pdf")