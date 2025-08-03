Example for Configuring Telnet Login for an IPv4 User
=====================================================

In this example, VTY user interfaces and login parameters are configured for an IPv4 user to implement Telnet login from an IPv4 client.

#### Networking Requirements

It is required that an IPv4 user log in to a device through Telnet from a client on a different network segment for remote maintenance.

**Figure 1** Telnet login![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents GigabitEthernet0/0/0.


  
![](images/fig_dc_vrp_basic_cfg_004701.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Establish a physical connection.
2. Assign an IP address to the management interface on P1.
3. Configure VTY user interface parameters, including the limit on incoming and outgoing calls.
4. Configure Telnet user information.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the management interface on P1
* Maximum number of VTY user interfaces: 10
* Number of the ACL that is used to prohibit users from logging in to another device: 3001
* Timeout period of a user connection: 20 minutes
* Number of rows displayed on a terminal screen: 30
* Buffer size for historical commands: 20
* Telnet user information (authentication mode: AAA, user name: huawei, password: YsHsjx\_202206)

#### Procedure

1. Connect the PC and the device to the network.
2. Assign an IP address to the management interface on P1.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname P1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~P1] interface GigabitEthernet0/0/0
   ```
   ```
   [~P1-GigabitEthernet0/0/0] undo shutdown
   ```
   ```
   [*P1-GigabitEthernet0/0/0] ip address 10.137.217.33 255.255.254.0
   ```
   ```
   [*P1-GigabitEthernet0/0/0] commit
   ```
   ```
   [~P1-GigabitEthernet0/0/0] quit
   ```
3. Enable the Telnet server function.
   
   
   ```
   [~P1] telnet server enable
   ```
   ```
   [*P1] telnet server-source -i GigabitEthernet0/0/0
   ```
   ```
   [*P1] commit
   ```
4. Configure VTY user interfaces on the device.
   
   
   
   # Set the maximum number of VTY user interfaces.
   
   ```
   [~P1] user-interface maximum-vty 10
   ```
   ```
   [*P1] commit
   ```
   
   # Configure an ACL to prohibit users from logging in to another device.
   
   ```
   [~P1] acl 3001
   ```
   ```
   [*P1-acl4-advance-3001] rule deny tcp source any destination-port eq telnet
   ```
   ```
   [*P1-acl4-advance-3001] quit
   ```
   ```
   [*P1] user-interface vty 0 9
   ```
   ```
   [*P1-ui-vty0-9] acl 3001 outbound
   ```
   
   # Set terminal attributes for the VTY user interfaces.
   
   ```
   [*P1-ui-vty0-9] shell
   ```
   ```
   [*P1-ui-vty0-9] idle-timeout 20
   ```
   ```
   [*P1-ui-vty0-9] screen-length 30
   ```
   ```
   [*P1-ui-vty0-9] history-command max-size 20
   ```
   
   # Set an authentication mode for the VTY user interfaces.
   
   ```
   [*P1-ui-vty0-9] authentication-mode aaa
   ```
   ```
   [*P1-ui-vty0-9] commit
   ```
   ```
   [~P1-ui-vty0-9] quit
   ```
5. Set Telnet user information on the device.
   
   
   
   # Specify the login authentication mode.
   
   ```
   [~P1] aaa
   ```
   ```
   [*P1-aaa] local-user huawei password
   ```
   ```
   Please configure the password (8-128)
   Enter Password:
   Confirm Password:
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If **cipher** or **irreversible-cipher** is not specified, a password is entered in man-machine interaction mode and the system does not display the entered password.
     
     When the user security policy is configured, the value is a string of 8 to 128 case-insensitive characters without spaces. When the user security policy is not configured, the value is a string of 1 to 128 case-insensitive characters without spaces.When the user security policy is configured, the password cannot be the same as the user name or its reverse. The password must contain the following characters: upper-case character, lower-case character, digit, and special character.
     
     Special characters do not include question marks (?) or spaces. However, when double quotation marks are used around a password, spaces are allowed in the password.
     + Double quotation marks cannot contain double quotation marks if spaces are used in a password.
     + Double quotation marks can contain double quotation marks if no space is used in a password.
     
     For example, the password "Aa123"45"" is valid, but the password "Aa 123"45"" is invalid.
   * If **cipher** is specified, a password can be entered in either simple text or cipher text.
     
     If a password is entered in simple text, the password requirements are the same as those when **cipher** is not specified. When you input a password in simple text, the system displays the password in simple text mode, which brings risks.
     
     A password is displayed in cipher text in the configuration file regardless of whether it is entered in simple text or cipher text.
   * If **irreversible-cipher** is specified, a password can be entered in either simple text or irreversible cipher text.
     
     If a password is entered in simple text, the password requirements are the same as those when **irreversible-cipher** is not specified.
     
     A password is displayed in cipher text in the configuration file regardless of whether it is entered in simple text or irreversible cipher text.
   ```
   [*P1-aaa] local-user huawei service-type telnet
   ```
   ```
   [*P1-aaa] local-user huawei level 3
   ```
   ```
   [*P1-aaa] commit
   ```
   ```
   [~P1-aaa] quit
   ```
6. Log in to P1 from the PC.
   
   
   
   Enter the Windows Command Prompt window and run the **telnet** command to log in to P1.
   
   Press **Enter** and enter a user name and password in the login window. After authentication succeeds, a command prompt of the user view is displayed.

#### Configuration Files

* P1 configuration file

```
#
sysname P1
#
acl number 3001
 rule 5 deny tcp destination-port eq telnet
#
aaa
 local-user huawei password irreversible-cipher $1c$]zV2B\j!z:$hRujV[%/IE|0MwBQ}5sAX(RdE[oj#5otqG6=@>KK$
 local-user huawei service-type telnet
 local-user huawei level 3
#
interface GigabitEthernet0/0/0
 undo shutdown
 ip address 10.137.217.33 255.255.254.0
#
telnet server enable
telnet server-source -i GigabitEthernet0/0/0
#
user-interface maximum-vty 10
#
user-interface vty 0 9
 authentication-mode aaa
 history-command max-size 20
 idle-timeout 20 0
 screen-length 30
 acl 3001 outbound
#
return
```