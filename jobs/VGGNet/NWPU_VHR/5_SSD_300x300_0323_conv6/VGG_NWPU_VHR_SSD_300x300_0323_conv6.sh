cd /home/zs/workspace/fanxi/caffe2
./build/tools/caffe train \
--solver="models/VGGNet/NWPU_VHR/SSD_300x300_0323_conv6/solver.prototxt" \
--weights="models/VGGNet/NWPU_VHR/SSD_300x300_0323_conv6/3w_based.caffemodel" \
--gpu 0 2>&1 | tee jobs/VGGNet/NWPU_VHR/SSD_300x300_0323_conv6/VGG_NWPU_VHR_SSD_300x300_0323_conv6.log
