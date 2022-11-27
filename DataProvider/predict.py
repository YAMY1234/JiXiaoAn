import os

from numpy import argmax as np_argmax, array as np_array
from torch import from_numpy as torch_from_numpy, long as torch_long, load as torch_load

from DataProvider.args import Config

modelname="lym_transformer_10epoch4-19 10-46.pkl"
config = Config()
batch_size = config.batch_size

def predict(x_test):
    test = torch_from_numpy(x_test).to(torch_long).to(config.device) # 我来改进模型的话，可以把这个数据放到model里面去，这样就不用读取了
    modelPATH = os.path.join(os.path.abspath(os.path.dirname(__file__))) + r"/model/" + modelname
    model = torch_load(modelPATH)
    model.eval()
    res = []
    test_pre = model(test)
    res.extend(np_argmax(np_array(test_pre.data.cpu()), axis=1))
    return res
