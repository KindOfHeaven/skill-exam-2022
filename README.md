# skill-exam-2022
Ten Kirill 244024 N42503c

## Task 1
**Name** - GitHub Skills Test  
**Preparation** - This task need no preparation  
**Implementation** - The local repository was initialized. I also created an online repository on GitHub and connected the local one to the online repository. After filling the initialized repository with based folders/info (folder for the first task and screens, README.md, etc...), I committed and pushed these changes to the online repo.  
**Troubleshooting** - No troubles were faced.  
**Verification** - Current repo is a verification for this task. Also, there are screens of implementation process in the folder task1/ScreensTask1/*

## Task 2
**Name** - Ansible Skills Test  
**Preparation** - For this task we need a remote machine. I used my second laptop as a remote machine. In order to connect to it I had to:  
1. Enable ssh connection to the device:  
    ```  
    sudo systemsetup -setremotelogin on  
    ```  
2. Install sshpass for the local machine. There were some troubles, which will be discussed in the specific topic.  
    ```  
    brew install hudochenkov/sshpass/sshpass  
    ```  
**Implementation** - To implement this task, following steps were taken:  
0. Ansible was already installed on my machine  
1. Were created 'hosts' file to use as an inventory for ansible:  
    ```  
    [webservers]  
    192.168.0.107 ansible_host=192.168.0.107 ansible_ssh_user=kirillten ansible_ssh_pass=ansible123  
    ```  
2. Were created ansible.cfg to use as a config for ansible:  
    ```  
    [default]  
    # hosts  
    inventory=./hosts  
    # RSA  
    host_key_checking = False  
    # retry files  
    retry_files_enable = False  
    ```  
3. Were created ansible playbook, in which we describe tasks to implement on the hosts:    
    ```
        - hosts: webservers  
        become: no  
          tasks:  
            - name: INSTALL NGINX  
              homebrew: name=nginx state=latest  
              notify:  
                - nginx systemd  
            - name: TEST NGINX  
              uri:  
                  url: http://{{ ansible_host }}  
                  method: GET  
          handlers:  
            - name: nginx systemd  
              systemd:  
                  name: nginx   
                  enabled: yes  
                  state: started  
    ```  
4. I've chosen nginx as a server, and as a test task we just try to access the default page.  

**Troubleshooting** - There was trouble with sshpass. Brew (package manager for OSX) will not install this package with following message:  
```  
We won't add sshpass because it makes it too easy for novice SSH users to ruin SSH's security.  
```  
So, I had to look for workaround and, as I found out, there is a repo with sshpass to install it bypassing brew security. It names is 'hudochenkov/sshpass/sshpass'  

**Verification** - I ran the playbook filed and got a success for all task. The default page returned 200, which means nginx is running OK.  
All used files and screenshots with implementation/verification can be found in task2/ScreensTask2  

## Task 3
**Name** - Docker  
**Preparation** - I had to install docker. I did it based on the official docs for Apple Silicon Mac  
**Implementation** - To implement this task, I've copied necessary files Dockerfile and startup.sh from ```https://github.com/cturra/docker-ntp```. After that, I've modified Dockerfile to find the right path to startup.sh. Then, I had to build and run docker using:
```
docker build -t randntp .
```
**Troubleshooting** - I faced a problem with using docker on osx. That is a basic problem for this os as turned out.
To solve this problem I had to run docker desktop app and run 'get-started' image. After that everything works fine.  
**Verification** - To verify, that connection was established I ran 
``` sudo sntp -sS 127.0.0.1 ``` which is macos analog for ntpdate. The result is below:
```
+0.057098 +/- 0.012743 127.0.0.1 127.0.0.1
```
This shows, that connection between container and local machine was established successfully.  
All used files and screenshots with implementation/verification can be found in task3/ScreensTask3


## Task 5
**Name** - Unit Testing  
**Preparation** - Copy the python module from the task  
**Implementation** - I've written test using unittest module for python. These were simple equality tests. As a result we got all 4 tests passed, which means that functions work as expected  
**Troubleshooting** - No troubles in this one  
**Verification** - The screen in the task5/ScreensTask5 shows the result
