ebgp-interface-sensitive (BGP multi-instance VPN instance IPv4 address family view)
===================================================================================

ebgp-interface-sensitive (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **ebgp-interface-sensitive** command immediately resets BGP sessions between the local interface and directly connected EBGP peers if the local interface goes Down.

The **undo ebgp-interface-sensitive** command disables the function.



By default, this function is enabled.


Format
------

**ebgp-interface-sensitive**

**undo ebgp-interface-sensitive**


Parameters
----------

None

Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If the **ebgp-interface-sensitive** command is not configured, the system does not immediately select a sub-optimal route for packet transmission if the local interface goes Down. Instead, the system waits for a period (180s by default) before checking whether another interface can be used to send packets to the same destination address. This will interrupt services for a period of time. If the **ebgp-interface-sensitive** command is run, BGP can fast detect an EBGP link failure and use another interface to establish a BGP peer relationship with the remote peer.If the interface used for a BGP connection alternates between Up and Down, run the **undo ebgp-interface-sensitive** command to prevent repeated BGP session deletion and reestablishment caused by route flapping, which reduces network bandwidth consumption.



**Precautions**



If the interface used for a BGP connection alternates between Up and Down, do not run the **ebgp-interface-sensitive** command.




Example
-------

# Enable the system to automatically reset BGP sessions between the local interface and directly connected EBGP peers if the local interface goes Down.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vrf1
[*HUAWEI-bgp-instance-a-vrf1] ebgp-interface-sensitive

```