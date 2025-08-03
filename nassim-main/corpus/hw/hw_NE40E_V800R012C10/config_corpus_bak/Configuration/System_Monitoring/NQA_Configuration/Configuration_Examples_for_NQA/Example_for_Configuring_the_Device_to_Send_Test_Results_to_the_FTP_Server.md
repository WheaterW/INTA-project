Example for Configuring the Device to Send Test Results to the FTP Server
=========================================================================

Delivering test results to the FTP server can save the test results to the maximum extent.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172373160__fig_dc_vrp_cfg_00533502), DeviceA serves as the client to perform an ICMP test and send test results to the FTP server through FTP.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interfaces 1 and 2 represent GE0/1/0 and GE0/2/0, respectively.

**Figure 1** Configuring the device to send test results to the FTP server  
![](images/fig_dc_vrp_cfg_00533502.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set parameters for configuring the device to send test results to the FTP server.
2. Start a test instance.
3. Verify the configuration.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the FTP server
* Username and password used for logging in to the FTP server
* Name of a file in which test results are saved through FTP
* Interval at which test results are uploaded through FTP

#### Procedure

1. Set parameters for configuring the device to send test results to the FTP server.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] nqa upload test-type icmp ftp ipv4 10.1.2.8 file-name test1 port 21 username ftp password YsHsjx_202206 interval 600 retry 3
   ```
   ```
   [*DeviceA] commit
   ```
2. Start a test instance.
   
   
   ```
   [~DeviceA] nqa test-instance admin icmp
   ```
   ```
   [*DeviceA] test-type icmp
   ```
   ```
   [*DeviceA] destination-address ipv4 10.1.1.10
   ```
   ```
   [*DeviceA-admin-icmp] start now
   ```
   ```
   [*DeviceA-admin-icmp] commit
   ```
   ```
   [~DeviceA-admin-icmp] quit
   ```
3. Verify the configuration.
   
   
   
   # Display information about the files that are being uploaded and the files that have been uploaded.
   
   ```
   [~DeviceA] display nqa upload file-info
   ```
   ```
   The total number of upload file records is : 2                                  
   ---------------------------------------------------------------                 
   FileName   : NQA_38ba47987301_icmp_20230814112319701_test1.xml                  
   Status     : Upload success                                                     
   RetryTimes : 3
   UploadTime : 2023-08-14 11:23:21.697                                            
                                                                                   
   ---------------------------------------------------------------
   FileName   : NQA_38ba47987301_icmp_20230814112421710_test1.xml                  
   Status     : Uploading                                                          
   RetryTimes : 3
   UploadTime : --                                                                 
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceA
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/1/0
  ```
  ```
   ip address 10.1.1.11 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/2/0
  ```
  ```
   ip address 10.1.2.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  nqa upload test-type icmp ftp ipv4 10.1.2.8 file-name test1 port 21 username ftp password %^%#`P'|9L1x62lN*b+C~wMTT|$EA7+z0XOFC_,B$M+"%^%# interval 600 retry 3
  ```
  ```
   nqa test-instance admin icmp
  ```
  ```
   test-type icmp
  ```
  ```
   destination-address ipv4 10.1.1.10
  ```
  ```
   start now
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceB
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   ip address 10.1.1.10 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```