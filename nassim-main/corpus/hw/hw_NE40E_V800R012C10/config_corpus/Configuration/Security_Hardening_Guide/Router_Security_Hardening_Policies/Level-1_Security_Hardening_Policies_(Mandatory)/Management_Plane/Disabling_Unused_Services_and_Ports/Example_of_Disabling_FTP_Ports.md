Example of Disabling FTP Ports
==============================

Example of Disabling FTP Ports

#### Networking Requirements

Files must be transferred in Secure File Transfer Protocol (SFTP) mode to ensure file transfer reliability. File Transfer Protocol (FTP) ports of devices must be disabled to ensure device security and prevent unauthorized users from attacking devices using FTP ports.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Check whether the FTP port of a device is enabled and whether the FTP port needs to be disabled.
2. Disable the FTP port to prevent users from transferring files using FTP.
3. View the status of the FTP port of the device and check whether the FTP port is successfully disabled.

#### Data Preparation

None


#### Procedure

1. Check the status of the IPv4 FTP port.
   ```
   <HUAWEI> display tcp status
   ----------------------------------------------------------------------------
   Cid/SocketID         Local Addr:Port       Foreign Addr:Port   VPNID      State
   ----------------------------------------------------------------------------
   0x80932724/131216    0.0.0.0:22            0.0.0.0:0           1          LISTEN 
   0x80C8272A/131218    0.0.0.0:23            0.0.0.0:0           1          LISTEN
   0x80952725/131219    0.0.0.0:21            0.0.0.0:0           1          LISTEN
   ```
   
   The command output shows that the FTP port is enabled.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The FTP server may listen to another port. You can run the following command to view the port number listened by the FTP server.
   
   ```
   <HUAWEI> display ftp-server
   ```
   ```
   Server state             : Enabled
   IPv6 server state        : disabled
   Timeout value (mins)     : 30
   IPv6 Timeout value (mins): 30
   Listen port              : 21
   IPv6 listen port         : 21
   ACL name                 :
   IPv6 ACL name            : 
   ACL number               :
   IPv6 ACL number          : 
   Current user count       : 0
   Max user number          : 15
   ```
2. Disable the FTP port.
   ```
   <HUAWEI> system-view
   [~HUAWEI] undo ftp server
   Warning: The operation will stop the FTP server. Do you want to continue? [Y/N]:y
   Info: Succeeded in closing the FTP server.
   [*HUAWEI] commit
   ```
3. Check whether the FTP port is successfully disabled.
   ```
   <HUAWEI> display tcp status
   ----------------------------------------------------------------------------
   Cid/SocketID         Local Addr:Port       Foreign Addr:Port   VPNID      State
   ----------------------------------------------------------------------------
   0x80932724/131216    0.0.0.0:22            0.0.0.0:0           1          LISTEN 
   0x80C8272A/131218    0.0.0.0:23            0.0.0.0:0           1          LISTEN
   ```
   
   The command output shows that the FTP port is disabled.

#### Verifying the Security Hardening Result

* Run the **[**display tcp status**](cmdqueryname=display+tcp+status)** command to check the status of the FTP port.
* Run the [**display ftp-server**](cmdqueryname=display+ftp-server) command to check the status of the FTP server.