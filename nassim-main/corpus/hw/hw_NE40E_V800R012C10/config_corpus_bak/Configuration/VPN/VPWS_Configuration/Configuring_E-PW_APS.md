Configuring E-PW APS
====================

E-PW APS applies to scenarios where CEs asymmetrically access PEs.

#### Usage Scenario

E-PW APS applies to 3PE scenarios in which two CEs asymmetrically access three PEs over PWs. On the two PEs to which a CE is dual-homed, E-Trunk/MC-LMSP is used to determine the AC-side active/standby status.

The PWs can be either SS-PWs or MS-PWs. When PW OAM detects a fault on the active PW, it immediately notifies E-PW APS of the fault, which is then triggered to perform an active/standby PW switchover. See [Figure 1](#EN-US_TASK_0172369876__fig_dc_vrp_vpws_cfg_603401) and [Figure 2](#EN-US_TASK_0172369876__fig_dc_vrp_vpws_cfg_603402).

**Figure 1** E-PW APS networking for MS-PWs  
![](images/fig_dc_vrp_vpws_cfg_603401.png "Click to enlarge")  

**Figure 2** E-PW APS networking for SS-PWs  
![](images/fig_dc_vrp_vpws_cfg_603402.png)  
#### Pre-configuration Tasks

Before configuring PW protection, complete the following tasks:

* Configure IP addresses and an IGP on PEs.
* Establish public network tunnels between PEs. The public network tunnels can be:
  
  + TE tunnel: To establish a TE tunnel, you must enable MPLS, MPLS TE, and RSVP-TE both globally and per interface on each public network node along the tunnel, and enable CSPF in the MPLS view of the tunnel ingress.
* Enable MPLS L2VPN on PEs.


[Configuring a PW Protection Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6035.html)

In an E-PW APS scenario, a PW protection group consists of either primary and secondary PWs or primary and bypass PWs. The primary and secondary PWs can be either SS-PWs or MS-PWs.

[Configuring PW APS Instances and Binding PW Protection Groups to These Instances](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6036.html)

This section describes how to configure PW and E-PW APS instances and bind PW protection groups to the APS instances.

[Configuring PW OAM to Detect Public Network Link Faults](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6031-01.html)

PW OAM includes Multiprotocol Label Switching Transport Profile (MPLS-TP) OAM and MPLS OAM. PW OAM can quickly detect PW faults, enabling speedy PW switching for service protection.

[(Optional) Configuring PW APS Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6032-01.html)

This section describes how to configure PW APS parameters, such as the switchback mode, hold time for PW switchover, and WTR time for PW switchback. In network O&M, you can manually trigger PW switching with commands.

[Configuring AC Dual-Homing Protection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6037.html)

If a CE is dual-homed to two PEs, configure MC-LAG to implement AC dual-homing protection.

[Checking the Configurations](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6033-01.html)

After you complete the configurations, check information about the PW APS instance and its associated PW protection groups.