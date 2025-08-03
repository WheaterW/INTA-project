Example for Configuring Telnet Login for an IPv6 User
=====================================================

In this example, VTY user interfaces and login parameters are configured for an IPv6 user to implement Telnet login from an IPv6 client.

#### Context

#### Networking Requirements

It is required that an IPv6 user log in to a device through Telnet from a client on a different network segment for remote maintenance.

**Figure 1** Telnet login![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GigabitEthernet0/0/0.


  
![](figure/en-us_image_0237276104.png)


#### Configuration Roadmap

1. Establish a physical connection.
2. Configure an IPv6 address for the management interface on the device.
3. Configure VTY user interface parameters, including the limit on incoming and outgoing calls.
4. Configure Telnet user information.

#### Data Preparation

The latest PuTTY version (0.70 latest release or 0.71) has been installed on the Telnet client, and IPv6 routes between the Telnet client and Interface 1 are available.

To complete the configuration, you need the following data:

* IPv6 address of the management interface on the device
* Maximum number of VTY user interfaces: 15
* Number of the ACL6 that is used to prohibit users from logging in to another Router: 3001
* Timeout period of a user connection: 20 minutes
* Number of rows displayed on a terminal screen: 30
* Buffer size for historical commands: 20
* User name (huawei123), password (YsHsjx\_202206), and authentication mode (AAA) of the IPv6 user who accesses the device through Telnet

#### Procedure

1. Connect the PC and the Router to the network.
2. Assign an IPv6 address to the management interface on the device.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Device
   [*HUAWEI] commit
   [~Device] interface GigabitEthernet0/0/0
   [~Device-GigabitEthernet0/0/0] undo shutdown
   [~Device-GigabitEthernet0/0/0] ipv6 enable
   [*Device-GigabitEthernet0/0/0] ipv6 address 2001:db8::1 32
   [*Device-GigabitEthernet0/0/0] commit
   [~Device-GigabitEthernet0/0/0] quit
   ```
3. Enable the Telnet server function.
   
   
   ```
   [~Device] telnet ipv6 server enable
   [*Device] telnet ipv6 server-source -a 2001:db8::1
   [*Device] commit
   ```
4. Configure VTY user interfaces on the Router.
   
   
   
   # Set the maximum number of VTY user interfaces.
   
   ```
   [~Device] user-interface maximum-vty 15
   [*Device] commit
   ```
   
   # Configure an ACL6 to prohibit users from logging in to another Router.
   
   ```
   [~Device] acl ipv6 3001
   [*Device-acl6-advance-3001] rule deny tcp source any destination-port eq telnet
   [*Device-acl6-advance-3001] quit
   [*Device] user-interface vty 0 14
   [*Device-ui-vty0-14] acl ipv6 3001 outbound
   ```
   
   # Set terminal attributes for the VTY user interfaces.
   
   ```
   [*Device-ui-vty0-14] shell
   [*Device-ui-vty0-14] idle-timeout 20
   [*Device-ui-vty0-14] screen-length 30
   [*Device-ui-vty0-14] history-command max-size 20
   ```
   
   # Set an authentication mode for the VTY user interfaces.
   
   ```
   [*Device-ui-vty0-14] authentication-mode aaa
   [*Device-ui-vty0-14] commit
   [~Device-ui-vty0-14] quit
   ```
5. Set Telnet user information on the Router.
   
   
   
   # Specify the login authentication mode.
   
   ```
   [~Device] aaa
   [*Device-aaa] local-user huawei123 password
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
   [*Device-aaa] local-user huawei123 service-type telnet
   ```
   ```
   [*Device-aaa] local-user huawei123 level 3
   ```
   ```
   [*Device-aaa] commit
   ```
   ```
   [~Device-aaa] quit
   ```
6. Log in to the device from the PC through Telnet.
   
   
   
   Double-click PuTTY.exe to open the **PuTTY Configuration** page, as shown in [Figure 2](#EN-US_TASK_0192846360__fig10367114586). Select **Session**, enter the IPv6 address of the server to be accessed in the **Host Name (or IP address)** text box, and use the default port number 23.
   
   **Figure 2** PuTTY configuration page for Telnet login  
   ![](figure/en-us_image_0194853414.png)
   
   Click **Open**. The system prompts you to enter the user name and password, as shown in [Figure 3](#EN-US_TASK_0192846360__fig16222165013585). In this example, the user name is huawei123, and the password is YsHsjx\_202206.
   
   **Figure 3** Login window  
   ![](figure/en-us_image_0194853879.png "Click to enlarge")

#### Device configuration file

```
#
sysname Device
#
acl number 3001
 rule 5 deny tcp destination-port eq telnet
#
aaa
 local-user huawei123 password irreversible-cipher $1c$]zV2B\j!z:$hRujV[%/IE|0MwBQ}5sAX(RdE[oj#5otqG6=@>KK$
 local-user huawei123 service-type telnet
 local-user huawei123 level 3
 local-user huawei123 state block fail-times 3 interval 5 
#
interface GigabitEthernet0/0/0
 undo shutdown
 ipv6 enable 
 ipv6 address 2001:DB8::1/32 
#
telnet ipv6 server enable
telnet ipv6 server-source -a 2001:db8::1
#
user-interface maximum-vty 15
#
user-interface vty 0 14
 acl ipv6 3001 outbound 
 authentication-mode aaa
 history-command max-size 20
 idle-timeout 20 0
 screen-length 30
#
return
```