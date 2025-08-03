ibgp-interface-sensitive (BGP-VPN instance IPv6 address family view)
====================================================================

ibgp-interface-sensitive (BGP-VPN instance IPv6 address family view)

Function
--------



The **ibgp-interface-sensitive** command enables BGP to delete the direct IBGP peer relationship established on a local interface upon a failure of the interface.

The **undo ibgp-interface-sensitive** command restores the default configuration.



By default, BGP is not enabled to delete the direct IBGP peer relationship established on a local interface upon a failure of the interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ibgp-interface-sensitive**

**undo ibgp-interface-sensitive**


Parameters
----------

None

Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the **ibgp-interface-sensitive** command is not run and a local interface on which a direct IBGP peer relationship is established fails, the system deletes the IBGP peer relationship only when the hold timer expires, which delays route switching. To address this problem, run the **ibgp-interface-sensitive** command to enable BGP to delete the direct IBGP peer relationship established on a local interface upon a failure of the interface.

**Precautions**



If a local interface on which a direct IBGP peer relationship is established alternates between Up and Down, do not run the **ibgp-interface-sensitive** command; otherwise, route flapping may occur.The command enables BGP to quickly respond to failures of a local interface on which a direct IBGP peer relationship is established but does not enable BGP to quickly respond to recovery of the interface. After the interface recovers, BGP uses its state machine to restore the relevant session.




Example
-------

# Enable BGP to delete the direct IBGP peer relationship established on a local interface upon a failure of the interface.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] ibgp-interface-sensitive

```