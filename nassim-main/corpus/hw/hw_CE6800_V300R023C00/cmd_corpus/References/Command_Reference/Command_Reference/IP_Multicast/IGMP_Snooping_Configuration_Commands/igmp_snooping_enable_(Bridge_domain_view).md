igmp snooping enable (Bridge domain view)
=========================================

igmp snooping enable (Bridge domain view)

Function
--------



The **igmp snooping enable** command enables IGMP snooping.

The **undo igmp snooping enable** command disables IGMP snooping.



By default, IGMP snooping is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping enable**

**undo igmp snooping enable**


Parameters
----------

None

Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

IGMP snooping runs on a Layer 2 device that is deployed between a Layer 3 device and user hosts. It maintains multicast forwarding entries by listening to multicast protocol packets transmitted between the upstream device and hosts, thereby controlling multicast data packet forwarding. Enabling IGMP snooping is the prerequisite for implementing Layer 2 multicast. The igmp snooping enable command can be used to enable IGMP snooping.The differences between the command configuration in the system view and that in the BD view are listed as follows:

* After the igmp snooping enable or **undo igmp snooping enable** command is run in the system view, IGMP snooping will be enabled or disabled globally. Running the **undo igmp snooping enable** command deletes all Layer 2 multicast commands on a device. The running Layer 2 multicast services are then terminated. To restore Layer 2 multicast services on the device, you must reconfigure the deleted multicast commands.After the igmp snooping enable or **undo igmp snooping enable** command is run in the BD view, IGMP snooping will be enabled or disabled in a specified BD. IGMP snooping can be enabled in a BD only after IGMP snooping is enabled globally. By default, IGMP snooping is still disabled in a BD though IGMP snooping is enabled in the system view.

**Precautions**



If a VXLAN VNI is configured in the BD view and multicast replication of BUM packets for the VNI is enabled on an NVE interface, IGMP snooping cannot be enabled in the BD view.If the vtep-src command has been run in the BD view, IGMP snooping cannot be enabled in the BD view.IGMP snooping and the l2 binding vlan command are mutually exclusive in a BD.




Example
-------

# Enable IGMP snooping in BD.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping enable

```