Example for Using TFTP to Access Other Devices
==============================================

You can run the TFTP software on the TFTP server and set the directory of source files on the server to upload and download files.

#### Networking Requirements

In the TCP/IP protocol suite, FTP is most commonly used to transfer files. However, FTP brings complex interactions between terminals and servers, which is hard to implement on terminals that do not run advanced operating systems. TFTP is designed for file transfer that does not require complex interactions between terminals and servers. It is simple, requiring a few costs. TFTP can be used only for simple file transfer without authentication.

On the network shown in [Figure 1](#EN-US_TASK_0172360135__fig_dc_vrp_basic_cfg_011101), a user logs in to a TFTP client from a PC and then uploads files to or downloads files from a TFTP server.

**Figure 1** Using TFTP to access another device  
![](images/fig_dc_vrp_basic_cfg_011101.png)  


#### Precautions

In insecure network environments, you are advised to use a secure protocol. [Example for Using SFTP to Log In to Another Device for File Access (ECC Authentication Mode)](dc_vrp_basic_cfg_0121.html) provides examples for secure protocols.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Run the TFTP software on the TFTP server and set the directory of source files on the server.
2. Use TFTP commands on the TFTP client to download files.
3. Use TFTP commands on the TFTP client to upload files.

#### Data Preparation

To complete the configuration, you need the following data:

* TFTP software to be installed on the TFTP server
* Name of the file to be downloaded and path of the file on the TFTP server
* Name of the file to be uploaded and path of the file on the TFTP client

#### Procedure

1. Enable the TFTP server function.
   
   
   
   Set **Current Directory** to the directory where the files to be downloaded reside on the TFTP server, as shown in [Figure 2](#EN-US_TASK_0172360135__fig_dc_vrp_basic_cfg_011102).
   
   **Figure 2** Setting the current directory on the TFTP server  
   ![](images/fig_dc_vrp_basic_cfg_011102.png)  
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The displayed window may vary with the TFTP software.
   
   Run the **tftpservermt** command on the client to enter the TFTP server path and run the following command:
   
   ```
   /home/tftpservermt # ./tftpserver -v -i tftpserver.ini
   TFTP Server MultiThreaded Version 1.61 Unix Built 1611
   starting TFTP...
   username: root
   alias / is mapped to /home/
   permitted clients: all
   server port range: all
   max blksize: 65464
   default blksize: 512
   default timeout: 3
   file read allowed: Yes
   file create allowed: Yes
   file overwrite allowed: Yes
   thread pool size: 1
   listening on: 0.0.0.0:69
   Accepting requests..
   ```
2. Log in to the TFTP client through the terminal emulation program of the PC to download a file.
   
   
   ```
   <HUAWEI> tftp 10.18.26.141 get a.txt cfcard:/b.txt
   ```
   ```
   Warning: cfcard:/b.txt exists, overwrite? Please select
   [Y/N]:y
   Transfer file in binary mode.
   Please wait for a while...
   /
   3338 bytes transferred
   File transfer completed
   ```
3. Verify the configuration.
   
   
   
   Run the **dir** command on the TFTP client to view the directory in which the downloaded file is saved.
   
   ```
   <HUAWEI> dir
   ```
   ```
   Directory of 0/17#cfcard:/
   
     Idx  Attr     Size(Byte)  Date        Time(LMT)   FileName
       0  -rw-     3,338       Jan 25 2011  09:27:41   b.txt
       1  -rw-     103,265,123 Jan 25 2011  06:49:07   V800R023C00SPC500B020D0123.cc
       2  -rw-     92,766,274  Jan 25 2011  06:49:10   V800R023C00SPC500SPC007B008D1012.cc
   
   109,867,396 KB total (102,926,652 KB free)
   ```
4. Log in to the TFTP client through the terminal emulation program of the PC to upload a file.
   
   
   ```
   <HUAWEI> tftp 10.111.16.160 put sample.txt
   ```
   ```
     Info: Transfer file in binary mode.
   Please wait for a while...
   \     100% [***********]
   File transfer completed
   ```

#### Configuration Files

None