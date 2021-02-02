import os
import getpass
print("\n\n")
def hdfs_file(node,location):
    if location == "remote":
        if node == "namenode":

            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")

            os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<configuration>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<property>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<name>dfs.name.dir</name>' >> /etc/hadoop/hdfs-site.xml")
            name_dir = input("Enter the namenode folder name:")
            os.system("echo '<value>%s</value>' >> /etc/hadoop/hdfs-site.xml"%name_dir)
            os.system("echo '</property>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")
            os.system("scp  /etc/hadoop/hdfs-site.xml 'root@%s':/etc/hadoop/hdfs-site.xml"%remoteip)

        elif node == "datanode":

            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")

            os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<configuration>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<property>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<name>dfs.data.dir</name>' >> /etc/hadoop/hdfs-site.xml")
            data_dir = input("Enter the datanode folder name:")
            os.system("echo '<value>%s</value>' >> /etc/hadoop/hdfs-site.xml"%data_dir)
            os.system("echo '</property>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")
            os.system("scp  /etc/hadoop/hdfs-site.xml 'root@%s':/etc/hadoop/hdfs-site.xml"%remoteip)

    elif location == "local":
        if node == "namenode":

            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")

            os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<configuration>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<property>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<name>dfs.name.dir</name>' >> /etc/hadoop/hdfs-site.xml")
            name_dir = input("Enter the namenode folder name:")
            os.system("echo '<value>%s</value>' >> /etc/hadoop/hdfs-site.xml"%name_dir)
            os.system("echo '</property>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")

        elif node == "datanode":

            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")

            os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<configuration>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<property>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<name>dfs.data.dir</name>' >> /etc/hadoop/hdfs-site.xml")
            data_dir = input("Enter the datanode folder name:")
            os.system("echo '<value>%s</value>' >> /etc/hadoop/hdfs-site.xml"%data_dir)
            os.system("echo '</property>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")

#core file

def core_file(node,location):
    if location == "remote":
        if node == "namenode":
                    
            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")

            os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")
            os.system("echo '<configuration>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<property>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<value>hdfs://0.0.0.0:9001</value>' >> /etc/hadoop/core-site.xml")
            os.system("echo '</property>' >> /etc/hadoop/core-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")
            os.system("scp  /etc/hadoop/core-site.xml 'root@%s':/etc/hadoop/core-site.xml"%remoteip)

        elif node == "datanode":
                    
            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")

            os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")
            os.system("echo '<configuration>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<property>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site.xml")
            name_node_ip = input("Enter namenode ip:")
            os.system("echo '<value>hdfs://%s:9001</value>' >> /etc/hadoop/core-site.xml"%name_node_ip)
            os.system("echo '</property>' >> /etc/hadoop/core-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")
            os.system("scp  /etc/hadoop/core-site.xml 'root@%s':/etc/hadoop/core-site.xml"%remoteip)


    elif location == "local":
        if node == "namenode":

            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")

            os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")
            os.system("echo '<configuration>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<property>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site.xml")
            name_node_ip = input("Enter namenode ip:")
            os.system("echo '<value>hdfs://%s:9001</value>' >> /etc/hadoop/core-site.xml"%name_node_ip)
            os.system("echo '</property>' >> /etc/hadoop/core-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")

        elif node == "datanode":

            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")

            os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")
            os.system("echo '<configuration>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<property>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site.xml")
            name_node_ip = input("Enter namenode ip:")
            os.system("echo '<value>hdfs://%s:9001</value>' >> /etc/hadoop/core-site.xml"%name_node_ip)
            os.system("echo '</property>' >> /etc/hadoop/core-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")

