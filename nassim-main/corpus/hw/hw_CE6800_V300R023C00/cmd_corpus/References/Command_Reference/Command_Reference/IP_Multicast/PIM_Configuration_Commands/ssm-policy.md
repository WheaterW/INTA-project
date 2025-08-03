ssm-policy
==========

ssm-policy

Function
--------



The **ssm-policy** command sets the range of Source-Specific Multicast (SSM) group addresses.

The **undo ssm-policy** command restores the default configuration.



By default, the range of SSM group addresses is 232.0.0.0/8.


Format
------

**ssm-policy** { *basic-acl-number* | **acl-name** *acl-name* }

**undo ssm-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basic-acl-number* | Specifies the number of the basic ACL that defines the range of SSM group addresses. | The value ranges from 2000 to 2999. |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **ssm-policy** command specifies the range of PIM-SSM group addresses. All interfaces on which PIM-SM is enabled consider that multicast groups that belong to the address range are in PIM-SSM mode.With the **ssm-policy** command configured, the SSM group address range can be beyond 232.0.0.0/8, and the valid multicast group address ranges from 224.0.1.0 to 239.255.255.255. The groups that are not in the SSM group address range all adopt the Any-Source Multicast (ASM) mode.The SSM mode can be used in the following situations:

* The address of the multicast group is in the range of SSM group addresses, the network segment where the host resides runs IGMPv3, and the source address is specified in the Report message.
* The address of the multicast group is in the range of SSM group addresses, the network segment where the host resides runs IGMPv1 or IGMPv2, and the device connected with the host is configured with SSM mapping.

**Prerequisites**

The **multicast routing-enable** command is run in the public network instance view or VPN instance view.Related ACL rules have been defined.

**Configuration Impact**

If the **ssm-policy** command is run more than once, the latest configuration overrides the previous one.

**Precautions**

The **ssm-policy** command and the **acl** command are used together. In the ACL view, you can set the address range of SSM multicast groups by specifying the source parameter in the **rule** command.The ssm-policy and **pim dm** commands are mutually exclusive.


Example
-------

# In the public network instance, set the range of PIM SSM multicast addresses to 232.1.0.0/16 by using a numbered ACL.
```
<HUAWEI> system-view
[~HUAWEI] acl number 2000
[*HUAWEI-acl4-basic-2000] rule permit source 232.1.0.0 0.0.255.255
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] ssm-policy 2000

```

# In the public network instance, set the range of PIM SSM multicast addresses to 232.1.0.0/16 by using a named ACL.
```
<HUAWEI> system-view
[~HUAWEI] acl name myacl basic
[*HUAWEI-acl4-basic-myacl] rule permit source 232.1.0.0 0.0.255.255
[*HUAWEI-acl4-basic-myacl] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] ssm-policy acl-name myacl

```