# -*- coding:utf-8 -*-
import numpy as np
np.set_printoptions(threshold=np.inf)
import caffe
from caffe.model_libs import *
#import _init_paths
import collections
from collections import OrderedDict
caffe.set_mode_cpu
'''
net0 = caffe.Net('/home/zs/workspace/fanxi/caffe/models/VGGNet/NWPU_VHR512/SSD_512x512/deploy.prototxt',\
    '/home/zs/workspace/fanxi/caffe/models/VGGNet/NWPU_VHR512/SSD_512x512/VGG_NWPU_VHR512_SSD_512x512_iter_100000.caffemodel',caffe.TRAIN) #TEST/TRAIN
'''
net0 = caffe.Net('/home/zs/workspace/fanxi/caffe2/models/VGGNet/NWPU_VHR/SSD_300x300_0323_conv6/deploy.prototxt',\
    '/home/zs/workspace/fanxi/caffe2/models/VGGNet/NWPU_VHR/SSD_300x300_0323_conv6/VGG_NWPU_VHR_SSD_300x300_0323_conv6_iter_26000.caffemodel',caffe.TRAIN) #TEST/TRAIN
    #�ҵ�python�ű���prototxt,caffemodel�ļ�����ͬ��Ŀ¼���ˣ�����ļ�·�������޸�?#for k,v in net0.params.items():
#  print v[0].data.shape
#  print k,v[0].data
conv1_1_w = net0.params['conv1_1'][0].data
conv1_2_w = net0.params['conv1_2'][1].data

#ģ�Ͳ�����������net.params��������ֵ���������python����Ǹ��ֵ䣬���Զ�ģ�Ͳ����Ĳ����Ͷ�python�ֵ����һ����['conv1_1/conv']�Ǽ�����[0]��Ȩ��ά��

#print conv1_1_w
#print len(conv1_1_w)
#print conv1_2_w
#print len(conv1_2_w)
keys0 = net0.params.keys()
#print net0.params[keys0[1]][0].data
#print net0.params.keys()
#for key0 in keys0:   # ������в���������?#    print key0

net1 = caffe.Net('/home/zs/workspace/fanxi/caffe2/models/VGGNet/NWPU_VHR/SSD_300x300_0324_conv4_2/deploy.prototxt',\
      '/home/zs/workspace/fanxi/caffe2/models/VGGNet/NWPU_VHR/SSD_300x300_0324_conv4_2/VGG_NWPU_VHR_SSD_300x300_0324_conv4_2_iter_6.caffemodel',caffe.TRAIN)
keys1 = net1.params.keys()
#print len(net1.params['conv1_1'])
for key1 in keys1:
  if key1 in keys0:
    print key1
    print len(net0.params[key1])
    for i in range (len(net0.params[key1])):
      net1.params[key1][i] = net0.params[key1][i]
net1.save('/home/zs/workspace/fanxi/caffe2/models/VGGNet/NWPU_VHR/SSD_300x300_0324_conv4_2/2w6_based.caffemodel')

#check
'''
net2 = caffe.Net('/home/zs/workspace/fanxi/caffe2/models/VGGNet/NWPU_VHR/SSD_300x300_0322_conv4_1/deploy.prototxt',\
      '/home/zs/workspace/fanxi/caffe2/models/VGGNet/NWPU_VHR/SSD_300x300_0322_conv4_1/2w6_based.caffemodel',caffe.TRAIN)
net1 = caffe.Net('/home/zs/workspace/fanxi/caffe2/models/VGGNet/NWPU_VHR/SSD_300x300_0322_conv4_1/deploy.prototxt',\
     '/home/zs/workspace/fanxi/caffe2/models/VGGNet/NWPU_VHR/SSD_300x300_0322_conv4_1/VGG_NWPU_VHR_SSD_300x300_0322_conv4_1_iter_37.caffemodel',caffe.TRAIN)
'''
print "-----------------new-------"
print net2.params['conv1_1'][0].data[0]
print "-----------------vgg-------------"
print net0.params['conv1_1'][0].data[0]
print "-----------------net1------------"
print net1.params['conv1_1'][0].data[0]
