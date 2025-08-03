Configuring EVPN Carrier's Carrier (LDP Multi-Instance)
=======================================================

Configuring_EVPN_Carrier's_Carrier_(LDP_Multi-Instance)

#### Usage Scenario

If a BGP/MPLS IP VPN user is a service provider that offers BGP/MPLS IP VPN services to its clients, carrier's carrier can be configured. Compared with basic BGP/MPLS IP VPN, the key to the carrier's carrier model lies in the access of Level 1 carrier CEs to Level 1 carrier PEs. [Table 1](#EN-US_TASK_0000001214273083__table1414188793) describes how carrier's carrier is implemented.

**Table 1** Implementation of carrier's carrier
| Solution | Solution Between Level 1 Carrier PEs and Level 1 Carrier CEs | Solution Between Level 2 Carrier PEs and Level 1 Carrier CEs |
| --- | --- | --- |
| Solution 1 | Use an IGP and LDP multi-instance to exchange routing information. | Use an IGP and LDP to exchange routing information. |
| Solution 2 | Use IBGP to exchange labeled IPv4 VPN routes. | BGP label distribution solution: Establish IBGP peer relationships to establish complete public network tunnels between the PEs of the Level 2 carrier. |
| Use EBGP to exchange labeled IPv4 VPN routes. | LDP label distribution for BGP: No IBGP peer relationship is established. After the Level 2 carrier's devices learn labeled public network BGP routes from the Level 1 carrier's devices, the Level 2 carrier's devices import these BGP routes into the IGP and trigger LDP to distribute labels for these routes. In this manner, complete LDP LSPs can be established between the Level 2 carrier PEs. |


The following describes solution 1, that is, the LDP multi-instance solution.


#### Pre-configuration Tasks

Before configuring carrier's carrier, complete the following tasks:

* Configure an IGP for the Level 1 carrier's MPLS backbone network to ensure IP connectivity on the backbone network.
* Configure basic MPLS functions and MPLS LDP for the Level 1 carrier's MPLS backbone network.
* Establish EVPN IBGP peer relationships between Level 1 carrier's PEs.
* Configure an IGP for the Level 2 carrier's IP or MPLS network to ensure IP connectivity.
* Configure basic MPLS functions and LDP on the Level 2 carrier network and set up LSPs.


[Configuring Level 1 Carrier CEs to Access Level 1 Carrier PEs (Using LDP Multi-Instance)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_csc_0002.html)

If the Level 1 and Level 2 carriers are in the same AS, the Level 1 carrier takes the Level 2 carrier as its VPN user.

[Configuring Level 2 Carrier CEs to Access Level 2 Carrier PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_csc_0004.html)

Similar to the configuration of CEs accessing PEs in a basic BGP/MPLS IP VPN scenario, you need to create a VPN instance on Level 2 carrier PEs and configure a routing protocol for these PEs to communicate with CEs.

[Configuring External Route Exchange Between Level 2 Carrier PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_csc_0005.html)

An MP-BGP peer relationship is established between Level 2 carrier PEs to exchange IPv4 VPN routes.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_csc_0006.html)

After carrier's carrier is configured, you can view information about public network routes on Level 1 and Level 2 carriers' PEs and CEs and VPN routes on their PEs.