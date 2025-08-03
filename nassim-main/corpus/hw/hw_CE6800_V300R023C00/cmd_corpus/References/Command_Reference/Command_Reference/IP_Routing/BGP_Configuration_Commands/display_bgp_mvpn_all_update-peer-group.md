display bgp mvpn all update-peer-group
======================================

display bgp mvpn all update-peer-group

Function
--------



The **display bgp mvpn all update-peer-group** command displays information about update peer-groups.




Format
------

**display bgp mvpn all update-peer-group** [ **index** *update-group-index* ]


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

The display bgp mvpn all update-peer-group verbose slave command displays details about update peer-groups of BGP components in the current system.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about MVPN BGP update peer-groups.
```
<HUAWEI> display bgp mvpn all update-peer-group

  The MVPN instance's update peer group number : 1
  Keep buffer update peer group number : 0
  BGP Version : 4

  Group ID : 2
  Group Type : internal
  Addr Family : IPv4-MVPN
  AdvMinTimeVal : 15
  Total Peers : 2
  Leader Peer : 3.3.3.3
  Peers List : 3.3.3.3    4.4.4.4

```

**Table 1** Description of the **display bgp mvpn all update-peer-group** command output
| Item | Description |
| --- | --- |
| The MVPN instance's update peer group number | Number of update peer-groups in an instance. |
| Keep buffer update peer group number | Number of update peer-groups stored in the batch buffer. |
| BGP Version | BGP version. |
| Group Type | Type of an update peer-group. |
| Group ID | Update group ID of the BGP peer. |
| Addr Family | Address family. |
| AdvMinTimeVal | Minimum interval at which Update messages with the same route prefix are sent. |
| Total Peers | Indicates the total number of peers in an update-group. |
| Peers List | List of peers. |
| Leader Peer | IP addresses of peers in an update peer-group. |