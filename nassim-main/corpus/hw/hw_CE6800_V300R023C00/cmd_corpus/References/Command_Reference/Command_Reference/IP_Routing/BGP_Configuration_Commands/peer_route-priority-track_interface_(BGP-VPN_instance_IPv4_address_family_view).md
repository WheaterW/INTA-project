peer route-priority-track interface (BGP-VPN instance IPv4 address family view)
===============================================================================

peer route-priority-track interface (BGP-VPN instance IPv4 address family view)

Function
--------



The **peer route-priority-track interface** command configures BGP to detect the status changes of an Eth-Trunk interface connected to a specified peer and adjust the priority of BGP routes received from the peer accordingly.

The **undo peer route-priority-track interfac**e command restores the default configuration.



By default, BGP does not detect the status changes of an Eth-Trunk interface connected to a peer or adjust the priority of BGP routes received from a peer.


Format
------

**peer** *peerIpv4Addr* **route-priority-track** **interface** { *interface-name* | *localIfType* *localIfNum* }

**undo peer** *peerIpv4Addr* **route-priority-track** **interface** { *interface-name* | *localIfType* *localIfNum* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a BGP peer. | The value is in dotted decimal notation. |
| *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *localIfType* | Specifies the type of an interface. | - |
| *localIfNum* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

BGP-VPN instance IPv4 address family view


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
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] q
[*HUAWEI-vpn-instance-vpn1] q
[*HUAWEI] interface Eth-Trunk 0
[*HUAWEI-Eth-Trunk0] q
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] peer 10.1.1.2 as-number 100
[*HUAWEI-bgp-vpn1] peer 10.1.1.2 route-priority-track interface Eth-Trunk 0

```