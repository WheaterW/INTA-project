ssm-policy(IPv6 PIM view)
=========================

ssm-policy(IPv6 PIM view)

Function
--------



The **ssm-policy** command sets the range of IPv6 Source-Specific Multicast (SSM) group addresses.

The **undo ssm-policy** command restores the default value.



By default,the range of IPv6 SSM group addresses is FF3x::/32. (The value of x cannot be 1 or 2.)

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ssm-policy** { *basic-acl6-number* | **acl6-name** *acl6-name* }

**undo ssm-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basic-acl6-number* | Specifies the number of a basic IPv6 ACL. This ACL defines the range of IPv6 SSM group addresses. | The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6-name* | Specifies the name of a named basic IPv6 ACL. | The value is a string of 1 to 64 case-sensitive characters without spaces. The value must start with a letter (a to z or A to Z, case sensitive). |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the **ssm-policy** command is configured on a device, all PIM-SM interfaces on the device consider that multicast groups whose addresses are within the SSM group address range adopt the PIM-SSM model.The SSM group address range can be out of FF3x::/32. The groups that are not in the SSM group address range all adopt the Any-Source Multicast (ASM) model.The SSM model is triggered in the following situations:

* Multicast group addresses are in the SSM group address range, Multicast Listener Discovery version 2 (MLDv2) is run on the user network segment, and multicast source addresses are specified in Report messages.
* Multicast group addresses are in the SSM group address range, MLDv1 is run on the user network segment, and SSM mapping is configured on the Router connected with user hosts.

Example
-------

# Set the range of SSM group addresses to FF31:0:8192::/96 in an SSM policy.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2000
[*HUAWEI-acl6-basic-2000] rule permit source ff31:0:8192:: 96
[*HUAWEI-acl6-basic-2000] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] ssm-policy 2000

```

# Create a named IPv6 ACL, setting the range of SSM group addresses to FF31:0:8192::/96.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 name myacl6 basic
[*HUAWEI-acl6-basic-myacl6] rule permit source ff31:0:8192:: 96
[*HUAWEI-acl6-basic-myacl6] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] ssm-policy acl6-name myacl6

```