cd /home/zs/workspace/fanxi/caffe2
./build/tools/caffe test \
--solver="models/VGGNet/NWPU_VHR/SSD_300x300_0323_conv6/solver.prototxt" \
--snapshot="models/VGGNet/NWPU_VHR/SSD_300x300_0323_conv6/VGG_NWPU_VHR_SSD_300x300_0323_conv6_iter_26000.solverstate" \
--gpu 0 2>&1 | tee jobs/VGGNet/NWPU_VHR/5_SSD_300x300_0323_conv6_score/VGG_NWPU_VHR_SSD_300x300_0323_conv6.log
