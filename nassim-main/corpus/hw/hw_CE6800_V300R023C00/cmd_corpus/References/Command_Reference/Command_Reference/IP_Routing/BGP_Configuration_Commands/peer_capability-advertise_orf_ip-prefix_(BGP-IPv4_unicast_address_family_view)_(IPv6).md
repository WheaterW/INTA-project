peer capability-advertise orf ip-prefix (BGP-IPv4 unicast address family view) (IPv6)
=====================================================================================

peer capability-advertise orf ip-prefix (BGP-IPv4 unicast address family view) (IPv6)

Function
--------



The **peer capability-advertise orf ip-prefix** command configures a BGP device to advertise the prefix-based ORF capability to its peer.

The **undo peer capability-advertise orf ip-prefix** command cancels the configuration.



By default, a BGP device is not configured to advertise the prefix-based ORF capability to its peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **capability-advertise** **orf** **ip-prefix** { **both** | **receive** | **send** }

**peer** *peerIpv6Addr* **capability-advertise** **orf** **non-standard-compatible** **ip-prefix** { **both** | **receive** | **send** }

**undo peer** *peerIpv6Addr* **capability-advertise** **orf** **ip-prefix** { **both** | **receive** | **send** }

**undo peer** *peerIpv6Addr* **capability-advertise** **orf** **non-standard-compatible** **ip-prefix** { **both** | **receive** | **send** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a BGP peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **both** | Indicates that a peer is allowed to send and receive ORF packets. | - |
| **receive** | Indicates that a peer is allowed only to receive ORF packets. | - |
| **send** | Indicates that a peer is allowed only to send ORF packets. | - |
| **non-standard-compatible** | Indicates that ORF supported by Huawei devices is compatible with that supported by a non-Huawei device. | - |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The outbound route filtering (ORF) function uses the import policy of the peer as the export policy of the local end to filter the routes to be sent. The routes that do not comply with the import policy of the peer are not sent to the peer.Users want the carrier to send only the required routes, but the carrier does not want to maintain different export policies for each user. Against this backdrop, the ORF feature can meet the requirements of customers and carriers. ORF supports on-demand route advertisement, which reduces bandwidth consumption and configuration workload.

**Precautions**

Enabling or disabling the ORF capability of a peer causes the BGP peer relationship to be disconnected and re-established.


Example
-------

# Configure a BGP device to advertise the prefix-based ORF capability to its peer or peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer FE80::1 as-number 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer FE80::1 enable
[*HUAWEI-bgp-af-ipv4] peer FE80::1 capability-advertise orf ip-prefix both

```