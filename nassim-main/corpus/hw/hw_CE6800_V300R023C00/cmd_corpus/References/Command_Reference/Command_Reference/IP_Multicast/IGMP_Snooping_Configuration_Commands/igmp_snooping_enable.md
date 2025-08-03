igmp snooping enable
====================

igmp snooping enable

Function
--------



The **igmp snooping enable** command enables IGMP snooping.

The **undo igmp snooping enable** command disables IGMP snooping.



By default, IGMP snooping is disabled.


Format
------

**igmp snooping enable**

**undo igmp snooping enable**


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

IGMP snooping runs on a Layer 2 device between a Layer 3 device and user hosts. The Layer 2 device listens to multicast protocol messages exchanged between the upstream Layer 3 device and user hosts to maintain multicast forwarding entries. In this manner, the Layer 2 device manages and controls forwarding of multicast data packets. Enabling IGMP snooping is the prerequisite for implementing Layer 2 multicast. To enable IGMP snooping, run the igmp-snooping enable command.The differences between using this command in the system view and in the VLAN view are as follows:

* Running this command in the system view enables IGMP snooping globally. If you run the **undo igmp snooping enable** command in the system view, IGMP snooping is disabled on the entire device, all Layer 2 multicast commands on the device are deleted, and running Layer 2 multicast services are interrupted. To restore Layer 2 multicast services on the device, you must reconfigure the deleted multicast commands.
* Running this command in the VLAN view enables or disables IGMP snooping in the BD. IGMP snooping can be enabled in a BD only after IGMP snooping is enabled globally. After IGMP snooping is enabled in the system view, IGMP snooping is still disabled in a BD by default.

**Precautions**

When this function is configured in the VLAN view, the configuration fails in the following situations:

* The dot1q sub-interface has been bound to the VLAN.
* IGMP snooping cannot be used together with VLAN mapping or VLAN stacking in a VLAN.

Example
-------

# Enable IGMP snooping in VLAN 2.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] igmp snooping enable

```

# Enable IGMP snooping globally.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable

```