bsr-policy
==========

bsr-policy

Function
--------



The **bsr-policy** command limits the range of valid bootstrap router (BSR) addresses, so that the Router discards messages received from the BSRs not in the specified address range, preventing BSR spoofing.

The **undo bsr-policy** command restores the default configuration.



By default, the range of valid BSR addresses is not limited, so that the Router considers messages received from all BSRs valid.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bsr-policy** { *basic-acl6-number* | **acl6-name** *acl6-name* }

**undo bsr-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basic-acl6-number* | Specifies the number of a basic IPv6 ACL, which defines a policy for filtering BSR messages based on source addresses. | The value is an integer ranging from 2000 to 2999.  The value of this parameter must be the same as that of the acl6-number parameter specified in the acl ipv6 command. |
| **acl6-name** *acl6-name* | Specifies the name of a named basic IPv6 ACL. | The value is a string of 1 to 64 case-sensitive characters without spaces. The value must start with a letter (a to z or A to Z, case sensitive).  The value of this parameter must be the same as that of the acl6-name parameter specified in the acl ipv6 command. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On an IPv6 PIM-SM network that uses the BSR mechanism, any Router can be configured as a candidate-bootstrap router (C-BSR) and participate in a BSR election. The winner of the BSR election is responsible for advertising RP information on the network. These mechanisms leave chances for BSR spoofing.

* Some malicious hosts construct pseudo BSR messages and send the messages to the Routers, attempting to change rendezvous point (RP) mappings on the Routers.Common preventive measures for such attacks: BSR messages are multicast packets with the TTL being 1. Such BSR spoofing commonly occurs on network edge Routers.Since the BSR resides inside the network while hosts reside outside the network, you can enable the Routers to perform neighbor and RPF checks on received BSR messages to filter out pseudo BSR messages.
* Attackers control some Routers on the network or a Router accesses the network illegally.The attacker can set the controlled Router as a C-BSR and make the C-BSR win the BSR election to control RP information advertisement on the network.Common preventive measures for such attacks: A Router will flood BSR messages on the network after being configured as a C-BSR. BSR messages are multicast packets being forwarded hop by hop, with the TTL being 1. Therefore, you can configure neighbors not to accept the BSR messages flooded by this Router using the **bsr-policy** command on each Router to set the range of valid BSR addresses. For example, you can set the addresses on 2001:DB8:1::1/128 and 2001:DB8:2::1/128 as valid BSR addresses. The Routers then do not accept or forward the messages from the BSR beyond the ranges, preventing invalid BSRs.The preceding two solutions can ensure the BSR security on the network; however, if an attacker controls a valid BSR, such a problem still exists.

Example
-------

# In the public network instance, create a named IPv6 ACL and specify addresses on the network segment 2001:DB8:2::2/64 as valid BSR addresses.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 name myacl6 basic
[*HUAWEI-acl6-basic-myacl6] rule permit source 2001:DB8:2::2 64
[*HUAWEI-acl6-basic-myacl6] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] bsr-policy acl6-name myacl6

```

# In the public network instance, specify addresses on 2001:DB8:2::2/64 as valid BSR addresses.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2001
[*HUAWEI-acl6-basic-2001] rule permit source 2001:DB8:2::2 64
[*HUAWEI-acl6-basic-2001] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim] bsr-policy 2001

```