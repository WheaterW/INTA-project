Example for Configuring a Device to Communicate with NMSs Through SNMPv2c
=========================================================================

Example for Configuring a Device to Communicate with NMSs Through SNMPv2c

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001513030410__fig_dc_vrp_snmp_cfg_002401), two NMSs (NMS1 and NMS2) connect to the device over a public network. According to the network planning, NMS2 can manage every MIB object on the device, whereas NMS1 does not manage the device.

On the device, only the modules that are enabled by default are allowed to send alarms to NMS2. This prevents an excess of unwanted alarms from being sent to NMS2, which would otherwise make fault locating difficult. Inform messages need to be used to ensure that alarms are received by NMS2, because alarms sent by the device have to travel across the public network to reach NMS2.

The contact information of the device administrator needs to be configured on the device, in order to help the NMS administrator contact the device administrator if a fault occurs.

**Figure 1** Network diagram of configuring a device to communicate with an NMS through SNMPv2c![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001512830938.png)

#### Precautions

If the network environment is insecure, you are advised to use SNMPv3 for communication with the NMS.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the SNMP agent function.
2. Configure the device to run SNMPv2c.
3. Configure an ACL to allow NMS2 to manage MIB objects on the device.
4. Configure a source interface for SNMP to receive and respond to NMS request packets.
5. Configure the device to send Inform messages to NMS2.
6. Configure the contact information of the device administrator.
7. Configure NMS2.

#### Procedure

1. Run the **install feature-software WEAKEA** command in the user view to install the weak security algorithm/protocol feature package (WEAKEA). By default, the device provides the weak security algorithm/protocol feature package WEAKEA.
2. Configure available routes between the device and the NMSs. Detailed configurations are not provided.
3. Enable the SNMP agent function.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] snmp-agent password min-length 9
   [*DeviceA] snmp-agent
   [*DeviceA] commit
   ```
4. Configure the device to run SNMPv2c.
   
   
   ```
   [~DeviceA] snmp-agent sys-info version v2c
   [*DeviceA] commit
   ```
5. Configure a source interface for SNMP to receive and respond to NMS request packets.
   
   
   ```
   [*DeviceA] snmp-agent protocol source-interface 100ge 1/0/1
   [*DeviceA] commit
   ```
6. Configure the NMS access permission.
   
   
   
   # Configure an ACL to allow NMS2 to manage and disallow NMS1 from managing the device.
   
   ```
   [~DeviceA] acl 2001
   [*DeviceA-acl4-basic-2001] rule 5 permit source 1.1.1.2 0.0.0.0
   [*DeviceA-acl4-basic-2001] rule 6 deny source 1.1.1.1 0.0.0.0
   [*DeviceAacl4-basic-2001] commit
   [~DeviceA-acl4-basic-2001] quit
   ```
   
   # Configure a MIB view.
   
   ```
   [~DeviceA] snmp-agent mib-view excluded allexthgmp 1.3.6.1.4.1.2011.6.7
   [*DeviceA] commit
   ```
   
   # Configure a community to reference an ACL to allow NMS2 to manage the objects in the MIB view.
   
   ```
   [~DeviceA] snmp-agent community write adminnms2 mib-view allexthgmp acl 2001
   [*DeviceA] commit
   ```
7. Configure the alarm function.
   
   
   ```
   [~DeviceA] snmp-agent target-host inform address udp-domain 1.1.1.2 params securityname Huawei-1234 v2c
   [*DeviceA] snmp-agent inform timeout 5 resend-times 6 pending 7
   [*DeviceA] snmp-agent trap enable
   [*DeviceA] snmp-agent notification-log enable
   [*DeviceA] snmp-agent notification-log global-ageout 36
   [*DeviceA] commit
   ```
8. Configure the contact information of the device administrator.
   
   
   ```
   [~DeviceA] snmp-agent sys-info contact call Operator at 010-12345678
   [*DeviceA] commit
   ```
9. Configure NMS2.
   
   
   
   For details about NMS configuration, see the corresponding NMS configuration guide.

#### Verifying the Configuration

# Check the configured SNMP version.

```
<DeviceA> display snmp-agent sys-info version
SNMP version running in the system:
           SNMPv2c SNMPv3
```

# Check information about the SNMP community name.

```
<DeviceA> display snmp-agent community
   Community name: %@%##!!!!!!!!!"!!!!"!!!!*!!!!PR=uJ|5'u%-3Bw@/>NzBr/k=X0[ALT.K~:,!!!!!2jp5!!!!!!U!!!!%{+lTl_[/Jh<3.<4RvQ/.Z'33]YwP
