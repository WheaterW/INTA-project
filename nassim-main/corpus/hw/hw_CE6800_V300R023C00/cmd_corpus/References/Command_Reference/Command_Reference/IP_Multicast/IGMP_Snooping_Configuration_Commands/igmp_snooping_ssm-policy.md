igmp snooping ssm-policy
========================

igmp snooping ssm-policy

Function
--------



The **igmp snooping ssm-policy** command configures an Source Specific Multicast Mapping (SSM) group address range.

The **undo igmp snooping ssm-policy** command restores the default setting.



By default, the SSM group address range is from 232.0.0.0 to 232.255.255.255.


Format
------

**igmp snooping ssm-policy** { *basic-acl-number* | **acl-name** *acl-name* }

**undo igmp snooping ssm-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basic-acl-number* | Specifies the number of a basic ACL. The basic ACL defines a multicast group address range. | The value is an integer ranging from 2000 to 2999. |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a user joins a multicast group with the address within the Any-Source Multicast (ASM) multicast address range but wants to enjoy SSM services, the **igmp snooping ssm-policy** command can be used to add this multicast group address to the SSM group address range.

**Prerequisites**

A basic ACL specified by basic-acl-number or acl-name has been configured.

**Configuration Impact**

After the **igmp snooping ssm-policy** command is run, the SSM group address range specified by basic-acl-number or acl-name can be beyond the range of 232.0.0.0 to 232.255.255.255. The group addresses out of the SSM group address range are applicable to the ASM model.

**Precautions**

If a specified multicast address is configured to be within the SSM group address range and IGMPv2 users use this multicast address to receive SSM multicast services, a multicast device does not delete the (S, G) entry corresponding to this multicast address when it receives an IGMPv2 Leave message. The (S, G) entry can be deleted through the multicast entry aging mechanism or can be deleted when the multicast device receives an IGMPv3 Leave message.


Example
-------

# Configure group address 225.1.1.123 to be within the SSM group address range in VLAN 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] acl number 2008
[*HUAWEI-acl-basic-2008] rule permit source 225.1.1.123 0
[*HUAWEI-acl-basic-2008] quit
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] igmp snooping ssm-policy 2008

```