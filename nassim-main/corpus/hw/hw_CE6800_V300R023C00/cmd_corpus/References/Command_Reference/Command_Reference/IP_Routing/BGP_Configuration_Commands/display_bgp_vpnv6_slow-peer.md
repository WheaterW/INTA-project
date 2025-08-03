display bgp vpnv6 slow-peer
===========================

display bgp vpnv6 slow-peer

Function
--------



The **display bgp vpnv6 slow-peer** command displays information about slow BGP VPNv6 peers.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **slow-peer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv6 slow-peer** command displays information about slow BGP VPNv6 peers.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about slow BGP VPNv6 peers.
```
<HUAWEI> display bgp vpnv6 vpn-instance vpn1 slow-peer
 Total number of peers : 2                 
 Switchback detection timer: Remaining 3581 Second(s)
  Peer            LastSlowEndTime              SlowStartTime                SlowCount
  2001:DB8:1::2   2019-09-15 20:41:33+00:00    2019-09-16 00:02:33+00:00            3
  2001:DB8:1::3   2019-09-15 23:02:40+00:00    2019-09-16 00:02:40+00:00            5

```

**Table 1** Description of the **display bgp vpnv6 slow-peer** command output
| Item | Description |
| --- | --- |
| Total number of peers | Number of slow peers. |
| Switchback detection timer | Remaining time of the slow peer switchback timer. |
| Peer | Peer address. |
| LastSlowEndTime | Time when a peer last exits the slow peer state. |
| SlowStartTime | Time when a slow peer is detected. |
| SlowCount | Number of times a peer is identified as a slow peer. |