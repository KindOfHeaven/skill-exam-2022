# skill-exam-2022
Ten Kirill 244024 N42503c

## Task 1
**Name** - GitHub Skills Test
**Preparation** - This task need no preparation
**Implementation** - The local repository was initialized. I also created an online repository on GitHub and connected the local one to the online repository. After filling the initialized repository with based folders/info (folder for the first task and screens, README.md, etc...), I committed and pushed these changes to the online repo.
**Troubleshooting** - No troubles were faced.
**Verification** - Current repo is a verification for this task. Also, there are screens of implementation process in the folder task1/ScreensTask1/*

**Screens

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
**Name** - 
