import sys
import time
from scapy.all import ifaces
from threading import Thread
from PyQt5.QtWidgets import (QMainWindow,QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget, QMainWindow,
                             QTableWidgetItem, QMessageBox)
from mainWindow import *
from PyQt5.QtCore import *
from Net_table import Ui_Form as Net_table
from PyQt5.QtGui import QColor, QBrush
from alldataDiag import Ui_Dialog as allDataDialog

from DataProvider.main import DataLoop, analysList

tcpItem={'time' : 1650210862.0,'Source' : '182.61.200.166:443',
'Destination' : '100.80.65.96:62093','len' : 56,'info': 'TCP',
'Procotol': 'HTTPS','interArrival_time' : 0.0,'protocol_index ': 0,'flow_index ': 5,'label' : 0,'spec':[255.,169.,70.,90.,255.,169.,70.,90.,169.,70.,90.,255.,169.,70.,90.,169.,70.,90.,255.,169.,70.,90.,169.,70.,90.,255.,169.,70.,90.]
    }
arpItem=tcpItem.copy()
arpItem['info']='ARP'
udpItem=tcpItem.copy()
udpItem['info']='UDP'
eudpItem=udpItem.copy()
eudpItem['label']=1
icmpItem=tcpItem.copy()
icmpItem['info']='ICMP'
otherItem=tcpItem.copy()
otherItem['info']='DNS'
otherItem['label']=1
#选择的网卡
str_chosed_net_card=""
#抓包数的全局变量
# packet_list=[arpItem,arpItem,otherItem,icmpItem,udpItem,eudpItem,udpItem,tcpItem,tcpItem,udpItem]
packet_list = analysList
#网卡列表
net_card_lists = None
#文件读取的名称传入
file_read_mode = ""
# 暂停读取
pose_sign = 1
#选择网卡的界面


import os
from DataBase import *
toplogo = os.path.join(os.path.abspath(os.path.dirname(__file__)), '纯logo金.png')
whiteLogo =  os.path.join(os.path.abspath(os.path.dirname(__file__)), '白色条形.png')
toplogo = './纯logo金.png'
whiteLogo =  './白色条形.png'

