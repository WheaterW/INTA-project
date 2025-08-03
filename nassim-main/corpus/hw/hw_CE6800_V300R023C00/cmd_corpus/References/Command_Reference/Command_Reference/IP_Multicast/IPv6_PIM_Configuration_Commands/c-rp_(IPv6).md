c-rp (IPv6)
===========

c-rp (IPv6)

Function
--------



The **c-rp** command configures a candidate-rendezvous point (C-RP) on a Router, so that the Router can announce itself as a C-RP to the bootstrap router (BSR).

The **undo c-rp** command deletes a C-RP.



By default, no C-RP is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**c-rp** *ipv6-address* [ **group-policy** { *basic-acl6-number* | **acl6-name** *acl6-name* } | **priority** *priority* | **holdtime** *hold-interval* | **advertisement-interval** *adv-interval* ] \*

**undo c-rp** *ipv6-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies a IPv6 address. | The value is a 128-digit hexadecimal number in the format of X:X::X:X. |
| **group-policy** *basic-acl6-number* | Specifies the range of multicast groups that a C-RP serves. You can define the range of multicast groups by creating an IPv6 ACL. groupPolicyNum specifies the number of a basic IPv6 ACL. | The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6-name* | Specifies the name of a named basic IPv6 ACL. | The value is a string of 1 to 64 case-sensitive characters without spaces. The value must start with a letter (a to z or A to Z, case sensitive). |
| **priority** *priority* | Specifies a priority value for a C-RP. A larger value indicates a lower C-RP priority. | The value is an integer ranging from 0 to 255. The default value is 192. |
| **holdtime** *hold-interval* | Specifies a timeout period during which a BSR waits to receive an Advertisement message from a C-RP. | The value is an integer ranging from 1 to 65535, in seconds. The default value is 150. |
| **advertisement-interval** *adv-interval* | Specifies an interval at which a C-RP sends Advertisement messages. | The value is an integer ranging from 1 to 65535, in seconds. The default value is 60. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

An RP is the core of a PIM-SM domain, and thus a C-RP must be able to communicate with the other devices in the PIM-SM domain. Configuring a C-RP on the Router on the backbone network and reserving enough bandwidth between the Router and each of the other devices in the PIM-SM domain are recommended.An RP is elected from C-RPs based on the following rules:

* The C-RP wins if it serves the group address that users join has the longest mask.
* If group addresses that users join and are served by C-RPs have the same mask length, the priorities of the C-RPs are compared. The C-RP with the highest priority wins (a larger priority value indicates a lower priority).
* In case of the same priority, hash functions are operated. The C-RP that has the greatest calculated value wins.
* If all the preceding factors are the same, the C-RP that has the highest address wins.

Example
-------

# In the public network instance, configure 100GE 1/0/1 with the IPv6 address 2001:db8:1::1 as a C-RP of PIM-SM multicast domain ff02:0:1391::/96. Use basic ACL 2069 to configure the C-RP and set the priority of the C-RP to 10.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] acl ipv6 2069
[*HUAWEI-acl6-basic-2069] rule permit source ff02:0:1391:: 96
[*HUAWEI-acl6-basic-2069] quit
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] c-rp 2001:db8:1::1 group-policy 2069 priority 10

```