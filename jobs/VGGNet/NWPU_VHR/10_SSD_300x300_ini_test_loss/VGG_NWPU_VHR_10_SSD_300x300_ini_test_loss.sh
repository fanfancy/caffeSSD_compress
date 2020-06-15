cd /home/zs/workspace/fanxi/caffe2
./build/tools/caffe train \
--solver="models/VGGNet/NWPU_VHR/10_SSD_300x300_ini_test_loss/solver.prototxt" \
--snapshot="models/VGGNet/NWPU_VHR/10_SSD_300x300_ini_test_loss/VGG_NWPU_VHR_10_SSD_300x300_ini_test_loss_iter_111.solverstate" \
--gpu 0 2>&1 | tee jobs/VGGNet/NWPU_VHR/10_SSD_300x300_ini_test_loss/VGG_NWPU_VHR_10_SSD_300x300_ini_test_loss.log
