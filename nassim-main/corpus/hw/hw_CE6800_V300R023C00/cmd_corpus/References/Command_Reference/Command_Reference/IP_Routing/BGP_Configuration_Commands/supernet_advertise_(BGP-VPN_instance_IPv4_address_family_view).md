supernet advertise (BGP-VPN instance IPv4 address family view)
==============================================================

supernet advertise (BGP-VPN instance IPv4 address family view)

Function
--------



The **supernet advertise** command enables a device to advertise BGP supernet unicast routes to BGP peers.

The **undo supernet advertise** command restores the default configuration.



By default, BGP supernet unicast routes are considered invalid and are not advertised to peers or delivered to the IP routing table.


Format
------

**supernet unicast advertise enable**

**supernet unicast advertise disable**

**undo supernet unicast advertise enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **unicast** | Indicates supernet unicast routes. | - |
| **disable** | Disables the device from sending BGP supernet routes. | - |
| **enable** | Enables the device to send BGP supernet routes. | - |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A BGP supernet route has the same destination address and next hop address or has a more detailed destination address than the next hop address. Any route that meets either of the following conditions is a BGP supernet route:

* If bitwise AND operations are performed on the destination address mask with the destination address and next hop address, the two obtained network addresses are the same, and destination address mask is greater than or equal to the next hop address mask..
* If bitwise AND operations are performed on the destination address mask with the destination address and next hop address, the two obtained network addresses are different. If bitwise AND operations are performed on the next hop address mask with the destination address and next hop address, however, the two obtained network addresses are the same.BGP supernet routes include BGP supernet labeled routes and BGP supernet unicast routes. When a Huawei device connects to a non-Huawei device, to enable the Huawei device to advertise BGP supernet unicast routes received from the non-Huawei device to BGP peers, run the **supernet unicast advertise enable** command on the Huawei device.

**Precautions**

If the next hop to which a supernet route is recursed is also a BGP route, this command does not take effect.


Example
-------

# Configure a BGP device to advertise BGP supernet unicast routes to its peers.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] supernet unicast advertise enable

```

# Disable a BGP device from advertising labeled BGP supernet routes.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] supernet label-route advertise disable

```