Example for Configuring HWTACACS and Local Authentication and User Privilege Level Authorization for Administrators
===================================================================================================================

Example for Configuring HWTACACS and Local Authentication and User Privilege Level Authorization for Administrators

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001563995893__fig1348613432384), an HWTACACS server is deployed on an enterprise network. The enterprise requires that the administrator use HWTACACS authentication to log in to DeviceA through STelnet. The specific requirements are as follows:

1. The administrator can log in to the device through STelnet only after entering a correct user name and password.
2. After the administrator logs in to the device through STelnet, the privilege level 3 is authorized to the administrator.
3. If the server does not respond to the authentication request from the device (for example, the link between the device and server is disconnected), local authentication is performed when the administrator attempts to log in to the device.

**Figure 1** Network diagram for configuring HWTACACS and local authentication and user privilege level authorization for administrators![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001512836206.png)

#### Configuration Roadmap

1. Configure STelnet login on DeviceA: Set the authentication mode for accessing VTY user interfaces to AAA, enable the STelnet service, and configure the authentication mode and service type for SSH users.
2. Configure HWTACACS authentication on DeviceA: Create an HWTACACS server template and configure AAA schemes.
3. Configure a local user on DeviceA.
4. Configure the HWTACACS server.

#### Precautions

* Ensure that there are reachable routes between devices before the configuration.
* Ensure that the shared key in the HWTACACS server template is the same as that configured on the HWTACACS server.
* If the login account is not created on the server but exists on the local host, HWTACACS authentication is considered failed, and local authentication is not performed. Local authentication is performed only when the server is down or does not respond.
* If the accounting mode is set to HWTACACS in an accounting scheme, the administrator will pass local authentication but fail to log in to the device because accounting will fail to start after the link between the device and server is disconnected. To prevent this problem, run the **accounting start-fail** **online** command in the accounting scheme view to allow users to go online after initial accounting fails. By default, users are allowed to go online after initial accounting fails.


#### Procedure

1. Configure IP addresses for interfaces.
   
   
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
   ```
   
   # Set the authentication mode and protocol for accessing VTY user interfaces 0 to 4 to AAA and SSH, respectively.
   
   ```
   [*DeviceA] user-interface vty 0 4 
   [*DeviceA-ui-vty0-4] authentication-mode aaa 
   [*DeviceA-ui-vty0-4] protocol inbound ssh
   [*DeviceA-ui-vty0-4] quit
   ```
   
   # Enable the SSH server function on DeviceA.
   
   ```
   [*DeviceA] stelnet server enable 
   [*DeviceA] ssh server-source -i vlanif 10
   ```
   
   # Set the authentication mode of all SSH users to password authentication.
   
   ```
   [*DeviceA] ssh authentication-type default password
   [*DeviceA] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If only the authentication mode and service type of a few SSH users need to be set to password authentication and STelnet, you can specify the SSH user name to set the authentication mode and service type of a single SSH user. For example, set the authentication mode and service type of an SSH user named **admin** to password authentication and STelnet, respectively.
   
   [DeviceA] **ssh user admin authentication-type password**
   
   [DeviceA] **ssh user admin service-type stelnet**
3. Configure HWTACACS authentication, authorization, and accounting.
   
   
   
   # Create an HWTACACS server template named **template1** for communication between DeviceA and the HWTACACS server.
   
   ```
   [~DeviceA] hwtacacs-server template template1 
   [*DeviceA-hwtacacs-template1] hwtacacs-server authentication 10.1.6.6 49 
   [*DeviceA-hwtacacs-template1] hwtacacs-server authorization 10.1.6.6 49 
   [*DeviceA-hwtacacs-template1] hwtacacs-server accounting 10.1.6.6 49 
   [*DeviceA-hwtacacs-template1] hwtacacs-server shared-key cipher YsHsjx_202206139 
   [*DeviceA-hwtacacs-template1] quit
   [*DeviceA] commit
   ```
   
   # Create an authentication scheme named **sch1** and set the authentication mode to HWTACACS and local authentication.
   
   ```
   [~DeviceA] aaa 
   [~DeviceA-aaa] authentication-scheme sch1
   [*DeviceA-aaa-authen-sch1] authentication-mode hwtacacs local
   [*DeviceA-aaa-authen-sch1] quit
   ```
   
   # Configure an authorization scheme named **sch2** and set the authorization mode to HWTACACS and local authorization.
   
   ```
   [*DeviceA-aaa] authorization-scheme sch2 
   [*DeviceA-aaa-author-sch2] authorization-mode hwtacacs local
   [*DeviceA-aaa-author-sch2] quit
   ```
   
   # Create an accounting scheme named **sch3** and set the accounting mode to HWTACACS accounting.
   
   ```
   [*DeviceA-aaa] accounting-scheme sch3 
   [*DeviceA-aaa-accounting-sch3] accounting-mode hwtacacs 
   [*DeviceA-aaa-accounting-sch3] quit
   ```
   
   # Apply the HWTACACS server template and AAA schemes to the domain **huawei.com**.
   
   ```
   [*DeviceA-aaa] domain huawei.com 
   [*DeviceA-aaa-domain-huawei.com] hwtacacs-server template1 
   [*DeviceA-aaa-domain-huawei.com] authentication-scheme sch1 
   [*DeviceA-aaa-domain-huawei.com] authorization-scheme sch2 
   [*DeviceA-aaa-domain-huawei.com] accounting-scheme sch3 
   [*DeviceA-aaa-domain-huawei.com] quit 
   [*DeviceA-aaa] quit
   ```
   
   # Set the domain **huawei.com** as the global default administrative domain.
   
   ```
   [*DeviceA] domain huawei.com admin 
   [*DeviceA] commit
   ```
