Configuring PBB VPLS
====================

Configuring_PBB_VPLS

#### Usage Scenario

Typical scenarios of PBB VPLS are classified into the following types:

* Fully meshed PBB VPLS
  
  [Figure 1](#EN-US_TASK_0172370781__fig_dc_vrp_pbb-vpls_cfg_000401) shows a typical HVPLS network with UPEs, SPEs, and NPEs. Basic PBB configurations need to be performed on this network to replace QinQ with MAC-in-MAC. This helps reduce the number of MAC address entries that SPEs must learn in a VPLS service, improving network scalability.
  
  **Figure 1** Network diagram of fully meshed PBB VPLS  
  ![](images/fig_dc_vrp_pbb-vpls_cfg_000401.png)
* Network diagram of PBB VPLS with an E-Trunk determining the master/backup status of NPEs
  
  On the network shown in [Figure 2](#EN-US_TASK_0172370781__fig_dc_vrp_pbb-vpls_cfg_000402), UPEs are dual-homed to SPEs, and SPEs are in turn dual-homed to NPEs. An E-Trunk determines the master/backup status of NPEs. If SPE1 directly connects to CE3, PBB VPLS can then enable CE1 to communicate with CE2 and CE3.
  
  **Figure 2** Network diagram of a PBB VPLS residential service with an E-Trunk determining the master/backup status of NPEs  
  ![](images/fig_dc_vrp_pbb-vpls_cfg_000402.png)  
  
  **Figure 3** Network diagram of a PBB VPLS enterprise service with an E-Trunk determining the master/backup status of NPEs  
  ![](images/fig_dc_vrp_pbb-vpls_cfg_000403.png)
* Local PBB VPLS connection
  
  On the network shown in [Figure 4](#EN-US_TASK_0172370781__fig_fig_dc_vrp_pbb-vpls_cfg_000404), CE1 is dual-homed to UPE1 and UPE2, and an E-Trunk determines the master/backup status of the UPEs. Normally, UPE1 serves the master device according to the E-Trunk negotiation result, and CE1 communicates with CE2 through UPE1 over a remote PBB VPLS connection. If the link between CE1 and UPE1 fails or UPE1 fails, CE1 communicates with CE2 through UPE2 over a local connection.
  
  During the configuration of a local connection on UPE2, two I-VSIs are bound to the same B-VSI and assigned the same I-tag. One I-VSI's B-DMAC address is the same as the other I-VSI's B-SMAC address.
  
  **Figure 4** Network diagram of a local PBB VPLS connection  
  ![](images/fig_dc_vrp_pbb-vpls_cfg_000404.png)

#### Pre-configuration Tasks

Before configuring PBB VPLS, complete the following tasks:

* Configure LSR IDs for PEs and Ps, and configure an IGP for PEs and Ps to have reachable routes to each other and learn LSR IDs from each other.
* Configure MPLS and MPLS LDP, and set up LDP sessions.
* Enable MPLS L2VPN on PEs.


[Enabling I-VSI and B-VSI Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-vpls_cfg_0005.html)

Enabling I-VSI and B-VSI functions is the prerequisite for configuring PBB VPLS.

[Configuring an I-VSI and a B-VSI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-vpls_cfg_0006.html)

An I-VSI can be bound to a B-VSI only after their B-MAC addresses and the I-VSI's I-tag are configured.

[Binding an I-VSI to a B-VSI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-vpls_cfg_0007.html)

A CE can access a PW only after the corresponding I-VSI is bound to a B-VSI.

[Binding an AC Interface to an I-VSI and Specifying a VPLS Peer for a B-VSI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-vpls_cfg_0008.html)

In PBB VPLS, an AC interface must be bound to each I-VSI and a VPLS peer must be specified for each B-VSI. 

[(Optional) Enabling CFM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-vpls_cfg_0009.html)

To suppress unidirectional multicast and unknown unicast packets, enable CFM for PBB VPLS. 

[Verifying the PBB VPLS Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-vpls_cfg_0010.html)

After configuring PBB VPLS, check the configurations, including the B-SMAC address, B-DMAC address, and VSI information.