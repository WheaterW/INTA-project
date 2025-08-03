ip source check user-bind check-item (interface view)
=====================================================

ip source check user-bind check-item (interface view)

Function
--------



The **ip source check user-bind check-item** command configures IP packet check items on an interface.

The **undo ip source check user-bind check-item** command restores the default IP packet check items.



By default, the IP packet check items on an interface include the IP address, MAC address, VLAN, and interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ip source check user-bind check-item** { **ip-address** | **mac-address** | **vlan** } \*

**undo ip source check user-bind check-item**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip-address** | Checks whether the IP address of an IP packet matches a binding entry. | - |
| **mac-address** | Checks whether the MAC address of an IP packet matches a binding entry. | - |
| **vlan** | Checks whether VLAN information of an IP packet matches a binding entry. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When you check an IP packet against the binding table, run the ip source check user-bind check-item command to specify the check items for the IP packet on an interface. When receiving an IP packet, the device checks the packet according to the configured check items. Only the packet that passes the check can be forwarded. Otherwise, the packet is discarded. The optional check items for IP packets include the source IP address, source MAC address, and VLAN ID. The interface information is mandatory.

**Prerequisites**

IP packet checking has been enabled using the **ipv4 source check user-bind enable** command in the interface view.

**Precautions**

When there are a large number of binding entries, it takes a long time to check IP packets after IP packet checking is configured. As a result, the forwarding efficiency of IP packets is affected.

This command takes effect only for dynamic binding entries. In static binding, the device checks IP packets against the entries in the static binding table.


Example
-------

# Enable IP packet check on 100GE1/0/1 to check whether the IP address in the IP packet matches the binding table.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] ipv4 source check user-bind enable
[*HUAWEI-100GE1/0/1] ip source check user-bind check-item ip-address

```