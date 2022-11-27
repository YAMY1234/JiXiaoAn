#! /usr/bin/python3
# coding:utf-8
# Auther:VChao
# 2020/09/14

import dpkt
import struct
import os
from socket import AF_INET, inet_pton
from socket import inet_ntop
import dpkt
import socket
import datetime
from dpkt import tcp
from dpkt.compat import compat_ord
def mac_addr(address):
    return ':'.join('%02x' % compat_ord(b) for b in address)

def inet_to_str(inet):
    try:
        return socket.inet_ntop(socket.AF_INET,inet)
    except:
        return False
def main():
    new_s_mac=b'\xBC\x17\xB8\xD0\xFD\xD6'
    new_d_mac=b'\x48\x89\xE7\xE8\x17\x0A'
    sum=0
    with open(r'mawilab_20_30w.pcap', "rb") as fin:
        with open("attack.pcap", "wb") as fout:
            pcapin = dpkt.pcap.Reader(fin)
            pcapout = dpkt.pcap.Writer(fout)
            for ts, buf in pcapin:
                Eth = dpkt.ethernet.Ethernet(buf)
                # print(Eth.src)
                # print(new_s_mac)
                Eth.src=new_s_mac
                Eth.dst=new_d_mac
                # print("Ethernet Frame : ", mac_addr(Eth.src), mac_addr(Eth.dst), Eth.type)
                # print(Eth)
                if Eth.type==2048:

                    ip = Eth.data
                    ip.dst=inet_pton(AF_INET,'192.168.43.59')
                    if isinstance(ip.data, dpkt.tcp.TCP):  # 解包，判断传输层协议是否是TCP，即当你只需要TCP时，可用来过滤
                        tcp = ip.data
                        # 修改端口
                        tcp.dport=445
                        pseheader = ip.src + ip.dst + b'\x00' * 2 + b'\x00\x06' + struct.pack('>I', len(tcp))
                        # 将原始TCP的校验和置零
                        tcp.sum = 0
                        # 拿到所有的tcp数据
                        all_tcp = tcp.pack()
                        # 如果TCP数据是奇数，要补零，但是测试中发现不加也没事，可能是底层库帮忙做了
                        if len(all_tcp) % 2 != 0: all_tcp += b'\x00'
                        tcp.sum = dpkt.in_cksum(pseheader + all_tcp)
                        # 验证校验和是否正确
                        assert dpkt.in_cksum(pseheader + tcp.pack()) == 0
                        ip.data = tcp
                        temp = dpkt.ethernet.Ethernet(src=Eth.src, dst=Eth.dst, type=Eth.type, data=ip)
                        pcapout.writepkt(temp, ts=ts)
                    elif isinstance(ip.data, dpkt.udp.UDP):
                        udp= ip.data
                        udp.dport=445
                        ip.data = udp
                        temp = dpkt.ethernet.Ethernet(src=Eth.src, dst=Eth.dst, type=Eth.type, data=ip)
                        pcapout.writepkt(temp, ts=ts)
                    sum+=1
                    if sum>=400:
                        return


if __name__ == "__main__":
    main()