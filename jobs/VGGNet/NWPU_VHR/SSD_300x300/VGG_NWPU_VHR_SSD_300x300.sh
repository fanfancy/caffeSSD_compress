cd /home/zs/workspace/fanxi/caffe
./build/tools/caffe train \
--solver="models/VGGNet/NWPU_VHR/SSD_300x300/solver.prototxt" \
--weights="models/VGGNet/VGG_ILSVRC_16_layers_fc_reduced.caffemodel" \
--gpu 0 2>&1 | tee jobs/VGGNet/NWPU_VHR/SSD_300x300/VGG_NWPU_VHR_SSD_300x300.log
