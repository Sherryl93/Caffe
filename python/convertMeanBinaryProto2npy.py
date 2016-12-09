##########################################################################################################
## Objective: To convert mean Binary Proto to npy                                                       ##
## Input: file .binaryproto                                                                             ##
## Output: file .npy                                                                                    ##
##########################################################################################################
import os
import sys
import numpy as np

##Add Caffe path to current directory
def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)
caffe_dir = '../../caffe/'
python_path=os.path.join(caffe_dir,'python')
add_path(python_path)


import caffe #import caffe

MEAN_FILE = '../../.binaryproto' #your binaryproto file
blob=caffe.proto.caffe_pb2.BlobProto()
data = open( MEAN_FILE , 'rb' ).read()
blob.ParseFromString(data)
arr=np.array(caffe.io.blobproto_to_array(blob))
out=arr[0]
out_dir= '../.../.npy' ##Desired output directory
np.save(out_dir,out)

