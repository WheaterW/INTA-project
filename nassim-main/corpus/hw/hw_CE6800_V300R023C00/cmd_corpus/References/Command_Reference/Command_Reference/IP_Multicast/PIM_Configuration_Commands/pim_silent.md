pim silent
==========

pim silent

Function
--------



The **pim silent** command enables the PIM silent function on an interface.

The **undo pim silent** command disables the PIM silent function on an interface.



By default, the PIM silent function is not enabled on an interface.


Format
------

**pim silent**

**undo pim silent**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent malicious hosts from constructing pseudo PIM Hello messages to attack a Router, enable PIM silent using the **pim silent** command on an interface connected to hosts. After PIM silent is enabled on an interface, all PIM packets will be discard by this interface, and all PIM neighbors and PIM state machines will be deleted for this interface. The interface automatically becomes a static designated router (DR). IGMP functions, however, are not affected on the interface.

**Precautions**

PIM silent applies only to interfaces directly connected to a host network segment on which only one PIM device is deployed.The **pim silent** command is mutually exclusive with the **pim timer dr-switch-delay** command.The **pim silent** command is mutually exclusive with the **pim dm** command.The **pim silent** command is mutually exclusive with the **pim bfd enable** command.Note:If PIM silent is enabled on an interface connected to a router, a PIM neighbor relationship cannot be set up on the interface, causing multicast faults.If a host network segment connects to multiple Routers and PIM silent is enabled on interfaces of multiple Routers, all these interfaces become static DRs, causing multicast faults.



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Configure the PIM silent function on VLANIF 1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] pim silent

```