Configuring the LDP GR Helper
=============================

You can configure a device to function as a GR Helper to help a neighbor with the LDP GR process.

#### Usage Scenario

In LDP GR, a Restarter, with the help of the Helper, ensures uninterrupted forwarding during an active main board (AMB)/standby main board (/SMB) switchover or when a protocol is restarted.

During an active/standby switchover or system upgrade, if GR is not enabled, the neighbor deletes the LSP because the session goes down. As a result, traffic and services are interrupted for a short time. In this case, you can configure LDP GR to ensure that labels remain unchanged before and after an unexpected active/standby switchover or protocol restart. In addition, you can restore the establishment of LDP sessions and LSPs after the active/standby switchover or system upgrade is complete. This ensures uninterrupted MPLS forwarding.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

LDP only supports the GR Helper.



#### Pre-configuration Tasks

Before configuring LDP GR, complete the following tasks:

* Configure IGP GR.
* Configure a local LDP session.


[Enabling LDP GR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0025.html)

Enable LDP GR on both the GR Restarter and its neighboring nodes

[(Optional) Configuring GR Helper Timers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0026.html)

Configuring GR Helper timers includes configuring the LDP session Reconnect timer and LSP Recovery timer.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0027.html)

After configuring LDP GR, you can view information about the LDP protocol and the LDP session.