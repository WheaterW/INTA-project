ospf bfd enable per-link one-arm-echo
=====================================

ospf bfd enable per-link one-arm-echo

Function
--------



The **ospf bfd enable per-link one-arm-echo** command enables OSPF link-based loopback detection.



By default, OSPF link-based loopback detection is disabled.


Format
------

**ospf bfd enable per-link one-arm-echo**


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

**Usage Scenario**

Multiple physical interfaces can be bound to an Eth-Trunk interface in a VLAN. If the per-link one-arm-echo parameter is not specified, the BFD session may go down as long as one physical interface goes down. As a result, the OSPF neighbor relationship goes down. If per-link one-arm-echo is specified, the BFD sessions goes down only when all physical interfaces are down. This ensures that OSPF neighbor relationships can be established.

**Prerequisites**



BFD has been enabled on the interface.




Example
-------

# Configure the BFD feature on the vlanif 1 interface.
```
<HUAWEI> system-view
[~HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface vlanif 1
[*HUAWEI-Vlanif1] ospf bfd enable per-link one-arm-echo

```