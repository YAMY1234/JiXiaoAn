#coding:UTF-8
# from scapy.all import *
import os
import time

from scapy.all import corrupt_bytes

protocol_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../..")
class PcapDecode:
    def __init__(self):
        # 我自己的记录文件
        self.flowDict = {}
        self.flow_index = 0
        self.flowIdDict = {}
        self.protocolDict = {}
        self.protocol_index = 0
        # ETHER:读取以太网层协议配置文件
        with open(protocol_path+ '/protocol/ETHER', 'r', encoding='UTF-8') as f:
            ethers = f.readlines()
        self.ETHER_DICT = dict()
        for ether in ethers:
            ether = ether.strip().strip('\n').strip('\r').strip('\r\n')
            self.ETHER_DICT[int(ether.split(':')[0])] = ether.split(':')[1]  # 将配置文件中的信息(0257:Experimental)存入dict

        # IP:读取IP层协议配置文件
        with open(protocol_path + '/protocol/IP', 'r', encoding='UTF-8') as f:
            ips = f.readlines()
        self.IP_DICT = dict()
        for ip in ips:
            ip = ip.strip().strip('\n').strip('\r').strip('\r\n')
            self.IP_DICT[int(ip.split(':')[0])] = ip.split(':')[1]  # 将配置文件中的信息(41:IPv6)存入dic

        # PORT:读取应用层协议端口配置文件
        with open(protocol_path + '/protocol/PORT', 'r', encoding='UTF-8') as f:
            ports = f.readlines()
        self.PORT_DICT = dict()
        for port in ports:
            port = port.strip().strip('\n').strip('\r').strip('\r\n')
            self.PORT_DICT[int(port.split(':')[0])] = port.split(':')[1]  # 如：21:FTP

        # TCP:读取TCP层协议配置文件
        with open(protocol_path + '/protocol/TCP', 'r', encoding='UTF-8') as f:
            tcps = f.readlines()
        self.TCP_DICT = dict()
        for tcp in tcps:
            tcp = tcp.strip().strip('\n').strip('\r').strip('\r\n')
            self.TCP_DICT[int(tcp.split(':')[0])] = tcp.split(':')[1]  # 465:SMTPS

        # UDP:读取UDP层协议配置文件
        with open(protocol_path + '/protocol/UDP', 'r', encoding='UTF-8') as f:
            udps = f.readlines()
        self.UDP_DICT = dict()
        for udp in udps:
            udp = udp.strip().strip('\n').strip('\r').strip('\r\n')
            self.UDP_DICT[int(udp.split(':')[0])] = udp.split(':')[1]  # 513:Who

    # 解析以太网层协议 ---ether_decode——ip_decode(tcp_decode or udp_decode)
    def ether_decode(self, p):
        data = dict()  # 解析出的信息以dict的形式保存
        if p.haslayer("Ether"):  # scapy.haslayer,将pcap包中的信息分层，再处理
            data = self.ip_decode(p)  # 解析IP层协议
            data['time'] = time.mktime(time.localtime(p.time))
            flow_interval_key = data['Source'].split(':')[0]+'-' # +data['Destination'].split(':')[0]
            if(flow_interval_key not in self.flowDict):
                # 设置flow_index
                self.flowIdDict[flow_interval_key] = self.flow_index
                self.flow_index += 1

                # 设置inter_arrival时间
                data['interArrival_time'] = -1
                self.flowDict[flow_interval_key] = data['time']
            else:
                data['interArrival_time'] = data['time'] - self.flowDict[flow_interval_key]
                self.flowDict[flow_interval_key] = data['time']

            if data['Procotol'] not in self.protocolDict:
                self.protocolDict[data['Procotol']] = self.protocol_index
                self.protocol_index += 1

            data['protocol_index'] = self.protocolDict[data['Procotol']]
            # 通过当前的流id来获取对应的flow_index
            data['flow_index'] = self.flowIdDict[flow_interval_key]
            return data
        else:
            # data['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(p.time))
            data['time'] = time.mktime(time.localtime(p.time))
            data['Source'] = 'Unknow'
            data['Destination'] = 'Unknow'
            data['Procotol'] = 'Unknow'
            data['len'] = len(corrupt_bytes(p))
            data['info'] = p.summary()
            data['interArrival_time'] = -1
            data['protocol_index'] = -1
            data['flow_index'] = -1
            return data

    #解析IP层协议
    def ip_decode(self, p):
        data = dict()
        if p.haslayer("IP"):  #2048:Internet IP (IPv4) ，分IPV4和IPV6和其他协议
            ip = p.getlayer("IP")
            if p.haslayer("TCP"):  #6:TCP
                data = self.tcp_decode(p, ip)
                return data
            elif p.haslayer("UDP"): #17:UDP
                data = self.udp_decode(p, ip)
                return data
            else:
                if ip.proto in self.IP_DICT:  # 若ip分层中的协议信息在字典中，则提取ip分层中的源地址、目的地址、协议（转换）等
                    data['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(p.time))
                    data['Source'] = ip.src
                    data['Destination'] = ip.dst
                    data['Procotol'] = self.IP_DICT[ip.proto]
                    data['len'] = len(corrupt_bytes(p))
                    data['info'] = p.summary()
                    return data
                else:
                    data['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(p.time))
                    data['Source'] = ip.src
                    data['Destination'] = ip.dst
                    data['Procotol'] = 'IPv4'
                    data['len'] = len(corrupt_bytes(p))
                    data['info'] = p.summary()
                    return data
        elif p.haslayer("IPv6"):  #34525:IPv6
            ipv6 = p.getlayer("IPv6")
            if p.haslayer("TCP"):  #6:TCP
                data = self.tcp_decode(p, ipv6)
                return data
            elif p.haslayer("UDP"): #17:UDP
                data = self.udp_decode(p, ipv6)
                return data
            else:
                if ipv6.nh in self.IP_DICT:
                    data['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(p.time))
                    data['Source'] = ipv6.src
                    data['Destination'] = ipv6.dst
                    data['Procotol'] = self.IP_DICT[ipv6.nh]
                    data['len'] = len(corrupt_bytes(p))
                    data['info'] = p.summary()
                    return data
                else:
                    data['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(p.time))
                    data['Source'] = ipv6.src
                    data['Destination'] = ipv6.dst
                    data['Procotol'] = 'IPv6'
                    data['len'] = len(corrupt_bytes(p))
                    data['info'] = p.summary()
                    return data
        else:
            if p.type in self.ETHER_DICT:
                data['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(p.time))
                data['Source'] = p.src
                data['Destination'] = p.dst
                data['Procotol'] = self.ETHER_DICT[p.type]
                data['len'] = len(corrupt_bytes(p))
                data['info'] = p.summary()
                return data
            else:
                data['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(p.time))
                data['Source'] = p.src
                data['Destination'] = p.dst
                data['Procotol'] = hex(p.type)  # 若在字典中没有改协议，则以16进制的形式显示
                data['len'] = len(corrupt_bytes(p))
                data['info'] = p.summary()
                return data

    #解析TCP层协议
    def tcp_decode(self, p, ip):
        data = dict()
        tcp = p.getlayer("TCP")
        data['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(p.time))
        data['Source'] = ip.src + ":" + str(ip.sport)
        data['Destination'] = ip.dst + ":" + str(ip.dport)
        data['len'] = len(corrupt_bytes(p))
        data['info'] = p.summary()
        if tcp.dport in self.PORT_DICT:  #若端口信息在PORT_DICT\TCP_DICT中则转换为已知
            data['Procotol'] = self.PORT_DICT[tcp.dport]
        elif tcp.sport in self.PORT_DICT:
            data['Procotol'] = self.PORT_DICT[tcp.sport]
        elif tcp.dport in self.TCP_DICT:
            data['Procotol'] = self.TCP_DICT[tcp.dport]
        elif tcp.sport in self.TCP_DICT:
            data['Procotol'] = self.TCP_DICT[tcp.sport]
        else:
            data['Procotol'] = "TCP"
        return data

    #解析UDP层协议
    def udp_decode(self, p, ip):
        data = dict()
        udp = p.getlayer("UDP")
        data['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(p.time))
        data['Source'] = ip.src + ":" + str(ip.sport)
        data['Destination'] = ip.dst + ":" + str(ip.dport)
        data['len'] = len(corrupt_bytes(p))
        data['info'] = p.summary()
        if udp.dport in self.PORT_DICT:  #若端口信息在PORT_DICT\UDP_DICT中则转换为已知
            data['Procotol'] = self.PORT_DICT[udp.dport]
        elif udp.sport in self.PORT_DICT:
            data['Procotol'] = self.PORT_DICT[udp.sport]
        elif udp.dport in self.UDP_DICT:
            data['Procotol'] = self.UDP_DICT[udp.dport]
        elif udp.sport in self.UDP_DICT:
            data['Procotol'] = self.UDP_DICT[udp.sport]
        else:
            data['Procotol'] = "UDP"
        return data


PD = PcapDecode()
def analysis_pcap(p):
    data =  PcapDecode.ether_decode(PD, p)
    return data


# if __name__ == '__main__':
#     # pkts = sniff(iface="eth0",count=3) 简单的抓取数据包
#     # wrpcap("demo.pcap", pkts)  保存为demo.pcap
#     PD = PcapDecode()  # 实例化该类为PD
#     pcap_file_path = r"mawilab_30w.pcap"
#     pcap_test = rdpcap(pcap_file_path)  # 这个demo.pcap包含3次连接
#     data_result = dict()  # 将解析结果存入dict
#     cnt =0
#     res_li = []
#     for p in pcap_test:
#         cnt+=1
#         if cnt//1000==0:
#             print(cnt)
#         data_result = PcapDecode.ether_decode(PD, p)
#         t_res = []
#         t_res.append(data_result['flow_index'])
#         t_res.append(data_result['time'])
#         t_res.append(data_result['interArrival_time'])
#         t_res.append(data_result['protocol_index'])
#         t_res.append(data_result['len'])
#         res_li.append(t_res)
#
#     res_li = np.array(res_li)
#     np.save(pcap_file_path.split('.')[0] + '_feature.npy',res_li)
#
#     import json
#     with open(pcap_file_path.split('.')[0]+'_flowIdDict.txt','w') as f:
#         f.write(json.dumps(PD.flowIdDict, indent=4, ensure_ascii=False))
#     with open(pcap_file_path.split('.')[0]+'_protocolDict.txt','w') as f:
#         f.write(json.dumps(PD.protocolDict, indent=4, ensure_ascii=False))