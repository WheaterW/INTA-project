Configuring the Device to Obtain Packets Forwarded by the Hardware
==================================================================

Configuring the Device to Obtain Packets Forwarded by the Hardware

#### Context

If the device fails to forward traffic correctly, you can configure the device to obtain hardware-forwarded packets for analysis. In this way, you can process invalid packets promptly to ensure correct transmission of network data.

Only one instance for obtaining hardware-forwarded packets is supported.

![](public_sys-resources/note_3.0-en-us.png) 

* Enabling the packet capture function affects device performance. Therefore, exercise caution when using this function.
* The device may fail to obtain packets or obtain all packets in some cases (for example, when there are too many packets of a following type: protocol packets sent to the CPU, packets sent by the local device, session update packets, some discarded packets, and obtained packets). In such cases, you are advised to use other methods to obtain packets, such as mirroring.

* The hardware-forwarded packets can be obtained on Eth-Trunk interfaces, but not on specified Eth-Trunk member interfaces.
* When using commands to configure the packet capture function, you can configure a maximum of four interfaces to obtain packets.


#### Procedure

1. Configure an instance for obtaining hardware-forwarded packets.
   
   
   
   For device models excluding the CE6885-LL working in low latency mode:
   
   ```
   [capture-packet](cmdqueryname=capture-packet) { { interface { interface-type interface-number | interface-name } &<1-4> } | { acl { acl-number | name acl-name } } } * [ vxlan [ vni vni-id ] | [ vlan vlan-id | inner-vlan cvlan-id ] * ] [ clear payload ] destination { file filename | terminal } [ time-out time | packet-num number | packet-len length ] * [ inbound | outbound ]
   ```
   ```
   [capture-packet](cmdqueryname=capture-packet) { { interface { interface-type interface-number | interface-name } &<1-4> } | { acl ipv6 { acl-number2 | name acl-name } } } * [ vxlan [ vni vni-id ] | [ vlan vlan-id | inner-vlan cvlan-id ] * ] [ clear payload ] destination { file filename | terminal } [ time-out time | packet-num number | packet-len length ] * [ inbound | outbound ]
   ```
   
   For the CE6885-LL (low latency mode):
   
   ```
   [capture-packet](cmdqueryname=capture-packet) { { interface { interface-type interface-number | interface-name } &<1-4> } | acl { acl-number | name acl-name } } * [ vlan vlan-id ] * [ clear payload ] destination { file filename | terminal } [ time-out time | packet-num number | packet-len length ] * inbound 
   ```
   
   You can configure the command parameters listed in the following table to obtain packets that match specified rules.
   
   | Parameter | Description |
   | --- | --- |
   | **interface** { *interface-type* *interface-number* } | Obtains packets on a specified interface. |
   | **acl** [ **ipv6** ] { *acl-number* | **name** *acl-name* } | Obtains packets that match a specified ACL. |
   | **vlan** *vlan-id* | Obtains packets from a specified VLAN. |
   | **inner-vlan** *cvlan-id* | Obtains packets with a specified inner VLAN ID. |
   | **clear payload** | Clears the payload of obtained packets. |
   | **destination** { **terminal** | **file** *file-name* } | * **destination terminal**: Displays obtained packet information on a terminal. * **destination file** *file-name*: Saves obtained packet information to a specified .cap file. |
   | **time-out** *time* | Specifies the timeout period for obtaining packets. The device stops obtaining packets when the timeout period expires. |
   | **packet-num** *number* | Specifies the number of packets to be obtained. The device stops obtaining packets when the specified number of packets are obtained.  You can set **packet-num** *number* and **time-out** *time* based on the traffic volume on an interface. Specifically, if a large number of packets are forwarded on the interface, set a small value of *time* and a large value of *number*; otherwise, set a large value of *time* and a small value of *number*. |
   | **packet-len** *length* | Specifies the length of obtained packets to be displayed on the terminal or stored on the storage medium. |
   | **outbound** | Obtains outgoing packets. |
   | **inbound** | Obtains incoming packets. |
   | **vxlan** | Obtains the VXLAN packets in which the inner packets match the specified conditions. |
   | **vni** *vin-id* | Obtains the VXLAN packets matching the specified VNI. |