def menu():
    os.system("tput setaf 1")
    print("\t\t\t\t\t\tTECH-ASSISTANT MENU")

    os.system("tput setaf 7")
    print("\t\t\t\t\t=========----------------=========")

    os.system("tput setaf 2")
    print("""
            \t\t\t\tPress  1: To Run date command.
            \t\t\t\tPress  2: To Run cal command.
            \t\t\t\tPress  3: To Find ip of your computer.
            \t\t\t\tPress  4: To check connectivity of your internet.
            \t\t\t\tPress  5: To setup web-server for first time with httpd.
            \t\t\t\tPress  6: To setup webserver httpd.
            \t\t\t\tPress  7: TO create partition.
            \t\t\t\tPress  8: To format partition.
            \t\t\t\tPress  9: To mount partition.
            \t\t\t\tPress 10: To increase/decrese storage size.
            \t\t\t\tPress 11: To create hdfs cluster(change in hdfs file)
            \t\t\t\tPress 12: To format  namenode
            \t\t\t\tPress 13: To create hdfs cluster(change in core file).
            \t\t\t\tPress 14: To start (namenode/datanode).
            \t\t\t\tPress 15: To stop (namenode/datanode).
            \t\t\t\tPress 16: To store file in datanode.
            \t\t\t\tPress 17: To retrieve file stored in datanode.
            \t\t\t\tPress 18: To get report of cluster
            \t\t\t\tPress 19: To get docker menu list.
	    \t\t\t\tPress 20: To get aws menu list
            \t\t\t\tPress 21: To Exit.
            
            """)
    os.system("tput setaf 7")
    
def aws():
    while True:
        os.system("tput setaf 1")
        print("\t\t\t\t\t\t           AWS-MENU")

        os.system("tput setaf 7")
        print("\t\t\t\t\t===========-----------------------===========")

        os.system("tput setaf 2")
        print("""
                \t\t\tPress  1:To create key-pairs.
                \t\t\tPress  2:To describe key-pairs 
		\t\t\tPress  3:To create volumes. 
                \t\t\tPress  4:To create security groups.  
                \t\t\tPress  5:To launch ec2 instances
                \t\t\tPress  6:To describe ec2 instances.
                \t\t\tPress  7:To create s3 bucket.
                \t\t\tPress  8:To Exit.
                """)
        os.system("tput setaf 7")
	
        ch = input("Enter your choice:")
        if int(ch) == 1:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            a = "taskkey"
            os.system("aws ec2 create-key-pair --key-name {}".format(a))
            print("\n\n")
            os.system("tput setaf 7")
	 
        elif int(ch) == 2:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            os.system("aws ec2 describe-key-pairs")
            print("\n\n")
            os.system("tput setaf 7")

        elif int(ch) == 3:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            os.system("aws ec2 create-volume --availability-zone  us-east-1a --no-encrypted  --size 1")
            print("\n\n")
            os.system("tput setaf 7")
	
        elif int(ch) == 4:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            os.system("aws ec2 create-security-group --group-name {} --description {} --vpc-id vpc-0df0ed77".format( "Tasksg","Allows"))
            print("\n\n")
            os.system("tput setaf 7")

	
        elif int(ch) == 5:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            os.system("aws ec2 run-instances --image-id ami-098f16afa9edf40be --instance-type t2.micro --count 1 --subnet-id subnet-48d71869 --security-group-ids sg-97c523b5  --key-name taskkey ")
            print("\n\n")
            os.system("tput setaf 7")

        elif int(ch) == 6:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            os.system("aws ec2 describe-instances")
            print("\n\n")
            os.system("tput setaf 7")

        elif int(ch) == 7:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            os.system("aws s3 mb s3://aws-taskbucket-1234")
            print("\n\n")
            os.system("tput setaf 7")

        elif int(ch) == 8:
            break

        else:

            os.system("tput setaf 1")
            print("""
                    \t.....Wrong input.....
                    \t.....Wrong input.....
                    \t.....Wrong input.....
                    """)
        input("Press Enter to continue..........")
        os.system("clear")  
        os.system("tput setaf 7")

