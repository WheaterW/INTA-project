peer listen-only connect-only (BGP multi-instance VPN instance IPv4 address family view) (group)
================================================================================================

peer listen-only connect-only (BGP multi-instance VPN instance IPv4 address family view) (group)

Function
--------



The **peer listen-only** command configures a peer group to only listen to connection requests and not to initiatively send connection requests.

The **undo peer listen-only** command cancels the function.

The **peer connect-only** command configures a peer group to send connection requests but rejects connection requests.

The **undo peer connect-only** command restores the default setting.



By default, a peer group listens to and accepts connection requests and sends connection requests.


Format
------

**peer** *group-name* { **listen-only** | **connect-only** }

**undo peer** *group-name* { **listen-only** | **connect-only** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


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

# Configure peer group to only listen to connection requests from the remote peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] group test
[*HUAWEI-bgp-instance-a-vpna] peer test listen-only

```