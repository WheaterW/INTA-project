display bgp vpn-target update-peer-group
========================================

display bgp vpn-target update-peer-group

Function
--------



The **display bgp vpn-target update-peer-group** command displays information about update peer-groups in the BGP-VPN-Target address family.




Format
------

**display bgp vpn-target update-peer-group** [ **index** *update-group-index* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **index** *update-group-index* | Specifies the index of an update peer-group. | The value is an integer ranging from 0 to 65535. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



Details about update peer-groups can be displayed based on the update peer-group index.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about an update peer-group with a specified index in the BGP-VPN-Target address family.
```
<HUAWEI> display bgp vpn-target update-peer-group index 0
 Group ID : 0
 BGP Version : 4
 Group Type : internal
 Addr Family : BGP-VT
 Total Peers : 1
 AdvMinTimeVal : 30
 Leader Peer : 192.168.1.2

 Total format packet number : 3
 Total send packet number : 3
 Total replicate packet number : 0
 The replication percentages(%) : 0

 Peers List : 192.168.1.2

```

**Table 1** Description of the **display bgp vpn-target update-peer-group** command output
| Item | Description |
| --- | --- |
| Group ID | ID of an update peer-group. |
| Group Type | Type of an update peer-group:   * external: indicates an EBGP peer update peer-group. * internal: indicates an IBGP peer update peer-group. * unknown: indicates an unknown update peer-group. |
| BGP Version | BGP version. |
| Addr Family | Address family. |
| Total Peers | Total number of peers in an update peer-group. |
| Total format packet number | Total number of formatted packets. |
| Total send packet number | Total number of sent packets. |
| Total replicate packet number | Total number of sent packets - Total number of formatted packets. |
| Peers List | List of peers. |
| AdvMinTimeVal | Minimum interval at which Update messages with the same route prefix are sent. |
| Leader Peer | Representative of an update peer-group. |
| The replication percentages(%) | Replication percentage: (Total number of sent packets - Total number of formatted packets) x 100/Total number of formatted packets. |