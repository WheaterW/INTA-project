igmp snooping enable (System view)
==================================

igmp snooping enable (System view)

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

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

IGMP snooping runs on a Layer 2 device that is deployed between a Layer 3 device and user hosts. It maintains multicast forwarding entries by listening to multicast protocol packets transmitted between the upstream device and hosts, thereby controlling multicast data packet forwarding. Enabling IGMP snooping is the prerequisite for implementing Layer 2 multicast. The igmp snooping enable command can be used to enable IGMP snooping.The differences between the command configuration in the system view and that in the VLAN view are listed as follows:

* After the igmp snooping enable or **undo igmp snooping enable** command is run in the system view, IGMP snooping will be enabled or disabled globally. Running the **undo igmp snooping enable** command deletes all Layer 2 multicast commands on a device. The running Layer 2 multicast services are then terminated. To restore Layer 2 multicast services on the device, you must reconfigure the deleted multicast commands.
* After the igmp snooping enable or **undo igmp snooping enable** command is run in the VLAN view, IGMP snooping will be enabled or disabled in a specified VLAN. IGMP snooping can be enabled in a VLAN only after IGMP snooping is enabled globally. By default, IGMP snooping is still disabled in a VLAN though IGMP snooping is enabled in the system view.

**Precautions**

The igmp snooping enable command fails to be run in a VLAN in any of the following situations:

* A Dot1q termination sub-interface has been added to the VLAN.

Example
-------

# Enable IGMP snooping globally.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable

```