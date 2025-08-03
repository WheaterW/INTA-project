l2 binding vlan
===============

l2 binding vlan

Function
--------



The **l2 binding vlan** command binds a VLAN to a BD.

The **undo l2 binding vlan** command cancels the binding relationship between a VLAN and a BD.



By default, a VLAN is not bound to a BD.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**l2 binding vlan** *vlan-id*

**undo l2 binding vlan** *vlan-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Specifies a VLAN ID. | The value is an integer ranging from 1 to 4094. |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On the VXLAN network, you need to configure VXLAN service access points on a VXLAN network edge node. After you run the **l2 binding vlan** command to bind a VLAN to a BD. The interfaces added to the VLAN become VXLAN service access points.

**Prerequisites**

The VLAN to be bound to the BD has been created.The default VLAN, MAC-VLAN, IP-VLAN, protocol-VLAN, and management-VLAN cannot be bound to a BD.

**Precautions**



After a VLAN is bound to a BD, the VLANIF interface corresponding to the VLAN cannot be created.Binding a VLAN to a BD and Layer 2 proxy ARP are mutually exclusive. After a VLAN is configured as a VXLAN service access point, you are not advised to enable Layer 2 proxy ARP.After a VLAN is bound to a BD, other service configurations in the VLAN become invalid because the broadcast domain is switched to the BD.Binding a VLAN to a BD and IGMP snooping in a BD are mutually exclusive and cannot be configured together.




Example
-------

# Bind VLAN 10 to BD 10.
```
<HUAWEI> system-view
[~HUAWEI] vlan 10
[*HUAWEI-vlan10] quit
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] l2 binding vlan 10

```