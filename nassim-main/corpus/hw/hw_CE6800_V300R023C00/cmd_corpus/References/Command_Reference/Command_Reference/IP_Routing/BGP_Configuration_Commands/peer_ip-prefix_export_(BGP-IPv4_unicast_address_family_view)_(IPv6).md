peer ip-prefix export (BGP-IPv4 unicast address family view) (IPv6)
===================================================================

peer ip-prefix export (BGP-IPv4 unicast address family view) (IPv6)

Function
--------



The **peer ip-prefix export** command configures a policy based on an IP prefix list for filtering BGP routes to be advertised to a specified peer.

The **undo peer ip-prefix export** command cancels this configuration.



By default, no route filtering policy based on an IP address prefix list is configured for a peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **ip-prefix** *ip-prefix-name* **export**

**undo peer** *peerIpv6Addr* **ip-prefix** [ *ip-prefix-name* ] **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number in format X:X:X:X:X:X:X:X. |
| **ip-prefix** *ip-prefix-name* | Specifies the name of an IP prefix list. | The name is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **export** | Applies a filtering policy to the routes to be advertised to a peer. | - |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To filter routes to be advertised to a specified peer, you can run the **peer ip-prefix export** command to configure a route filtering policy based on an IP prefix list.

**Prerequisites**

If the **peer ip-prefix** command specifies an IP prefix list that does not exist for a peer, use the **ip ip-prefix** command to create an IP prefix list.

**Configuration Impact**

After an IP prefix list is specified for a peer, the device filters routes based on the IP prefix list when advertising routes to the peer. Only the routes that pass the filtering of the IP prefix list can be advertised.

**Precautions**

If you run both this command and the **peer route-filter export** command, the latest configuration overrides the previous one.If the length of the filter name is less than or equal to six characters and the name matches the first six characters of export, when running the **undo peer ip-prefix export** command, you only need to enter the keyword export instead of the filter name.


Example
-------

# Configure a route filtering policy named prefix1 based on an IP prefix list.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix prefix1 permit 10.1.1.1 8 greater-equal 17 less-equal 18
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer 2001:DB8:1::1 enable
[*HUAWEI-bgp-af-ipv4] peer 2001:DB8:1::1 ip-prefix prefix1 export

```