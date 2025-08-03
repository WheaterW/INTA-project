Configuring VPLS PW Redundancy
==============================

Configuring VPLS PW redundancy improves PW switching efficiency and minimizes the impact of device faults on services.

#### Usage Scenario

Using VPLS to establish a Metro Ethernet that carries high-speed Internet (HSI), voice over IP (VoIP), Internet Protocol Television (IPTV), mobile backhaul, business applications, and other services has become a trend for large service provider networks. This trend imposes higher requirements on VPLS reliability. The ME 1.3 solution, also called the VPLS aggregation solution, uses E-VRRP to implement network convergence. Compared with the VPLS PW redundancy solution, the ME 1.3 solution provides a higher convergence speed, but has the following disadvantages:

* Some features are Huawei-specific, and therefore cannot be used when Huawei devices communicate with non-Huawei devices.
* Additional configurations, such as mVSIs and mPWs, are required, consuming a lot of network resources.
* PWs in a PW protection group cannot be manually switched on a UPE. PW switching on a UPE can only be triggered by VRRP switching on NPEs.
* This solution is complex.

VPLS PW redundancy does not have the preceding problems and can therefore be used to improve VPLS network reliability.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Only PWE3 VPLS supports PW redundancy.
* When configuring VPLS PW redundancy, you are advised to configure consistent parameters for the primary and secondary PWs. Otherwise, the secondary PW may fail to take over services when the primary PW fails, leading to service interruption.

VPLS PW redundancy has two networking scenarios:

* HVPLS scenario: Shown in [Figure 1](#EN-US_TASK_0172370170__fig_dc_vrp_vpls_cfg_504901), this scenario is best suited for multicast services, such as IPTV. The HVPLS network instead of the VPLS network is recommended. This is because service traffic transmitted by CEs at the point of presence (POP) layer are advertised by PEs to all PWs. As HVPLS uses a hierarchical architecture, it requires fewer PWs and less bandwidth between SPEs and NPEs.
* VPLS accessing VPWS: Shown in [Figure 2](#EN-US_TASK_0172370170__fig_dc_vrp_vpls_cfg_504902), this scenario is best suited for unicast services, such as HSI, VoIP, and mobile backhaul. If VPWS is configured on NPEs, the NPEs do not need to learn the MAC addresses of user terminals, reducing the burden on NPEs.

**Figure 1** VPLS PW redundancy in an HVPLS networking scenario  
![](images/fig_dc_vrp_vpls_cfg_504901.png)
**Figure 2** VPLS PW redundancy in a VPLS accessing VPWS networking scenario  
![](images/fig_dc_vrp_vpls_cfg_504902.png)

When using VPLS PW redundancy to ensure network reliability, note the following:

* To speed up IPTV service convergence, configure the secondary PW to forward IGMP packets and learn which users join multicast groups.
* If services need to be terminated on PWs before accessing the Layer 3 network, consider the impact of PW switching on services for the Layer 3 network.

#### Pre-configuration Tasks

Before configuring VPLS PW redundancy, complete the following tasks:

* Configure IP addresses and an IGP on PEs.
* Establish public network tunnels between PEs. The public network tunnels can be:
  
  + LDP tunnels: To establish an LDP tunnel, you must enable MPLS and MPLS LDP both globally and per interface on each public network node along the tunnel. If two PEs are indirectly connected, establish a remote LDP session between them.
  + TE tunnels: To establish a TE tunnel, you must enable MPLS, MPLS TE, and RSVP-TE both globally and per interface on each public network node along the tunnel, and enable CSPF in the MPLS view of the tunnel ingress.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    Because pseudo wire emulation edge-to-edge (PWE3) uses LDP to distribute VPN labels, you must globally enable MPLS LDP on PEs and establish MPLS LDP sessions if TE tunnels are used as public network tunnels.
    
    If the public network tunnels are not LDP tunnels, you must configure tunnel policies and apply them to these tunnels.
* Enable MPLS L2VPN on PEs.


[Configuring a PW](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5050.html)

The following describes how to configure a PW in two networking modes: HVPLS and VPLS accessing VPWS. Currently, only LDP PWs can be configured.

[Adding PWs to a PW Protection Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5051.html)

After configuring PWs, add them to a PW protection group, specify PW priorities, and configure PW protection group parameters to implement PW redundancy.

[(Optional) Associating Spoke PW Status with Hub PW Status](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5052.html)

After spoke PW status is associated with hub PW status, a spoke PW will go down if the associated hub PWs all go down, triggering a primary/secondary spoke PW switchover.

[(Optional) Configuring BFD for PW](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5053.html)

After configuring PWs, configure BFD for PW to detect the faults of the primary PW to speed up fault detection and improve PW switching performance.

[(Optional) Manually Switching PWs in a PW Protection Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5054.html)

In PW maintenance, you can manually switch services to the standby PW to facilitate maintenance operations.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5055.html)

After the configuration is complete, check information about the PW redundancy protection group for a specified VSI, including PWs in the protection group and related VSI and LDP VC information.