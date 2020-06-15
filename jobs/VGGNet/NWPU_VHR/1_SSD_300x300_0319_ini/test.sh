cd /home/zs/workspace/fanxi/caffe2
./build/tools/caffe train \
--solver="models/VGGNet/NWPU_VHR/SSD_300x300_0319_ini/solver.prototxt" \
--weights="models/VGGNet/NWPU_VHR/SSD_300x300_0319_ini/VGG_NWPU_VHR_SSD_300x300_0319_ini_iter_20000.caffemodel" \
--gpu 0 2>&1 | tee jobs/VGGNet/NWPU_VHR/1_SSD_300x300_0319_ini/test_0528.log
