ipv6-family
===========

ipv6-family

Function
--------



The **ipv6-family** command enables and enters the IPv6 address family view of BGP.

The **undo ipv6-family** command disables the IPv6 address family view and deletes the configurations in the view.



By default, the IPv6 address family view of BGP is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6-family unicast**

**ipv6-family**

**undo ipv6-family** [ **unicast** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **unicast** | Displays the unicast address family view. | - |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If no parameter is specified, the IPv6 unicast address family view is displayed by default. Similarly, if you run the **undo ipv6-family** command without specifying any parameter, the configurations of the IPv6 unicast address family are deleted.

**Configuration Impact**

The **undo ipv6-family** command with no VPN instance specified deletes all IPv6 unicast address family configurations.


Example
-------

# Enter the BGP-IPv6 unicast address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6]

```