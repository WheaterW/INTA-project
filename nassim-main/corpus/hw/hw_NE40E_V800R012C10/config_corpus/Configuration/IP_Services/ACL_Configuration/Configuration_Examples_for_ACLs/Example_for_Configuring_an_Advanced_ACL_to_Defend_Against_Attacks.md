Example for Configuring an Advanced ACL to Defend Against Attacks
=================================================================

This section provides an example for configuring an advanced ACL to defend against attacks.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172364651__fig_dc_vrp_acl4_cfg_007601), DeviceA, DeviceB, and DeviceC are access devices whereas DeviceD, DeviceE, and DeviceF are core devices. The access devices connect to the core devices through 10 Gbit/s interfaces. Voice and 3G services run on the network. To control user access and ensure network and device security, security policies need to be configured on the access routers to prevent ICMP packet attacks. To achieve this purpose, configure an advanced ACL on DeviceA.

If the attacker (PC) attacks the network shown in [Figure 1](#EN-US_TASK_0172364651__fig_dc_vrp_acl4_cfg_007601), DeviceA can use the configured advanced ACL to prevent the ICMP packet attacks.

**Figure 1** Configuring an advanced ACL to defend against attacks![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0000001576583941.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set passwords for users that log in to a device using the NMS and CLI to improve login security.
2. Record all information about unsuccessful logins in a log file and output log information to the console interface for network administrators to check the login information.
3. Configure an advanced ACL on DeviceA and apply the advanced ACL to QoS services to defend against ICMP packet attacks.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface
* Password for users that log in to a device using the NMS and CLI
* Number of the advanced ACL

#### Procedure

1. Assign an IP address to each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172364651__example920376786214033) in this section.
2. Set a password for users that log in to a device using the NMS and CLI. 
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] user-interface console 0
   [*DeviceA-ui-con0] shell
   [*DeviceA-ui-con0] authentication-mode password
   [*DeviceA-ui-con0] set authentication password cipher YsHsjx_202206
   [*DeviceA-ui-con0] idle-timeout 30 0
   [*DeviceA-ui-con0] commit
   [~DeviceA-ui-con0] quit
   [~DeviceA] user-interface maximum-vty 15
   [*DeviceA] user-interface vty 5 14
   [*DeviceA-ui-vty5-14] shell
   [*DeviceA-ui-vty5-14] authentication-mode password
   [*DeviceA-ui-vty5-14] set authentication password cipher YsHsjx_202206
   [*DeviceA-ui-vty5-14] idle-timeout 30 0
   [*DeviceA-ui-vty5-14] commit
   [~DeviceA-ui-vty5-14] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configurations of the other access Routers are similar to the configuration of DeviceA.
3. Record all information about unsuccessful logins in a log file and output log information to the console interface.
   
   
   ```
   [~DeviceA] info-center enable
   [*DeviceA] info-center source default channel 9 log level warning
   [*DeviceA] info-center logfile channel channel9
   [*DeviceA] commit
   [~DeviceA] quit
   <DeviceA> terminal logging
   ```
4. Configure an advanced ACL on DeviceA and apply the advanced ACL to QoS services to defend against ICMP packet attacks.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] acl number 3001
   ```
   ```
   [*DeviceA-acl4-advance-3001] description anti-virus
   ```
   ```
   [*DeviceA-acl4-advance-3001] rule 5 deny icmp
   ```
   ```
   [*DeviceA-acl4-advance-3001] commit
   ```
   ```
   [~DeviceA-acl4-advance-3001] quit
   ```
   ```
   [~DeviceA] traffic classifier anti-virus
   ```
   ```
   [*DeviceA-classifier-anti-virus] if-match acl 3001
   ```
   ```
   [*DeviceA-classifier-anti-virus] commit
   ```
   ```
   [~DeviceA-classifier-anti-virus] quit
   ```
   ```
   [~DeviceA] traffic behavior anti-virus
   ```
   ```
   [*DeviceA-behavior-anti-virus] commit
   ```
   ```
   [~DeviceA-behavior-anti-virus] quit
   ```
   ```
   [~DeviceA] traffic policy anti-virus
   ```
   ```
   [*DeviceA-trafficpolicy-anti-virus] classifier anti-virus behavior anti-virus
   ```
   ```
   [*DeviceA-trafficpolicy-anti-virus] commit
   ```
   ```
   [~DeviceA-trafficpolicy-anti-virus] quit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] traffic-policy anti-virus inbound
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] traffic-policy anti-virus outbound
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
5. Verify the configuration. 
   
   
   
   # Ping DeviceA from the PC. The command output shows that the ping operation fails.
   
   ```
   c:\>ping 172.16.1.1
   
   Pinging 172.16.1.1 with 32 bytes of data:
   Request timed out.
   Request timed out.
   Request timed out.
   Request timed out.
   
   Ping statistics for 172.16.1.1:
       Packets: Sent = 4, Received = 0, Lost = 4 <100% loss>,
   ```
   
   # Delete the advanced ACL on DeviceA. Then the command output shows that ping operation is successful.
   
   ```
   c:\>ping 172.16.1.1
   
   Pinging 172.16.1.1 with 32 bytes of data:
   Reply from 172.16.1.1: bytes=32 time<1ms TTL=128
   Reply from 172.16.1.1: bytes=32 time<1ms TTL=128
   Reply from 172.16.1.1: bytes=32 time<1ms TTL=128
   Reply from 172.16.1.1: bytes=32 time<1ms TTL=128
   
   Ping statistics for 172.16.1.1:
       Packets: Sent = 4, Received = 4, Lost = 0 <0% loss>,
   Approximate round trip times in mill-seconds:
       Minimum = 0ms, Maximum = 0 ms, Average = 0ms
   ```

#### Configuration Files

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the configuration file of DeviceA is provided.

* DeviceA configuration file
  
  ```
  #
   sysname DeviceA
  #
  info-center enable
   info-center source default channel 9 log level warning
   info-center logfile channel channel9
  #
  acl number 3001
   description anti-virus
   rule 5 deny icmp
  #
  traffic classifier anti-virus
   if-match acl 3001
  #
  traffic behavior anti-virus
  #
  traffic policy anti-virus
   classifier anti-virus behavior anti-virus
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   traffic-policy anti-virus inbound
   traffic-policy anti-virus outbound
  #
  user-interface maximum-vty 15
  user-interface console 0
  shell
   authentication-mode password
   set authentication password cipher $1c$$
   idle-timeout 30 0
  user-interface vty 0 4
  user-interface vty 5 14
  shell
   set authentication password cipher $1c$`g=H/qo%;7$b6Za%2'[D!0blsOXF=.3QCNC-f)co,[aeE.`e`-<$
   idle-timeout 30 0
  user-interface vty 16 20
  #
  return
  ```