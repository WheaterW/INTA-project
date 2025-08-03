Example for Configuring a Device to Communicate with NMSs Using SNMPv3 USM Users
================================================================================

Example for Configuring a Device to Communicate with NMSs Using SNMPv3 USM Users

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001563750749__fig_dc_vrp_snmp_cfg_002501), two NMSs (NMS1 and NMS2) connect to the device over a public network. According to the network planning, NMS2 can manage every MIB object on the device, whereas NMS1 does not manage the device.

On the device, only the modules that are enabled by default are allowed to send alarms to NMS2. This prevents an excess of unwanted alarms from being sent to NMS2, which would otherwise make fault locating difficult.

The data transmitted between NMS2 and the device needs to be encrypted and the NMS administrator needs to be authenticated because the data has to travel across the public network. The contact information of the device administrator needs to be configured on the device, in order to help the NMS administrator contact the device administrator if a fault occurs.

**Figure 1** Network diagram of configuring a device to communicate with an NMS through SNMPv3![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001512671346.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the SNMP agent function.
2. Configure the device to run SNMPv3.
3. Configure a source interface for SNMP to receive and respond to NMS request packets.
4. Configure an ACL to allow NMS2 to manage MIB objects on the device. Set the authentication and encryption algorithms for data to **sha2-256** and **aes128** respectively.
5. Configure the device to send trap messages to NMS2.
6. Configure the contact information of the device administrator.
7. Configure NMS2.

#### Procedure

1. Configure available routes between the device and the NMSs. Detailed configurations are not provided.
2. Enable the SNMP agent function.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] snmp-agent password min-length 10
   [*DeviceA] snmp-agent
   [*DeviceA] commit
   ```
3. Configure the device to run SNMPv3.
   
   
   ```
   [~DeviceA] snmp-agent sys-info version v3
   [*DeviceA] commit
   ```
4. Configure a source interface for SNMP to receive and respond to NMS request packets.
   
   
   ```
   [*DeviceA] snmp-agent protocol source-interface 100ge 1/0/1
   [*DeviceA] commit
   ```
5. Configure the NMS access permission.
   
   
   
   # Configure an ACL to allow NMS2 to manage and disallow NMS1 from managing the device.
   
   ```
   [~DeviceA] acl 2001
   [*DeviceA-acl4-basic-2001] rule 5 permit source 1.1.1.2 0.0.0.0
   [*DeviceA-acl4-basic-2001] rule 6 deny source 1.1.1.1 0.0.0.0
   [*DeviceA-acl4-basic-2001] commit
   [~DeviceA] quit
   ```
   
   # Configure a MIB view.
   
   ```
   [~DeviceA] snmp-agent mib-view included iso iso
   [*DeviceA] commit
   ```
   
   # Configure a user group and a user. Configure authentication and encryption for data of the user.
   
   ```
   [~DeviceA] snmp-agent group v3 admin privacy write-view iso notify-view iso read-view iso
   [*DeviceA] snmp-agent usm-user v3 nms2-admin group admin acl 2001
   [*DeviceA] snmp-agent usm-user v3 nms2-admin authentication-mode sha2-256
   Please configure the authentication password (8-255)
   Enter Password:
   Confirm Password:   
   [*DeviceA] snmp-agent usm-user v3 nms2-admin privacy-mode aes128
   Please configure the privacy password (8-255)
   Enter Password:
   Confirm Password:
   [*DeviceA] commit
   ```
6. Configure the alarm function.
   
   
   ```
   [~DeviceA] snmp-agent target-host trap address udp-domain 1.1.1.2 params securityname nms2-admin v3 privacy
   [*DeviceA] snmp-agent trap enable
   [*DeviceA] commit
   ```
7. Configure the contact information of the device administrator.
   
   
   ```
   [~DeviceA] snmp-agent sys-info contact call Operator at 010-12345678
   [*DeviceA] commit
   ```
8. Configure the NMS.
   
   
   
   For details about NMS configuration, see the corresponding NMS configuration guide.

#### Verifying the Configuration

# Check the configured SNMP version.

```
<DeviceA> display snmp-agent sys-info version
SNMP version running in the system:
           SNMPv3
```

# Check the user group information.

```
<DeviceA> display snmp-agent group admin
   Group name: admin
       Security model: USM AuthPriv
       Readview: iso
       Writeview: iso
       Notifyview: iso
       Storage-type: nonVolatile
```

# Check the user information.

```
<DeviceA> display snmp-agent usm-user
   User name: nms2-admin
       Engine ID: 800007DB03D0C65B951201 active
       Authentication Protocol: sha2-256
       Privacy Protocol: aes128
       Group name: admin
       Acl: 2001
       State: Active
```
# Check the configured ACL.
```
<DeviceA> display acl 2001
Basic ACL 2001, 2 rules
ACL's step is 5
 rule 5 permit ip source 1.1.1.2 0 (4 times matched)
 rule 6 deny source 1.1.1.1 0 (0 times matched)
```

# Check the MIB view.

```
<DeviceA> display snmp-agent mib-view viewname iso
View name: iso
       MIB Subtree: iso
       Subtree mask: 80(Hex)
       Storage-type: nonVolatile
       View Type: included
       View status: active 
```

# Check the target host.

```
<DeviceA> display snmp-agent target-host
Target host NO. 1
---------------------------------------------------------------------------
  Host name                        : __targetHost_1_27466
  IP address                       : 1.1.1.2
  Source interface                 : -
  VPN instance                     : -
  Security name                    : nms2-admin
  Alarm Port                       : 162 
  Event Port                       : 162
  Type                             : trap
  Version                          : v3
  Level                            : Privacy
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
   rule 5 permit source 1.1.1.2 0.0.0.0
   rule 6 deny source 1.1.1.1 0.0.0.0
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 1.1.2.1 255.255.255.0
   
  #
  ospf 1
   area 0.0.0.0
    network 1.1.2.0 0.0.0.255
    network 1.1.3.1 0.0.0.0
  #
  snmp-agent
  snmp-agent local-engineid 800007DB03D0C65B951201
  #
  snmp-agent sys-info contact call Operator at 010-12345678
  snmp-agent sys-info version v3
  snmp-agent password min-length 10
  snmp-agent group v3 admin privacy read-view iso write-view iso notify-view iso
  snmp-agent target-host host-name __targetHost_1_27466 trap address udp-domain 1.1.1.2 params securityname nms2-admin v3 privacy
  #
  snmp-agent mib-view included iso iso
  snmp-agent usm-user v3 nms2-admin
  snmp-agent usm-user v3 nms2-admin group admin
  snmp-agent usm-user v3 nms2-admin authentication-mode sha2-256 cipher %+%##!!!!!!!!!"!!!!"!!!!*!!!!PR=uJ|5'u%{Ku|VKwEyE-uN:Pp9K`O+oLF,!!!!!2jp5!!!!!!<!!!!6r!o;)ju=D<fXX.r3a`QWe'gPol7aEif^M'!!!!!%+%#
  snmp-agent usm-user v3 nms2-admin privacy-mode aes128 cipher %+%##!!!!!!!!!"!!!!"!!!!*!!!!PR=uJ|5'u%B.79IwRIE3(xTzFsYNQ5iH4;X!!!!!2jp5!!!!!!<!!!!A"X3:)AC815G!a6]bVc8-wj'EK9!&V<M0HP!!!!!%+%#
  snmp-agent usm-user v3 nms2-admin acl 2001
  #
  snmp-agent protocol source-interface 100GE1/0/1
  #
  snmp-agent trap enable
  #
  return
  ```