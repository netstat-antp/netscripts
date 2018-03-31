import paramiko
import socket


class sshcmd(object):

    def __init__(self, devList, cmdList, userID, pword):
        self.devList = devList
        self.cmdList = cmdList
        self.userID = userID
        self.pword = pword

    def sendcmd(self):
        for dev in self.devList:
            try:
                print '+' * 80
                print '\n[+] Connecting to: ' + dev + '\n'
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(dev, username=self.userID, password=self.pword, allow_agent=False, look_for_keys=False, timeout=3)
                for cmd in self.cmdList:
                    print '\n'
                    print "\n[+] Command [" + cmd + "] results:"
                    stdin, stdout, stderr = ssh.exec_command(cmd)
                    print '\n'
                    for line in stdout.readlines():
                        print line
                    for line in stderr.readlines():
                        print line
                print '\n'
                print '\n[-] Exiting:   ' + dev + '\n'
                ssh.close()
            except socket.error as e0:
                print '[!] Error connecting to: ' + dev
                print '[!] Socket error: ', e0
                print '\n'
            except paramiko.SSHException as e1:
                print '[!] Error connecting to: ' + dev
                print '[!] Connection failed: ', e1
                print '\n'
            except paramiko.AuthenticationException as e2:
                print '[!] Error connecting to: ' + dev
                print '[!] Authentication failed: ', e2
                print '\n'
            except paramiko.BadHostKeyException as e3:
                print '[!] Error connecting to: ' + dev
                print '[!] Server host key check failed: ', e3
                print '\n'
            except paramiko.BadAuthenticationType as e4:
                print '[!] Error connecting to: ' + dev
                print '[!] Authentication type bad: ', e4
                print '\n'
        print '+' * 80
        print '\n[+] Command sequence complete. Exiting program.'
        ssh.close()



