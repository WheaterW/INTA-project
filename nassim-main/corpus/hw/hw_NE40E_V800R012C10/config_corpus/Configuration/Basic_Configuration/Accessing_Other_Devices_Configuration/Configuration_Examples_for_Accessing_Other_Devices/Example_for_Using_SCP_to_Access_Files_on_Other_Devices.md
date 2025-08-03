Example for Using SCP to Access Files on Other Devices
======================================================

To allow SCP client to access the SSH server and download files.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172360150__fig_dc_vrp_basic_cfg_012901), the device functioning as the SCP client has a reachable route to the SSH server and can download files from the SSH server.

**Figure 1** Using SCP to access another device  
![](images/fig_dc_vrp_basic_cfg_012901.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a local RSA key pair on the SSH server.
2. Create an SSH user on the SSH server.
3. Enable the SCP service function on the SSH server.
4. Enable first authentication on the SSH client.
5. Specify the IP address of the source interface on the SCP client.
6. Download files from the SSH server to the SCP client.

#### Data Preparation

To complete the configuration, you need the following data:

* SSH user name, authentication mode, and authentication password
* IP address of the source interface on the SCP client
* Names and paths of the source and destination files

#### Procedure

1. Configure the SSH server to generate a local RSA key pair.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname SSH Server
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~SSH Server] rsa local-key-pair create
   ```
   ```
   The key name will be: SSH Server_Host  
   The range of public key size is (2048, 3072).  
   NOTE: Key pair generation will take a short while.  
   Please input the modulus [default = 3072]:3072
   ```
2. Create an SSH user on the SSH server.
   
   
   
   # Configure VTY user interfaces.
   
   ```
   [*SSH Server] user-interface vty 0 4
   ```
   ```
   [*SSH Server-ui-vty0-4] authentication-mode aaa
   ```
   ```
   [*SSH Server-ui-vty0-4] protocol inbound ssh
   ```
   ```
   [*SSH Server-ui-vty0-4] quit
   ```
   
   # Create an SSH user named client001 and specify the password authentication mode for the user.
   
   ```
   [*SSH Server] ssh user client001
   Info: Succeeded in adding a new SSH user.
   ```
   ```
   [*SSH Server] ssh user client001 authentication-type password
   ```
   ```
   [*SSH Server] ssh server cipher aes256_gcm aes128_gcm aes256_ctr aes192_ctr aes128_ctr 
   ```
   ```
   [*SSH Server] ssh server hmac sha2_512 sha2_256
   ```
   ```
   [*SSH Server] ssh server key-exchange dh_group_exchange_sha256 
   ```
   ```
   [*SSH Server] ssh server publickey rsa_sha2_256 rsa_sha2_512 
   ```
   ```
   [*SSH Server] ssh server dh-exchange min-len 3072
   ```
   ```
   [*SSH Server] ssh client publickey rsa_sha2_256 rsa_sha2_512
   ```
   ```
   [*SSH Server] ssh client cipher aes256_gcm aes128_gcm aes256_ctr aes192_ctr aes128_ctr 
   ```
   ```
   [*SSH Server] ssh client hmac sha2_512 sha2_256 
   ```
   ```
   [*SSH Server] ssh client key-exchange dh_group_exchange_sha256 
   ```
   
   # Set the password to %TGB6yhn7ujm for the SSH user client001.
   
   ```
   [*SSH Server] aaa
   ```
   ```
   [*SSH Server-aaa] local-user client001 password
   Please configure the password (8-128)
   Enter Password:
   Confirm Password:
   Info: A new user is added.
   ```
   ```
   [*SSH Server-aaa] local-user client001 service-type ssh
   ```
   ```
   [*SSH Server-aaa] local-user client001 level 3
   ```
   ```
   [*SSH Server-aaa] quit
   ```
   
   # Set the service type of the SSH user client001 to **all**.
   
   ```
   [*SSH Server] ssh user client001 service-type all
   ```
3. Enable the SCP service function on the SSH server.
   
   
   ```
   [*SSH Server] scp server enable
   ```
   ```
   [*SSH Server] commit
   ```
4. Download files from the server to the SCP client.
   
   
   
   # For the first login, enable first authentication on the SSH client.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname SCP Client
   ```
   ```
   [*SCP Client] ssh client first-time enable
   ```
   
   # Set the source IP address of the SCP client to 1.1.1.1 (the IP address of a loopback interface).
   
   ```
   [*SCP Client] scp client-source -a 1.1.1.1
   Info: Succeeded in setting the source address of the SCP client to 1.1.1.1.
   ```
   
   # Use the AES128 algorithm to encrypt the **license.txt** file, and download the file to the local user directory from the remote SCP server at 172.16.104.110.
   
   ```
   [*SCP Client] scp -a 1.1.1.1 -cipher aes128 client001@172.16.104.110:license.txt license.txt
   ```
   ```
   [*SCP Client] commit
   ```
5. Verify the configuration.
   
   
   
   Run the [**display scp-client**](cmdqueryname=display+scp-client) command on the SCP client. The command output is as follows:
   
   ```
   <HUAWEI> display scp-client
   ```
   ```
    The source address of SCP client is 1.1.1.1.
   ```

#### Configuration Files

* SCP server configuration file
  
  ```
  #
   sysname SSH Server
  #
  aaa
   local-user client001 password irreversible-cipher @%@%1-w$!gvBa#6W,ZUm2EN*BYqNWwI3BV\uV`%_oauS;RQB%>>~GV#QzO~k/8;U6;@%@%
   local-user client001 service-type ssh
   local-user client001 level 3
   # 
   scp server enable 
   ssh user client001
   ssh user client001 authentication-type password
   ssh user client001 service-type all
  #
  ssh server cipher aes256_gcm aes128_gcm aes256_ctr aes192_ctr aes128_ctr 
  ssh server hmac sha2_512 sha2_256 
  ssh server key-exchange dh_group_exchange_sha256
  #
  ssh server publickey rsa_sha2_256 rsa_sha2_512
  #
  ssh server dh-exchange min-len 3072
  #
  ssh client publickey dsa ecc rsa rsa_sha2_256 rsa_sha2_512
  #
  ssh client cipher aes256_gcm aes128_gcm aes256_ctr aes192_ctr aes128_ctr
  ssh client hmac sha2_512 sha2_256
  ssh client key-exchange dh_group_exchange_sha256
  #
  user-interface vty 0 4
   authentication-mode aaa
   protocol inbound ssh
  #
  return
  ```
* SCP client configuration file
  
  ```
  #
   sysname SCP Client
  #
   ssh client first-time enable
   scp client-source 1.1.1.1
  #
  return
  ```