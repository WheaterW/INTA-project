display bgp evpn update-peer-group
==================================

display bgp evpn update-peer-group

Function
--------



The **display bgp evpn update-peer-group** command displays information about update peer-groups of BGP EVPN routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp evpn update-peer-group** [ **index** *update-group-index* ]

**display bgp** [ **instance** *instance-name* ] **evpn** **update-peer-group** [ **index** *update-group-index* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **index** *update-group-index* | Specifies the index of an update peer-group. | The value is an integer ranging from 0 to 65535. |
| **instance** *instance-name* | Specifies the name of a BGP instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command is used to view information about the update peer-group in the BGP-EVPN address family.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the update peer-groups in a BGP-EVPN address family.
```
<HUAWEI> display bgp evpn update-peer-group
  The EVPN instance's update peer group number : 1
  Keep buffer update peer group number : 0
  BGP Version : 4
  Group ID : 1
  Group Type : internal 
  Addr Family : EVPN  AdvMinTimeVal : 0
  Total Peers : 1
  Leader Peer : 10.44.44.88

```

**Table 1** Description of the **display bgp evpn update-peer-group** command output
| Item | Description |
| --- | --- |
| The EVPN instance's update peer group number | Number of update peer-groups in the EVPN instance. |
| Keep buffer update peer group number | Number of update peer-groups stored in the buffer. |
| BGP Version | BGP version. |
| Group ID | ID of an update peer-group. |
| Group Type | Type of an update peer-group:   * external: indicates an EBGP peer update peer-group. * internal: indicates an IBGP peer update peer-group. * unknown: indicates an unknown update peer-group. |
| Addr Family | Address family. |
| AdvMinTimeVal | Minimum interval at which Update messages with the same route prefix are sent. |
| Total Peers | Total number of peers in an update peer-group. |
| Leader Peer | Representative of an update peer-group. |