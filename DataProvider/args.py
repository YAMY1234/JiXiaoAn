import datetime
import os

from torch import device as torch_device, cuda as torch_cuda


class Config(object):

    """配置参数"""
    def __init__(self):
        self.model_name = 'Transformer'
        self.embedding_pretrained = None                                 # 预训练词向量
        self.device = torch_device('cuda:0' if torch_cuda.is_available() else 'cpu')   # 设备
        self.dropout = 0.5                                              # 随机失活
        self.num_classes = 2                        # 类别数
        # self.batch_size = 128                                           # mini-batch大小
        self.batch_size = 32                                           # mini-batch大小
        self.pad_size = 64                                               # 每句话处理成的长度(短填长切)
        # self.n_vocab = None#这里需要读取数据的部分进行赋值

        self.n_vocab = 256#这里需要读取数据的部分进行赋值
        self.learning_rate = 5e-4                                       # 学习率
        self.embed = 300           # 词向量维度，表示溢出的维度，其实大于256就可以我觉得，因为词向量的维度是个固定的东西嘛
        self.dim_model = 300
        self.hidden = 1024
        self.last_hidden = 512
        self.num_head = 5
        self.num_encoder = 2
        self.n_splits = 5#k折交叉验证

        # 我的后来相关的内容：
        self.num_epochs = 50                                            # epoch数
        nowt=datetime.datetime.now()
        # self.modelpath =  os.path.join(os.path.abspath(os.path.dirname(__file__))) +r"/model/lym_transformer_10epoch3-4 11-15.pkl"
        self.modelpath = os.path.join(os.path.abspath(os.path.dirname(__file__))) +r"/model/lym_transformer_10epoch"+\
            str(nowt.month)+"-"+str(nowt.day)+" "+str(nowt.hour)+"-"+str(nowt.minute)+".pkl"
    