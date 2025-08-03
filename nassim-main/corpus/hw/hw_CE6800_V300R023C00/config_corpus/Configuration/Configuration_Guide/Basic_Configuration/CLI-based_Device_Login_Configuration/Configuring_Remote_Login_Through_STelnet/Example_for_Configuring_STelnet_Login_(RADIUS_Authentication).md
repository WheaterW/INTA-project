Example for Configuring STelnet Login (RADIUS Authentication)
=============================================================

Example for Configuring STelnet Login (RADIUS Authentication)

#### Networking Requirements

The network administrator requires secure remote login to a device and high network security for protecting the network against unauthorized access. To meet the requirements, you can configure STelnet login based on RADIUS authentication.

In [Figure 1](#EN-US_TASK_0000001608515697__fig1016891519504), DeviceA functions as an SSH server and there are reachable routes between it and the RADIUS server. The IP address and port number of the RADIUS server are 10.1.6.6 and 1812, respectively.

**Figure 1** Network diagram for configuring STelnet login based on RADIUS authentication  
![](figure/en-us_image_0000001821163306.png)![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set device interface parameters.
2. Configure the SSH server to generate a local key pair to implement secure data exchange between the server and client.
3. Configure STelnet to enable users to log in to the device through STelnet.
4. Configure an ACL rule to ensure that only users matching the ACL rule can log in to the device.
5. Configure the RADIUS protocol to implement RADIUS authentication. After the configuration is complete, users must use the user name and password configured on the RADIUS server to log in to the device through STelnet, ensuring login security.
6. Configure the RADIUS server.

#### Configuration Precautions

* Ensure that the SSH server login software has been installed on the user terminal before configuring STelnet login.
* Ensure that there are reachable routes between the user terminal and the device and between the device and RADIUS server.

* After a domain is configured as the global default administrative domain, the AAA configuration in this domain is used, regardless of whether the user name of the administrator contains the domain name.
* Ensure that a user has been configured on the RADIUS server. In this example, the user **admin123@huawei.com** (*user name*@*domain name*) and password **YsHsjx\_202206** have been configured on the RADIUS server.
* If the RADIUS server does not support the user names containing domain names, run the **undo radius-server user-name domain-included** command to configure the device not to encapsulate the domain name in the user name when sending packets to the RADIUS server.

#### Procedure

1. Set interface parameters.
   
   
   
   # Configure IP addresses for interfaces.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] commit
   [~DeviceA] vlan batch 10 20
   [*DeviceA] interface 100ge 1/0/1 
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2 
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 20
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ip address 10.1.1.2 255.255.255.0
   [*DeviceA-Vlanif10] quit
   [*DeviceA] interface vlanif 20
   [*DeviceA-Vlanif20] ip address 10.1.6.2 255.255.255.0
   [*DeviceA-Vlanif20] quit
   [*DeviceA] commit
   ```
2. Configure STelnet login.
   
   
   
   # Configure DeviceA to generate a local key pair.
   
   
   
   ```
   [~DeviceA] rsa local-key-pair create
   The key name will be:Host
   The range of public key size is (2048, 4096).
   NOTE: Key pair generation will take a short while.
   Please input the modulus [default = 3072]:3072
   [*DeviceA] commit
   ```
   
   # Configure a VTY user interface on the SSH server.
   
   ```
   [~DeviceA] user-interface vty 0 4 
   [~DeviceA-ui-vty0-4] authentication-mode aaa
   [~DeviceA-ui-vty0-4] protocol inbound ssh
   [*DeviceA-ui-vty0-4] user privilege level 3
   [*DeviceA-ui-vty0-4] quit
   [*DeviceA] commit
   ```
   # Configure the public key algorithm, encryption algorithm, key exchange algorithm list, HMAC authentication algorithm, and minimum key length on the SSH server.
   ```
   [~DeviceA] ssh server cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
   [*DeviceA] ssh server hmac sha2_256 sha2_512
   [*DeviceA] ssh server key-exchange dh_group_exchange_sha256 dh_group16_sha512
   [*DeviceA] ssh server publickey rsa_sha2_256 rsa_sha2_512
   [*DeviceA] commit
   ```
   
   # Create an SSH user on the server and set the authentication mode to password authentication.
   
   ```
   [~DeviceA] ssh user admin123
   [*DeviceA] ssh user admin123 authentication-type password
   [*DeviceA] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To configure password authentication for multiple SSH users, run the **ssh authentication-type default password** command to specify password authentication as the default authentication mode of SSH users. After this configuration is complete, you do not need to repeatedly configure the authentication mode and service type for each SSH user, simplifying configuration and improving efficiency.
   
   # Enable the STelnet function and set the user service type to STelnet.
   
   ```
   [~DeviceA] stelnet server enable
   [*DeviceA] ssh server-source all-interface
   [*DeviceA] ssh user admin123 service-type stelnet
   [*DeviceA] commit
   ```
3. Configure an ACL rule to allow the administrator to log in.
   
   
   ```
   [~DeviceA] acl 2000
   [*DeviceA-acl4-basic-2000] rule permit source 10.137.217.10 0
   [*DeviceA-acl4-basic-2000] quit
   [*DeviceA] ssh server acl 2000
   [*DeviceA] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The ACL configuration is optional.
4. Configure RADIUS authentication.
   
   
   
   # Configure a RADIUS server template for communication between DeviceA and the RADIUS server.
   
   ```
   [~DeviceA] radius-server template template1
   [*DeviceA-radius-template1] radius-server authentication 10.1.6.6 1812 weight 80
   [*DeviceA-radius-template1] radius-server shared-key cipher YsHsjx_202206
   [*DeviceA-radius-template1] quit
   [*DeviceA] commit
   ```
   
   # Configure an AAA authentication scheme and set the authentication mode to RADIUS.
   
   ```
   [~DeviceA] aaa
   [*DeviceA-aaa] authentication-scheme auth1
   [*DeviceA-aaa-authen-auth1] authentication-mode radius
   [*DeviceA-aaa-authen-auth1] quit
   ```
   
   # Create a domain, and apply the AAA authentication scheme and RADIUS server template to the domain.
   
   ```
   [*DeviceA-aaa] domain huawei.com
   [*DeviceA-aaa-domain-huawei.com] authentication-scheme auth1
   [*DeviceA-aaa-domain-huawei.com] radius-server template1
   [*DeviceA-aaa-domain-huawei.com] quit
   [*DeviceA-aaa] quit
   [*DeviceA] commit
   ```
   
   # Configure the domain **huawei.com** as the global default administrative domain so that the administrator does not need to enter the domain name when logging in to the device.
   
   ```
   [~DeviceA] domain huawei.com admin
   [*DeviceA] commit
   ```
5. Configure the RADIUS server.
   
   
   
   The configuration includes the following steps: add a device, add a user, and set the user privilege level to 3.

#### Verifying the Configuration

Use OpenSSH to log in to the SSH server from the client. Access the Windows CLI and run the OpenSSH commands to access the device using STelnet. On the login page, enter the user name **admin123** and password **YsHsjx\_202206** configured on the RADIUS server as prompted, and press **Enter**. If the authentication succeeds, you can successfully log in to DeviceA through STelnet. (The following information is for reference only.)

```
C:\Documents and Settings\Administrator> ssh admin123@10.1.1.2
Enter passphrase for key 'C:\Users\User/.ssh/id_rsa':
Enter password:

Warning: Negotiated key exchange algorithm and identity key for server authentication are not safe. It is recommended that you disable the insecure algorithm or upgrade the client.

Warning: The initial password poses security risks.
The password needs to be changed. Change now? [Y/N]:n
Info: The max number of VTY users is 21, the number of current VTY users online is 1, and total number of terminal users online is 2.
      The current login time is 2022-09-28 12:07:34.
      The last login time is 2022-09-28 06:44:35 from 172.16.0.1 through SSH.
      The last login failure time is 2022-09-28 11:59:21 from 172.16.0.1 through SSH. Consecutive login failures since the last successful login: 3.
<DeviceA>
```

#### Configuration Scripts

```
#
sysname DeviceA
#
acl number 2000
 rule 5 permit source 10.137.217.10 0
#
radius-server template template1                                                        
 radius-server shared-key cipher %+%##!!!!!!!!!"!!!!"!!!!*!!!!SKvr${[Fs.3t@/5k|BENhEu>W(3\~XG!!D;!!!!!2jp5!!!!!!A!!!!3"pK8qv!}9M#(4$jGWvQF/R[CNe/+:W^jk8HUe&W%+%#
 radius-server authentication 10.1.6.6 1812 weight 80                           
#
aaa
 authentication-scheme auth1    
  authentication-mode radius   
 domain huawei.com            
  authentication-scheme auth1     
  radius-server template1      
#  
domain huawei.com admin 
#
vlan batch 10 20
#
interface Vlanif10
 ip address 10.1.1.2 255.255.255.0
#
interface Vlanif20
 ip address 10.1.6.2 255.255.255.0
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 10
#
interface 100GE1/0/2
 port link-type trunk
 port trunk allow-pass vlan 20
#
stelnet server enable
ssh user admin123
ssh user admin123 authentication-type password
ssh user admin123 service-type stelnet
ssh server-source all-interface
ssh server acl 2000
#
user-interface vty 0 4           
 authentication-mode aaa 
 user privilege level 3
 protocol inbound ssh
#
ssh server cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
ssh server hmac sha2_256 sha2_512
ssh server key-exchange dh_group_exchange_sha256 dh_group16_sha512
ssh server publickey rsa_sha2_256 rsa_sha2_512
#
return 
```