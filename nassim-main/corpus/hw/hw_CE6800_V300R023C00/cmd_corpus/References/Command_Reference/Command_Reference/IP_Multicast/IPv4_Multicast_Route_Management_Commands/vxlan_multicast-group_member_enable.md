vxlan multicast-group member enable
===================================

vxlan multicast-group member enable

Function
--------



The **vxlan multicast-group member enable** command adds an interface to a multicast group.

The **undo vxlan multicast-group member enable** command disables an interface from being added to a multicast group.



By default, an interface is not added to a multicast group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vxlan multicast-group member enable**

**undo vxlan multicast-group member enable**


Parameters
----------

None

Views
-----

VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In a scenario where an M-LAG is connected to a VXLAN network and multicast replication is used, you need to create a VLAN on the devices that set up the M-LAG and run the **vxlan multicast-group member enable** command on the VLANIF interface to add the interface to a multicast group so that the M-LAG devices synchronize VXLAN-encapsulated multicast packets through the peer-link.Only one VLANIF interface can be added to a multicast group. Do not deploy other services on the VLANIF interface.


Example
-------

# Add VLANIF 2 to the multicast group.
```
<HUAWEI> system-view
[~HUAWEI] vlan 2
[*HUAWEI-vlan2] quit
[*HUAWEI] interface vlanif 2
[*HUAWEI-Vlanif2] vxlan multicast-group member enable

```