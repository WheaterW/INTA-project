peer oscillation-dampening (BGP multi-instance view)
====================================================

peer oscillation-dampening (BGP multi-instance view)

Function
--------



The **peer oscillation-dampening** command enables BGP to suppress the establishment of a specified peer relationship that flaps continuously.

The **peer oscillation-dampening disable** command disables BGP from suppressing the establishment of a specified peer relationship that flaps continuously.

The **undo peer oscillation-dampening** command deletes the configuration of enabling the suppression function for a specified peer.

The **undo peer oscillation-dampening disable** command deletes the configuration of disabling the suppression function for a specified peer.



By default, BGP suppresses the establishment of a BGP peer relationship that flaps continuously.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *peerIpv4Addr* | *ipv6-address* } **oscillation-dampening**

**peer** { *peerIpv4Addr* | *ipv6-address* } **oscillation-dampening** **disable**

**undo peer** { *peerIpv4Addr* | *ipv6-address* } **oscillation-dampening**

**undo peer** { *peerIpv4Addr* | *ipv6-address* } **oscillation-dampening** **disable**

For CE6885-LL (low latency mode):

**peer** *peerIpv4Addr* **oscillation-dampening**

**peer** *peerIpv4Addr* **oscillation-dampening** **disable**

**undo peer** *peerIpv4Addr* **oscillation-dampening**

**undo peer** *peerIpv4Addr* **oscillation-dampening** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *peerIpv4Addr* | Specifies the IPv4 address of a BGP peer. | The value is in dotted decimal notation. |
| **peer** *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a BGP peer relationship is established, the local device learns all routes from the peer and also advertises its local routes to the peer. If the peer relationship is disconnected, the local device deletes all the routes learned from the peer.Generally, a large number of BGP routes exist, and in this case, a large number of routes change and a large amount of data is processed when the BGP peer relationship is flapping. As a result, a high volume of resources are consumed, causing high CPU usage. To prevent high CPU usage in this case, BGP needs to be enabled to suppress the establishment of the peer relationship if it flaps continuously. Such suppression is implemented for a BGP peer relationship that flaps for more than five times consecutively, and the suppression period increases as the number of flapping times increases. You can run the **display bgp peer verbose** command to check the remaining time that BGP waits to establish the BGP peer relationship.After the peer relationship stops flapping for a certain period, suppression on the peer relationship establishment is automatically removed. To immediately remove the suppression, you can run the **peer oscillation-dampening disable** command. Alternatively, you can run a **reset** command or another command that can cause the peer relationship to be disconnected and re-established.

**Precautions**

By default, the initial time that the device waits to establish a peer relationship is 10s. If the **peer timer connect-retry** command is run, the configured ConnectRetry interval is used as the initial waiting time.If peer dampening is configured and the initial time of waiting for peer relationship establishment is less than 600s, the actual time that the device waits to establish the peer relationship equals the initial waiting time plus the dampening period. The dampening time increases with the number of flapping times until the waiting time for establishing a peer relationship reaches 600s.If the peer oscillation-dampening [ disable ] command is run on the local peer and the specified peer is added to the peer group, the configuration of the peer takes precedence over the configuration of the peer group.If the peer oscillation-dampening [ disable ] command is not run on a local peer, the peer inherits the configurations of the peer group after being added to the peer group, and retains the configurations of the peer group even after being removed from the peer group.


Example
-------

# Enable BGP to suppress the establishment of a specified peer relationship that flaps continuously.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] peer 10.1.1.1 as-number 200
[*HUAWEI-bgp-instance-a] peer 10.1.1.1 oscillation-dampening

```