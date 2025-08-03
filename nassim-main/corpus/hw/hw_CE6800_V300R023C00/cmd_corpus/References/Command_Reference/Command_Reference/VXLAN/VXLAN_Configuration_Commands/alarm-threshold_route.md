alarm-threshold route
=====================

alarm-threshold route

Function
--------



The **alarm-threshold route** command sets a threshold and log recovery percentage for the number of EVPN routes.

The **undo alarm-threshold route** command cancels the settings.



By default, the threshold and log recovery percentage for the number of EVPN routes are not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**alarm-threshold route** *route-number* [ **recovery-percentage** *percentage* ]

**undo alarm-threshold route** *route-number* [ **recovery-percentage** *percentage* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *route-number* | Specifies the threshold for the number of EVPN routes. | The value is an integer ranging from 1 to 4294967295. |
| **recovery-percentage** *percentage* | Specifies the log recovery percentage. | The value is an integer ranging from 1 to 95. After the threshold for the number of EVPN routes is set, the log recovery percentage is 80 by default. |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When a distributed VXLAN gateway is deployed, EVPN serves as the control plan to deliver routes. As more and more hosts access the gateway, routes stored on the control plane increase greatly, consuming a lot of memory resources. To better monitor the impact of an increase in route quantity on memory and prevent device restart caused by memory insufficiency, run the **alarm-threshold route** command to set a threshold for the number of routes. When the number of routes exceeds the threshold, a user log will be generated. When the number of routes equals the log recovery percentage, a recovery log will be generated.


Example
-------

# Set a threshold and log recovery percentage for the number of EVPN routes.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] alarm-threshold route 10000 recovery-percentage 90

```