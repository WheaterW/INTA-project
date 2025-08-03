igmp snooping group-policy (Bridge domain view)
===============================================

igmp snooping group-policy (Bridge domain view)

Function
--------



The **igmp snooping group-policy** command limits the range of multicast groups that hosts can join.

The **undo igmp snooping group-policy** command cancels the configuration.



By default, hosts can join any multicast group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping group-policy** { *acl-number* | **acl-name** *acl-name* } [ **version** *number* ]

**undo igmp snooping group-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the number of an ACL. | The value is an integer ranging from 2000 to 3999. |
| **acl-name** *acl-name* | Specifies the name of a named ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **version** *number* | Specifies the version number of IGMP packets. | The value is an integer ranging from 1 to 3. |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The igmp snooping group-policy command is used to limit the range of multicast groups that user hosts can join.

**Prerequisites**

IGMP snooping has been enabled globally and in a BD.Rules have been configured for a specified basic ACL.

**Configuration Impact**

After the igmp snooping group-policy command is run, user hosts cannot join multicast groups beyond the configured multicast group range. If the igmp snooping group-policy command is run more than once, all configurations take effect.

**Precautions**

If no IGMP version is specified, the device applies the multicast group address limit to the received IGMP messages of all versions (V1, V2, and V3). In addition, the configured ACL must be a basic ACL.For numbered ACLs and named ACLs:

* In the basic ACL view, you can set the range of multicast groups that an interface is allowed to join by specifying the source parameter in the **rule** command.
* In the advanced ACL view, you can set the range of multicast sources that an interface is allowed to join by specifying the source parameter in the **rule** command, and set the range of multicast groups that an interface is allowed to join by specifying the destination parameter in the **rule** command.IGMPv1/v2 Report messages are not filtered based on the source parameter.

Example
-------

# Allow the user hosts in BD 10 to join only multicast group 225.1.1.123.
```
<HUAWEI> system-view
[~HUAWEI] acl number 2008
[*HUAWEI-acl-basic-2008] rule permit source 225.1.1.123 0
[*HUAWEI-acl-basic-2008] rule deny source any
[*HUAWEI-acl-basic-2008] quit
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping enable
[*HUAWEI-bd10] igmp snooping group-policy 2008

```