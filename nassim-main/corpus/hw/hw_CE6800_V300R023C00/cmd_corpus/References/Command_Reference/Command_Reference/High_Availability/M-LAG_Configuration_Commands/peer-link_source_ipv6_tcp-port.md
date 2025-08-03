peer-link source ipv6 tcp-port
==============================

peer-link source ipv6 tcp-port

Function
--------



The **peer-link source ipv6 tcp-port** command specifies the IPv6 address bound to the TCP channel for M-LAG synchronization packets.

The **undo peer-link source ipv6 tcp-port** command cancels the IPv6 address bound to the TCP channel for M-LAG synchronization packets.



By default, no TCP link channel is configured for M-LAG synchronization packets.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer-link source ipv6** *ipv6-address1* [ **vpn-instance** *vpnname* ] **peer** *ipv6-address2* **tcp-port** *portnum*

**undo peer-link source ipv6** *ipv6-address1* [ **vpn-instance** *vpnname* ] **peer** *ipv6-address2* **tcp-port** *portnum*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address1* | Specifies the local IPv6 address bound to M-LAG synchronization packets. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **vpn-instance** *vpnname* | Specifies the VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. |
| **peer** *ipv6-address2* | Specifies the local IPv6 address bound to M-LAG synchronization packets. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *portnum* | Specifies the destination TCP port number of M-LAG synchronization packets. | The value is an integer that ranges from 1 to 65535. The port number must not be well-known or used by other modules already. |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To improve M-LAG synchronization reliability when a device is dual-homed to a common Ethernet, VXLAN, or IPv6 network through an M-LAG, you need to bind the IPv6 addresses and TCP port numbers of the Layer 3 interfaces on the two M-LAG devices to a TCP channel. This is used only for ARP/ND entry synchronization between the two M-LAG devices.

**Precautions**

Either the peer-link source ipv6 tcp-port or peer-link source ip tcp-port command can be configured. They cannot be configured together. The TCP port number of the local device must be the same as that of the peer device. The IPv6 addresses of the local and remote devices bound to the channel for M-LAG synchronization packets cannot be the same, and cannot be set to link-local addresses, multicast addresses, unspecified addresses, or loopback addresses.


Example
-------

# Set the source IPv6 address to 2001:db8:1::1, the peer IPv6 address to 2001:db8:1::2, and the TCP port number to 2048 for M-LAG synchronization on the peer-link interface.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[~HUAWEI-dfs-group-1] peer-link source ipv6 2001:db8:1::1 peer 2001:db8:1::2 tcp-port 2048

```