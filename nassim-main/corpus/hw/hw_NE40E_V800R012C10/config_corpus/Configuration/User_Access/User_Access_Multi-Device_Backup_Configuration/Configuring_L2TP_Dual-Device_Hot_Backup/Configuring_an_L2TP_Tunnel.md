Configuring an L2TP Tunnel
==========================

An L2TP tunnel can be used to provide access services for enterprises, small ISPs, and the staff on business trips over a public network.

#### Context

For details, see [L2TP Access Configuration](dc_ne_l2tp_cfg_013681.html) in the *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - User Access*.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The preference of the route from an LNS to the master LAC must be higher than that of the route from the LNS to the backup LAC. The LNS will switch traffic
to the route destined for the backup LAC only if a fault occurs on the network side of the master LAC.


![](../../../../public_sys-resources/notice_3.0-en-us.png) 

In L2TP dual-device hot backup scenarios, when an L2TP tunnel is established on an L3VPN and URPF is configured on the LACs' network side, if the master LAC's access side fails, downstream traffic packets are discarded on the backup LAC.