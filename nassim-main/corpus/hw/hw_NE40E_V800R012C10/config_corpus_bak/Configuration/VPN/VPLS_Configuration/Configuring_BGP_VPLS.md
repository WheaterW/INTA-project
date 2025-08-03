Configuring BGP VPLS
====================

This section describes how to configure BGP VPLS, which uses VPN targets for automatic VPLS PE discovery.

#### Usage Scenario

BGP VPLS applies to scenarios where PEs can use BGP as the VPLS signaling protocol.

On the network shown in [Figure 1](#EN-US_TASK_0139427942__fig_dc_vrp_vpls_cfg_600501), PE1, PE2, and PE3 belong to the same VPLS network.

* To enable CEs connected to PE1, PE2, and PE3 to communicate with each other by constructing a full-mesh VPLS network, ensure that PE1, PE2, and PE3 have matching VPN targets.
* To enable CE1 to communicate with both CE2 and CE3 and prevent CE2 and CE3 from communicating with each other, ensure that the import VPN target of PE1 is the same as the export VPN targets of PE2 and PE3, and that the export VPN target of PE1 is the same as the import VPN targets of PE2 and PE3. The VPN targets of PE2 and PE3 do not need to match.

**Figure 1** Network diagram of BGP VPLS  
![](images/fig_dc_vrp_vpls_cfg_600501.png)  


#### Pre-configuration Tasks

Before configuring BGP VPLS, complete the following tasks:

* Configure IP addresses and IGP routes on PEs and Ps.
* Configure LSR IDs and enable MPLS functions on PEs and Ps.
* Establish tunnels between PEs to transmit service data.


[Configuring BGP Peers to Exchange VPLS Information](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6006.html)

BGP VPLS shares TCP connections with BGP and inherits most BGP configurations. A major difference between BGP and BGP VPLS is that BGP VPLS requires PEs to exchange VPLS information as BGP peers in the L2VPN AD address family view.

[Configuring a VSI and BGP Signaling](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6007.html)

This section describes how to configure BGP VPLS, specifically, a VSI with BGP signaling.

[Binding an AC Interface to a VSI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5005-02.html)

The view in which an AC interface is bound to a VSI depends on the type of link between the PE and CE.

[(Optional) Configuring Flow Label-based Load Balancing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6110.html)

After flow label-based load balancing is configured for an L2VPN, L2VPN services can be classified by flow labels and forwarding paths can be selected based on the flow labels, improving forwarding efficiency. 

[(Optional) Configuring a Huawei Device to Communicate with a Non-Huawei Device](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6008.html)



[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6010.html)

After configuring BGP VPLS, check local and remote VSI and VPLS connection information.