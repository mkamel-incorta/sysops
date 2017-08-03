## Script Written By Mohamed Khaled Aug 3rd 2017 ########
# Script Upgrades the current Running Incorta    ########
# usage is python AutomatedUpgrade.py  "/home/incorta/IncortaAnalytics" "incorta-installer.jar" #########
#########################################################
import os , sys, getopt
installpath = sys.argv[1]
sourcejar = sys.argv[2]
#def main(argv):
#   try:
#      opts, args = getopt.getopt(argv,"h:p:s:")
#   except getopt.GetoptError:
#      print 'test.py -p <installPath> -s <incorta-installer.jar localtion>'
#      sys.exit(2)
#   for opt, arg in opts:
#      if opt == '-h':
#         print 'test.py -p <installPath>'
#         sys.exit()
#      elif opt in ("-p"):
#         installpath = arg
#      elif opt in ("-s"):
#         sourcejar = arg
#if __name__ == "__main__":
#   main(sys.argv[1:])

cmd = "java -jar "+sourcejar+" < .upgrade.rsp"
respfile = open(".upgrade.rsp","w+")
respfile.write("\r\n")
respfile.write("\r\n")
respfile.write("Y\r\n")
respfile.write(installpath +"\r\n")
respfile.write("Y\r\n")
respfile.write("2\r\n")
respfile.write("\r\n")
respfile.write("3\r\n")
respfile.write("\r\n")
respfile.close()
os.system(cmd)
#os.system("java -jar incorta-installer.jar < .upgrade.rsp")
os.system("rm -rf  .upgrade.rsp")
