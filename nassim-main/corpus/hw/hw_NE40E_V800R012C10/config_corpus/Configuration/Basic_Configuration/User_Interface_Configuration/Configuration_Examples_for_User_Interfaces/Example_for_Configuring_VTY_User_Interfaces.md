Example for Configuring VTY User Interfaces
===========================================

This section provides an example for configuring VTY user interfaces so that you can log in to the device through Telnet or SSH (STelnet) in AAA mode. The configuration involves the user level, authentication mode, authentication password, maximum number of VTY user interfaces, maximum number of incoming and outgoing calls, and terminal attributes.

#### Networking Requirements

To log in to a router using Telnet or SSH for local or remote configuration and maintenance, configure VTY user interfaces, including the maximum number of VTY user interfaces, limit on incoming and outgoing calls, terminal attributes, user levels, and authentication modes. You can configure parameters based on use and security requirements.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set the maximum number of VTY user interfaces.
2. Configure the limit on incoming and outgoing calls for VTY user interfaces.
3. Configure terminal attributes for the VTY user interfaces.
4. Set a user level for the VTY user interfaces.
5. Configure an authentication mode and password for the VTY user interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Maximum number of VTY user interfaces: 21
* Number of the ACL applied to limit incoming calls for the VTY user interfaces: 2000
* Timeout period of an idle connection: 30 minutes
* Number of rows displayed on a terminal screen: 30
* Buffer size for historical commands: 20
* User level: 15
* User authentication mode: AAA

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The ACL number for limiting incoming and outgoing calls in VTY user interfaces, password, and user name do not have default values. Other parameters have default values, which are recommended.



#### Procedure

1. Set the maximum number of VTY user interfaces.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] user-interface maximum-vty 21
   ```
   ```
   [*HUAWEI] commit
   ```
2. Configure the limit on incoming and outgoing calls for VTY user interfaces.
   
   
   ```
   [~HUAWEI] acl 2000
   ```
   ```
   [*HUAWEI-acl4-basic-2000] rule permit source 10.1.1.1 0
   ```
   ```
   [*HUAWEI-acl4-basic-2000] quit
   ```
   ```
   [*HUAWEI] user-interface vty 0 17
   ```
   ```
   [*HUAWEI-ui-vty0-17] acl 2000 inbound
   ```
   ```
   [*HUAWEI-ui-vty0-17] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In this case, users whose source IP addresses are not 10.1.1.10 cannot access the device.
3. Configure terminal attributes for the VTY user interfaces.
   
   
   ```
   [~HUAWEI-ui-vty0-17] shell
   ```
   ```
   [*HUAWEI-ui-vty0-17] idle-timeout 30
   ```
   ```
   [*HUAWEI-ui-vty0-17] screen-length 30
   ```
   ```
   [*HUAWEI-ui-vty0-17] history-command max-size 20
   ```
   ```
   [*HUAWEI-ui-vty0-17] commit
   ```
4. Set a user level for the VTY user interfaces.
   
   
   ```
   [~HUAWEI-ui-vty0-17] user privilege level 3
   ```
   ```
   [*HUAWEI-ui-vty0-17] commit
   ```
5. Set the user authentication mode to AAA for the VTY user interfaces.
   
   
   ```
   [~HUAWEI-ui-vty0-17] authentication-mode aaa
   ```
   ```
   [*HUAWEI-ui-vty0-17] commit
   ```
   ```
   [~HUAWEI-ui-vty0-17] quit
   ```
   
   After configuring the VTY user interfaces, you can log in to the device through Telnet or SSH (STelnet) in password authentication mode to implement local or remote maintenance. For details about how to log in to the device through Telnet or SSH (STelnet), see [Configuring a User to Log In Through Telnet](dc_vrp_basic_cfg_0030.html) or [Configuring STelnet Login](dc_vrp_basic_cfg_0037.html).
6. Configure VTY user information.
   
   
   ```
   [~HUAWEI] aaa
   [~HUAWEI-aaa] local-user admin1234 password irreversible-cipher YsHsjx_202206
   [*HUAWEI-aaa] local-user admin1234 service-type ssh
   [*HUAWEI-aaa] local-user admin1234 level 3
   [*HUAWEI-aaa] commit
   ```
7. Verify the configuration.
   
   
   
   After completing the configuration, run the [**display user-interface**](cmdqueryname=display+user-interface) command to check the status of the VTY user interfaces.
   
   Use VTY 14 as an example:
   
   ```
   [~HUAWEI] display user-interface vty 14
   ```
   ```
     Idx  Type     Tx/Rx      Modem Privi ActualPrivi Auth  Int
     48   VTY 14              -     3     -           A     -
     +    : Current UI is active.
     F    : Current UI is active and work in async mode.
     Idx  : Absolute index of UIs.
     Type : Type and relative index of UIs.
     Privi: The privilege of UIs.
     ActualPrivi: The actual privilege of user-interface.
     Auth : The authentication mode of UIs.
         A: Authenticate use AAA.
         P: Authenticate use current UI's password.
     Int  : The physical location of UIs.
   ```

#### Configuration Files

```
#
acl number 2000
 rule 5 deny source 10.1.1.1 0
#
user-interface maximum-vty 21
# 
aaa  
 local-user admin123 password irreversible-cipher $1d$+,JS+))\\2$KVNj(.3`_5x0FCKGv}H&.kUTI`Ff&H*eBqO.ua>)$  
 local-user admin123 service-type ssh  
 local-user admin123 level 3 
#
user-interface vty 0 17
 authentication-mode aaa
 user privilege level 3
 history-command max-size 20
 idle-timeout 30 0
 screen-length 30
 acl 2000 inbound
return
```