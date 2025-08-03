peer capability-advertise orf ip-prefix (BGP-IPv4 unicast address family view)
==============================================================================

peer capability-advertise orf ip-prefix (BGP-IPv4 unicast address family view)

Function
--------



The **peer capability-advertise orf ip-prefix** command configures a BGP device to advertise the prefix-based ORF capability to its peer.

The **undo peer capability-advertise orf ip-prefix** command cancels the configuration.



By default, a BGP device is not configured to advertise the prefix-based ORF capability to its peer.


Format
------

**peer** *ipv4-address* **capability-advertise** **orf** **ip-prefix** { **both** | **receive** | **send** }

**peer** *ipv4-address* **capability-advertise** **orf** **non-standard-compatible** **ip-prefix** { **both** | **receive** | **send** }

**undo peer** *ipv4-address* **capability-advertise** **orf** **ip-prefix** { **both** | **receive** | **send** }

**undo peer** *ipv4-address* **capability-advertise** **orf** **non-standard-compatible** **ip-prefix** { **both** | **receive** | **send** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in the dotted decimal format. |
| **both** | Indicates that a peer is allowed to send and receive ORF packets. | - |
| **receive** | Indicates that a peer is allowed only to receive ORF packets. | - |
| **send** | Indicates that a peer is allowed only to send ORF packets. | - |
| **non-standard-compatible** | Indicates that ORF supported by Huawei devices is compatible with that supported by a non-Huawei device. | - |



Views
-----

BGP-IPv4 unicast address family view,BGP view


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
[*HUAWEI-bgp] peer 10.11.11.1 as-number 200
[*HUAWEI-bgp] peer 10.11.11.1 capability-advertise orf ip-prefix both

```