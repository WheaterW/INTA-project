Example for Configuring a Device to Communicate with an NMS Through a Local SNMPv3 User
=======================================================================================

This section provides an example to describe how to configure a device to communicate with an NMS through SNMPv3 and how to specify the MIB objects that can be managed by the NMS.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172361044__fig_dc_vrp_snmp_cfg_003801), two NMSs (NMS1 and NMS2) and the Router are connected across a public network. According to the network planning, NMS2 can use a local SNMPv3 user account to manage every MIB object on the Router, and NMS1 does not manage the Router.

The data transmitted between NMS2 and the Router needs to be encrypted and the NMS administrator needs to be authenticated because the data has to travel across the public network.

Contact information of the device administrator needs to be configured on the Router. This helps the NMS administrator contact the device administrator if a fault occurs.

**Figure 1** Networking diagram for configuring a device to communicate with an NMS through a local SNMPv3 user  
![](images/fig_dc_vrp_snmp_cfg_002501.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an AAA task group and grant permissions.
2. Configure an AAA user group and associate it with the task group.
3. Configure a local AAA user and set its access service type to SNMP.
4. Enable the SNMP agent.
5. Configure the Router to run SNMPv3.
6. Configure a source interface for SNMP to receive and respond to NMS request packets.
7. Configure a local SNMPv3 user.
8. Configure the contact information of the device administrator.
9. Configure NMS2.

#### Data Preparation

To complete the configuration, you need the following data:

* SNMP version
* User group name
* Task group name
* User name and password
* Authentication and encryption algorithms. SHA2-256 and a higher-complexity algorithm are recommended for authentication, and AES128 and a higher-complexity algorithm are recommended for encryption.
* Contact information of the device administrator

#### Procedure

1. Configure available routes between the Router and the NMSs. Details for the configuration procedure are not provided here.
2. Configure an AAA task group and grant permissions.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] aaa
   ```
   ```
   [*HUAWEI-aaa] task-group tg1
   ```
   ```
   [*HUAWEI-aaa-task-group-tg1] task snmp read
   ```
   ```
   [*HUAWEI-aaa-task-group-tg1] task snmp write
   ```
   ```
   [*HUAWEI-aaa-task-group-tg1] commit
   ```
   ```
   [~DeviceA-aaa-task-group-tg1] quit
   ```
3. Configure an AAA user group and associate it with the task group.
   
   
   ```
   [~DeviceA-aaa] user-group grp1
   ```
   ```
   [*DeviceA-aaa-user-group-grp1] task-group tg1
   ```
   ```
   [*DeviceA-aaa-user-group-grp1] commit
   ```
   ```
   [~DeviceA-aaa-user-group-grp1] quit
   ```
4. Configure a local AAA user and set its access service type to SNMP.
   
   
   ```
   [~DeviceA-aaa] local-user nms2-admin password
   Please configure the password (8-128)
   Enter Password:                                                                 
   Confirm Password:
   ```
   ```
   [*DeviceA-aaa] local-user nms2-admin user-group grp1
   ```
   ```
   [*DeviceA-aaa] local-user nms2-admin level 3
   ```
   ```
   [*DeviceA-aaa] local-user nms2-admin service-type snmp
   ```
   ```
   [*DeviceA-aaa] commit
   ```
   ```
   [~DeviceA-aaa] quit
   ```
5. Enable the SNMP agent.
   
   
   ```
   [~DeviceA] snmp-agent password min-length 10
   ```
   ```
   [*DeviceA] snmp-agent
   ```
   ```
   [*DeviceA] commit
   ```
6. Configure the Router to run SNMPv3.
   
   
   ```
   [~DeviceA] snmp-agent sys-info version v3
   ```
   ```
   [*DeviceA] commit
   ```
7. Configure a source interface for SNMP to receive and respond to NMS request packets.
   
   
   ```
   [~DeviceA] snmp-agent protocol source-interface Loopback0
   ```
   ```
   [*DeviceA] commit
   ```
8. Configure a local SNMPv3 user.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In this command, the authentication algorithms MD5, SHA, and SHA2-224 and the encryption algorithms DES56 and 3DES168 are weak security algorithms and are not recommended. To configure a weak security algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.
   
   ```
   [~DeviceA] snmp-agent local-user v3 nms2-admin authentication-mode sha2-256 privacy-mode aes128
   Please configure the authentication password (10-255)
   Enter Password:
   Confirm Password:
   Please configure the privacy password (10-255)
   Enter Password:
   Confirm Password:
   ```
   ```
   [*DeviceA] commit
   ```
9. Configure the contact information of the device administrator.
   
   
   ```
   [~DeviceA] snmp-agent sys-info contact call Operator at 010-12345678
   ```
   ```
   [*DeviceA] commit
   ```
10. Configure the NMS.
    
    
    
    For details on how to configure NMS2, see the relevant NMS configuration guide.
11. Verify the configuration.
    
    
    
    After the configuration is complete, run the following commands to verify that the configuration has taken effect.
    
    # Check the configured SNMP version.
    
    ```
    [~DeviceA] display snmp-agent sys-info version
    ```
    ```
    SNMP version running in the system:
    ```
    ```
               SNMPv3
    ```
    
    # Check local user information.
    
    ```
    <DeviceA> display snmp-agent local-user
    ```
    ```
    User name: nms2-admin                                                        
           Engine ID: 800007DB03001974593301                                        
           Authentication Protocol: sha2-256                                             
           Privacy Protocol: aes128                                                 
           State: Active 
    ```
    
    # Check the contact information of the device administrator.
    
    ```
    <DeviceA> display snmp-agent sys-info contact
    The contact person for this managed node:
               call Operator at 010-12345678 
    ```

#### Configuration Files

```
#
sysname DeviceA
#
aaa
 local-user nms2-admin password irreversible-cipher %#%#n}=%C*UimYlx9-:$>T=*_y4PX*e~u6I_Aa9s=I1$%#%#
 local-user nms2-admin service-type snmp
 local-user nms2-admin user-group grp1
 #
 task-group tg1
  task snmp write
 #
 user-group grp1
  task-group tg1
 #
interface GigabitEthernet0/1/0
 undo shutdown
 ip address 1.1.2.1 255.255.255.0
#
interface loopback0
 ip address 1.1.3.1 255.255.255.255
#
ospf 1
 area 0.0.0.0
  network 1.1.2.0 0.0.0.255
  network 1.1.3.1 0.0.0.0
#
snmp-agent
snmp-agent password min-length 10
snmp-agent local-engineid 800007DB03001974593301
#
snmp-agent protocol source-interface Loopback0
#
snmp-agent sys-info contact call Operator at 010-12345678
snmp-agent sys-info version v3
snmp-agent local-user v3 nms2-admin authentication-mode sha2-256 cipher %#%#n}=%C*UimYlx9-:$>T=*_y4PX*e~u6I_Aa9s=I1$%#%# privacy-mode aes128 cipher %#%#at{pQGh!uMyq..8WSJ(<bU`~K_)[f-}s&*Gmw!iE%#%# 
#
return
```