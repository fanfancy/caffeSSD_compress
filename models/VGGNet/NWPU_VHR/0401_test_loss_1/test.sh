cd /home/zs/workspace/fanxi/caffe2
for i in {2000..40000..2000}
do
    echo "$i"
    echo "*****models/VGGNet/SSD_300x300_0319_ini/VGG_NWPU_VHR_SSD_300x300_0319_ini_iter_"$i"_2000.caffemodel****"
    ./build/tools/caffe train \
    --solver="models/VGGNet/NWPU_VHR/0401_test_loss_1/solver.prototxt" \
    --weights="models/VGGNet/NWPU_VHR/SSD_300x300_0319_ini/VGG_NWPU_VHR_SSD_300x300_0319_ini_iter_"$i".caffemodel" \
    --gpu 0 2>&1 | tee -a models/VGGNet/NWPU_VHR/0401_test_loss_1/test_result.log
done