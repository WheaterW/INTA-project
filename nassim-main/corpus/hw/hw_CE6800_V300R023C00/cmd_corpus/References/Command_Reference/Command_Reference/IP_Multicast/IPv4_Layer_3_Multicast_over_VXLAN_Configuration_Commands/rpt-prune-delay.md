rpt-prune-delay
===============

rpt-prune-delay

Function
--------



The **rpt-prune-delay** command configures the pruning delay time when the RPT switches to SPT in the NG MVPN sharing tree scenario.

The **undo rpt-prune-delay** command restores the default configuration.



By default, the pruning delay time is 60 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**rpt-prune-delay** *delay-time*

**undo rpt-prune-delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delay-time* | Configures the RPT pruning delay time. | The value is an integer ranging from 0 to 1800, in seconds. |



Views
-----

VPN instance IPv4 address family MVPN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In the NG MVPN sharing tree scenario, when the RPT switches to the SPT, the root PE of RPT prunes the received BGP source-active routes. To delay the pruning, run the rpt-prune-delay command.

**Configuration Impact**

If the rpt-prune-delay command is run several times, the latest configuration overrides the previous one.

**Precautions**

The pruning delay time configured using the rpt-prune-delay command takes effect on next RPT-SPT switching.

The command can be only configured on the root PE of an RPT.


Example
-------

# Configure the pruning delay time to 120 seconds for the VPN instance mcast1.
```
<HUAWEI> system-view
[~HUAWEI] multicast mvpn 2.2.2.2
[*HUAWEI] ip vpn-instance mcast1
[*HUAWEI-vpn-instance-mcast1] ipv4-family
[*HUAWEI-vpn-instance-mcast1-af-ipv4] route-distinguisher 100:200
[*HUAWEI-vpn-instance-mcast1-af-ipv4] multicast routing-enable
[*HUAWEI-vpn-instance-mcast1-af-ipv4] mvpn
[*HUAWEI-vpn-instance-mcast1-af-ipv4-mvpn] rpt-prune-delay 120

```