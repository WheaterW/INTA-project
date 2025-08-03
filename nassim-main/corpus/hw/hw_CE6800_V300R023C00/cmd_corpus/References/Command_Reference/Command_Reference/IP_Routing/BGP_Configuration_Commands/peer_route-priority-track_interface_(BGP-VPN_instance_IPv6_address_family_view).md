peer route-priority-track interface (BGP-VPN instance IPv6 address family view)
===============================================================================

peer route-priority-track interface (BGP-VPN instance IPv6 address family view)

Function
--------



The **peer route-priority-track interface** command configures BGP to detect the status changes of an Eth-Trunk interface connected to a specified peer and adjust the priority of BGP routes received from the peer accordingly.

The **undo peer route-priority-track interfac**e command restores the default configuration.



By default, BGP does not detect the status changes of an Eth-Trunk interface connected to a peer or adjust the priority of BGP routes received from a peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **route-priority-track** **interface** { *interface-name* | *localIfType* *localIfNum* }

**undo peer** *peerIpv6Addr* **route-priority-track** **interface** { *interface-name* | *localIfType* *localIfNum* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format X:X:X:X:X:X:X:X. |
| *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *localIfType* | Specifies an interface type. | - |
| *localIfNum* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In BGP over M-LAG networking, you can run this command on the M-LAG device. When the M-LAG member interface pointing to the peer fails (if there are multiple member interfaces between the M-LAG and the peer, the M-LAG considers that the peer fails only when all interfaces fail): After detecting the status change of the member interface, BGP adjusts the priority of the route received from the specified peer to the lowest (the MED is adjusted to the maximum value and the Local\_Pref is adjusted to the minimum value).After BGP is configured to detect the Eth-Trunk interface status and adjust the route priority, BGP adjusts the priority of the route received from the specified peer to the lowest (the MED is adjusted to the maximum value and the Local\_Pref is adjusted to the minimum value) after detecting the interface status change.



**Precautions**

Each BGP peer can be bound to a maximum of four Eth-Trunk interfaces.The priority of this command is higher than that of the peer route-policy or peer route-filter command. If both commands are configured, this command takes effect when the link is faulty.By default, an interface on a device is a Layer 3 interface. After you run the **peer route-priority-track interface** command to specify an interface, changing the interface type to Layer 2 may affect Layer 3 services. Therefore, exercise caution when changing the interface type.


Example
-------

# Configure BGP to detect the status changes of an Eth-Trunk interface connected to a specified peer and adjust the priority of BGP routes received from the peer accordingly.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 as-number 200
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 route-priority-track interface Eth-Trunk 0

```