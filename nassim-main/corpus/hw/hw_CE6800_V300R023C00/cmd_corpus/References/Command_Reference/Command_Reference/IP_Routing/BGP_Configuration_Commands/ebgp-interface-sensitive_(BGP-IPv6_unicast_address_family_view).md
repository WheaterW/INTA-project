ebgp-interface-sensitive (BGP-IPv6 unicast address family view)
===============================================================

ebgp-interface-sensitive (BGP-IPv6 unicast address family view)

Function
--------



The **ebgp-interface-sensitive** command immediately resets BGP sessions between the local interface and directly connected EBGP peers if the local interface goes Down.

The **undo ebgp-interface-sensitive** command disables the function.



By default, this function is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ebgp-interface-sensitive**

**undo ebgp-interface-sensitive**


Parameters
----------

None

Views
-----

BGP-IPv6 unicast address family view


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
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] ebgp-interface-sensitive

```