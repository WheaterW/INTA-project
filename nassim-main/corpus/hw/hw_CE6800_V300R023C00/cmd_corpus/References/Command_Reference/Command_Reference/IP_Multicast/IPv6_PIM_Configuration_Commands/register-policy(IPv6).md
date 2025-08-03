register-policy(IPv6)
=====================

register-policy(IPv6)

Function
--------



The **register-policy** command configures a policy used by a rendezvous point (RP) to filter Register messages.

The **undo register-policy** command restores the default configuration.



By default, no Register message filter policy is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**register-policy** { *registerPolicyAclNum* | **acl6-name** *regPolicyName* }

**undo register-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *registerPolicyAclNum* | Specifies the number of an advanced IPv6 ACL. | The value is an integer ranging from 3000 to 3999. |
| **acl6-name** *regPolicyName* | Specifies the name of an advanced IPv6 ACL. | The value is a string of 1 to 64 case-sensitive characters without spaces. The value must start with a letter (a to z or A to Z, case sensitive). |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent Register message attacks, run the **register-policy** command to enable a Router to permit or deny specific Register messages.The **register-policy** command takes effect only for subsequently received Register messages. That is, the multicast entries that have been registered successfully are not deleted and can still be used for multicast data forwarding.

**Prerequisites**

The **multicast ipv6 routing-enable** command is run in the public network instance view.

**Configuration Impact**

If the **register-policy** command is run more than once, the latest configuration overrides the previous one.If the (S, G) information contained in a Register message is denied by ACL rules or if no ACL action is configured for the (S, G) information, the RP discards the Register message and does not register the multicast source indicated by the (S, G) information.The RP accepts only Register messages permitted by ACL rules. If a specified ACL does not exist, the RP discards all Register messages and does not register any multicast sources.


Example
-------

# Create a named IPv6 ACL to configure the RP to accept the Register messages sent by the multicast source on the network segment 2001:db8:1::/64 to the multicast group FF02:13::/64.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 name myacl6
[*HUAWEI-acl6-advance-myacl6] rule permit ipv6 source 2001:db8:1:: 64 destination ff02:13:: 64
[*HUAWEI-acl6-advance-myacl6] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] register-policy acl6-name myacl6

```

# Configure the RP to accept the Register messages sent by the multicast source on the network segment 2001:db8:1::/64 to the multicast group FF02:13::/64.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 3000
[*HUAWEI-acl6-advance-3000] rule permit ipv6 source 2001:db8:1:: 64 destination ff02:13:: 64
[*HUAWEI-acl6-advance-3000] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] register-policy 3000

```