def docker():
    while True:
        os.system("tput setaf 1")
        print("\t\t\t\t\t\t         DOCKER-MENU")

        os.system("tput setaf 7")
        print("\t\t\t\t\t===========-----------------------===========")

        os.system("tput setaf 2")
        print("""
                \t\t\tPress  1:To install docker in your RHEL8 os.
                \t\t\tPress  2:To check docker info.  
                \t\t\tPress  3:To pull os images from docker hub.
                \t\t\tPress  4:To check how many docker images you have.
                \t\t\tPress  5:To run your docker os(container).(to install newos on the top of docker) 
                \t\t\tPress  6:To start os(container).
                \t\t\tPress  7:To stop os(container).
                \t\t\tPress  8:To get terminal of os(container)which is just started with option no 20.
                \t\t\tPress  9:To show container state..
                \t\t\tPress 10:To remove any os(container) from docker.
                \t\t\tPress 11:To remove any os  images of docker.
                \t\t\tPress 12:To Exit.
                """)
        os.system("tput setaf 7")
    
        ch = input("Enter your choice:")
        if int(ch) == 1:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            os.system("yum install docker-ce --nobest")
            os.system("tput setaf 7")
    
        elif int(ch) == 2:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            os.system("docker info")
            os.system("tput setaf 7")
    
        elif int(ch) == 3:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            os_name=input("image name:")
            os_version=input("image version:")
            os.system("docker pull {0}:{1} ".format(os_name,os_version))
            os.system("tput setaf 7")
    
        elif int(ch) == 4:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            os.system("docker images")
            os.system("tput setaf 7")

        elif int(ch) == 5:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            os_name=input("Write your os name:")
            os.system("docker run -it --name {}  ubuntu:latest".format(os_name))
            os.system("tput setaf 7")     
        
        elif int(ch) == 6:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            os_name=input("Write your osname that you want to stop")
            os.system("docker start {}".format(os_name))
            os.system("tput setaf 7") 

        elif int(ch) == 7:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            os_name=input("Write your osname that you want to start")
            os.system("docker stop {}".format(os_name))

            os.system("tput setaf 7")

        elif int(ch) == 8:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            os_name=input("write os name to get terminal of that os: ")
            os.system("docker attach {}".format(os_name))
            os.system("tput setaf 7")

        elif int(ch) == 9:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            os.system("docker ps -a")
            os.system("tput setaf 7")

        elif int(ch) == 10:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            os_name=input("Container name that you want to remove:")
            os.system("docker rm {}".format(os_name))
            os.system("tput setaf 7")

        elif int(ch) == 11:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            image_name=input("Image name that you want to remove:")
            image_version=input("Image version that you want to remove:")
            os.system("docker rmi -f {}:{}".format(image_name,image_version))
            os.system("tput setaf 7")

        elif int(ch) == 12:
            break

        else:

            os.system("tput setaf 1")
            print("""
                    \t.....Wrong input.....
                    \t.....Wrong input.....
                    \t.....Wrong input.....
                    """)
        input("Press Enter to continue..........")
        os.system("clear")

    
    
        os.system("tput setaf 7")
    

