statistics enable(VLAN view)
============================

statistics enable(VLAN view)

Function
--------



The **statistics enable** command enables VLAN packet statistics collection.

The **undo statistics enable** command disables VLAN packet statistics collection.



By default, VLAN packet statistics collection is disabled.


Format
------

**statistics enable**

**undo statistics enable**


Parameters
----------

None

Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, VLAN packet statistics collection is disabled. Before you run the **display vlan statistics** command to view VLAN packet statistics on a specified sub-interface for fault locating, run this command in the VLAN view to enable VLAN packet statistics collection. Otherwise, you cannot view VLAN packet statistics on the sub-interface.



**Prerequisites**

The VLAN has been created using the **vlan** command in the system view.A Layer 2 Ethernet interface has been added to the VLAN.If the interface is a Layer 3 Ethernet interface , run the **portswitch** command in the interface view to switch the interface to a Layer 2 interface.

* If the Layer 2 Ethernet interface directly connects to a user terminal,
* Configure the Layer 2 Ethernet interface as an access interface using the **port link-type access** command.
* Add the access interface to the VLAN using the **port default vlan vlan-id** command.
* If the Layer 2 Ethernet interface connects to an interface of another switching device,
* Configure the interface as a trunk interface using the **port link-type trunk** command to configure the interface as a trunk interface.
* Add the trunk interface to specified VLANs using the **port trunk allow-pass vlan** command.

**Configuration Impact**



After running the statistic enable command, you can run the **display vlan statistics** command to view VLAN packet statistics, which help locate faults.




Example
-------

# Enable packet statistics of VLAN 10.
```
<HUAWEI> system-view
[~HUAWEI] vlan 10
[*HUAWEI-vlan10] statistics enable

```