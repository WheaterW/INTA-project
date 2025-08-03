igmp snooping group-policy (VLAN view)
======================================

igmp snooping group-policy (VLAN view)

Function
--------



The **igmp snooping group-policy** command limits the range of multicast groups that hosts can join.

The **undo igmp snooping group-policy** command cancels the configuration.



By default, hosts can join any multicast group.


Format
------

**igmp snooping group-policy** { *GrpAclNum* | **acl-name** *GrpAclName* } [ **version** *GrpAclVer* ]

**undo igmp snooping group-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *GrpAclNum* | Specifies the number of an ACL. | The value is an integer ranging from 2000 to 3999. |
| **acl-name** *GrpAclName* | Specifies the name of a named ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
| **version** *GrpAclVer* | Specifies the version number of IGMP packets. | The value is an integer that is 1, 2, or 3. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The igmp snooping group-policy command is used to limit the range of multicast groups that user hosts can join.

**Prerequisites**

IGMP snooping has been enabled globally and in a VLAN.Rules have been configured for a specified basic ACL.

**Configuration Impact**

After the igmp snooping group-policy command is run, user hosts cannot join multicast groups beyond the configured multicast group range. If the igmp snooping group-policy command is run more than once, all configurations take effect.

**Precautions**

If no IGMP version is specified, the device applies the multicast group address limit to the received IGMP messages of all versions (V1, V2, and V3). In addition, the configured ACL must be a basic ACL.When you run this command in the VLAN view, the configuration fails in the following situations:

* The dot1q sub-interface has been bound to the VLAN.

For numbered ACLs and named ACLs:

* In the basic ACL view, you can set the range of multicast groups that an interface is allowed to join by specifying the source parameter in the **rule** command.
* In the advanced ACL view, you can set the range of multicast sources that an interface is allowed to join by specifying the source parameter in the **rule** command, and set the range of multicast groups that an interface is allowed to join by specifying the destination parameter in the **rule** command.IGMPv1/v2 Report messages are not filtered based on the source parameter.

Example
-------

# Allow the user hosts in VLAN 100 to join only multicast group 225.1.1.123.
```
<HUAWEI> system-view
[~HUAWEI] acl number 2008
[*HUAWEI-acl-basic-2008] rule permit source 225.1.1.123 0
[*HUAWEI-acl-basic-2008] rule deny source any
[*HUAWEI-acl-basic-2008] quit
[*HUAWEI] vlan 100
[*HUAWEI-vlan100] igmp snooping enable
[*HUAWEI-vlan100] igmp snooping group-policy 2008

```