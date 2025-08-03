l2protocol-tunnel vlan
======================

l2protocol-tunnel vlan

Function
--------



The **l2protocol-tunnel vlan** command enables Layer 2 protocol tunneling on a tagged interface.

The **undo l2protocol-tunnel vlan** command disables Layer 2 protocol tunneling on a tagged interface.



By default, Layer 2 protocol tunneling is disabled on tagged interfaces.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**l2protocol-tunnel** { **all** | **user-defined-protocol** *protocol-name* | { *protocol* } &<1-19> } **vlan** { *low-vid* [ **to** *high-vid* ] } &<1-10>

**undo l2protocol-tunnel** { **all** | **user-defined-protocol** *protocol-name* | { *protocol* } &<1-19> } **vlan** { *low-vid* [ **to** *high-vid* ] } &<1-10>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Enables or disables Layer 2 protocol tunneling for all supported standard and user-defined Layer 2 protocols. | - |
| **user-defined-protocol** *protocol-name* | Enables or disables Layer 2 protocol tunneling for a user-defined protocol. | The value is a string of 1 to 31 case-insensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |
| *protocol* | Enables or disables Layer 2 protocol tunneling for a specified Layer 2 protocol. | The following protocols are supported:   * cdp * dldp * dtp * eoam3ah * gmrp * gvrp * hgmp * lacp * lldp * pagp * pvst+ * stp * udld * vtp   You must select at least one protocol and at most all protocols. |
| *low-vid* | Specifies a start VLAN ID. | The value is an integer ranging from 1 to 4094. It must be smaller than the end VLAN ID. |
| *high-vid* | Specifies an end VLAN ID. | The value is an integer ranging from 1 to 4094. It must be greater than the start VLAN ID. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Layer 2 protocols running between user networks, such as Multiple Spanning Tree protocol (MSTP), Link Aggregation Control Protocol (LACP), must traverse a backbone network to perform Layer 2 protocol calculation.When each edge device interface on a backbone network connects to more than one user network and Layer 2 protocol data units (PDUs) from the user networks carry VLAN tags, run the l2protocol-tunnel vlan command to configure Layer 2 protocol tunneling on tagged interfaces to allow the Layer 2 PDUs from the user networks to be tunneled across the backbone network.

**Configuration Impact**

If the l2protocol-tunnel vlan command is run more than once, all configurations take effect.


Example
-------

# Enable STP tunneling on the tagged interface 100GE1/0/1. The VLAN IDs of STP packets range from 100 to 200.
```
<HUAWEI> system-view
[~HUAWEI] l2protocol-tunnel stp group-mac 00e0-fc12-3456
[*HUAWEI] vlan batch 100 to 200
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] port link-type trunk
[*HUAWEI-100GE1/0/1] l2protocol-tunnel stp vlan 100 to 200

```