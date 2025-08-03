c-rp policy (IPv6 PIM view)
===========================

c-rp policy (IPv6 PIM view)

Function
--------



The **c-rp policy** command limits the range of valid candidate-rendezvous point (C-RP) addresses and the range of multicast addresses served by a C-RP. The bootstrap router (BSR) drops C-RP messages that carry addresses not in the range of valid C-RP addresses.

The **undo c-rp policy** command restores the default configuration.



By default, the range of valid C-RP addresses and the range of multicast groups served by a C-RP are not limited. That is, the BSR considers all received C-RP messages valid.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**c-rp policy** { *advanced-acl-number* | **acl6-name** *acl6-name* }

**undo c-rp policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *advanced-acl-number* | Specifies the number of an advanced IPv6 ACL that defines the range of valid C-RP addresses and the range of groups served by a C-RP. | The value is an integer ranging from 3000 to 3999. |
| **acl6-name** *acl6-name* | Specifies the name of a named IPv6 ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On a PIM SM network that uses the BSR mechanism, any router can be configured as a C-RP, and serves the multicast groups in a specified address range. Each C-RP sends its information to the BSR in unicast mode. The BSR summarizes all received C-RP information as an RP-set, and floods it through BSR messages on the entire network. The local router then works out the RP to which a specific multicast group address range corresponds based on the RP-set.To protect valid C-RPs from being spoofed, run the c-rp policy command to limit the range of valid C-RP addresses and the range of multicast group addresses served by a C-RP. You must configure the same filtering rule on each C-BSR because any C-BSR may become the BSR.


Example
-------

# Use a named IPv6 ACL to configure a C-RP policy on the C-BSR for the public network instance: only 2001:db8:1::1/128 can function as the C-RP, and the C-RP is allowed to serve only the multicast groups whose addresses are in the range of ff03::101/128.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 name myacl6
[*HUAWEI-acl6-advance-myacl6] rule permit ipv6 source 2001:db8:1::1 128 destination ff03::101 128
[*HUAWEI-acl6-advance-myacl6] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] c-rp policy acl6-name myacl6

```

# Configure a C-RP policy on the C-BSR for the public network instance: only 2001:db8:1::1/128 can function as the C-RP, and the C-RP is allowed to serve only the multicast groups whose addresses are in the range of ff03::101/128.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 number 3100
[*HUAWEI-acl6-advance-3100] rule permit ipv6 source 2001:db8:1::1 128 destination ff03::101 128
[*HUAWEI-acl6-advance-3100] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] c-rp policy 3100

```