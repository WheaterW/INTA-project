ip source check user-bind check-item (VLAN view)
================================================

ip source check user-bind check-item (VLAN view)

Function
--------



The **ip source check user-bind check-item** command configures IP packet check items in a VLAN.

The **undo ip source check user-bind check-item** command restores the default IP packet check items in a VLAN.



By default, IP packets in a VLAN are checked based on the IP address, MAC address, VLAN ID, and interface number.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ip source check user-bind check-item** { **ip-address** | **mac-address** | **interface** } \*

**undo ip source check user-bind check-item**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip-address** | Checks whether the IP address and VLAN of an IP packet matches a binding entry. | - |
| **mac-address** | Checks whether the MAC address and VLAN of an IP packet matches a binding entry. | - |
| **interface** | Checks whether interface information and VLAN of an IP packet matches a binding entry. | - |



Views
-----

VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When configuring the device to check IP packets against the binding table, you can run the ip source check user-bind check-item command to specify the check items for IP packets in a VLAN. When receiving an IP packet, the device checks the packet according to the configured check items. Only the packet that passes the check can be forwarded. Otherwise, the packet is discarded. The optional check items of IP packets include the source IP address, source MAC address, and interface. The VLAN information is mandatory.

**Prerequisites**

IP packet checking has been enabled using the **ipv4 source check user-bind enable** command in the VLAN view.

**Precautions**

When a large number of binding entries exist, it takes a long time to check IP packets after the IP packet check function is enabled. As a result, the forwarding efficiency of IP packets is affected.This command takes effect only for dynamic binding entries. In static binding, the checks IP packets against the entries in the static binding table.


Example
-------

# Enable IP packet checking in VLAN 100 to check whether the IP address of the IP packet matches the binding table.
```
<HUAWEI> system-view
[~HUAWEI] vlan 100
[*HUAWEI-vlan100] ipv4 source check user-bind enable
[*HUAWEI-vlan100] ip source check user-bind check-item ip-address

```