# toplogo='C:/Users/javen/Desktop/纯logo金.png'
# whiteLogo='C:/Users/javen/Desktop/高清Logo/白色条形.png'
from style import *
class all_data_card(QWidget,allDataDialog):
    def __init__(self):
        super(all_data_card, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("济小安网络安全专家")

class chose_network_card(QWidget):
    def __init__(self,list,timer,netCardLabel,stopButton,chooseNetCard):
        super().__init__()
        self.init_ui(list)
        self.timer2=timer
        self.netCardLabel=netCardLabel
        self.stopButton=stopButton
        self.chooseNetCard=chooseNetCard

    def init_ui(self,list):
        self.label = QLabel('请选择要捕获的网卡：')
        self.net_card=[]
        for i in net_card_lists:
            temp=QRadioButton(i)
            temp.toggled.connect(self.onClicked)
            self.net_card.append(temp)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        for i in self.net_card:
            layout.addWidget(i)

        self.setGeometry(400, 400, 300, 50)

        self.setLayout(layout)
        self.setWindowTitle('选择网卡')

    def onClicked(self):
        radioBtn = self.sender()
        global str_chosed_net_card, pose_sign
        if radioBtn.isChecked():
            pose_sign = 0
            str_chosed_net_card=radioBtn.text()
            radioBtn.setAutoExclusive(False)
            radioBtn.setChecked(False)
            radioBtn.setAutoExclusive(True)

            temp = str(self.netCardLabel.text())[:7]
            temp += str_chosed_net_card
            for i in range(26-len(temp)):
                temp+=' '

            self.netCardLabel.setText(temp)
            self.stopButton.setStyleSheet(stopStyle)
            self.chooseNetCard.setStyleSheet(startClickStyle)
            self.close()
            self.timer2.start(500)


#表格
class NetTable(QWidget, Net_table):
    def __init__(self):
        super(NetTable, self).__init__()
        self.setupUi(self)
        self.setMinimumWidth(30)
        self.setMinimumHeight(30)
def turnToTxt(lis):
    pass
#主界面
class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("济小安网络安全专家")
        self.setWindowIcon(QtGui.QIcon(toplogo))
        self.imgLabel.setStyleSheet("QLabel{border-image:url("+whiteLogo+");}")
        # self.netCardLabel()
        self.TCP_W = NetTable()
        self.TCPButton.setStyleSheet(tableButtonChosedStyle)
        self.TCP_W.tableWidget.doubleClicked.connect(self.doubleTcp)
        self.ARP_W =NetTable()
        self.ARP_W.hide()
        self.ARP_W.tableWidget.doubleClicked.connect(self.doubleArp)
        self.UDP_W = NetTable()
        self.UDP_W.hide()
        self.UDP_W.tableWidget.doubleClicked.connect(self.doubleUdp)
        self.ICMP_W = NetTable()
        self.ICMP_W.hide()
        self.ICMP_W.tableWidget.doubleClicked.connect(self.doubleIcmp)
        self.OTHER_W = NetTable()
        self.OTHER_W.hide()
        self.OTHER_W.tableWidget.doubleClicked.connect(self.doubleOther)
        self.BAD_W=NetTable()
        self.BAD_W.hide()
        self.BAD_W.tableWidget.doubleClicked.connect(self.doubleBad)
        self.horizontalLayout.addWidget(self.TCP_W)
        self.horizontalLayout.addWidget(self.ARP_W)
        self.horizontalLayout.addWidget(self.UDP_W)
        self.horizontalLayout.addWidget(self.ICMP_W)
        self.horizontalLayout.addWidget(self.OTHER_W)
        self.horizontalLayout.addWidget(self.BAD_W)

        self.alludpSum=0
        self.allarpSum=0
        self.alltcpSum=0
        self.allbadSum=0
        self.allicmpSum=0
        self.allotherSum=0
        self.last_packet_sum = 0
        self.adding_rate = 0

        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.operate)  # 计时结束调用operate()方法
        # self.timer.start(1000)  # 设置计时间隔并启

        self.all_data_card=all_data_card()
        self.chose_net_card_dia = chose_network_card(net_card_lists,self.timer,self.netCardLabel,self.stopButton,self.chooseNetCard)
        self.chooseNetCard.clicked.connect(self.funChooseNetCard)
        self.ARPButton.clicked.connect(self.showARP)
        self.TCPButton.clicked.connect(self.showTCP)
        self.UDPButton.clicked.connect(self.showUDP)
        self.ICMPButton.clicked.connect(self.showICMP)
        self.OTHERButton.clicked.connect(self.showOTHER)
        self.BADButton.clicked.connect(self.showBAD)
        self.fileButton.clicked.connect(self.getFileDir)
        self.stopButton.clicked.connect(self.stopTimer)
        self.clearButton.clicked.connect(self.clearTable)

    def change_form(self,s):
        slen = len(s) // 3
        t = ""
        row = (slen - 1) // 16 + 1
        for r in range(row):
            t += '0x{:04X} '.format(r + 1)
            if 16 * r + 16 < slen:
                t += s[r * 16 * 3:(r * 16 + 16) * 3]
            else:
                t += s[r * 16 * 3:]
            t += '\n'
        return t

    def doubleTcp(self):
        self.all_data_card.show()
        for i in self.TCP_W.tableWidget.selectedItems():
            s=getInfo(i.text(),"TCP")
            s=self.change_form(s)
            self.all_data_card.textBrowser.setText(s)
            break

    def doubleUdp(self):
        self.all_data_card.show()
        for i in self.UDP_W.tableWidget.selectedItems():
            s=getInfo(i.text(),"UDP")
            s=self.change_form(s)
            self.all_data_card.textBrowser.setText(s)
            break
    def doubleArp(self):
        self.all_data_card.show()
        for i in self.ARP_W.tableWidget.selectedItems():
            s=getInfo(i.text(),"ARP")
            s=self.change_form(s)
            self.all_data_card.textBrowser.setText(s)
            break
    def doubleIcmp(self):
        self.all_data_card.show()
        for i in self.OTHER_W.tableWidget.selectedItems():
            s=getInfo(i.text(),"ICMP")
            s=self.change_form(s)
            self.all_data_card.textBrowser.setText(s)
            break
    def doubleOther(self):
        self.all_data_card.show()
        for i in self.OTHER_W.tableWidget.selectedItems():
            s=getInfo(i.text(),"OTHER")
            s=self.change_form(s)
            self.all_data_card.textBrowser.setText(s)
            break
    def doubleBad(self):
        self.all_data_card.show()
        for i in self.BAD_W.tableWidget.selectedItems():
            s=getInfo(i.text(),"BAD")
            s=self.change_form(s)
            self.all_data_card.textBrowser.setText(s)
            break

    def funChooseNetCard(self):
        self.chose_net_card_dia.show()

    def clearTable(self):
        drop_table()
        while self.ARP_W.tableWidget.rowCount() > 0:
            self.ARP_W.tableWidget.removeRow(0)
        while self.TCP_W.tableWidget.rowCount() > 0:
            self.TCP_W.tableWidget.removeRow(0)
        while self.UDP_W.tableWidget.rowCount() > 0:
            self.UDP_W.tableWidget.removeRow(0)
        while self.BAD_W.tableWidget.rowCount() > 0:
            self.BAD_W.tableWidget.removeRow(0)
        while self.ICMP_W.tableWidget.rowCount() > 0:
            self.ICMP_W.tableWidget.removeRow(0)
        while self.OTHER_W.tableWidget.rowCount() > 0:
            self.OTHER_W.tableWidget.removeRow(0)
        self.alludpSum = 0
        self.allarpSum = 0
        self.alltcpSum = 0
        self.allbadSum = 0
        self.allicmpSum = 0
        self.allotherSum = 0
        self.rlabel.setText("0.00%")
        self.rlabel.setStyleSheet("color:#009ad6;")
        self.rlabel_2.setText("0.00%")
        self.rlabel_2.setStyleSheet("color:#009ad6;")


    def stopTimer(self):
        global str_chosed_net_card
        global pose_sign
        str_chosed_net_card = ""
        pose_sign = 1
        self.stopButton.setStyleSheet(stopClickStyle)
        self.timer.stop()
        self.chooseNetCard.setStyleSheet(startStyle)

    def setButtonCom(self):
        self.TCPButton.setStyleSheet(tableButtonCommonStyle)
        self.ARPButton.setStyleSheet(tableButtonCommonStyle)
        self.UDPButton.setStyleSheet(tableButtonCommonStyle)
        self.ICMPButton.setStyleSheet(tableButtonCommonStyle)
        self.OTHERButton.setStyleSheet(tableButtonCommonStyle)
        self.BADButton.setStyleSheet(badTableStyle)

    def showARP(self):
        self.TCP_W.hide()
        self.UDP_W.hide()
        self.BAD_W.hide()
        self.ICMP_W.hide()
        self.OTHER_W.hide()
        self.ARP_W.show()
        self.setButtonCom()
        self.ARPButton.setStyleSheet(tableButtonChosedStyle)

    def showTCP(self):
        self.ARP_W.hide()
        self.UDP_W.hide()
        self.BAD_W.hide()
        self.ICMP_W.hide()
        self.OTHER_W.hide()
        self.TCP_W.show()

        self.setButtonCom()
        self.TCPButton.setStyleSheet(tableButtonChosedStyle)

    def showUDP(self):
        self.ARP_W.hide()
        self.TCP_W.hide()
        self.BAD_W.hide()
        self.ICMP_W.hide()
        self.OTHER_W.hide()
        self.UDP_W.show()
        self.setButtonCom()
        self.UDPButton.setStyleSheet(tableButtonChosedStyle)

    def showBAD(self):
        self.ARP_W.hide()
        self.TCP_W.hide()
        self.UDP_W.hide()
        self.ICMP_W.hide()
        self.OTHER_W.hide()
        self.BAD_W.show()
        self.setButtonCom()
        self.BADButton.setStyleSheet(tableButtonChosedStyle)

    def showICMP(self):
        self.ARP_W.hide()
        self.TCP_W.hide()
        self.UDP_W.hide()
        self.BAD_W.hide()
        self.OTHER_W.hide()
        self.ICMP_W.show()
        self.setButtonCom()
        self.ICMPButton.setStyleSheet(tableButtonChosedStyle)

    def showOTHER(self):
        self.ARP_W.hide()
        self.TCP_W.hide()
        self.UDP_W.hide()
        self.BAD_W.hide()
        self.ICMP_W.hide()
        self.OTHER_W.show()
        self.setButtonCom()
        self.OTHERButton.setStyleSheet(tableButtonChosedStyle)

    def getFileDir(self):
        global file_read_mode, pose_sign
        filePath, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", "./","*.pcap")
        pose_sign = 0
        file_read_mode = filePath
        self.timer.start(2000)

    #每次执行的
    def operate(self):
        packet_list.reverse()
        udpSum=0
        arpSum=0
        tcpSum=0
        badSum=0
        icmpSum=0
        otherSum=0
        tcpList=[]
        udpList=[]
        arpList=[]
        icmpList=[]
        otherList=[]
        badList=[]
        for i in range(len(packet_list)):
            row=packet_list[i]
            temp=[]
            time_local = time.localtime(row['time'])
            strtime = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
            temp.append(strtime)
            temp.append(str(row['Source']))
            temp.append(str(row['Destination']))
            temp.append(str(row['len']))
            temp.append(str(row['info']))
            if row['label']==0 or 'ARP' in row['info']:
                temp.append('否')
            else:
                temp.append('是')
            s=''
            for i in row['spec']:
                s+= '{:02X} '.format(int(i))
            temp.append(s)
            if row['label']==1:
                self.BAD_W.tableWidget.insertRow(badSum)
                badList.append(temp)
                badSum+=1
            if 'ARP' in row['info']:
                self.ARP_W.tableWidget.insertRow(arpSum)
                arpList.append(temp)
                arpSum+=1
            elif 'TCP' in row['info']:
                self.TCP_W.tableWidget.insertRow(tcpSum)
                tcpList.append(temp)
                tcpSum+=1
            elif 'UDP' in row['info']:
                self.UDP_W.tableWidget.insertRow(udpSum)
                udpList.append(temp)
                udpSum+=1
            elif 'ICMP' in row['info']:
                self.ICMP_W.tableWidget.insertRow(icmpSum)
                icmpList.append(temp)
                icmpSum+=1
            else :
                self.OTHER_W.tableWidget.insertRow(otherSum)
                otherList.append(temp)
                otherSum+=1

        for i in range(tcpSum):
            index=self.alltcpSum+tcpSum-i
            t = QTableWidgetItem(str(index))
            t.setForeground(QBrush(QColor(255, 255, 255)))
            t.setBackground(QBrush(QColor(20, 100, 160)))
            self.TCP_W.tableWidget.setItem(i, 0, t)
            insertDataBase([index,tcpList[i][6]],"TCP")
            for j in range(len(tcpList[i])-1):
                t = QTableWidgetItem(tcpList[i][j])
                if tcpList[i][5] == '是':
                    t.setBackground(QBrush(QColor('#aa2116')))
                elif (index)%2==0:
                    t.setBackground(QBrush(QColor(75,85,95)))
                else:
                    t.setBackground(QBrush(QColor(42,35,45)))
                t.setForeground(QBrush(QColor(255,255,255)))
                self.TCP_W.tableWidget.setItem(i, 1+j, t)
        self.alltcpSum+=len(tcpList)

        for i in range(udpSum):
            index=self.alludpSum+udpSum-i
            t = QTableWidgetItem(str(index))
            t.setForeground(QBrush(QColor(255, 255, 255)))
            t.setBackground(QBrush(QColor(20, 100, 160)))
            self.UDP_W.tableWidget.setItem(i, 0, t)
            insertDataBase([index,udpList[i][6]],"UDP")
            for j in range(len(udpList[i])-1):
                t = QTableWidgetItem(udpList[i][j])
                if udpList[i][5] == '是':
                    t.setBackground(QBrush(QColor('#aa2116')))
                elif (index)%2==0:
                    t.setBackground(QBrush(QColor(75,85,95)))
                else:
                    t.setBackground(QBrush(QColor(42,35,45)))
                t.setForeground(QBrush(QColor(255,255,255)))
                self.UDP_W.tableWidget.setItem(i, 1+j, t)
        self.alludpSum+=len(udpList)

        for i in range(arpSum):
            index=self.allarpSum+arpSum-i
            t = QTableWidgetItem(str(index))
            t.setForeground(QBrush(QColor(255, 255, 255)))
            t.setBackground(QBrush(QColor(20, 100, 160)))
            self.ARP_W.tableWidget.setItem(i, 0, t)
            insertDataBase([index,arpList[i][6]],"ARP")
            for j in range(len(arpList[i])-1):
                t = QTableWidgetItem(arpList[i][j])
                if arpList[i][5] == '是':
                    t.setBackground(QBrush(QColor('#aa2116')))
                elif (index)%2==0:
                    t.setBackground(QBrush(QColor(75,85,95)))
                else:
                    t.setBackground(QBrush(QColor(42,35,45)))
                t.setForeground(QBrush(QColor(255,255,255)))
                self.ARP_W.tableWidget.setItem(i, 1+j, t)
        self.allarpSum+=len(arpList)
        # if self.last_packet_sum != 0:
        #     self.adding_rate = len(packet_list) - self.last_packet_sum
        # self.last_packet_sum = len(packet_list)
        for i in range(icmpSum):
            index=self.allicmpSum+icmpSum-i
            t = QTableWidgetItem(str(index))
            t.setForeground(QBrush(QColor(255, 255, 255)))
            t.setBackground(QBrush(QColor(20, 100, 160)))
            self.ICMP_W.tableWidget.setItem(i, 0, t)
            insertDataBase([index,icmpList[i][6]],"ICMP")
            for j in range(len(icmpList[i])-1):
                t = QTableWidgetItem(icmpList[i][j])
                if icmpList[i][5] == '是':
                    t.setBackground(QBrush(QColor('#aa2116')))
                elif (index)%2==0:
                    t.setBackground(QBrush(QColor(75,85,95)))
                else:
                    t.setBackground(QBrush(QColor(42,35,45)))
                t.setForeground(QBrush(QColor(255,255,255)))
                self.ICMP_W.tableWidget.setItem(i, 1+j, t)
        self.allicmpSum+=len(icmpList)

        for i in range(otherSum):
            index = self.allotherSum + otherSum - i
            t = QTableWidgetItem(str(index))
            t.setForeground(QBrush(QColor(255, 255, 255)))
            t.setBackground(QBrush(QColor(20, 100, 160)))
            self.OTHER_W.tableWidget.setItem(i, 0, t)
            insertDataBase([index, otherList[i][6]], "OTHER")
            for j in range(len(otherList[i]) - 1):
                t = QTableWidgetItem(otherList[i][j])
                if otherList[i][5] == '是':
                    t.setBackground(QBrush(QColor('#aa2116')))
                elif (index) % 2 == 0:
                    t.setBackground(QBrush(QColor(75, 85, 95)))
                else:
                    t.setBackground(QBrush(QColor(42, 35, 45)))
                t.setForeground(QBrush(QColor(255, 255, 255)))
                self.OTHER_W.tableWidget.setItem(i, 1 + j, t)
        self.allotherSum += len(otherList)

        for i in range(badSum):
            index=self.allbadSum+badSum-i
            t = QTableWidgetItem(str(index))
            t.setForeground(QBrush(QColor(255, 255, 255)))
            t.setBackground(QBrush(QColor(20, 100, 160)))
            self.BAD_W.tableWidget.setItem(i, 0, t)
            insertDataBase([index,badList[i][6]],"BAD")
            for j in range(len(badList[i])-1):
                t = QTableWidgetItem(badList[i][j])
                t.setBackground(QBrush(QColor('#aa2116')))
                t.setForeground(QBrush(QColor(255,255,255)))
                self.BAD_W.tableWidget.setItem(i, 1+j, t)
        self.allbadSum+=len(badList)
        raid=0
        if (icmpSum+arpSum+tcpSum+udpSum+otherSum)!= 0:
            raid = badSum/(icmpSum+arpSum+tcpSum+udpSum+otherSum)
        nraid=round(raid*100,2)
        if (icmpSum+arpSum+tcpSum+udpSum+otherSum)!= 0:
            self.rlabel.setText(format(nraid,".2f")+'%')
            if nraid>5:
                self.rlabel.setStyleSheet("color:red;")
            else:
                self.rlabel.setStyleSheet("color:#009ad6;")

        all_raid=0
        if (self.allicmpSum+self.allarpSum+self.alltcpSum+self.alludpSum+self.allotherSum)!= 0:
            all_raid = self.allbadSum/(self.allicmpSum+self.allarpSum+self.alltcpSum+self.alludpSum+self.allotherSum)
        nraid=round(all_raid*100,2)
        self.rlabel_2.setText(format(nraid,".2f")+'%')
        if nraid>5:
            self.rlabel_2.setStyleSheet("color:red;")
        else:
            self.rlabel_2.setStyleSheet("color:#009ad6;")
        packet_list.clear()


def start_Qt():
    init_data_base()
    drop_table()
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

def change_packetList():
    global str_chosed_net_card, file_read_mode, pose_sign
    while 1:
        while pose_sign or (str_chosed_net_card == "" and file_read_mode == ""):
            time.sleep(1)
        if str_chosed_net_card != "":
            while pose_sign == 0:
                DataLoop(str_chosed_net_card, file_read_mode)
        else:
            DataLoop(str_chosed_net_card, file_read_mode)
        pose_sign = 0
        file_read_mode = ""
        str_chosed_net_card = ""

if __name__ == '__main__':
    ifacesList = list(ifaces.data.values())
    net_card_lists = [i.name for i in ifacesList]
    #抓包
    t1 = Thread(target=change_packetList, args=())
    t1.start()
    #界面
    t2 = Thread(target=start_Qt, args=())
    t2.start()