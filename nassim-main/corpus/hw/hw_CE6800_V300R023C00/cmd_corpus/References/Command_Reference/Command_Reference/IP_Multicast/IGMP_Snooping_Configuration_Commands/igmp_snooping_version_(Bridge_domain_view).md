igmp snooping version (Bridge domain view)
==========================================

igmp snooping version (Bridge domain view)

Function
--------



The **igmp snooping version** command sets a version for IGMP messages that can be processed by IGMP snooping.

The **undo igmp snooping version** command restores the default configuration.



By default, IGMP snooping can process IGMPv1 and IGMPv2 messages but cannot process IGMPv3 messages.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping version** *number*

**undo igmp snooping version**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies an IGMP version number. | The value is 1, 2, or 3. |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command is used on a Layer 2 device that is connected to hosts that support different IGMP versions.If the version number is set to 1, only IGMPv1 messages can be processed. If the version number is set to 2, IGMPv1 and IGMPv2 messages can be processed. If the version number is set to 3, IGMPv1, IGMPv2, and IGMPv3 messages can be processed.

**Configuration Impact**

If the IGMP snooping version is changed from 3 to 2:

* The system deletes all dynamically generated IGMP forwarding entries.
* The system processes statically configured Layer 2 multicast forwarding entries as follows:
* If interfaces are configured to statically join multicast groups with no multicast source specified, the system does not delete the static IGMP forwarding entries.
* If interfaces are configured to statically join source-specific multicast groups, the system deletes the static forwarding entries. When the IGMP snooping version is changed to 3, the system re-generates forwarding entries.

Example
-------

# Set an IGMP snooping version to 1 in BD 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping version 1

```