Example for Configuring a Device to Communicate with an NMS Through a USM SNMPv3 User
=====================================================================================

This section provides an example to describe how to configure a device to communicate with an NMS through SNMPv3 and how to specify the MIB objects that can be managed by the NMS.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172361041__fig_dc_vrp_snmp_cfg_002501), two NMSs (NMS1 and NMS2) and the Router are connected across a public network. According to the network planning, NMS2 can manage every MIB object on the Router, and NMS1 does not manage the Router.

On the Router, only the modules that are enabled by default are allowed to send alarms to NMS2. This prevents an excess of unwanted alarms from being sent to NMS2. Excessive alarms make fault location difficult.

The data transmitted between NMS2 and the Router needs to be encrypted and the NMS administrator needs to be authenticated because the data has to travel across the public network.

Contact information of the device administrator needs to be configured on the Router. This helps the NMS administrator contact the device administrator if a fault occurs.

**Figure 1** Networking diagram for configuring a device to communicate with an NMS through SNMPv3  
![](images/fig_dc_vrp_snmp_cfg_002501.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the SNMP agent.
2. Configure the Router to run SNMPv3.
3. Configure a source interface for SNMP to receive and respond to NMS request packets.
4. Configure an ACL to allow NMS2 to manage every MIB object on the Router.
5. Configure the trap function to allow the Router to send alarms to NMS2.
6. Configure the contact information of the device administrator.
7. Configure NMS2.

#### Data Preparation

To complete the configuration, you need the following data:

* SNMP version
* User group name
* User name and password
* Authentication and encryption algorithms. SHA2-256 and a higher-complexity algorithm are recommended for authentication, and AES128 and a higher-complexity algorithm are recommended for encryption.
* ACL number
* IP address of the NMS
* Contact information of the device administrator

#### Procedure

1. Configure available routes between the Router and the NMSs. Details for the configuration procedure are not provided here.
2. Enable the SNMP agent.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] snmp-agent password min-length 10
   ```
   ```
   [*HUAWEI] snmp-agent
   ```
   ```
   [*HUAWEI] commit
   ```
3. Configure the Router to run SNMPv3.
   
   
   ```
   [~DeviceA] snmp-agent sys-info version v3
   ```
   ```
   [*DeviceA] commit
   ```
   
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
4. Configure a source interface for SNMP to receive and respond to NMS request packets.
   
   
   ```
   [~DeviceA] snmp-agent protocol source-interface Loopback0
   ```
   ```
   [*DeviceA] commit
   ```
5. Configure access permissions of the NMSs.
   
   # Configure an ACL to allow NMS2 to manage and disallow NMS1 from managing the Router.
   ```
   [~DeviceA] acl 2001
   ```
   ```
   [*DeviceA-acl4-basic-2001] rule 5 permit source 1.1.1.2 0.0.0.0
   ```
   ```
   [*DeviceA-acl4-basic-2001] rule 6 deny source 1.1.1.1 0.0.0.0
   ```
   ```
   [*DeviceA-acl4-basic-2001] commit
   ```
   ```
   [~DeviceA-acl4-basic-2001] quit
   ```
   
   # Configure a MIB view.
   
   ```
   [~DeviceA] snmp-agent mib-view included iso iso
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure a user group and a user in this group and enable user data authentication and encryption.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In this command, the authentication algorithms MD5, SHA, and SHA2-224 and the encryption algorithms DES56 and 3DES168 are weak security algorithms and are not recommended. To configure a weak security algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.
   
   ```
   [~DeviceA] snmp-agent group v3 admin privacy write-view iso notify-view iso read-view iso
   [*DeviceA] snmp-agent usm-user v3 nms2-admin group admin acl 2001
   [*DeviceA] snmp-agent usm-user v3 nms2-admin authentication-mode sha2-256
   Please configure the authentication password (10-255)
   Enter Password:
   Confirm Password:
   [*DeviceA] snmp-agent usm-user v3 nms2-admin privacy-mode aes128
   Please configure the privacy password (10-255)
   Enter Password:
   Confirm Password:
   ```
   ```
   [*DeviceA] commit
   ```
