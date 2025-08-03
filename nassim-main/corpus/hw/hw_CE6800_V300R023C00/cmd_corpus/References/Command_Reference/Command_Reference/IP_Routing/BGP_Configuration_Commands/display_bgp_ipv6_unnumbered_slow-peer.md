display bgp ipv6 unnumbered slow-peer
=====================================

display bgp ipv6 unnumbered slow-peer

Function
--------



The **display bgp ipv6 unnumbered slow-peer** command displays information about unnumbered slow BGP peers.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 unnumbered slow-peer**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check information about unnumbered slow BGP peers after enabling detection of unnumbered slow BGP peers, run the **display bgp ipv6 unnumbered slow-peer** command. The output includes the time when a peer began to be identified as a slow peer, the time when a peer last exited the slow peer state, the number of times a peer has been identified as a slow peer, and the remaining time for a peer to exit the slow peer state.

**Precautions**

The **display bgp ipv6 unnumbered slow-peer** command displays only information about slow BGP peers in the IPv6 unicast address family.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about slow BGP peers of the unnumbered type.
```
<HUAWEI> display bgp ipv6 unnumbered slow-peer

 Total number of peers : 6
 Switchback detection timer: Remaining 239 Second(s)

  Peer                             LastSlowEndTime             SlowStartTime               SlowCount   Interface
  FE80::3AA0:16FF:FE61:402         2021-09-15 02:55:20+00:00   2021-09-15 02:51:42+00:00   1           100GE1/0/1
  FE80::3AA0:16FF:FE61:1200        2021-09-15 02:55:20+00:00   2021-09-15 02:51:42+00:00   1           Vlanif4089
  FE80::3AA0:16FF:FE61:1200        2021-09-15 02:55:20+00:00   2021-09-15 02:51:42+00:00   1           Vlanif4090
  FE80::3AA0:16FF:FE21:1200        2021-09-15 02:59:50+00:00   2021-09-15 02:56:10+00:00   1           Eth-Trunk1
  FE80::3AA0:16FF:FE41:301         2021-09-15 02:28:04+00:00   2021-07-24 07:20:42+00:00   1           100GE1/0/2.10
  FE80::3AA0:16FF:FE41:301         2021-09-15 02:28:08+00:00   2021-07-24 07:20:42+00:00   1           100GE1/0/2.11

```

**Table 1** Description of the **display bgp ipv6 unnumbered slow-peer** command output
| Item | Description |
| --- | --- |
| Total number of peers | Number of slow peers. |
| Switchback detection timer | Remaining time for a peer to exit the slow peer state. |
| Peer | Peer IP address. |
| LastSlowEndTime | Time when a peer last exited the slow peer state. |
| SlowStartTime | Time when a peer began to be identified as a slow peer. |
| SlowCount | Number of times a peer has been identified as a slow peer. |
| Interface | Unnumbered interface. |