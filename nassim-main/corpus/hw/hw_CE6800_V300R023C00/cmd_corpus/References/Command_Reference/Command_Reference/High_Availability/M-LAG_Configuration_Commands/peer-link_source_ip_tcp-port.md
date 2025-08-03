peer-link source ip tcp-port
============================

peer-link source ip tcp-port

Function
--------



The **peer-link source ip tcp-port** command specifies the IP address bound to the TCP channel for M-LAG synchronization packets.

The **undo peer-link source ip tcp-port** command cancels the IP address bound to the TCP channel for M-LAG synchronization packets.



By default, no TCP link channel is configured for M-LAG synchronization packets.


Format
------

**peer-link source ip** *ipv4-address1* [ **vpn-instance** *vpnname* ] **peer** *ipv4-address2* **tcp-port** *portnum*

**undo peer-link source ip** *ipv4-address1* [ **vpn-instance** *vpnname* ] **peer** *ipv4-address2* **tcp-port** *portnum*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address1* | Specifies the local IP address bound to M-LAG synchronization packets. | The value is in dotted decimal notation. |
| **vpn-instance** *vpnname* | Specifies the VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. |
| **peer** *ipv4-address2* | Specifies the peer IP address of M-LAG synchronization packets. | The value is in dotted decimal notation. |
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

To improve M-LAG synchronization reliability when a device is dual-homed to a common Ethernet, VXLAN, or IP network through an M-LAG, you need to bind the IP addresses and TCP port numbers of the Layer 3 interfaces on the two M-LAG devices to a TCP channel. This is used only for ARP/ND entry synchronization between the two M-LAG devices.

**Precautions**

Either the peer-link source ip tcp-port or peer-link source ipv6 tcp-port command can be configured. They cannot be configured together. The TCP port number of the local device must be the same as that of the remote device. The IPv4 addresses of the local and remote devices bound to the channel for M-LAG synchronization packets must be different, and cannot be set to non-class A, B, or C addresses or loopback addresses.


Example
-------

# Set the source IPv4 address to 10.1.0.3, the peer IPv4 address to 10.1.0.4, and the TCP port number to 2048 for M-LAG synchronization on the peer-link interface.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[~HUAWEI-dfs-group-1] peer-link source ip 10.1.0.3 peer 10.1.0.4 tcp-port 2048

```