igmp snooping explicit-tracking
===============================

igmp snooping explicit-tracking

Function
--------



The **igmp snooping explicit-tracking** command enables host tracking on interfaces in a specified VLAN or VLAN range.

The **undo igmp snooping explicit-tracking** command restores the default configuration.



By default, host tracking is disabled on interfaces in VLANs.


Format
------

**igmp snooping explicit-tracking** [ **all-version** ]

**undo igmp snooping explicit-tracking** [ **all-version** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all-version** | Enables the host tracking function for IGMP of all versions. | - |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In Layer 2 multicast scenarios, after a device receives a VLAN host's Leave message for a group, the device sends a Group-specific Query message and considers that the host has left the group and deletes the corresponding forwarding entry only if the device does not receive a response from the user within a specified wait period.To speed up the device's response to VLAN users' leave requests, run the igmp snooping explicit-tracking command to enable host tracking. After this function takes effect, the device records group join status of each multicast host and does not send a group-specific Query message any more after receiving a Leave message. The device considers that a host has left a group immediately after receiving a Leave message from the host. This function shortens the leave process and reduces network bandwidth consumption.

**Prerequisites**

IGMP snooping has been enabled using the **igmp snooping enable** command.

**Precautions**



Host tracking can be configured only in common VLAN scenarios, but not in MVLAN or user VLAN scenarios.IGMPv3 host tracking can be configured only when IGMPv3 is used and no IGMPv1/v2 multicast user exists.In an IGMP on-demand scenario, after host tracking is configured, users who have ordered multicast programs need to order multicast programs again.If the host tracking function is enabled after a multicast user orders a multicast program, the host tracking configuration does not take effect immediately because the system needs to obtain the join status of the multicast user after the host tracking function is enabled. To make the configuration take effect immediately, run the **reset igmp snooping group** command to delete existing program information.After the **reset igmp snooping group** command is run, multicast traffic of multicast users in the VLAN is interrupted temporarily. The multicast users can receive multicast traffic only after they join the multicast group again.




Example
-------

# Enable host tracking on interfaces in a specified VLAN.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] igmp snooping enable
[*HUAWEI-vlan10] igmp snooping version 3
[*HUAWEI-vlan10] igmp snooping explicit-tracking

```