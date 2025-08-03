dhcpv6 remote-id format
=======================

dhcpv6 remote-id format

Function
--------



The **dhcpv6 remote-id format** command sets the format of the Remote-ID in DHCPv6 messages.

The **undo dhcpv6 remote-id format** command restores the default format of the Remote-ID in DHCPv6 messages.



By default, the default format of the Remote-ID in DHCPv6 messages is used.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dhcpv6 remote-id format** { **default** | **user-defined** *user-defined-text* }

**undo dhcpv6 remote-id format**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **default** | Indicates to adopt the default format of the remote ID. The default format of the remote ID is %duid %portname:%04svlan.%04cvlan, where the values of the outer VLAN ID and inner VLAN ID are integers and composed of four characters. If the length is shorter than four characters, 0s are prefixed to the value. For example, if the outer VLAN value in the DHCPv6 packets received by the device is 11, the inner VLAN value is 22, the inbound interface is VLANIF100, and the relay agent's DUID is 0003000180FB063545B3, the Remote-ID option generated during the system parsing process is 0003000180FB063545B3 vlanif100:0011.0022. | - |
| **user-defined** *user-defined-text* | Specifies a user-defined format as the Remote-ID format. A user-defined format can be:   * Format defined by keywords: The Remote-ID is defined based on the keywords supported by the user-defined format. For example, if the name of the device to which the users are connected and the outer VLAN to which the users belong need to be recorded, the user-defined format can be %sysname %svlan. If the device name is HUAWEI and the S-VLAN is 100, the user location information recorded by the Remote-ID is HUAWEI 100. For description of the keywords supported by the user-defined format, see the usage guide. * Format defined by common character strings: The Remote-ID is directly defined as a character string. For example, if all users on an interface are located in the office building named N8, the Remote-ID can be directly defined as N8. * Mixed format: The Remote-ID is defined by both the keywords and common character strings. For example, the Remote-ID can be defined as %sysname N8. | The value is a string of 1 to 247 case-sensitive characters, spaces supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The Remote-ID records user access information such as the DUID of the DHCPv6 packets sent from the clients to the device. The device functions as a. When receiving a request packet from a DHCPv6 client and forwarding the packet to the DHCPv6 server, the device can insert the Remote-ID option into the packet to identify the location of the DHCPv6 client. The location information is used by the DHCPv6 server to assign IPv6 addresses and network parameters. You can run the **dhcpv6 remote-id format** command to configure the format of the Remote-ID inserted into DHCPv6 packets.The keywords supported by the user-defined option format and their meanings are as follows:

* duid: ID of a trunk.
* sysname: indicates the device name of the trunk.
* portname: name of the inbound interface for the device to receive DHCPv6 packets from the client
* porttype: indicates the type of the inbound interface for the device to receive DHCPv6 packets from the client. In some scenarios, the interface type is specified when the NAS interface is configured.
* iftype: indicates the type of the inbound interface for the device to receive DHCPv6 packets from the client.
* mac: MAC address of the device.
* slot: indicates the slot ID of the board that receives DHCPv6 packets from the client.
* subslot: indicates the subslot ID of the DHCPv6 packet sent from the client to the device.
* port: indicates the number of the interface through which the device receives DHCPv6 packets from the client.
* svlan: indicates the outer VLAN ID of DHCPv6 packets sent by the client.
* cvlan: inner VLAN ID of DHCPv6 packets sent by a client
* length: indicates the total length of the content following the keyword, excluding the length of the keyword.

Example
-------

# Set the customized format for the remote ID carried in DHCPv6 messages and encapsulate the MAC address of the device into the remote ID.
```
<HUAWEI> system-view
[~HUAWEI] dhcpv6 remote-id format user-defined "%mac"

```