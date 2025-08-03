protocol-vlan
=============

protocol-vlan

Function
--------



The **protocol-vlan** command configures the classification of VLANs based on protocols and specifies the protocol template.

The **undo protocol-vlan** command deletes the setting.



By default, the classification of VLANs based on protocols is not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**protocol-vlan** [ *protocol-index1* ] { **at** | **ipv4** | **ipv6** | **ipx** { **ethernetii** | **llc** | **raw** | **snap** } | **mode** { **ethernetii-etype** *etype-id1* | **llc** { **dsap** *dsapValue* **ssap** *ssapValue* } | **snap-etype** *etype-id1* } }

**undo protocol-vlan** { *protocol-index1* [ **to** *protocol-index2* ] | **all** }

**undo protocol-vlan** *protocol-index1* { **at** | **ipv4** | **ipv6** | **ipx** { **ethernetii** | **llc** | **raw** | **snap** } | **mode** { **ethernetii-etype** *etype-id1* | **llc** { **dsap** *dsapValue* **ssap** *ssapValue* } | **snap-etype** *etype-id1* } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *protocol-index1* | Specifies the index of a start protocol template. | The value is an integer in the range 0 to 15. |
| **at** | Classifies VLANs based on AppleTalk. | - |
| **ipv4** | Classifies VLANs based on IPv4. | - |
| **ipv6** | Classifies VLANs based on IPv6. | - |
| **ipx** | Classifies VLANs based on IPX. | - |
| **ethernetii** | Indicates that the encapsulation format of Ethernet packets is Ethernet II. | - |
| **llc** | Indicates that the encapsulation format of Ethernet packets is Logical Link Control (LLC). | - |
| **raw** | Indicates that the encapsulation format of Ethernet packets is raw. | - |
| **snap** | Indicates that the encapsulation format of Ethernet packets is snap. | - |
| **mode** | Indicates a user-defined protocol. | - |
| **ethernetii-etype** *etype-id1* | Specifies the value of the protocol type that matches the encapsulation format of Ethernet II. | The value is a string of characters. You can enter a question mark (?) and select a value from the displayed value range. |
| **dsap** *dsapValue* | Specifies the destination service access point. | The value ranges from 0x0 to 0xFF, in hexadecimal notation. The default value is 0x0. |
| **ssap** *ssapValue* | Specifies the source service access point. | The value ranges from 0x0 to 0xFF, in hexadecimal notation. The default value is 0x0. |
| **snap-etype** *etype-id1* | Specifies the value of the protocol type that matches the encapsulation format of Sub-Network Access Protocol (SNAP). | The value is a string of characters. You can enter a question mark (?) and select a value from the displayed value range. |
| *protocol-index2* | Specifies the index of a start protocol template. | The value is an integer in the range 0 to 15. |
| **all** | Indicates the indexes of all protocols bound to vlan-id. | - |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Protocol-based VLAN classification and IP subnet-based VLAN classification are called network layer-based VLAN classification. Network layer-based VLAN classification reduces manual configuration workload and allows terminals to easily join a VLAN, transfer from one VLAN to another, or exit a VLAN.

**Configuration Impact**

VLANs are classified based on the protocol field in Layer 2 frames in protocol-based VLAN classification. The protocol field indicates the network protocol running at Layer 3 and can be IPv4, IPv6, IPX, or AppleTalk. You can classify packets with different protocols into different VLANs for transmission.

**Precautions**

When configuring the source and destination service access points, note the following:

* dsap-id and ssap-id cannot be both set to aa.
* dsap-id and ssap-id cannot be both set to 0xe0. 0xe0 indicates llc, the encapsulation format of IPX packets.
* dsap-id and ssap-id cannot be both set to 0xff. 0xff indicates raw, the encapsulation format of IPX packets.

Example
-------

# Configure the classification of VLANs based on IPv4.
```
<HUAWEI> system-view
[~HUAWEI] vlan 3
[*HUAWEI-vlan3] protocol-vlan ipv4

```