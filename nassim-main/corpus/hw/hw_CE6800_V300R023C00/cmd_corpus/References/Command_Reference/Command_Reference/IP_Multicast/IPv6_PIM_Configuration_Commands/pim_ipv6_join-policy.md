pim ipv6 join-policy
====================

pim ipv6 join-policy

Function
--------



The **pim ipv6 join-policy** command enables an interface to filter join information in IPv6 Join/Prune messages.

The **undo pim ipv6 join-policy** command restores the default configuration.



By default, an interface does not filter join information in IPv6 Join/Prune messages.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**pim ipv6 join-policy** { *jpPolicyAclNum* | { **acl6-name** *jpPolicyName* } | { **asm** { *joinPruneAsmPolicyAclNum* | **acl6-name** *jpAsmPolicyName* } | **ssm** { *joinPruneSsmPolicyAclNum* | **acl6-name** *jpSsmPolicyName* } } }

**undo pim ipv6 join-policy**

**undo pim ipv6 join-policy ssm**

**undo pim ipv6 join-policy asm**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *jpPolicyAclNum* | Specifies the number of an advanced IPv6 ACL. | The value is an integer ranging from 3000 to 3999. |
| **acl6-name** *jpPolicyName* | Specifies the name of a named IPv6 ACL. | The value is a string of 1 to 32 case-sensitive characters without spaces.The name must start with a letter or digit, and cannot contain only digits. |
| **asm** | Enables an interface to filter join information of group addresses in the ASM address range. | - |
| *joinPruneAsmPolicyAclNum* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| *jpAsmPolicyName* | Specifies the name of a named IPv6 ACL. | The value is a string of 1 to 32 case-sensitive characters without spaces.The name must start with a letter or digit, and cannot contain only digits. |
| **ssm** | Enables an interface to filter join information sent by specified source addresses to group addresses in the SSM address range. | - |
| *joinPruneSsmPolicyAclNum* | Specifies the number of an advanced IPv6 ACL. | The value is an integer ranging from 3000 to 3999. |
| *jpSsmPolicyName* | Specifies the name of a named IPv6 ACL. | The value is a string of 1 to 32 case-sensitive characters without spaces.The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To protect a Router against IPv6 Join/Prune message attacks, run the pim ipv6 join-policy command to configure a join information filter policy by setting valid source and group address ranges for IPv6 Join/Prune messages. The policy enables the Router to discard join information that does not match the specified filter policy.

**Precautions**

The command can be used to filter PIM Join messages in either of the following modes:(1) The pim ipv6 join-policy { asm { <basic-acl6-number> | acl6-name <acl6-name> } | ssm { <advanced-acl6-number> | acl6-name <acl6-name> } } command filters PIM Join messages with multicast group addresses in the ASM or SSM address range. If PIM Join messages with multicast group addresses in the ASM address range need to be filtered, the asm parameter must be specified in the command. If PIM Join messages with multicast group addresses in the SSM address range need to be filtered, the ssm parameter must be specified in the command.(2) The pim ipv6 join-policy {<advanced-acl6-number> | acl6-name <acl6-name> } } command filters PIM Join messages with multicast group addresses both in the ASM and SSM address ranges.The precautions for configuring filtering rules are as follows:When configuring filtering rules for an advanced ACL or a named ACL:For the rules used to filter PIM Join messages with multicast group addresses in the ASM address range:(1) To filter (\*, G) PIM Join messages, the source address in the ACL rule must be set to 0::0 or any, and the destination address must be set to the multicast group address based on which the messages are to be filtered.(2) To filter (S, G) PIM Join messages:In an ACL rule, if the source address is set to a multicast source address and the destination address is set to a multicast group address, the messages are filtered based on the multicast source address and multicast group address.In an ACL rule, if the source address is set to a multicast source address and the destination address is set to any, the messages are filtered based on the multicast source address.In an ACL rule, if the source address is set to any and the destination address is set to a multicast group address, the messages are filtered based on the multicast group address.(3) The filtering rules do not take effect on (S, G, RPT) PIM Join messages.For the rules used to filter PIM Join messages with multicast group addresses in the SSM address range:(1) To filter (S, G) PIM Join messages:In an ACL rule, if the source address is set to a multicast source address and the destination address is set to a multicast group address, the messages are filtered based on the multicast source address and multicast group address.In an ACL rule, if the source address is set to a multicast source address and the destination address is set to any, the messages are filtered based on the multicast source address.In an ACL rule, if the source address is set to any and the destination address is set to a multicast group address, the messages are filtered based on the multicast group address.


Example
-------

# In the public network instance, configure 100GE1/0/1 to accept the join information with the group address FF25::1.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 number 2001
[*HUAWEI-acl6-basic-2001] rule permit source ff25::1 128
[*HUAWEI-acl6-basic-2001] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] pim ipv6 join-policy asm 2001

```

# In the public network instance, use a named ACL6 to configure 100GE1/0/1 to accept the join information with the source address 2001:db8:4::4 and group address FF35::1.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 name myacl
[*HUAWEI-acl6-advance-myacl] rule permit ipv6 source 2001:db8:4::4 128 destination ff35::1 128
[*HUAWEI-acl6-advance-myacl] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] pim ipv6 join-policy ssm acl6-name myacl

```