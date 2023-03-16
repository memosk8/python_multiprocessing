import multiprocessing
import GPUtil
import torch


use_cuda = torch.cuda.is_available()
device = torch.device("cuda:2" if use_cuda else "cpu")
print(multiprocessing.cpu_count(), GPUtil.getAvailable(),use_cuda)