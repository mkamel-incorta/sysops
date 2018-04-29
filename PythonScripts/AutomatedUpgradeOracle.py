## Script Written By Mohamed Khaled Aug 3rd 2017 ########
# Script Upgrades the current Running Incorta    ########
# usage is python AutomatedUpgrade.py  "/home/incorta/IncortaAnalytics" "Incorta-Source-Dir" #########
#########################################################
import os , sys, getopt
installpath = sys.argv[1]
sourcedir = sys.argv[2]
oraclepassword = sys.argv[3]
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
#         sourcedir = arg
#if __name__ == "__main__":
#   main(sys.argv[1:])

stopCmd = 'sh "'+installpath+'/stop.sh" && ps -ef | grep "'+installpath+'/" | cut -c 10-15 | xargs kill -9 '
unzipCmd = 'unzip -o "'+sourcedir+'"/incorta-package.zip -d "'+sourcedir+'"'
cmd = 'java -jar "'+sourcedir+'"/incorta-installer.jar < .upgrade.rsp'
startCmd= 'sh "'+installpath+'/start.sh"'
respfile = open(".upgrade.rsp","w+")
respfile.write("\r\n")
respfile.write("\r\n")
respfile.write("Y\r\n")
respfile.write(installpath +"\r\n")
respfile.write("Y\r\n")
respfile.write("2\r\n")
respfile.write(oraclepassword+"\r\n")
respfile.write("\r\n")
respfile.write("3\r\n")
respfile.write("\r\n")
respfile.close()
os.system(stopCmd)
os.system(unzipCmd)
os.system(cmd)
os.system(startCmd)
os.system("rm -rf  .upgrade.rsp")
