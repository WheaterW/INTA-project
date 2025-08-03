peer filter-policy import (BGP-IPv4 unicast address family view) (IPv6)
=======================================================================

peer filter-policy import (BGP-IPv4 unicast address family view) (IPv6)

Function
--------



The **peer filter-policy import** command configures an ACL-based policy for filtering BGP routes received from a specified peer.

The **undo peer filter-policy import** command cancels this configuration.



By default, no filtering policy is configured for the routes received from peers.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **filter-policy** *aclNum* **import**

**peer** *peerIpv6Addr* **filter-policy** **acl-name** *aclname* **import**

**undo peer** *peerIpv6Addr* **filter-policy** *aclNum* **import**

**undo peer** *peerIpv6Addr* **filter-policy** **acl-name** *aclname* **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *aclNum* | Specifies the number of the basic ACL. | The value is an integer ranging from 2000 to 2999. |
| **acl-name** *aclname* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces and starts with a letter (a to z or A to Z). |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If you do not want to receive all routes from a peer, you can run the **peer filter-policy import** command to configure an ACL-based filtering policy to filter the routes received from the peer.

**Precautions**

For a named ACL, when the **rule** command is used to configure a filtering rule, only the configurations specified by source and time-range take effect.Select a correct basic ACL based on the address family type of the peer.For a peer, only one route filtering policy can take effect. If the **peer filter-policy** command is run more than once, the latest configuration takes effect.


Example
-------

# Set the filtering policy for peers.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl4-basic-2001] rule permit
[*HUAWEI-acl4-basic-2001] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 200
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer 2001:DB8:1::1 enable
[*HUAWEI-bgp-af-ipv4] peer 2001:DB8:1::1 filter-policy 2001 import

```