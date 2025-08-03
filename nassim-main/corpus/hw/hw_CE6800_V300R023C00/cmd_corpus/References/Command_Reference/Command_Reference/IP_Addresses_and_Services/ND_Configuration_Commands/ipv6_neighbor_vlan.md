ipv6 neighbor vlan
==================

ipv6 neighbor vlan

Function
--------



The **ipv6 neighbor vlan** command configures a static neighbor cache entry for the VLAN to which an interface belongs.

The **undo ipv6 neighbor** command deletes the static neighbor cache entry configured for the VLAN to which an interface belongs.



By default, no static neighbor entry is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 neighbor** *ipv6-address* *mac-address* **vlan** *vlan-id* { *interface-name* | *interface-type* *interface-number* }

**undo ipv6 neighbor** *ipv6-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a static neighbor entry. | - |
| *mac-address* | Specifies the MAC address of a static neighbor entry. | The value is a 12-digit hexadecimal number, in the format of H-H-H. Each H is 4 digits. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be a multicast MAC address or an all-F broadcast MAC address. |
| **vlan** *vlan-id* | Specifies the ID of a VLAN to which an interface belongs. | The value is an integer ranging from 1 to 4094. |
| *interface-type* | Specifies the type of a physical interface. | The value is an integer ranging from 1 to 4094. |
| *interface-number* | Specifies the number of a physical interface. | - |



Views
-----

VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To filter out invalid packets, you can run the ipv6 neighbor vlan command to configure static neighbor cache entries to bind the destination IPv6 addresses of these packets to nonexistent MAC addresses.

**Prerequisites**



In addition, before configuring a static IPv6 neighbor cache entry for the VXLAN tunnel side, ensure that a VNI ID has been associated with a BD using the **vxlan vni** command in the BD view on a VBDIF interface.The IPv6 function has been enabled on an interface using the **ipv6 enable** command.



**Configuration Impact**

A neighbor cache entry enters the REACHABLE state after being created, indicating that the interface connected to this neighbor is up. If the interface connected to this neighbor goes down, the neighbor cache entry does not exist.Static neighbor cache entries overwrite the neighbor entries dynamically learned by routing devices. That is, static neighbor cache entries have a higher priority than dynamically learned neighbor entries.

**Precautions**

A maximum of 16K static neighbor cache entries can be configured on each interface.If the IPv6 or MAC address specified in the **ipv6 neighbor** command is incorrect, communication with the corresponding neighbor fails.To clear dynamic neighbor entries, run the **reset ipv6 neighbors** command.


Example
-------

# Configure a static cache entry on VLANIF 10.
```
<HUAWEI> system-view
[~HUAWEI] vlan 10
[*HUAWEI-vlan10] quit
[*HUAWEI] interface Vlanif 10
[*HUAWEI-vlanif10] ipv6 enable
[*HUAWEI-vlanif10] ipv6 neighbor 2001:db8::1 fe-e0-89 vlan 10 100GE 1/0/1

```