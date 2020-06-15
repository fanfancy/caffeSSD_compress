# -*- coding:utf-8 -*-
import numpy as np
np.set_printoptions(threshold=np.inf)
import caffe
from caffe.model_libs import *
#import _init_paths
import collections
from collections import OrderedDict
caffe.set_mode_cpu

net0 = caffe.Net('/home/zs/workspace/fanxi/caffe2/models/VGGNet/NWPU_VHR/SSD_300x300_0323_conv6/deploy.prototxt',\
    '/home/zs/workspace/fanxi/caffe2/models/VGGNet/NWPU_VHR/SSD_300x300_0323_conv6/VGG_NWPU_VHR_SSD_300x300_0323_conv6_iter_22000.caffemodel',caffe.TRAIN) #TEST/TRAIN

params_txt = "params.txt"
pf = open (params_txt,'w')
wsum=0
bsum=0

for param_name in net0.params.keys():
      weights= net0.params[param_name][0].data
      if (len(net0.params[param_name]) > 1) :
            bias=net0.params[param_name][1].data
            bsum += len(bias)
      weights.shape=(-1,1)
      wsum += weights.shape[0]
      print ('\n')
      print (param_name)
      print ("weights,",weights.shape)
      print ("bias,",len(bias))
      #pf.write(param_name)
     
      #pf.write('\n')
      #pf.write('\n' + param_name + '_weight:\n\n')  
      
      #for w in weights:
      #      pf.write('%ff,'%w)
      #pf.write('\n\n' + param_name + '_bias:\n\n')  
      #for b in bias:
      #      pf.write('%ff,'%b)
      
      #pf.write('\n\n')
print ("wsum,",wsum)
print ("wsum/MB,",wsum*4)
print ("bsum,",bsum)
print ("bsum/MB,",bsum*4)

print ("w+bsum/MB,",wsum*4+bsum*4)
pf.close