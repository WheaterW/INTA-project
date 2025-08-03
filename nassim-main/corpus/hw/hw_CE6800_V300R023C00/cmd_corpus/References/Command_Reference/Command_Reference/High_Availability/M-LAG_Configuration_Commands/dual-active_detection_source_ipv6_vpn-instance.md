dual-active detection source ipv6 vpn-instance
==============================================

dual-active detection source ipv6 vpn-instance

Function
--------



The **dual-active detection source ipv6 vpn-instance** command configures an IPv6 address bound to a VPN instance.

The **undo dual-active detection source ipv6 vpn-instance** command cancels the configured IPv6 address bound to a VPN instance.



By default, no IPv6 address bound to a VPN instance is configured in a DFS group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dual-active detection source ipv6** *ipv6address1* **vpn-instance** *vpnname* [ **peer** *ipv6address2* [ **udp-port** *portnum* ] ] [ **timeout** *seconds* ]

**undo dual-active detection source ipv6** *ipv6address1* **vpn-instance** [ *vpnname* [ **peer** *ipv6address2* [ **udp-port** *portnum* ] ] [ **timeout** *seconds* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpnname* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. |
| **peer** *ipv6address2* | Binds the peer IPv6 address. | The value is a 32-digit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **udp-port** *portnum* | Specifies a UDP port number. | The value is an integer that ranges from 1025 to 2048. The default value is the smallest idle port number between 1025 and 2048. |
| **timeout** *seconds* | Specifies the timeout duration. | The value is an integer ranging from 3 to 60, in seconds. The default value is 45. |
| **ipv6** *ipv6address1* | Binds the source IPv6 address. | The value is a 32-digit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a CE is dual-homed to two PEs on an Ethernet, VXLAN, or IP network, to enable PEs to exchange heartbeat packets, DFS groups need to be bound to IP addresses of Layer 3 interfaces connecting the two PEs. If the IP network uses IPv6 addresses, a DFS group needs to be bound to an IPv6 address. If the CE connects to a VPN, you must specify the VPN instance bound to a DFS group.Assume that the heartbeat IP address and UDP port number of the peer device are specified when the heartbeat IP address bound to a DFS group is configured. When the configuration takes effect, the two M-LAG devices immediately start to send and receive heartbeat packets and negotiate the HB DFS master/backup status. In scenarios where enhanced DAD for secondary faults is enabled, if faults on the original DFS master device are rectified and the peer-link fault persists, the corresponding interfaces on the backup device are triggered to enter the Error-Down state based on the HB DFS master/backup status. This mechanism prevents abnormal traffic forwarding in the scenario where two master devices exist and improves device reliability.

**Precautions**

* Either the dual-active detection source ip vpn-instance or dual-active detection source ipv6 vpn-instance command can be configured. They cannot be configured together.
* The UDP port number of the local device must be the same as that of the peer device. To prevent a UDP port number conflict, you are advised to manually configure the UDP port number.
* The IPv6 addresses of the local and peer devices bound to a VPN instance must be different. In addition, the IPv6 addresses cannot be link-local addresses, multicast addresses, unspecified addresses, or loopback addresses.
* When binding an IP address to a DFS group, you are advised to configure the peer *ipv6address*parameter. Otherwise, the enhanced DAD for double-fault failures function does not take effect.

Example
-------

# Configure an IPv6 address bound to a VPN instance.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance 234
[*HUAWEI-vpn-instance-234] quit
[*HUAWEI] dfs-group 1
[~HUAWEI-dfs-group-1] dual-active detection source ipv6 2001:db8:1::1 vpn-instance 234 peer 2001:db8:1::2 udp-port 2048 timeout 30

```