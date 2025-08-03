Configuring the Device to Obtain Protocol Packets Destined for the Local Device
===============================================================================

Configuring the Device to Obtain Protocol Packets Destined for the Local Device

#### Context

If a device is not running as normal, you can configure the device to obtain packets destined for the local device for analysis. In this way, you can process invalid packets promptly to ensure stable running of the local device.

A maximum of eight instances for obtaining packets destined for the local device are supported.

![](public_sys-resources/note_3.0-en-us.png) 

* The packets destined for the local device can be obtained on Eth-Trunk interfaces, but not on specified Eth-Trunk member interfaces.
* After locating faults, immediately run the [**undo capture-packet**](cmdqueryname=undo+capture-packet) command to disable the packet capture function and delete the configuration of the packet capture function, thereby protecting information security and preventing device performance from being affected.


#### Procedure

1. Configure an instance for obtaining packets destined for the local device.
   
   
   
   For device models excluding the CE6885-LL working in low latency mode:
   
   
   
   ```
   [capture-packet local-host](cmdqueryname=capture-packet+local-host) [ interface { interface-type interface-number | interface-number } &<1-4> ] [ acl { acl-number | name acl-name } | vlan vlan-id | inner-vlan cvlan-id ] * destination { file filename | terminal } [ time-out time-value | packet-num number | packet-len length ] *
   ```
   ```
   [capture-packet local-host](cmdqueryname=capture-packet+local-host) [ interface { interface-type interface-number | interface-number } &<1-4> ] [ acl ipv6 { acl-number2 | name acl-name } | vlan vlan-id | inner-vlan cvlan-id ] * destination { file filename | terminal } [ time-out time-value | packet-num number | packet-len length ] *
   ```
   
   For the CE6885-LL working in low latency mode:
   
   ```
   [capture-packet local-host](cmdqueryname=capture-packet+local-host) [ interface { interface-type interface-number | interface-number } &<1-4> ] [ acl { acl-number | name acl-name } | vlan vlan-id ] * destination { file filename | terminal } [ time-out time-value | packet-num number | packet-len length ] *
   ```
   
   You can configure the command parameters listed in the following table to obtain packets that match specified rules.
   
   **Table 1** Parameters in the [**capture-packet local-host**](cmdqueryname=capture-packet+local-host) command
   | Parameter | Description |
   | --- | --- |
   | **interface** { *interface-type* *interface-number* } | Obtains packets on a specified interface. |
   | **acl** { *acl-number* | **name** *acl-name* }  **acl** **ipv6** { *acl-number2* | **name** *acl-name* } | Obtains packets that match a specified ACL. |
   | **vlan** *vlan-id* | Obtains packets from a specified VLAN. |
   | **inner-vlan** *cvlan-id* | Obtains packets with a specified inner VLAN ID. |
   | **destination** { **terminal** | **file** *file-name* } | * **destination terminal**: Displays obtained packet information on a terminal. * **destination file** *file-name*: Saves obtained packet information to a specified .cap file. |
   | **time-out** *time-value* | Specifies the timeout period for obtaining packets. The device stops obtaining packets when the timeout period expires. |
   | **packet-num** *number* | Specifies the number of packets to be obtained. The device stops obtaining packets when the specified number of packets are obtained.  You can set **packet-num** *number* and **time-out** *time* based on the traffic volume on an interface. Specifically, if a large number of packets are forwarded on the interface, set a small value of *time* and a large value of *number*; otherwise, set a large value of *time* and a small value of *number*. |
   | **packet-len** *length* | Specifies the length of obtained packets to be displayed on the terminal or stored on the storage medium. |