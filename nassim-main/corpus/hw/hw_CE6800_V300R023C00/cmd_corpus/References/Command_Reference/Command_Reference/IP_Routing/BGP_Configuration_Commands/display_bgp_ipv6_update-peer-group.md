display bgp ipv6 update-peer-group
==================================

display bgp ipv6 update-peer-group

Function
--------



The **display bgp ipv6 update-peer-group** command displays information about update peer-groups.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 update-peer-group** [ **index** *update-group-index* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **index** *update-group-index* | Specifies the index of an update peer-group. | The value is an integer ranging from 0 to 65535. |
| **ipv6** | Displays information about IPv6 BGP update peer-groups. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp ipv6 update-peer-group** command is used to view information about all the update peer-groups in the IPv6 unicast address family on the public network.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all the update peer-groups in the IPv6 unicast address family on the public network.
```
<HUAWEI> display bgp ipv6 update-peer-group index 1
  Group ID : 1
  BGP Version : 4
  Group Type : internal 
  Addr Family : IPv6-UNC
  AdvMinTimeVal : 15
  Total Peers : 1
  Leader Peer : 2001:DB8:1:1::1:2 
  Total format packet number : 0
  Total send packet number : 0
  Total replicate packet number : 0 
  The replication percentages(%) : 0
  Peers List : 2001:DB8:1:1::1:2

```

**Table 1** Description of the **display bgp ipv6 update-peer-group** command output
| Item | Description |
| --- | --- |
| Group ID | Update group ID of the BGP peer. |
| Group Type | Type of an update peer-group:   * external: EBGP. * internal: IBGP. * unknown: unknown type. |
| BGP Version | BGP version. |
| Addr Family | Address family. |
| AdvMinTimeVal | Minimum interval at which Update messages with the same route prefix are sent. |
| Total Peers | Indicates the total number of peers in an update-group. |
| Total format packet number | Total format packet number. |
| Total send packet number | Total number of sent packets. |
| Total replicate packet number | Number of replicated packets. The value equals the total number of sent packets minus the total number of packets. |
| Peers List | List of peers. |
| Leader Peer | IP addresses of peers in an update peer-group. |
| The replication percentages(%) | Replication percentage: (Total number of sent packets - Total number of formatted packets) x 100/Total number of formatted packets. |