import mxnet as mx
import io
import os
from scipy import misc

import numpy as np

read_dir = r'F:\FaceDataset\faces_webface_112x112'
save_dir = r'F:\FaceDataset\faces_webface_112x112\img_sample'

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

idx_path = os.path.join(read_dir, 'train.idx')
bin_path = os.path.join(read_dir, 'train.rec')
imgrec = mx.recordio.MXIndexedRecordIO(idx_path, bin_path, 'r')
s = imgrec.read_idx(0)
header, _ = mx.recordio.unpack(s)
imgidx = list(range(1, int(header.label[0])))
total = len(imgidx)
cnt = 0
for i in imgidx:
    img_info = imgrec.read_idx(i)
    header, img = mx.recordio.unpack(img_info)
    l = int(header.label)
    img = io.BytesIO(img)
    img = misc.imread(img)
    print('============================================')
    print(img.dtype)
    print(np.max(img))
    print(np.min(img))
    print('============================================')
    misc.imsave(os.path.join(save_dir, str(cnt) + '.jpg'), img)
    cnt += 1
    if cnt >= 100:
        break
