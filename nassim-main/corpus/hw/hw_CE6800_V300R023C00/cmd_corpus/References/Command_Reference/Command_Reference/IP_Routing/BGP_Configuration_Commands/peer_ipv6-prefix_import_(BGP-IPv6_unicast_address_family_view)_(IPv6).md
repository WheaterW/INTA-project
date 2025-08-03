peer ipv6-prefix import (BGP-IPv6 unicast address family view) (IPv6)
=====================================================================

peer ipv6-prefix import (BGP-IPv6 unicast address family view) (IPv6)

Function
--------



The **peer ipv6-prefix import** command configures a policy based on an IPv6 prefix list for filtering BGP routes received from a specified peer.

The **undo peer ipv6-prefix import** command cancels this configuration.



By default, no route filtering policy based on an IP address prefix list is configured for a peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **ipv6-prefix** *ipv6-prefix-name* **import**

**undo peer** *ipv6-address* **ipv6-prefix** [ *ipv6-prefix-name* ] **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The address is in the format of X:X:X:X:X:X:X:X. |
| **ipv6-prefix** *ipv6-prefix-name* | Indicates the filtering policy that is based on the IPv6 prefix list of the peer or peer group. | The value is a string of 1 to 169 case-sensitive characters. It cannot contain spaces. The string can contain spaces if it is enclosed with double quotation marks ("). |
| **import** | Applies a filtering policy to the routes received from a peer group. | - |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **peer ipv6-prefix import** command can be used to configure a route filtering policy that is based on an IPv6 prefix list for filtering BGP routes to be received from a specified peer, implementing route control.

**Prerequisites**

If the **peer ipv6-prefix** command specifies an IPv6 prefix list that does not exist for a peer, use the **ip ipv6-prefix** command to create an IPv6 prefix list.

**Configuration Impact**

If an IPv6 prefix list is specified for a peer group, all the members of the peer group inherit the configuration.After an IPv6 prefix list is specified for a peer, the peer filter the routes to be received from other peers based on the IPv6 prefix list. Only the routes that pass the filtering of the IPv6 prefix list can be received.

**Precautions**

The **peer ipv6-prefix import** command is mutually exclusive with the **peer route-filter import** commands.


Example
-------

# Configure a route filtering policy based on an IPv6 prefix list.
```
<HUAWEI> system-view
[~HUAWEI] ip ipv6-prefix list1 permit 2001:DB8:1::1 8 greater-equal 17 less-equal 18
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 enable
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 ipv6-prefix list1 import

```