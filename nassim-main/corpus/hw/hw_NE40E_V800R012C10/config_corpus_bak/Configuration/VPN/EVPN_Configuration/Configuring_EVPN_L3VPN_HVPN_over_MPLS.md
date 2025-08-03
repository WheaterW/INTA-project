Configuring EVPN L3VPN HVPN over MPLS
=====================================

An EVPN L3VPN HVPN over MPLS network is a hierarchical EVPN where multiple PEs play different roles and form a hierarchical structure to implement the functions of a single PE. This helps lower the requirements on PE performance.

#### Usage Scenario

Today's IP transport networks generally use complex L2VPN and L3VPN (HVPN) to carry Layer 2 and Layer 3 services, respectively. EVPN, in contrast, can carry both Layer 2 and Layer 3 services. To simplify service transport protocols, many IP transport networks will evolve to EVPN. Among them, L3VPN HVPN that carries Layer 3 services needs to evolve to EVPN L3VPN HVPN over MPLS.

[Figure 1](#EN-US_CONCEPT_0172370554__fig105144482014) shows the basic architecture of an HVPN that consists of the following device roles:

* UPE: directly connects to a user and is referred to as an underlayer PE or user-end PE, hence the name UPE. A UPE mainly provides user access.
* SPE: connects to UPEs and is located at the core of a network. An SPE is known as a superstratum PE or service provider-end PE, hence the name SPE. An SPE manages and advertises VPN routes.
* NPE: connects to SPEs and is located at the network side. An NPE is known as a network provider-end PE, hence the name NPE.

**Figure 1** Basic structure of an EVPN L3VPN HVPN over MPLS network  
![](figure/en-us_image_0000001286755138.png)  

An access network is deployed between the UPEs and SPE, and an aggregation network is deployed between the SPE and NPE. EVPN L3VPN HVPN over MPLS can be deployed on the access and aggregation networks only after IGP is deployed on each of them.

EVPN L3VPN HVPN over MPLS can be classified into EVPN L3VPN HoVPN over MPLS or EVPN L3VPN H-VPN over MPLS.

* EVPN L3VPN HoVPN over MPLS: The SPE advertises only default or summary routes to UPEs. UPEs do not have specific routes to the NPE and can only use default routes to send service data to the SPE, ensuring route isolation. In EVPN L3VPN HoVPN over MPLS networking, devices with relatively low route management capabilities can be used as UPEs, cutting network deployment costs.
* EVPN L3VPN H-VPN over MPLS: The SPE can advertise specific routes to UPEs. The UPEs function as RR clients and receive specific routes reflected by the SPE (functioning as the RR), facilitating route management and traffic forwarding control.

During evolution from traditional L3VPN HoVPN to EVPN L3VPN HoVPN over MPLS, the following interworking scenarios may occur:

* Interworking between EVPN L3VPN HoVPN over MPLS and common L3VPN: EVPN L3VPN HoVPN over MPLS is deployed between the UPE and SPE, and L3VPN is deployed between the SPE and NPE. The SPE advertises only default or summary routes to the UPE. After receiving specific routes (EVPN routes) from the UPE, the SPE encapsulates these routes into VPNv4 routes and advertises them to the NPE.
* Interworking between L3VPN HoVPN and EVPN L3VPN over MPLS: L3VPN HoVPN is deployed between the UPE and SPE, and EVPN L3VPN over MPLS is deployed between the SPE and NPE. The SPE advertises only default or summary routes to the UPE. After receiving specific routes (L3VPN routes) from the UPE, the SPE encapsulates these routes into EVPN routes and advertises them to the NPE.


#### Pre-configuration Tasks

Before configuring EVPN L3VPN HVPN over MPLS, complete the following tasks:

Configure IGP between the UPE and SPE and between the SPE and NPE to ensure IP connectivity. Different types of IGP protocols or IGP protocols of the same type but in different processes can be deployed at different network layers.


[Configuring EVPN L3VPN HoVPN over MPLS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0080.html)

On an EVPN L3VPN HoVPN over MPLS network, the UPE only needs to obtain a default route from the SPE. This implementation reduces the route storage space required on the UPE while ensuring route isolation.

[Configuring EVPN L3VPN H-VPN over MPLS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0081.html)

On an EVPN L3VPN H-VPN over MPLS network, the SPE functions as an RR and the UPE and NPE function as RR clients, which receive specific routes from the RR.

[Configuring Interworking Between EVPN L3VPN HoVPN over MPLS and Common L3VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0082.html)

During evolution from L3VPN HoVPN to EVPN L3VPN HoVPN over MPLS, interworking between EVPN L3VPN HoVPN over MPLS and common L3VPN is required. EVPN L3VPN HoVPN over MPLS is deployed between the UPE and SPE, and common L3VPN is deployed between the SPE and NPE.

[Configuring Interworking Between L3VPN HoVPN and EVPN L3VPN over MPLS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0083.html)

During evolution from L3VPN HoVPN to EVPN HoVPN over MPLS, interworking between L3VPN HoVPN and EVPN L3VPN over MPLS occurs. L3VPN HoVPN is deployed between the UPE and SPE, and EVPN L3VPN over MPLS is deployed between the SPE and NPE.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0084.html)

After configuring EVPN L3VPN HVPN over MPLS, verify the default or specific routes sent from the remote end on the UPE or NPE.