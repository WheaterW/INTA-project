peer listen-only connect-only (BGP-VPN instance IPv6 address family view) (group)
=================================================================================

peer listen-only connect-only (BGP-VPN instance IPv6 address family view) (group)

Function
--------



The **peer listen-only** command enables a peer group to listen to connection requests but not to send connection requests.

The **undo peer listen-only** command restores the default setting.

The **peer connect-only** command enables a peer group to send connection requests but not to accept connection requests.

The **undo peer connect-only** command restores the default setting.



By default, a peer group listens to and accepts connection requests and sends connection requests.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* { **listen-only** | **connect-only** }

**undo peer** *group-name* { **listen-only** | **connect-only** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable a peer group to listen to connection requests but not to send connection requests, run the **peer listen-only** command.To enable a peer group to send connection requests but not to accept connection requests, run the **peer connect-only** command.

**Configuration Impact**

If the peer listen-only and **peer connect-only** commands are both run, the latest configuration overrides the previous one.

**Precautions**

The **peer connect-only** command or the **peer listen-only** command cannot be run on both devices that are peers of each other. Otherwise, the peer relationship cannot be established.


Example
-------

# Enable peer group to send connection requests but rejects connection requests.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpn1] group test
[*HUAWEI-bgp-6-vpn1] peer test connect-only

```