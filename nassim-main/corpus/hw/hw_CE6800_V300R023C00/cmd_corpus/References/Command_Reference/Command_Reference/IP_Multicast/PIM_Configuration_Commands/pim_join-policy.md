pim join-policy
===============

pim join-policy

Function
--------



The **pim join-policy** command enables an interface to filter join information in Join/Prune messages.

The **undo pim join-policy** command restores the default configuration.



By default, an interface does not filter join information in Join/Prune messages.


Format
------

**pim join-policy** { *advanced-acl-number* | { **acl-name** *acl-name* } | { **asm** { *basic-acl-number* | **acl-name** *acl-name* } | **ssm** { *advanced-acl-number* | **acl-name** *acl-name* } } }

**undo pim join-policy**

**undo pim join-policy ssm**

**undo pim join-policy asm**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *advanced-acl-number* | Specifies the number of an advanced ACL. | The value is an integer that ranges from 3000 to 3999. |
| *acl-name* | Specifies a named ACL for ASM. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
| **acl-name** *acl-name* | Specifies the name of a named ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
| **asm** | Enables an interface to filter join information of group addresses in the ASM address range. | - |
| *basic-acl-number* | Specifies a basic ACL for ASM. | The value is an integer that ranges from 2000 to 2999. |
| **ssm** | Enables an interface to filter join information sent by specified source addresses to group addresses in the SSM address range. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To protect a Router against Join/Prune message attacks, run the pim join-policy command to configure a join information filter policy by setting valid source and group address ranges for Join/Prune messages. The policy enables the Router to discard join information that does not match the specified filter policy.

**Prerequisites**

The multicast routing-enable command has been run in the instance to which the interface belongs. This command is valid only for PIM-SM.

**Configuration Impact**

If asm or ssm is configured more than once, the latest configuration overrides the previous one. You can configure both a basic ACL and an advanced ACL to filter the join information with group addresses in the ASM address range and SSM address range, respectively.After the pim join-policy command is run:

* If join information carried in a Join/Prune message matches the permit clause defined in the ACL, the join information is accepted, and an (S, G) entry is created for the join information.
* If join information carried in a Join/Prune message matches the deny clause defined in the ACL or no action is defined for the join information, the join information is discarded, and no (S, G) entry is created for the join information.
* If the ACL specified by the advanced-acl-number parameter does not exist, all join information is discarded.

**Precautions**

The command can be used to filter PIM Join messages in either of the following modes:

1. The pim join-policy { asm { <basic-acl-number> | acl-name <acl-name> } | ssm { <advanced-acl-number> | acl-name <acl-name> } } command is used to specify whether to filter Join messages in the ASM group address range or SSM group address range. If PIM Join messages with multicast group addresses in the ASM address range need to be filtered, the asm parameter must be specified in the command. If PIM Join messages with multicast group addresses in the SSM address range need to be filtered, the ssm parameter must be specified in the command.You do not need to specify the ASM or SSM mode in the pim join-policy {<advanced-acl-number> | acl-name <acl-name> } } command. The pim join-policy {<advanced-acl-number> | acl-name <acl-name> } } command can filter the join requests of the ASM or SSM group range. The filtering rules are as follows:When configuring filtering rules for an advanced ACL or a named ACL:For the rules used to filter PIM Join messages with multicast group addresses in the ASM address range:
2. Filtering (\*, G) entries only: The source address in the ACL rule must be set to 127.255.255.254, and the destination address must be set to the group address to be filtered.
3. Filtering (S, G) entries with any source address: If the source address of an ACL rule is set to Any and the destination address is a multicast group address, (S, G) entries with any source address can be filtered.
4. Filtering (S, G) entries: If the source address in an ACL rule specifies a multicast source address and the destination address specifies a multicast group address, packets are filtered based on the source/group address. If the source address in an ACL rule specifies a multicast source address and the destination address is set to Any, packets are filtered based on the source address. If the source address in an ACL rule is set to Any and the destination address is a multicast group address, packets are filtered based on multicast groups.
5. (S, G, RPT) is not filtered.For the rules used to filter PIM Join messages with multicast group addresses in the SSM address range:Filtering (S, G) entries: If the source address in an ACL rule specifies a multicast source address and the destination address specifies a multicast group address, packets are filtered based on the source/group address. If the source address in an ACL rule specifies a multicast source address and the destination address is set to Any, packets are filtered based on the source address. If the source address in an ACL rule is set to Any and the destination address is a multicast group address, packets are filtered based on multicast groups.



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# In the public network instance, enable an interface to accept join information in which the source address is in the 10.10.0.0/16 range and group address in the 225.1.0.0/16 range, so that the device can create (S, G) entries for join information that meets the specified filter conditions.
```
<HUAWEI> system-view
[~HUAWEI] acl number 3000
[*HUAWEI-acl4-advance-3000] rule permit ip source 10.10.0.0 0.0.255.255 destination 225.1.0.0 0.0.255.255
[*HUAWEI-acl4-advance-3000] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] pim join-policy ssm 3000

```