def conditions():
    if int(ch) == 1:
        os.system("tput setaf 2")
        print("you press {} here is your requested date command".format(ch))
        print("\n")
        os.system("date")
        os.system("tput setaf 7")

    elif int(ch) == 2:
        os.system("tput setaf 2")
        print("you press {} here is your requested cal command".format(ch))
        print("\n")
        os.system("cal")
        os.system("tput setaf 7")

    elif int(ch) == 3:
        os.system("tput setaf 2")
        print("you press {} here is your requested ip command".format(ch))
        print("\n")
        os.system("ifconfig enp0s3")
        os.system("tput setaf 7")
	
    elif int(ch) == 4:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        os.system("ping -c 4 www.google.com")
        os.system("tput setaf 7")

    elif int(ch) == 5:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n") 
        os.system("yum install httpd")
        os.system("systemctl start httpd")
        os.system("systemctl status httpd")
        os.system("tput setaf 7")
	
    elif int(ch) == 6:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        os.system("systemctl start httpd")
        os.system("systemctl status httpd")
        os.system("tput setaf 7")

    elif int(ch) == 7:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        os.system("pvcreate /dev/sdb")
        os.system("pvcreate /dev/sdc")
        os.system("vgcreate arthvg /dev/sdb  /dev/sdc")
        os.system("lvcreate --size 12G --name arthlv arthvg")
        os.system("lvdisplay arthvg/arthlv")
        os.system("tput setaf 7")
		
    elif int(ch) == 8:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        os.system("mkfs.ext4 /dev/arthvg/arthlv")
        os.system("tput setaf 7")
	
    elif int(ch) == 9:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        os.system("mount /dev/arthvg/arthlv  /master")
        os.system("df -h")
        os.system("tput setaf 7")

    elif int(ch) == 10:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        size = input("How much storage you want to <add/remove> in gb:")
        di = input("what do you want to do<extend/reduce>:")
        os.system("lv{0} --size {1}G /dev/arthvg/arthlv".format(di,size)) 
        os.system("resize2fs /dev/arthvg/arthlv")
        os.system("tput setaf 7")

    elif int(ch) == 11:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        node = input("what do you want to configer<namenode/datanode>:")
        hdfs_file(node,location)
        os.system("tput setaf 7")
       
    elif int(ch) == 12:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        os.system("hadoop namenode -format")
        os.system("tput setaf 7")
	    
    elif int(ch) == 13:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        node = input("what do you want to configer<namenode/datanode>:")
        core_file(node,location)
        os.system("tput setaf 7")

    elif int(ch) == 14:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        nodestart = input("what do you want to start(namenode/datanode):")
        os.system("hadoop-daemon.sh start {}".format(nodestart))
        os.system("jps")
        os.system("tput setaf 7")

    elif int(ch) == 15:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        nodestop = input("what do you want to stop(namenode/datanode):")
        os.system("hadoop-daemon.sh stop {}".format(nodestop))
        os.system("jps")
        os.system("tput setaf 7")

    elif int(ch) == 16:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        file_name = input("Your file name:")
        os.system("hadoop fs -put {} /".format(file_name))
        os.system("tput setaf 7")

    elif int(ch) == 17:
        os.system("tput setaf 2")
        print("you press {} here is your requested file".format(ch))
        print("\n")
        os.system("hadoop fs -ls  /")
        file_name = input("Your file name:")
        os.system("hadoop fs -cat /{}".format(file_name))
        os.system("jps")
        os.system("tput setaf 7")

    elif int(ch) == 18:
        os.system("tput setaf 2")
        print("you press {} here is your requested file".format(ch))
        print("\n")
        os.system("hadoop dfsadmin -report | less")
        os.system("tput setaf 7")
        

    elif int(ch) == 19:
        os.system("clear")  
        docker()

    elif int(ch) == 20:
        os.system("clear")
        aws()

    elif int(ch) == 21:     
        exit()


    else:

        os.system("tput setaf 1")		
        print("""
                \t.....Wrong input.....
                \t.....Wrong input.....
                \t.....Wrong input.....
                """)
    input("Press Enter to continue..........")
    os.system("clear")	

def menu2():
    os.system("clear")
    os.system("tput setaf 1")
    print("\t\t\t\t\tWELCOME TO YOUR TECH -- ASSISTANT")

    os.system("tput setaf 7")
    print("\t\t\t\t\t=========----------------=========")

    print("\n")

menu2()
passwd = getpass.getpass("Enter your password: ")
os.system("clear")
if passwd != "redhat":
    exit()

menu2()
print("\n")
location = input("select your location where you want to run your code(remote/local):")
print("\n")
if location == "remote":
    remoteip = input("Enter your remote IP:")

