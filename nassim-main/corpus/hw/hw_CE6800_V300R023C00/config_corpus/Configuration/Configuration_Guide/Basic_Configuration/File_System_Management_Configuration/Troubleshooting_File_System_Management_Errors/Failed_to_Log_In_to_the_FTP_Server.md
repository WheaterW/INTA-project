Failed to Log In to the FTP Server
==================================

Failed to Log In to the FTP Server

#### Possible Causes

* The FTP server function is not enabled.
* The FTP server does not use the default port number, and the port number of the FTP server is not specified when the FTP server is accessed from the FTP client.
* The FTP user information, working directory, and user privilege level are not configured on the FTP server.
* The number of online FTP users reaches the upper limit.
* An ACL is configured on the FTP server to deny the access of the FTP user.

#### Procedure

1. Check whether the FTP server function is enabled.
   
   
   
   Run the [**display ftp server**](cmdqueryname=display+ftp+server) command in any view to check the status of the FTP server.
   
   * If the following information is displayed, the FTP server function is disabled:
     ```
     <HUAWEI> display ftp server
     Server state              : Disabled
     IPv6 server state         : Disabled
     Timeout value (mins)      : 10
     IPv6 Timeout value (mins) : 10
     Listen port               : 21
     IPv6 listen port          : 21
     ACL name                  : 
     IPv6 ACL name             : 
     ACL number                :  
     IPv6 ACL number           :  
     Current user count        : 0
     Max user number           : 15
     ```
     
     Run the [**ftp server enable**](cmdqueryname=ftp+server+enable) command in the system view to enable the FTP server function.
     
     ```
     <HUAWEI> system-view
     [~HUAWEI] ftp server enable
     Warning: FTP is not a secure protocol, and it is recommended to use SFTP.
     [*HUAWEI] commit
     ```
   * If the following information is displayed, the FTP server function is enabled:
     ```
     <HUAWEI> display ftp server
     Server state              : Enabled
     IPv6 server state         : Disabled
     Timeout value (mins)      : 10
     IPv6 Timeout value (mins) : 10
     Listen port               : 21
     IPv6 listen port          : 21
     ACL name                  : 
     IPv6 ACL name             : 
     ACL number                :  
     IPv6 ACL number           :  
     Current user count        : 0
     Max user number           : 15
     ```
2. Check whether the port number of the FTP server is the default port number.
   
   Run the [**display ftp server**](cmdqueryname=display+ftp+server) command in any view to check the FTP server port.
   ```
   <HUAWEI> display ftp server
   Server state              : Enabled
   IPv6 server state         : Disabled
   Timeout value (mins)      : 10
   IPv6 Timeout value (mins) : 10
   Listen port            : 21
   IPv6 listen port          : 21
   ACL name                  :
   IPv6 ACL name             :
   ACL number                :
   IPv6 ACL number           :
   Current user count        : 0
   Max user number           : 15
   ```
   
   
   
   If the FTP server port is not 21, run the [**ftp server port**](cmdqueryname=ftp+server+port) command to set the port number to 21.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] undo ftp server
   Info: Succeeded in closing the FTP server.
   [*HUAWEI] ftp server port 21
   [*HUAWEI] ftp server enable
   Warning: FTP is not a secure protocol, and it is recommended to use SFTP.
   [*HUAWEI] commit
   ```
   
   Alternatively, specify the port number of the FTP server on the FTP client when connecting to the FTP server from the FTP client.
3. Check whether the FTP user information, authorized directory, and user privilege level are configured.
   
   
   
   The user name, password, authorized directory, and user privilege level are mandatory for an FTP user. An FTP user cannot log in to the FTP server if the FTP authorized directory or user privilege level is not specified.
   
   For details, see [Configure a local FTP user.](vrp_file_cfg_0009.html#EN-US_TASK_0000001563990885__dc_cfg_file_0006step02) in "Configuring the Device as an FTP Server."
4. Check whether the number of users on the FTP server reaches the upper limit.
   
   
   
   Run the [**display ftp server users**](cmdqueryname=display+ftp+server+users) command to check whether the number of FTP users reaches 15.
5. Check whether an ACL is configured on the FTP server.
   
   
   
   Run the [**display ftp server**](cmdqueryname=display+ftp+server) command to check whether an ACL is configured on the FTP server.
   
   If an ACL is configured on the FTP server, the FTP server allows only access from the IP addresses permitted by the ACL rules.