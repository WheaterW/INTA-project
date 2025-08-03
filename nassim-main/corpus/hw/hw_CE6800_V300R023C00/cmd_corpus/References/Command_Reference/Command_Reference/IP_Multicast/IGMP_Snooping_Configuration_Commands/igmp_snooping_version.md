igmp snooping version
=====================

igmp snooping version

Function
--------



The **igmp snooping version** command sets a version for IGMP messages that can be processed by IGMP snooping.

The **undo igmp snooping version** command restores the default configuration.



By default, IGMP snooping can process IGMPv1 and IGMPv2 messages but cannot process IGMPv3 messages.


Format
------

**igmp snooping version** *number*

**igmp snooping version 3** [ **standard-full** ]

**undo igmp snooping version**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies an IGMP version number. | The value is 1, 2, or 3. |
| **3** | IGMPv3. | - |
| **standard-full** | Specify a standard IGMP. | - |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If hosts connected to a Layer 2 device support different IGMP versions, run the igmp snooping version command.When the version number is 1, only IGMPv1 packets can be processed. When the version number is 2, the can process both IGMPv1 and IGMPv2 packets. When the version number is 3, IGMPv1, IGMPv2, and IGMPv3 packets can be processed.If standard-full is not specified, the standard simplified version of IGMPv3 is used. If standard-full is specified, the standard full version of IGMPv3 is used. In the standard simplified version of IGMPv3

**Configuration Impact**

If the IGMP snooping version is changed from 3 to 2:

* The system deletes all dynamically generated IGMP forwarding entries.
* The system processes statically configured Layer 2 multicast forwarding entries as follows:
* If interfaces are configured to statically join multicast groups with no multicast source specified, the system does not delete the static IGMP forwarding entries.
* If interfaces are configured to statically join source-specific multicast groups, the system deletes the static forwarding entries. When the IGMP snooping version is changed to 3, the system re-generates forwarding entries.

Example
-------

# Set the version of IGMPv3 in VLAN 2.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] igmp snooping version 3

```