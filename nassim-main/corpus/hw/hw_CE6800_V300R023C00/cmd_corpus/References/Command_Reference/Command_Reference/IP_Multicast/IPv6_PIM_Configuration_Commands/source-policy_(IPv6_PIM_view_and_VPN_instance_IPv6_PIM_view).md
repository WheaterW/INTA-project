source-policy (IPv6 PIM view/VPN instance IPv6 PIM view)
========================================================

source-policy (IPv6 PIM view/VPN instance IPv6 PIM view)

Function
--------



The **source-policy** command configures a policy for filtering multicast data packets based on source addresses or based on source and group addresses.

The **undo source-policy** command restores the default configuration.



By default, the Router does not filter received multicast data packets based on source addresses or based on source and group addresses.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**source-policy** { *acl6-number* | **acl6-name** *acl6-name* }

**undo source-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl6-number* | Specifies number of a basic or an advanced IPv6 ACL. | The value is an integer ranging from 2000 to 3999. |
| **acl6-name** *acl6-name* | Specifies the name of an IPv6 ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To implement data flow control and limit information that downstream receivers can obtain, run the source-policy command to configure a policy using which the Router filters received multicast data packets based on source addresses or based on source and group addresses. The Router forwards a received multicast data packet only if it is permitted by an ACL rule defined in the filter policy, thus improving system security.The source-policy command configuration also applies to multicast data packets encapsulated in Register messages.

**Prerequisites**

The multicast routing function has been enabled using the **multicast ipv6 routing-enable** command in the public network instance view.

**Configuration Impact**

If the source-policy command is run more than once, the latest configuration overrides the previous one.

* If a basic IPv6 ACL is used, the Router forwards only multicast data packets whose source addresses are permitted by rules of the ACL.
* If an advanced IPv6 ACL is configured, the Router forwards only multicast data packets whose source and group addresses are both permitted by rules of the ACL.
* If the specified IPv6 ACL does not exist, the Router discards all multicast data packets.

Example
-------

# Create a named IPv6 ACL to allow multicast data packets with the source address 2001:db8::1 to be accepted and discard multicast data packets with the source address 2001:db8::2.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 name myacl6
[*HUAWEI-acl6-advance-myacl6] rule permit ipv6 source 2001:db8::1 128
[*HUAWEI-acl6-advance-myacl6] rule deny ipv6 source 2001:db8::2 128
[*HUAWEI-acl6-advance-myacl6] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] source-policy acl6-name myacl6

```

# Configure the device to accept multicast data packets with the source address 2001:db8::1 and discard multicast data packets with the source address 2001:db8::2.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 number 2001
[*HUAWEI-acl6-basic-2001] rule permit source 2001:db8::1 128
[*HUAWEI-acl6-basic-2001] rule deny source 2001:db8::2 128
[*HUAWEI-acl6-basic-2001] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] source-policy 2001

```