Configuring PW APS
==================

Pseudo wire (PW) automatic protection switching (APS) applies to scenarios where the primary and secondary PWs share the same source and same destination.

#### Usage Scenario

In a PW APS scenario, PW OAM detects the status of the active and standby PWs. When PW OAM detects a fault on the active PW, it immediately notifies PW APS of the fault, which is then triggered to perform an active/standby PW switchover. The PWs can be classified as single-segment PWs (SS-PWs) or multi-segment PWs (MS-PWs) or be classified as dynamic PWs or static PWs. See [Figure 1](#EN-US_TASK_0172369864__fig_dc_vrp_vpws_cfg_602801) and [Figure 2](#EN-US_TASK_0172369864__fig_dc_vrp_vpws_cfg_602802).

**Figure 1** PW APS networking for MS-PWs  
![](images/fig_dc_vrp_vpws_cfg_602801.png)  

**Figure 2** PW APS networking for SS-PWs  
![](images/fig_dc_vrp_vpws_cfg_602802.png)  
#### Pre-configuration Tasks

Before configuring PW protection, complete the following tasks:

* Configure IP addresses and an IGP on PEs.
* Establish public network tunnels between PEs. The public network tunnels can be:
  
  + TE tunnel: To establish a TE tunnel, you must enable MPLS, MPLS TE, and RSVP-TE both globally and per interface on each public network node along the tunnel, and enable CSPF in the MPLS view of the tunnel ingress.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    Because pseudo wire emulation edge-to-edge (PWE3) uses LDP to distribute VPN labels, you must globally enable MPLS LDP on PEs and establish remote MPLS LDP sessions if TE tunnels are used as public network tunnels.
    
    If the public network tunnels are not TE tunnels, you must configure tunnel policies and apply them to these tunnels.
* Enable MPLS L2VPN on PEs.


[Configuring a PW Protection Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6029.html)

In a PW APS scenario, a PW protection group consists of primary and secondary PWs. The PWs can be either SS-PWs or MS-PWs.

[Configuring a PW APS Instance and Bind a PW Protection Group to the PW APS Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6030.html)

The state machine of a PW APS instance determines the protection switching in PW protection groups associated with the instance.

[Configuring PW OAM to Detect Public Network Link Faults](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6031.html)

PW OAM includes Multiprotocol Label Switching Transport Profile (MPLS-TP) OAM and MPLS OAM. PW OAM can quickly detect PW faults, enabling speedy PW switching for service protection.

[(Optional) Configuring PW APS Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6032.html)

This section describes how to configure PW APS parameters, such as the switchback mode, hold time for PW switchover, and WTR time for PW switchback. In network O&M, you can manually trigger PW switching with commands.

[Verifying the PW APS Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6033.html)

After you complete the configurations, check information about the PW APS instance and its associated PW protection groups.