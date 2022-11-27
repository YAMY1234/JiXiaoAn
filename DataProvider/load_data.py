import os
from random import randint as random_randint

from numpy import array as np_array, load as np_load


#--------------------------加载数据----------------------------
def load_data(config):
    vocabs_size = 256 # 这个是词向量维度好吧
  
    data_path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "../.."))+ r"/Datasetbase/mawilab/"
    data = np_load(data_path+'mawilab_raw.npy')
    print(data.shape)
    labels = np_load(data_path + 'mawilab_20_30w_label.npy')
    def random_int_list(start, stop, length):
        start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
        length = int(abs(length)) if length else 0
        random_list = []
        for i in range(length):
            random_list.append(random_randint(start, stop))
        return random_list

    def get_train_test(features,labels,protion,mode):# 适合于一维、二维
        # features=features[0:100000]
        train_num=int(len(features)*protion)
        test_begin=train_num
        test_end=len(features)
        if mode=="无监督":
            normal_data = []
            for i in range(train_num):
                if labels[i] == 0:
                    normal_data.append(features[i])
            normal_labels = labels[labels == 0]
            
            labels = np_array(labels)
            features = np_array(features)
            normal_data = np_array(normal_data)
            normal_labels = np_array(normal_labels)
            
            train_num=len(normal_data)# 注意这一步不可少，因为被正常和非正常的分了之后trainnum的结果会发生变化
            x_train=normal_data[0:train_num]
            y_train=normal_labels[0:train_num]
        else:
            x_train=features[0:test_begin]
            y_train=labels[0:test_begin]
        x_test=features[test_begin:test_end]
        y_test=labels[test_begin:test_end]
        return x_train,y_train,x_test,y_test

    x_train,y_train,x_test,y_test=get_train_test(data,labels,4/5,"有监督")


    ##################随机抽取当中的部份数出来
    randbegin=0
    randend=len(x_train)
    samplenum=(randend-randbegin)//100
    index_list=random_int_list(randbegin,randend,samplenum)
    index_list.sort()
    new_x_train=[]
    new_y_train=[]
    for i in index_list:
        new_x_train.append(x_train[i])
        new_y_train.append(y_train[i])
    x_train=new_x_train
    y_train=new_y_train
    #删除无用变量
    del new_x_train
    del new_y_train
    ##############随机抽样结束

    train=x_train 
    targets=y_train

    # 对于每一个train当中的元素来说，保证其小于64？？啥玩意儿，不过我这个就算除了还是有小数存在的，我们先有监督的来分类试一试
    train = np_array(train)
    targets = np_array(targets)
    x_test = np_array(x_test)
    y_test = np_array(y_test)
    return train,targets,vocabs_size,x_test,y_test
