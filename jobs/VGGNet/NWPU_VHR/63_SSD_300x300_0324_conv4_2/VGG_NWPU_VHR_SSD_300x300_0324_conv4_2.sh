cd /home/zs/workspace/fanxi/caffe2
./build/tools/caffe train \
--solver="models/VGGNet/NWPU_VHR/SSD_300x300_0324_conv4_2/solver.prototxt" \
--weights="models/VGGNet/NWPU_VHR/SSD_300x300_0324_conv4_2/2w6_based.caffemodel" \
--gpu 0 2>&1 | tee jobs/VGGNet/NWPU_VHR/SSD_300x300_0324_conv4_2/VGG_NWPU_VHR_SSD_300x300_0324_conv4_2.log