6. Configure the trap function.
   
   
   ```
   [~DeviceA] snmp-agent target-host trap address udp-domain 1.1.1.2 params securityname nms2-admin v3 privacy
   [*DeviceA] snmp-agent trap enable
   ```
   ```
   [*DeviceA] commit
   ```
7. Configure the contact information of the device administrator.
   
   
   ```
   [~DeviceA] snmp-agent sys-info contact call Operator at 010-12345678
   ```
   ```
   [*DeviceA] commit
   ```
8. Configure the NMS.
   
   
   
   For details on how to configure NMS2, see the relevant NMS configuration guide.
9. Verify the configuration.
   
   
   
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
   
   # Check the user group information.
   
   ```
   <DeviceA> display snmp-agent group admin
   ```
   ```
      Group name: admin
          Security model: v3
          Readview: iso
          Writeview: iso
          Notifyview: iso
          Storage-type: nonVolatile
   
   ```
   
   # Check the user information.
   
   ```
   <DeviceA> display snmp-agent usm-user
   ```
   ```
      User name: nms2-admin,
          Engine ID: 800007DB0300259E0370C3 active
          Authentication Protocol: sha2-256
          Privacy Protocol: aes128
          Group-name: admin
          State: Active
          Acl: 2001
   ```
   # Check the configured ACL.
   ```
   <DeviceA> display acl 2001
   ```
   ```
   Basic ACL 2001, 2 rules
   ACL's step is 5
    rule 5 permit ip source 1.1.1.1 0 (4 times matched)
    rule 6 deny source 1.1.1.1 0 (0 times matched)
   ```
   
   # Check the MIB view.
   
   ```
   <DeviceA> display snmp-agent mib-view viewname iso
   ```
   ```
   View name: iso
          MIB Subtree: iso
          Subtree mask: FF80(Hex)
          Storage-type: nonVolatile
          View Type: included
          View status: active 
   
   ```
   
   # Check the target host.
   
   ```
   <DeviceA> display snmp-agent target-host
   Target-host NO. 1
   ---------------------------------------------------------------------------
     Host-name                        : -
     IP-address                       : 1.1.1.2
     Source interface                 : -
     VPN instance                     : -
     Security name                    : nms2-admin
     Port                             : 162
     Type                             : trap
     Version                          : v3
     Level                            : Privacy
     NMS type                         : NMS
     With ext-vb                      : No
     Notification filter profile name : -
   ---------------------------------------------------------------------------
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
# 
acl number 2001
 rule 5 permit source 1.1.1.2 0.0.0.0
 rule 6 deny source 1.1.1.1 0.0.0.0
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
snmp-agent local-engineid 800007DB03360102101100
#
snmp-agent protocol source-interface Loopback0
#
snmp-agent sys-info contact call Operator at 010-12345678
snmp-agent sys-info version v3
snmp-agent group v3 admin privacy write-view iso notify-view iso read-view iso
snmp-agent target-host trap address udp-domain 1.1.1.2 params securityname nms2-admin v3 privacy
#
snmp-agent mib-view included iso iso
snmp-agent usm-user v3 nms2-admin
snmp-agent usm-user v3 nms2-admin group admin
snmp-agent usm-user v3 nms2-admin authentication-mode sha2-256 cipher %#%#n}=%C*UimYlx9-:$>T=*_y4PX*e~u6I_Aa9s=I1$%#%#
snmp-agent usm-user v3 nms2-admin privacy-mode aes128 cipher %#%#at{pQGh!uMyq..8WSJ(<bU`~K_)[f-}s&*Gmw!iE%#%#
snmp-agent usm-user v3 nms2-admin acl 2001
#
snmp-agent trap enable
#
return
```