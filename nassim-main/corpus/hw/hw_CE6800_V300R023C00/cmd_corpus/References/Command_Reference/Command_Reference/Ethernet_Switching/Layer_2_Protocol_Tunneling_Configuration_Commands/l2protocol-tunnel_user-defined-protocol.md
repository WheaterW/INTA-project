l2protocol-tunnel user-defined-protocol
=======================================

l2protocol-tunnel user-defined-protocol

Function
--------



The **l2protocol-tunnel user-defined-protocol** command configures parameters for a user-defined Layer 2 protocol. The parameters include the protocol name, Ethernet encapsulation type, multicast destination MAC address, and multicast MAC address used to replace the multicast destination MAC address.

The **undo l2protocol-tunnel user-defined-protocol** command deletes parameters for a user-defined Layer 2 protocol.



By default, no parameters are configured for user-defined Layer 2 protocols.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**l2protocol-tunnel user-defined-protocol** *protocol-name* **protocol-mac** *protocol-mac* [ **encap-type** { { **ethernetii** **protocol-type** *protocol-type* } | { **llc** **dsap** *dsap-value* **ssap** *ssap-value* } | { **snap** **protocol-type** *protocol-type* } } ] **group-mac** { *group-mac* | **default-group-mac** }

**undo l2protocol-tunnel user-defined-protocol** *protocol-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *protocol-name* | Specifies a user-defined protocol name. | The value is a string of 1 to 31 case-insensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |
| **protocol-mac** *protocol-mac* | Specifies the destination MAC address in Layer 2 protocol data units (PDUs). The destination MAC address cannot be one in use on the local device. | The value is in the H-H-H format, where H is a 4-digit hexadecimal number. |
| **encap-type** | Specifies an Ethernet encapsulation type of user-defined Layer 2 PDUs.  When user-defined Layer 2 PDUs have the same destination MAC address and protocol type, specify a different encap-type to differentiate these Layer 2 PDUs. | - |
| **ethernetii** | Specifies Ethernet II for user-defined Layer 2 PDUs. | - |
| **protocol-type** *protocol-type* | Specifies the Ethernet encapsulation value. | The value is a hexadecimal integer.   * The value ranges from 0600 to FFFF for Ethernet II encapsulation type. * The value ranges from 0000 to FFFF for SNAP encapsulation type. |
| *protocol-type* | Specifies the SNAP encapsulation value. | The value is a hexadecimal integer ranging from 0x00 to 0xff. |
| **llc** | Specifies Logical Link Control (LLC) for user-defined Layer 2 PDUs. | - |
| **dsap** *dsap-value* | Specifies a destination service access point. | The value is a hexadecimal integer ranging from 0x00 to 0xff. |
| **ssap** *ssap-value* | Specifies a source service access point. | The value is a hexadecimal integer ranging from 0x00 to 0xff. |
| **snap** | Specifies the Sub-Network Access Protocol (SNAP) for user-defined Layer 2 PDUs. | - |
| **group-mac** *group-mac* | Specifies the multicast MAC address which is used to replace the destination MAC address in Layer 2 PDUs. | The value is in the H-H-H format, where H is a 4-digit hexadecimal number. group-mac must start with 0x01 and cannot be any of the following multicast MAC addresses:   * Multicast MAC addresses that are in use on the local device * 0180-C200-0000 to 0180-C200-002F, which are used for BPDUs * 010F-E200-0004, which is used for Smart Link packets * 0100-0CCC-CCCC and 0100-0CCC-CCCD, which are reserved for specific purposes |
| **default-group-mac** | Indicates the default group MAC address, which has a fixed value of 0100-0ccd-cdd0.  Most Layer 2 protocols can be identified by protocol type. You can configure a group MAC address for this type of protocol to reduce configuration workload. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To transparently transmit non-standard Layer 2 PDUs with specific multicast destination MAC addresses from user networks across a backbone network, run the l2protocol-tunnel user-defined-protocol command on backbone network devices.

**Follow-up Procedure**

Run the l2protocol-tunnel enable or **l2protocol-tunnel vlan** command to enable Layer 2 protocol tunneling for user-defined protocols on user-side interfaces of backbone network devices.

**Precautions**

You can leave the encapsulation type and protocol type unconfigured but must ensure a unique group-mac.Before configuring the DSAP and SSAP, note the following:

* dsap-id and ssap-id cannot be both set to 0xaa.
* dsap-id and ssap-id cannot be both set to 0xe0. 0xe0 indicates the LLC encapsulation format of IPX packets.
* dsap-id and ssap-id cannot be both set to 0xff. 0xff indicates the raw encapsulation format of IPX packets.

Example
-------

# Configure characteristic information about a user-defined Layer 2 protocol, with the protocol name huawei, MAC address 0100-c300-0100, and group MAC address 0100-5e00-0012.
```
<HUAWEI> system-view
[~HUAWEI] l2protocol-tunnel user-defined-protocol huawei protocol-mac 0180-c200-0017 group-mac 0100-5e00-0012

```