JkB^`J9g":TFqD-'B$kmL6;vyHwQ74KEFp22!!!!!!!!!!!!!!!%@%#                                                                             
       Group name: %@%##!!!!!!!!!"!!!!"!!!!*!!!!PR=uJ|5'u%-3Bw@/>NzBr/k=X0[ALT.K~:,!!!!!2jp5!!!!!!U!!!!%{+lTl_[/Jh<3.<4RvQ/.Z'33]YwP
JkB^`J9g":TFqD-'B$kmL6;vyHwQ74KEFp22!!!!!!!!!!!!!!!%@%#                                                                             
       Acl: 2001                                                                                                                    
       Alias name: __CommunityAliasName_01_8357                                                                                     
       Storage-type: nonVolatile 
```
# Check the configured ACL.
```
<DeviceA> display acl 2001
Basic ACL 2001, 2 rules
Acl's step is 5
 rule 5 permit source 1.1.1.2 0 (0 times matched)
 rule 6 deny source 1.1.1.1 0 (0 times matched)
```

# Check the MIB view.

```
<DeviceA> display snmp-agent mib-view viewname allexthgmp
View name: allexthgmp
       MIB Subtree: huaweiUtility.7
       Subtree mask: FF80(Hex)
       Storage-type: nonVolatile
       View Type: excluded
       View status: active
```

# Check the target host.

```
<DeviceA> display snmp-agent target-host
Target host NO. 1
---------------------------------------------------------------------------
  Host name                        : __targetHost_1_41354
  IP address                       : 1.1.1.2
  Source interface                 : -
  VPN instance                     : -
  Security name                    : %+%##!!!!!!!!!"!!!!$!!!!*!!!!%&K/U}|G\2KYm@@k}uDDU#gLLO<J"0Q'/kH!!!!!2jp5!!!!!!<!!!!rv4VL.ucqLA!PK/olg}.vn0tBf0m4'5^XcK!!!!!%+%# 
  Alarm Port                       : 162 
  Event Port                       : 162
  Type                             : inform
  Version                          : v2c
  Level                            : No authentication and privacy
  NMS type                         : NMS
  With ext vb                      : No
  Notification filter profile name : -
  Heart beat required              : No
---------------------------------------------------------------------------
```

# Check the contact information of the device administrator.

```
<DeviceA> display snmp-agent sys-info contact
The contact person for this managed node:
           call Operator at 010-12345678 
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
   sysname DeviceA
  #
  acl number 2001
   rule 5 permit source 1.1.1.2 0
   rule 6 deny source 1.1.1.1 0
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 1.1.2.1 255.255.255.0
   
  #
  ospf 1
   area 0.0.0.0
    network 1.1.2.0 0.0.0.255
  #
   snmp-agent 
   snmp-agent local-engineid 800007DB0300FDFDFD2211
   snmp-agent community write cipher %@%##!!!!!!!!!"!!!!"!!!!*!!!!PR=uJ|5'u%-3Bw@/>NzBr/k=X0[ALT.K~:,!!!!!2jp5!!!!!!U!!!!%{+lTl_[/Jh<3.<4RvQ/.Z'33]YwPJkB^`J9g":TFqD-'B$kmL6;vyHwQ74KEFp22!!!!!!!!!!!!!!!%@%# mib-view allexthgmp acl 2001 alias __CommunityAliasName_01_8357
  #
   snmp-agent sys-info contact call Operator at 010-12345678
   snmp-agent sys-info version v2c
   snmp-agent password min-length 9
   snmp-agent target-host host-name __targetHost_1_11752 inform address udp-domain 1.1.1.2 params securityname cipher %+%##!!!!!!!!!"!!!!"!!!!*!!!!PR=uJ|5'u%<OoF8~{B=#QW("E3cky"H*I%E!!!!!2jp5!!!!!!<!!!!%m9qN;K61!+'7q>-bKZ&qJzJ3nQ\g)WWHkL!!!!!%+%# v2c
  #
   snmp-agent mib-view excluded allexthgmp huaweiUtility.7
  #
  snmp-agent notification-log enable
  snmp-agent notification-log global-ageout 36
  snmp-agent inform timeout 5
  snmp-agent inform resend-times 6
  snmp-agent inform pending 7
  #
  snmp-agent protocol source-interface 100GE1/0/1
  #
  snmp-agent trap enable
  #
  return
  ```