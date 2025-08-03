Configuring LDP HVPLS
=====================

Before configuring LDP HVPLS, familiarize yourself with the usage scenario and complete the pre-configuration tasks.

#### Usage Scenario

On a typical VPLS network, all PEs are fully meshed. In this case, when a PE is added to the network, certain PEs are re-designated and PWs increase exponentially. As a result, many system resources are consumed and system performance is severely diminished, limiting VPLS networking deployment and application.

The essence of HVPLS lies in hierarchizing the VPLS network to facilitate deployment. You can connect multiple isolated HVPLS networks by establishing full-mesh connections between SPEs. This allows isolated HVPLS networks to communicate without the need for full-mesh PWs. This configuration improves the scalability, deployability, and flexibility of VPLS networks. In addition, broadcast packets are minimized due to fewer full-mesh connections, improving network performance.

**Figure 1** HVPLS networking  
![](images/fig_dc_vrp_vpls_cfg_500202.png)  


#### Pre-configuration Tasks

Before configuring HVPLS, complete the following tasks:

* Configure LSR IDs and enable MPLS and MPLS LDP on UPEs, SPEs, and Ps.
* Configure MPLS L2VPN on UPEs and SPEs.
* Establish tunnels between SPEs and between UPEs and SPEs for data transmission.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Establish remote LDP sessions if the SPEs or SPEs and UPEs are not directly connected but LDP LSPs need to be used on the public network.


[Configuring VPLS Between an SPE and a UPE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5010.html)

A switching provider edge (SPE) and an underlayer provider edge (UPE) set up a spoke PW, which does not comply with the split horizon principle.

[Configuring VPLS Between SPEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5011.html)

The VPLS configuration between SPEs is similar to the configuration of common VPLS.

[(Optional) Changing the MAC Address Update Speed on an HVPLS Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5012.html)



[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5013.html)

After configuring LDP HVPLS, check information about VPLS VSIs (including remote VSIs), VPLS connections, outbound interfaces of VSI PWs, and tunnel policies applied to VSIs.