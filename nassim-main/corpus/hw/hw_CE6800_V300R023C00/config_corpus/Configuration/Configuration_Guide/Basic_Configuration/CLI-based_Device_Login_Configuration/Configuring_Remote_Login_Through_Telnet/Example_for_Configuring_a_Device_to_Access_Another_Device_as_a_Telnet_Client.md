Example for Configuring a Device to Access Another Device as a Telnet Client
============================================================================

Example for Configuring a Device to Access Another Device as a Telnet Client

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001563893021__fig_dc_cfg_login_001901), there are reachable routes between the PC and Device1, and between Device1 and Device2. Users want to remotely manage and maintain Device2. However, there is no reachable route between the PC and Device2, and therefore users cannot directly log in to Device2 using Telnet. To address this issue, users can use Telnet to log in to Device1 and then use Telnet to log in to Device2 from Device1. An ACL rule also needs to be configured to only allow Device1 to access Device2 using Telnet, preventing unauthorized devices from telneting to Device2.

**Figure 1** Network diagram of configuring a device to access another device as a Telnet client![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001563893029.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the authentication mode and password for Telnet access on Device2.
2. Configure an ACL rule on Device2 to allow access from Device1.
3. Telnet to Device2 from Device1.

#### Configuration Precautions

In insecure network environments, you are advised to use a secure password authentication mode, encryption authentication algorithm, and protocol. For details about secure configuration examples, see [Example for Configuring a Device to Access Another Device as an STelnet Client (Password and RSA Authentication)](vrp_login_cfg_0017.html).


#### Procedure

1. Run the **install feature-software WEAKEA** command in the user view to install the weak security algorithm/protocol feature package (WEAKEA).
2. Configure the authentication mode and password for Telnet access on Device2.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Device2
   [*HUAWEI] commit
   [~Device2] user-interface vty 0 4
   [~Device2-ui-vty0-4] authentication-mode aaa
   [*Device2-ui-vty0-4] quit
   [*Device2] commit
   ```
3. Configure login user information.
   
   
   ```
   [~Device2] aaa
   [~Device2-aaa] local-user admin1234 password
   Please configure the login password (8-128)
   It is recommended that the password consist of four types of characters, including lowercase letters, uppercase letters, numerals and special characters. 
   Please enter password:                                      
   Please confirm password:                               
   [*Device2-aaa] local-user admin1234 service-type telnet
   [*Device2-aaa] local-user admin1234 privilege level 3
   [*Device2-aaa] quit
   [*Device2] commit
   ```
4. Configure an ACL rule on Device2 to allow access from Device1.
   
   
   ```
   [~Device2] acl 2000
   [*Device2-acl4-basic-2000] rule permit source 10.1.1.1 0
   [*Device2-acl4-basic-2000] quit
   [*Device2] user-interface vty 0 4
   [*Device2-ui-vty0-4] acl 2000 inbound
   [*Device2-ui-vty0-4] quit
   [*Device2] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The ACL configuration is optional.

#### Verifying the Configuration

# After the preceding configurations are complete, you can telnet to Device2 from Device1, but not from other devices.

```
<HUAWEI> system-view
[~HUAWEI] sysname Device1
[*HUAWEI] commit
[~Device1] quit
<Device1> telnet 10.2.1.1
Username:admin1234
Password:
Info: The max number of VTY users is 21, the number of current VTY users online is 1, and total number of terminal users online is 1.
      The current login time is 2020-12-15 14:23:00.
<Device2>
```

#### Configuration Scripts

Device2

```
#
sysname Device2
#
acl number 2000
 rule 5 permit source 10.1.1.1 0
#
aaa
 local-user admin1234 password irreversible-cipher $1d$g8wLJ`LjL!$CyE(V{3qg5DdU:PM[6=6O$UF-.fQ,Q}>^)OBzgoU$
 local-user admin1234 privilege level 3
 local-user admin1234 service-type telnet
#
user-interface vty 0 4
 acl 2000 inbound
 authentication-mode aaa
#
return
```