while True:        
        
        os.system("clear")
        menu()
        
        if location == "local":
            print("\n")	
            ch = input("Enter your choice:")        
            conditions()        
            

#remote login

        elif location == "remote":
            
            print("\n")
            ch = input("Enter your choice:")
            if int(ch) == 1:
                os.system("tput setaf 2")
                print("you press {} here is your requested date command".format(ch))
                print("\n")
                os.system("ssh {} date".format(remoteip))
                os.system("tput setaf 7")

            elif int(ch) == 2:
                os.system("tput setaf 2")
                print("you press {} here is your requested cal command".format(ch))
                print("\n")
                os.system("ssh {} cal".format(remoteip))
                os.system("tput setaf 7")

            elif int(ch) == 3:
                os.system("tput setaf 2")
                print("you press {} here is your requested ip command".format(ch))
                print("\n")
                os.system("ssh {} ifconfig enp0s3".format(remoteip))
                os.system("tput setaf 7")
	
            elif int(ch) == 4:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                os.system("ssh {} ping -c 4 www.google.com".format(remoteip))
                os.system("tput setaf 7")

            elif int(ch) == 5:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n") 
                os.system("ssh {} yum install httpd".format(remoteip))
                os.system("ssh {} systemctl start httpd".format(remoteip))
                os.system("ssh {} systemctl status httpd".format(remoteip))
                os.system("tput setaf 7")
	
            elif int(ch) == 6:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                os.system("ssh {} systemctl start httpd".format(remoteip))
                os.system("ssh {} systemctl status httpd".format(remoteip))
                os.system("tput setaf 7")

            elif int(ch) == 7:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                os.system("ssh {} pvcreate /dev/sdb".format(remoteip))
                os.system("tput set 7")
		
	
            elif int(ch) == 8:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                node = input("what do you want to configer<namenode/datanode>:")
                hdfs_file(node,location)
                os.system("tput setaf 7")
       
            elif int(ch) == 9:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                os.system("ssh {} hadoop namenode -format".format(remoteip))
                os.system("tput setaf 7")
	    
            elif int(ch) == 10:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                node = input("what do you want to configer<namenode/datanode>:")
                core_file(node,location)
                os.system("tput setaf 7")

            elif int(ch) == 11:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                nodestart = input("what do you want to start(namenode/datanode):")
                os.system("ssh {0} hadoop-daemon.sh start {1}".format(remoteip,nodestart))
                os.system("jps")
                os.system("tput setaf 7")

            elif int(ch) == 12:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                nodestop = input("what do you want to stop(namenode/datanode):")
                os.system("ssh {0} hadoop-daemon.sh stop {1}".format(remoteip,nodestop))
                os.system("jps")
                os.system("tput setaf 7")

            elif int(ch) == 13:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                file_name = input("Your file name:")
                os.system("ssh {0} hadoop fs -put {1} /".format(remoteip,file_name))
                os.system("tput setaf 7")

            elif int(ch) == 14:
                os.system("tput setaf 2")
                print("you press {} here is your requested file".format(ch))
                print("\n")
                file_name = input("Your file name:")
                os.system("ssh {0} hadoop fs -cat /{1}".format(remoteip,file_name))
                os.system("tput setaf 7")
	
            elif int(ch) == 15:
                os.system("clear")
                while True:
                    docker()

            elif int(ch) == 16:
                os.system("tput setaf 2")
                print("you press {} here is your requested file".format(ch))
                print("\n")
                os.system("ssh {} hadoop dfsadmin -report | less".format(remoteip))
                os.system("tput setaf 7")

            elif int(ch) == 17:     
                exit()
            
            else:

                os.system("tput setaf 1")		
                print("""
                        \t.....Wrong input.....
                        \t.....Wrong input.....
                        \t.....Wrong input.....
                    """)
            input("Press Enter to continue..........")
            os.system("clear")	        


