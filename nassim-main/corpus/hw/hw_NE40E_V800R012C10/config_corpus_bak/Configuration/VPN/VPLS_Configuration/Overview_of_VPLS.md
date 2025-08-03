Overview of VPLS
================

Overview_of_VPLS

#### Definition

VPLS, also called the transparent LAN service (TLS), is a point-to-multipoint (P2MP) L2VPN service provided over a public network. This MPLS- and Ethernet-based technology enables geographically isolated user sites to communicate over MANs and WANs as if they were on the same LAN.

[Figure 1](#EN-US_CONCEPT_0172370050__en-us_concept_0172356300_fig_dc_vrp_vpls_feature_500101) shows a typical VPLS network. On the network, users in different geographical regions communicate with each other through different PEs. From the user perspective, a VPLS network appears as a Layer 2 switched network, allowing users to communicate with each other like they do over a LAN.

**Figure 1** Typical VPLS scenario  
![](images/fig_feature_image_0003996350.png)  


#### Purpose

As enterprises set up more and more branches in different regions and adopt more flexible work arrangements, they are increasingly relying on applications such as Voice over Internet Protocol (VoIP), instant messaging, and teleconferencing. This imposes higher requirements on E2E data communication technologies. The key to implementing E2E data communication functions is a network capable of providing P2MP services.

Traditional asynchronous transfer mode (ATM) and frame relay (FR) technologies provide only Layer 2 point-to-point (P2P) connections. Furthermore, networks that adopt these technologies have disadvantages such as high construction costs, low speed, and complex deployment. The development of IP led to the emergence of MPLS VPN technology, which can provide VPN services over an IP network and offer advantages such as easy configuration and flexible bandwidth control. MPLS VPNs are classified into MPLS L2VPNs and MPLS L3VPNs:

* Traditional MPLS L2VPNs, such as VLL (VPWS) networks, can provide P2P services but not P2MP services over a public network.
* MPLS L3VPNs can provide P2MP services on the precondition that PEs keep routes destined for end users. This implementation requires PEs to have high routing performance.

VPLS, an MPLS-based Ethernet technology built upon traditional MPLS L2VPN, is designed to address the preceding problems.

* Like Ethernet, VPLS supports P2MP communication.
* MPLS is a Layer 2 label switching technology. For users, the entire MPLS IP backbone network appears as a Layer 2 switching device. PEs on such a network do not need to keep routes destined for end users.

VPLS integrates the advantages of Ethernet and MPLS technologies and provides a more comprehensive P2MP service solution for Internet service providers (ISPs). By emulating traditional LAN functions, VPLS enables geographically isolated users on different Ethernet LANs to communicate with each other over the ISP-provided IP/MPLS network as if they were on the same LAN.


#### Benefits

VPLS offers the following benefits:

* VPLS networks can be constructed based on ISPs' IP networks, reducing construction costs.
* VPLS networks inherit the high-speed advantage of the Ethernet.
* VPLS allows users to communicate over Ethernet links, regardless of whether these links are on WANs or LANs. This allows services to be rapidly and flexibly deployed.
* VPLS frees ISPs from configuring and maintaining routing policies, reducing operational expenditure (OPEX).