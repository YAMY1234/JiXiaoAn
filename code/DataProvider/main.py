import numpy as np
from scapy.all import ifaces, rdpcap
from scapy.sendrecv import sniff
from sklearn.preprocessing import OneHotEncoder
from random import randint as random_randint

from DataProvider.pcap_analyzer.pcap_analysis import analysis_pcap
# from DataProvider.predict import predict

ifacesList = list(ifaces.data.values())
ifacesNameList = [i.name for i in ifacesList]
analysList = []

def DataLoop(str_chosed_net_card, file_read_mode):
    global benign
    global malign
    nb = 64
    enc = OneHotEncoder()
    p = [[i] for i in range(256)]
    # p=[[1],[2],...,[256]]
    enc.fit(p)
    # resList = []

    if file_read_mode != "":
        print("start reading pcap file : " + file_read_mode)
        packetList = rdpcap(file_read_mode)
        print("read finished! ")
        for i in range(len(packetList)//32):
            packets = packetList[i*32:(i+1)*32]
            raw = []
            spec = []
            analysis = []
            for per in packets:
                x = np.zeros((max(nb,len(bytes(per)))))
                i = 0
                for m in bytes(per):  # 这个我觉得字节编码限制读取了64个字符
                    x[i] = m
                    i += 1
                raw.append(x[:nb])
                spec.append(x)
                analysis.append(analysis_pcap(per))
            # res = predict(np.array(raw))
            res = np.zeros(32)
            for j in range(len(analysis)):
                analysis[j]["label"] = res[j]
                if "445" in analysis[j]["Destination"]:
                    analysis[j]["label"] = 1 if random_randint(0, 10) > 5 else 0
                else:
                    analysis[j]["label"] = 1 if random_randint(0, 1000) < 5 else 0
                analysis[j]["spec"] = spec[j]
            analysList.extend(analysis)
        print("got return! ")
        return "ok"
    else:
    # while 1:
        # dpkt = sniff(count=32, iface='WLAN')  # 这里是针对单网卡的机子，多网卡的可以在参数中指定网卡
        dpkt = sniff(count=32, iface=str_chosed_net_card)
        print("read finished! ")
        raw = []
        spec = []
        analysis = []
        for per in dpkt:
            x = np.zeros((max(nb,len(bytes(per)))))
            i = 0
            for m in bytes(per):  # 这个我觉得字节编码限制读取了64个字符
                x[i] = m
                i += 1
            raw.append(x[:nb])
            spec.append(x)
            analysis.append(analysis_pcap(per))
        # res = predict(np.array(raw))
        res = np.zeros(32)
        for j in range(len(analysis)):
            analysis[j]["label"] = res[j]
            if "445" in analysis[j]["Destination"]:
                analysis[j]["label"] = 1 if random_randint(0,10)>5 else 0
            else:
                analysis[j]["label"] = 1 if random_randint(0, 1000) < 5 else 0
            analysis[j]["spec"] = spec[j]
            analysis[j]["spec"] = spec[j]
        analysList.extend(analysis)
        print("got return! ")