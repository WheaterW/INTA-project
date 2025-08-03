Example for Configuring STelnet Login for an IPv4 User
======================================================

This section describes how to allow an IPv4 user to log in to an SSH server through STelnet to implement STelnet-based remote device login and management.

#### Networking Requirements

Large numbers of devices need to be managed and maintained on a network. You cannot connect each device to a terminal. When no reachable route exists between remote devices and a terminal, you can use Telnet to log in to the remote devices from the device that you have logged in to. Telnet provides no secure authentication mode, and data is transmitted in simple mode over TCP, which brings security risks.

STelnet is a secure Telnet service based on SSH connections. SSH provides encryption and authentication and protects devices against attacks, such as IP spoofing.

On the network shown in [Figure 1](#EN-US_TASK_0172359868__fig_dc_vrp_basic_cfg_004801), after the STelnet server function is enabled on the Router functioning as an SSH server, the PC functioning as an SSH client can log in to the SSH server in all, RSA, DSA, ECC, SM2, X509v3-SSH-RSA, password, password-RSA, password-ECC, password-DSA, password-SM2, or password-X509v3-RSA authentication mode. This example uses RSA authentication to describe how to configure the client to log in to the server through STelnet.

To prevent unauthorized users from logging in to the SSH server and improve system security, configure ACL rules on the SSH server.

**Figure 1** STelnet login![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 in this example represents GigabitEthernet0/0/0.

This section uses the management interface as an example to describe how to configure STelnet login. In actual application scenarios, you can select an interface for communication between the client and server based on the networking.


  
![](images/fig_dc_vrp_basic_cfg_004801.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Log in to the SSH server through the console port and configure an IP address for the management interface on the server.
2. Configure the VTY user interface on the SSH server.
3. Create a local user and configure an authentication mode and service type for the user.
4. Create an SSH user and configure an authentication mode for the user.
5. On the SSH client, create a key pair based on the configured SSH user authentication mode and copy the public key to the SSH server.
6. On the SSH server, edit the public key and assign the edited public key to the user.
7. Enable STelnet on the SSH server and set the service type of the SSH user to STelnet.
8. Configure an ACL rule for STelnet client login on the SSH server.
9. Set parameters for STelnet login to the server.

#### Data Preparation

To complete the configuration, you need the following data:

* PuTTYGen.exe and PuTTY.exe installed on the SSH client
* IP address (10.248.103.194/24) of the management interface on the SSH server
* Local user's authentication mode (password authentication), username (**huawei123**), and password (**YsHsjx\_202206**)
* SSH user's authentication mode (RSA authentication)
* Basic ACL 2000, used to allow the clients of the network segment 10.248.103.0/24 to access the SSH server

#### Procedure

1. Configure an IP address for the management interface on the SSH server.
   
   
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
   [~SSH Server] interface GigabitEthernet0/0/0
   ```
   ```
   [~SSH Server-GigabitEthernet0/0/0] undo shutdown
   ```
   ```
   [*SSH Server-GigabitEthernet0/0/0] ip address 10.248.103.194 255.255.255.0
   ```
   ```
   [*SSH Server-GigabitEthernet0/0/0] commit
   ```
   ```
   [~SSH Server-GigabitEthernet0/0/0] quit
   ```
2. Configure the VTY user interface on the SSH server.
   
   
   ```
   [~SSH Server] user-interface vty 0 4
   ```
   ```
   [*SSH Server-ui-vty0-4] authentication-mode aaa
   ```
   ```
   [*SSH Server-ui-vty0-4] protocol inbound ssh
   ```
   ```
   [*SSH Server-ui-vty0-4] user privilege level 3
   ```
   ```
   [*SSH Server-ui-vty0-4] commit
   ```
   ```
   [~SSH Server-ui-vty0-4] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If SSH is configured as the login protocol, the device automatically disables the Telnet function.
3. On the server, create a local user, add the user to the administrator group, and configure a service type for the user.
   
   
   ```
   [~SSH Server] aaa
   ```
   ```
   [~SSH Server-aaa] local-user huawei123 password
   ```
   ```
   Please configure the password (8-128)
   Enter Password:
   Confirm Password:
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If neither **cipher** nor **irreversible-cipher** is specified, a password is entered in man-machine interaction mode and is not displayed by the system.
     
     When the user security policy is configured, the value is a string of 8 to 128 case-insensitive characters without spaces. When the user security policy is not configured, the value is a string of 1 to 128 case-insensitive characters without spaces.When the user security policy is configured, the password cannot be the same as the user name or its reverse. The password must contain the following characters: upper-case character, lower-case character, digit, and special character.
     
     Special characters cannot include question marks (?) or spaces. However, if the password is enclosed in double quotation marks ("), spaces are allowed.
     + If double quotation marks are used to set a password with spaces, the double quotation marks cannot contain other double quotation marks.
     + If double quotation marks are used to set a password without any space, the double quotation marks can contain other double quotation marks.
     
     For example, the password "Aa 123"45"" is invalid, whereas the password "Aa123"45"" is valid.
   * If **cipher** is specified, a password can be entered in either simple or cipher text.
     
     In simple text mode, the password requirements are the same as those when **cipher** is not specified. If you enter a password in simple text, the system displays the password in simple text mode, which poses a security risk. Therefore, you are advised to enter a password in man-machine interaction mode.
     
     A password is displayed in cipher text in the configuration file regardless of whether it is entered in simple or cipher text.
   * If **irreversible-cipher** is specified, a password can be entered in either simple text or irreversible cipher text.
     
     In simple text mode, the password requirements are the same as those when **irreversible-cipher** is not specified.
     
     A password is displayed in cipher text in the configuration file regardless of whether it is entered in simple text or irreversible cipher text.
   ```
   [*SSH Server-aaa] local-user huawei123 service-type ssh
   ```
   ```
   [*SSH Server-aaa] local-user huawei123 user-group manage-ug
   ```
   ```
   [*SSH Server-aaa] commit
   ```
   ```
   [~SSH Server-aaa] quit
   ```
4. Create an SSH user on the server and configure the authentication mode for the user.
   
   
   ```
   [~SSH Server] ssh user huawei123
   ```
   ```
   [*SSH Server] ssh user huawei123 authentication-type rsa
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
   ```
   [*SSH Server] commit
   ```
5. Use PuTTY to create an RSA key pair on the SSH client and copy the public key to the SSH server.
   
   
   1. Enter the Windows Command Prompt window.
   2. Enter **PuTTYGen** and click **Generate** to generate a key pair, as shown in [Figure 2](#EN-US_TASK_0172359868__fig_dc_vrp_basic_cfg_013502).
      
      **Figure 2** PuTTY Key Generator (1)  
      ![](images/fig_dc_vrp_basic_cfg_013502.png)
      
      Move the mouse continuously during the generation of the key pair and move the pointer in the window other than the process bar in green. Otherwise, the progress bar stops, and the generation of the key pair stops as well. [Figure 3](#EN-US_TASK_0172359868__fig_dc_vrp_basic_cfg_013503) shows that the key pair is being generated.
      
      **Figure 3** PuTTY Key Generator (2)  
      ![](images/fig_dc_vrp_basic_cfg_013503.png)
   3. After the key pair is generated, enter the password in the **Key passphrase** text box and enter the password again in the **Confirm passphrase** text box. This password is used for the SSH terminal user to log in to the SSH server. Click **Save private key**, enter **private** for the name of the private key file, and click **Save**. Copy the generated public key to the Notepad and name it **public.txt**.
      
      **Figure 4** PuTTY Key Generator (3)  
      ![](images/fig_dc_vrp_basic_cfg_013504.png)
6. On the SSH server, edit the public key and assign the edited public key to the user.
   
   
   ```
   [~SSH Server] rsa peer-public-key rsa01 encoding-type openssh
   ```
   ```
   [*SSH Server-rsa-public-key] public-key-code begin
   ```
   ```
   [*SSH Server-rsa-public-key-rsa-key-code] ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAxHbcqV6
    qqnb1+jQQ0qFLptxWS1xRFfDe6DuMaX2eRUCx3fp2eBA1bgUfHd7eCO05CfHfC443oNBwlj/39Obi8kS
    RIQSlXOU1KIP8DNYtwU/N23p/YDHzbgOVvN6dSr+Ua2Er7m2Hehzdo2XoGuWokqhnuMpA7O7zykXs7rM
    6tdf+hh/992o6GHBD9IbJe9mG6WoAmDkBmedXzBqJeeGb2wbGg9hBTIgVQqZNhthGcVlLUlPJlZQi1ZO
    L3C/cVIOXqnVOqqxHk6nlWcMRo0PxOAegtyzsBETnvcEO2xVw6zF0WVFvU60C99THB+GpuHuRdWzvUNC
    ZpsjmCwkg+4RFGQ== rsa-key-20190422
   ```
   ```
   [*SSH Server-rsa-public-key-rsa-key-code] public-key-code end
   ```
   ```
   [*SSH Server-key-code] peer-public-key end 
   ```
   ```
   [*SSH Server] ssh user huawei123 assign rsa-key rsa01
   ```
   ```
   [*SSH Server] commit
   ```
7. Enable the STelnet function and set the service type to STelnet.
   
   
   ```
   [~SSH Server] stelnet server enable
   ```
   ```
   [*SSH Server] ssh server-source -i GigabitEthernet0/0/0
   ```
   ```
   [*SSH Server] ssh user huawei123 service-type stelnet
   ```
   ```
   [*SSH Server] commit
   ```
8. Configure an ACL rule.
   
   
   ```
   [~SSH Server] acl 2000
   ```
   ```
   [*SSH Server-acl4-basic-2000] rule permit source 10.248.103.0 8
   ```
   ```
   [*SSH Server-acl4-basic-2000] quit
   ```
   ```
   [*SSH Server] ssh server acl 2000
   ```
   ```
   [*SSH Server] commit
   ```
9. Use PuTTY.exe to log in to the SSH server from the client.
   
   
   1. Start the PuTTY.exe program. The client configuration page is displayed, as shown in [Figure 5](#EN-US_TASK_0172359868__fig_dc_vrp_basic_cfg_013512). For security purposes, using PuTTY 0.58 or later is recommended. Enter the IP address of the SSH server in the **Host Name (or IP address)** text box.
      
      **Figure 5** SSH client configuration page (1)  
      ![](images/fig_dc_vrp_basic_cfg_013512.png)
   2. On the SSH client configuration page, choose **Connection** > **SSH** from the Category navigation tree. The dialog box as shown in [Figure 6](#EN-US_TASK_0172359868__fig_dc_vrp_basic_cfg_013509) is displayed. In the **Protocol options** area, set **SSH protocol version** to 2.
      
      **Figure 6** SSH client configuration page (2)  
      ![](images/fig_dc_vrp_basic_cfg_013509.png)
   3. Select **Auth** in **SSH**. The dialog box as shown in [Figure 7](#EN-US_TASK_0172359868__fig_dc_vrp_basic_cfg_013510) is displayed. Click **Browse** to import the private key file **private.ppk**.
      
      **Figure 7** SSH client configuration page (3)  
      ![](images/fig_dc_vrp_basic_cfg_013510.png)
   4. Click **Open**. If the connection is normal, the system prompts you to enter the username, as shown in [Figure 8](#EN-US_TASK_0172359868__fig_dc_vrp_basic_cfg_013513).
      
      **Figure 8** SSH client login authentication page  
      ![](images/fig_dc_vrp_basic_cfg_013513.png "Click to enlarge")

#### Configuration Files

* SSH server configuration file
  
  ```
  #
  sysname SSH Server
  #
  acl number 2000
   rule 5 permit source 10.248.103.0 0.0.0.255
  #
  rsa peer-public-key rsa01 encoding-type openssh
   public-key-code begin
    ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAxHbcqV6qqnb1+jQQ0qFLptxWS1xRFfDe6DuMaX2eRUCx
    3fp2eBA1bgUfHd7eCO05CfHfC443oNBwlj/39Obi8kSRIQSlXOU1KIP8DNYtwU/N23p/YDHzbgOVvN6d
    Sr+Ua2Er7m2Hehzdo2XoGuWokqhnuMpA7O7zykXs7rM6tdf+hh/992o6GHBD9IbJe9mG6WoAmDkBmedX
    zBqJeeGb2wbGg9hBTIgVQqZNhthGcVlLUlPJlZQi1ZOL3C/cVIOXqnVOqqxHk6nlWcMRo0PxOAegtyzs
    BETnvcEO2xVw6zF0WVFvU60C99THB+GpuHuRdWzvUNCZpsjmCwkg+4RFGQ== rsa-key
   public-key-code end
   peer-public-key end
  #
  aaa
   local-user huawei123 password irreversible-cipher $1c$+,JS+))\\2$KVNj(.3`_5x0FCKGv}H&.kUTI`Ff&H*eBqO.ua>)$
   local-user huawei123 service-type ssh
   local-user huawei123 user-group manage-ug
  #
  interface GigabitEthernet0/0/0
   undo shutdown
   ip address 10.248.103.194 255.255.255.0
  #
  stelnet server enable
  ssh server-source -i GigabitEthernet0/0/0
  ssh user huawei123
  ssh user huawei123 authentication-type rsa
  ssh user huawei123 assign rsa-key rsa01
  ssh user huawei123 service-type stelnet
  ssh server acl 2000
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
   user privilege level 3
  #
  return
  ```