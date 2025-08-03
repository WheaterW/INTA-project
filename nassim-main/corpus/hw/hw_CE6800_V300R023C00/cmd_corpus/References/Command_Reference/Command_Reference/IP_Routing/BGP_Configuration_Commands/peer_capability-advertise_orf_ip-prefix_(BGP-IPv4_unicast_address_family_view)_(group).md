peer capability-advertise orf ip-prefix (BGP-IPv4 unicast address family view) (group)
======================================================================================

peer capability-advertise orf ip-prefix (BGP-IPv4 unicast address family view) (group)

Function
--------



The **peer capability-advertise orf ip-prefix** command configures a BGP device to advertise the prefix-based ORF capability to its peer group.

The **undo peer capability-advertise orf ip-prefix** command cancels the configuration.



By default, a BGP device is not configured to advertise the prefix-based ORF capability to its peer group.


Format
------

**peer** *group-name* **capability-advertise** **orf** **ip-prefix** { **both** | **receive** | **send** }

**peer** *group-name* **capability-advertise** **orf** **non-standard-compatible** **ip-prefix** { **both** | **receive** | **send** }

**undo peer** *group-name* **capability-advertise** **orf** **ip-prefix** { **both** | **receive** | **send** }

**undo peer** *group-name* **capability-advertise** **orf** **non-standard-compatible** **ip-prefix** { **both** | **receive** | **send** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **both** | Allows the device to send and receive ORF messages. | - |
| **receive** | Allows the device only to receive ORF messages. | - |
| **send** | Allows the device only to send ORF messages. | - |
| **non-standard-compatible** | Indicates that the device is compatible with the devices of other vendors. | - |



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

# Configure a BGP device to advertise the prefix-based ORF capability to its peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test capability-advertise orf ip-prefix both

```