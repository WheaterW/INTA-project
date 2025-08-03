hub-mode enable
===============

hub-mode enable

Function
--------



The **hub-mode enable** command sets the access side mode to hub.

The **undo hub-mode enable** command cancels the hub mode on the access side.



By default, the access side mode is not set to hub.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**hub-mode enable**

**undo hub-mode enable**


Parameters
----------

None

Views
-----

100GE Layer 2 sub-interface view,10GE Layer 2 sub-interface view,200GE Layer 2 sub-interface view,25GE Layer 2 sub-interface view,400GE Layer 2 sub-interface view,50GE Layer 2 sub-interface view,Eth-Trunk Layer 2 sub-interface view,VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a VXLAN network, users connected to the same BD can directly communicate with each other. If access-side user isolation is configured using the **isolate enable** command in the BD view, to allow users connected to the BD through a VLAN or Layer 2 sub-interface to communicate with other users in the BD, run this command in the VLAN or Layer 2 sub-interface view to set the access-side mode to hub.On a VXLAN network, users in the same BD can directly communicate with each other. If unidirectional isolation from the access side to the tunnel side is configured in a BD using the **isolate remote enable** command in the BD view, to allow users connected to the BD through a VLAN or Layer 2 sub-interface to communicate with the tunnel side, run this command in the VLAN or Layer 2 sub-interface view to set the access-side mode to hub.

**Prerequisites**

If the VLAN access mode is set to hub, the VLAN has been bound to a BD using the **l2 binding vlan** command.


Example
-------

# Set the access-side mode of Layer 2 sub-interface 100GE1/0/1.1 to hub.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1.1 mode l2
[~HUAWEI-100GE1/0/1.1] hub-mode enable

```

# Set the access side mode of VLAN 10 to hub.
```
<HUAWEI> system-view
[~HUAWEI] vlan 10
[~HUAWEI-vlan10] quit
[~HUAWEI] bridge-domain 10
[~HUAWEI-bd10] l2 binding vlan 10
[~HUAWEI] vlan 10
[~HUAWEI-vlan10] hub-mode enable

```