4. Configure AAA local authentication. Set the local user name to **user1-huawei**, password to **YsHsjx\_202206**, and privilege level to 3.
   
   
   ```
   [~DeviceA] aaa
   [~DeviceA-aaa] local-user user1-huawei password irreversible-cipher YsHsjx_202206
   [*DeviceA-aaa] local-user user1-huawei service-type ssh
   [*DeviceA-aaa] local-user user1-huawei privilege level 3
   [*DeviceA-aaa] quit
   [*DeviceA] commit
   ```
5. Configure the HWTACACS server. Here, the Secure ACS is used as an example.
   
   
   
   The configuration includes adding a device, adding a user, and setting the user privilege level to 3.

#### Verifying the Configuration

* The administrator can log in to DeviceA through the STelnet client after entering the correct user name and password.
* When the link between DeviceA and the server is operational, run the **display access-user username** *user-name* **detail** command on DeviceA to check information about the user **user1-huawei**.
  
  In the command output, the values of **User access type**, **User Privilege**, **User authentication type**, **Current authentication method**, **Current authorization method**, and **Current accounting method** indicate that the user login mode is SSH, the privilege level is 3, the authentication type is administrator authentication, and the authentication, authorization, as well as accounting modes are HWTACACS.
  
  ```
  <DeviceA> display access-user username user1-huawei detail
   ------------------------------------------------------------------------------
  Basic:
    User ID                         : 16414
    User name                       : user1-huawei
    Domain-name                     : huawei.com
    User MAC                        : -
    User IP address                 : 10.1.1.10
    User IPv6 address               : -
    User access time                : 2024/07/01 10:49:22
    User accounting session ID      : example010000000000006d****010001e
    User access type                : SSH
    User Privilege                  : 3
    User Group                      : -
  
  AAA:
    User authentication type        : Administrator authentication
    Current authentication method   : HWTACACS
    Current authorization method    : HWTACACS
    Current accounting method       : HWTACACS
  ```
* When the link between DeviceA and the HWTACACS server is disconnected, run the **display access-user username** *user-name* **detail** command on DeviceA to check information about the user **user1-huawei**.
  
  In the command output, the values of **User access type**, **User Privilege**, **User authentication type**, **Current authentication method**, **Current authorization method**, and **Current accounting method** indicate that the login mode is SSH, the privilege level is 3, the authentication type is administrator authentication, the authentication and authorization modes are local, and the accounting mode is HWTACACS.
  
  ```
  <DeviceA> display access-user username user1-huawei detail
   ------------------------------------------------------------------------------
  Basic:
    User ID                         : 16414
    User name                       : user1-huawei
    Domain-name                     : huawei.com
    User MAC                        : -
    User IP address                 : 10.1.1.10
    User IPv6 address               : -
    User access time                : 2024/07/01 10:49:22
    User accounting session ID      : example010000000000006d****010001e
    User access type                : SSH
    User Privilege                  : 3
    User Group                      : -
  
  AAA:
    User authentication type        : Administrator authentication
    Current authentication method   : Local
    Current authorization method    : Local
    Current accounting method       : HWTACACS
  ```

#### Configuration Scripts

DeviceA

```
# 
sysname DeviceA 
# 
hwtacacs-server template template1                                           
 hwtacacs-server authentication 10.1.6.6                                    
 hwtacacs-server authorization 10.1.6.6                                   
 hwtacacs-server accounting 10.1.6.6  
 hwtacacs-server shared-key cipher %+%##!!!!!!!!!"!!!!"!!!!*!!!!SKvr${[Fs."u,S-6a-X1'[X=L"cpF!5Oz`1!!!!!2jp5!!!!!!A!!!!Ix>cM8i{y6!);(8Dr9:dK`&BHfE(H2=.:SH{@pT%+%#  
# 
aaa 
 authentication-scheme sch1     
  authentication-mode hwtacacs local
 authorization-scheme sch2                                                       
  authorization-mode hwtacacs local
 accounting-scheme sch3                                                          
  accounting-mode hwtacacs  
 domain huawei.com                                                               
  authentication-scheme sch1                                                     
  accounting-scheme sch3                                                         
  authorization-scheme sch2                                                      
  hwtacacs-server template1  
 local-user user1-huawei password irreversible-cipher $1d$OwseVRh@LH}ZeTBm$1nH4$ab>d(N{-%0!ab48y=Ic*xEUR4pVhR2"9-~,$
 local-user user1-huawei privilege level 3
 local-user user1-huawei service-type ssh   
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
ssh server-source -i Vlanif10
# 
user-interface vty 0 4           
 authentication-mode aaa           
 protocol inbound ssh
# 
return
```