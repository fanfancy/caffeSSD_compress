cd /home/zs/workspace/fanxi/caffe2
./build/tools/caffe train \
--solver="models/VGGNet/NWPU_VHR/SSD_300x300_conv5_3_0318/solver.prototxt" \
--snapshot="models/VGGNet/NWPU_VHR/SSD_300x300_conv5_3_0318/VGG_NWPU_VHR_SSD_300x300_conv5_3_0318_iter_40000.solverstate" \
--gpu 0 2>&1 | tee -a jobs/VGGNet/NWPU_VHR/SSD_300x300_conv5_3_0318/VGG_NWPU_VHR_SSD_300x300_conv5_3_0318.log
