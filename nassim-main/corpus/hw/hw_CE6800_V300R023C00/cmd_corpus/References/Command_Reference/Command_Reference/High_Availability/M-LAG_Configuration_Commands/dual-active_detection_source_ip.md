dual-active detection source ip
===============================

dual-active detection source ip

Function
--------



The **dual-active detection source ip** command binds an IPv4 address to a DFS group.

The **undo dual-active detection source ip** command unbinds an IPv4 address from a DFS group.



By default, a DFS group is not bound to any IPv4 address.


Format
------

**dual-active detection source ip** *ipv4-address1* [ **peer** *ipv4-address2* [ **udp-port** *portnum* ] ] [ **timeout** *seconds* ]

**undo dual-active detection source ip** *ipv4-address1* [ [ **peer** *ipv4-address2* [ **udp-port** *portnum* ] ] [ **timeout** *seconds* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *ipv4-address2* | Specifies the peer device's IPv4 address bound to a DFS group. | The value is in dotted decimal notation. |
| **udp-port** *portnum* | Specifies the UDP port number bound to a DFS group. | The value is an integer that ranges from 1025 to 2048. The default value is the smallest idle port number between 1025 and 2048. |
| **timeout** *seconds* | Specifies the timeout duration. | The value is an integer ranging from 3 to 60, in seconds. The default value is 45. |
| **ip** *ipv4-address1* | Specifies the IPv4 address bound to a DFS group. | The value is in dotted decimal notation. |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a CE is dual-homed to two PEs on an Ethernet, VXLAN, or IP network, to enable PEs to exchange heartbeat packets, DFS groups need to be bound to IP addresses of Layer 3 interfaces connecting the two PEs. If the CE connects to a VPN, you must specify the VPN instance bound to the DFS group.Assume that the heartbeat IP address and UDP port number of the peer device are specified when the heartbeat IP address bound to a DFS group is configured. When the configuration takes effect, the two M-LAG devices immediately start to send and receive heartbeat packets and negotiate the HB DFS master/backup status. In scenarios where enhanced DAD for secondary faults is enabled, if faults on the original DFS master device are rectified and the peer-link fault persists, the corresponding interfaces on the backup device are triggered to enter the Error-Down state based on the HB DFS master/backup status. This mechanism prevents abnormal traffic forwarding in the scenario where two master devices exist and improves device reliability.

**Prerequisites**

Create a DFS group and manually configure an IPv4 address.

**Precautions**

* Either the dual-active detection source ip or dual-active detection source ipv6 command can be configured. They cannot be configured together.
* The UDP port number of the local device must be the same as that of the peer device. To prevent a UDP port number conflict, you are advised to manually configure the UDP port number.
* The IPv4 addresses of the local and peer devices bound to a DFS group must be different. In addition, the IPv4 addresses cannot be non-class A, B, or C addresses or loopback addresses.
* When binding an IP address to a DFS group, you are advised to configure the peer *ipv4-address*parameter. Otherwise, the enhanced DAD for double-fault failures function does not take effect.

Example
-------

# Bind an IPv4 address to a DFS group.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] dual-active detection source ip 10.1.0.3 peer 10.1.0.4 udp-port 2048 timeout 30

```