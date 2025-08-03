Configuring an HVPN
===================

On an HVPN, PEs play different roles and provide different functions. These PEs form a hierarchical architecture to provide functions that are provided by one PE on a non-hierarchical VPN. HVPNs lower the performance requirements for PEs.

#### Usage Scenario

The BGP/MPLS IP VPN architecture is a plane model. The performance requirements for each PE on a BGP/MPLS IP VPN are the same. On a hierarchical network configured with BGP/MPLS IP VPN, the access or routing management capabilities of PEs are frequently challenged as the network expands in scale and service types increase. As a result, limited network performance and expansibility prevent VPN services from being deployed on a large scale.

To improve expansibility, BGP/MPLS IP VPN must adopt the HVPN model. On an HVPN, PEs play different roles and provide different functions. These PEs form a hierarchical architecture to provide the same functions as that are normally provided by a single PE on a non-hierarchical VPN.

Upper-level devices on an HVPN must have strong routing management and forwarding capabilities, but do not need strong access capabilities. Conversely, lower-level devices on an HVPN must have strong access capabilities, but do not need strong routing management or forwarding capabilities. Different types of devices can be deployed at different hierarchical levels. An HVPN features flexible device deployment and high expansibility. If the access, routing management, or forwarding capabilities of the PEs at a certain hierarchical level cannot meet actual requirements, you can deploy more PEs to that hierarchical level.

[Figure 1](#EN-US_CONCEPT_0172369400__fig_dc_vrp_mpls-l3vpn-v4_cfg_016401) shows the basic architecture of an HVPN, which consists of the following device roles:

* User-end provider edge (UPE): directly connects to CEs and provides access services for users.
* Superstratum provider edge (SPE): connects to UPEs and is located at the core of a network. An SPE manages and advertises VPN routes.
* Network provider edge (NPE): connects to SPEs and is located at the network side.

**Figure 1** HVPN architecture  
![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_016401.png)  

An HVPN can be either an HoVPN or an H-VPN:

* On an HoVPN, SPEs advertise default routes to UPEs. UPEs do not have specific routes to NPEs and can only send VPN service data to SPEs over default routes. As a result, route isolation is implemented. An HoVPN can use devices with relatively poor route management capabilities as UPEs, reducing network deployment costs.
* On an H-VPN, SPEs advertise specific routes to UPEs. UPEs function as RR clients to receive the specific routes reflected by SPEs functioning as RRs. This mechanism facilitates route management and traffic forwarding control.


#### Pre-configuration Tasks

Before you configure an HVPN, complete the following task:

[Configure a basic BGP/MPLS IP VPN.](dc_vrp_mpls-l3vpn-v4_cfg_0154.html)


[Configuring an HoVPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0165.html)

On an HoVPN, a UPE only needs to obtain a default route from an SPE. This implementation mechanism reduces the route storage space required on a UPE.

[Configuring an H-VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0166.html)

On an H-VPN, SPEs function as RRs and UPEs function as RR clients. UPEs receive specific routes from SPEs.

[(Optional) Configuring Route Re-origination](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0177.html)

On an HVPN, UPEs can communicate through SPEs and NPEs. You can configure route re-origination on SPEs to reduce the number of VPN labels assigned to VPNv4 routes received by the UPEs.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0167.html)

After you configure an HVPN, check on a local CE the default route or specific routes from this CE to a remote CE.