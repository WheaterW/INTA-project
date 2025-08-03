l2protocol-tunnel enable (Layer 2 interface view)
=================================================

l2protocol-tunnel enable (Layer 2 interface view)

Function
--------



The **l2protocol-tunnel enable** command enables Layer 2 protocol tunneling on an untagged interface.

The **undo l2protocol-tunnel enable** command disables Layer 2 protocol tunneling on an untagged interface.

The **l2protocol-tunnel disable** command disables Layer 2 protocol tunneling on an untagged interface.



By default, Layer 2 protocol tunneling is disabled on untagged interfaces.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**l2protocol-tunnel** { **all** | **user-defined-protocol** *protocol-name* | { *protocol* } &<1-16> } **enable**

**l2protocol-tunnel** { **all** | **user-defined-protocol** *protocol-name* | { *protocol* } &<1-16> } **disable**

**undo l2protocol-tunnel** { **all** | **user-defined-protocol** *protocol-name* | { *protocol* } &<1-16> } **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Enables or disables transparent transmission of packets of all standard Layer 2 protocols and user-defined Layer 2 protocols. | - |
| **user-defined-protocol** *protocol-name* | Enables or disables the user-defined protocol. | The name is a string of 1 to 31 case-insensitive characters, spaces not supported.  If spaces are used, the string must be enclosed in double quotation marks (" "). |
| *protocol* | Enables or disables Layer 2 protocol tunneling for a specified Layer 2 protocol. | The following protocols are supported:   * cdp * dldp * dtp * eoam3ah * gmrp * gvrp * hgmp * lacp * lldp * pagp * pvst+ * stp * udld * vtp   You must select at least one protocol and at most all protocols. |
| **enable** | Enables Layer 2 protocol transparent transmission. | - |
| **disable** | Disables Layer 2 protocol transparent transmission. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Layer 2 protocols running between user networks, such as Multiple Spanning Tree protocol (MSTP), Link Aggregation Control Protocol (LACP), must traverse a backbone network to perform Layer 2 protocol calculation.When each edge device interface on a backbone network connects to only one user network and Layer 2 protocol data units (PDUs) from the user networks do not carry VLAN tags, run the l2protocol-tunnel enable command to configure Layer 2 protocol tunneling on untagged interfaces to allow the Layer 2 PDUs from the user networks to be tunneled across the backbone network. Layer 2 PDUs from the user networks then travel through different Layer 2 tunnels to reach the destinations to perform Layer 2 protocol calculation.

**Prerequisites**

* The **l2protocol-tunnel group-mac** command has been run to configure an edge device to replace the multicast destination MAC addresses in Layer 2 PDUs with a specified multicast MAC address for all Layer 2 protocols except STP to be tunneled. STP has a default group MAC address.
* The **l2protocol-tunnel user-defined-protocol** command has been run to configure parameters for a user-defined Layer 2 protocol.

**Precautions**

The l2protocol-tunnel enable and **l2protocol-tunnel vlan** commands with the same Layer 2 protocol specified cannot be run on the same interface. If you run both commands on the same interface, the system prompts you with a configuration conflict.


Example
-------

# Enable tunneling for STP on the untagged interface 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] l2protocol-tunnel stp enable

```