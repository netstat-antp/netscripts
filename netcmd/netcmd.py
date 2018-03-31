from sshcmd import sshcmd
import getpass
import argparse

parser = argparse.ArgumentParser(description='Command Line Options')
parser.add_argument('-d', '--devices', help='Device List File', required='True')
parser.add_argument('-c', '--commands', help='Command List File', required='True')

args = parser.parse_args()

devFile = args.devices
cmdFile = args.commands

username = raw_input("Enter your username: ")
password = getpass.getpass("Enter your password: ")


try:
    f1 = open(devFile, 'r')
    devList = f1.read().splitlines()
    f1.close()
except IOError as e0:
    print "\n[-] Exception occured: " + str(e0)
    print "[-] File " + devFile + " does not exist. Try again."
    exit()

try:
    f2 = open(cmdFile, 'r')
    cmdList = f2.read().splitlines()
    f1.close()
except IOError as e1:
    print "\n[-] Exception occured: " + str(e1)
    print "[-] File " + cmdFile + " does not exist. Try again."
    exit()

sshcmdIns1 = sshcmd(devList, cmdList, username, password)
sshcmdIns1.sendcmd()

