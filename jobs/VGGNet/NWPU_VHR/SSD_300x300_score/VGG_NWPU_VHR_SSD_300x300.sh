cd /home/zs/workspace/fanxi/caffe
./build/tools/caffe train \
--solver="models/VGGNet/NWPU_VHR/SSD_300x300_score/solver.prototxt" \
--weights="models/VGGNet/NWPU_VHR/SSD_300x300/VGG_NWPU_VHR_SSD_300x300_iter_50000.caffemodel" \
--gpu 0 2>&1 | tee jobs/VGGNet/NWPU_VHR/SSD_300x300_score/VGG_NWPU_VHR_SSD_300x300_test50000.log
