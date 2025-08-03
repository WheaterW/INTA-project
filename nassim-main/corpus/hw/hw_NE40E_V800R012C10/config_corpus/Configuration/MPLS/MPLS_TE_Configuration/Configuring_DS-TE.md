Configuring DS-TE
=================

This feature combines traditional TE tunnels with the DiffServ model to provide QoS guarantee based on service types.

#### Usage Scenario

A static CR-LSP is easy to configure. Labels are manually allocated, and no signaling protocol is used to exchange control packets. The setup of a static CR-LSP consumes only a few resources, and you do not need to configure an IGP TE extension or CSPF for the static CR-LSP. However, static CR-LSP application is quite limited. A static CR-LSP cannot dynamically adapt to network changes and is limited in applications.

MPLS TE tunnels apply to one of the following VPN scenarios:

* A single TE tunnel transmits various types of services in a non-VPN scenario.
* A single TE tunnel transmits various types of services in a VPN instance.
* A single TE tunnel transmits various types of services in multiple VPN instances.
* A single TE tunnel transmits various types of VPN and non-VPN services.

Traditional MPLS TE tunnels (non-standard DS-TE tunnels) cannot transmit services based on service types in compliance with the quality of service (QoS). For example, when a TE tunnel carries both voice and video flows, video flows may have more duplicate frames than voice flows. Therefore, video flows require higher drop precedence than the voice flows. The same drop precedence, however, is used for voice and video flows on MPLS TE tunnels.

To prevent services over a tunnel from interfering with each other, establish a tunnel for each type of service in a VPN instance or for each type of non-VPN service. This solution wastes resources because a large number of tunnels are established when many VPN instances carry various services.

In the preceding MPLS TE tunnel scenarios, the DS-TE tunnel solution is optimal. An edge node in a DS-TE domain classifies services and adds service type information in the EXP field in packets. A transit node merely checks the EXP field to select a proper PHB to forward packets.

A DS-TE tunnel classifies services and reserves resources for each type of services, which improves network resource use efficiency. A DS-TE tunnel carries a maximum of eight types of services.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The IETF DS-TE tunnel configuration requires the ingress and egress hardware to support HQoS. The non-IETF DS-TE tunnel has no such a restriction.
* If the same type of service in multiple VPN instances is carried using the same CT of a DS-TE tunnel, the bandwidth of each type of service in each VPN instance can be set on an access CE to prevent services of the same type but different VPN instances from competing for resources.
* To prevent non-VPN services and VPN services from completing resources, you can configure DS-TE to carry VPN services only or configure the bandwidth for non-VPN services in DS-TE.


#### Pre-configuration Tasks

Before configuring DS-TE, complete the following tasks:

* Configure unicast static routes or an IGP to ensure the readability between LSRs at the network layer.
* Set an LSR ID on each LSR.
* Enable MPLS globally and on interfaces on all LSRs.
* Enable MPLS TE and RSVP-TE on all LSRs and their interfaces.
* Enable behavior aggregate (BA) traffic classification on each LSR interface along an LSP.


[Configuring a DS-TE Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0302.html)

You can configure an MPLS TE tunnel to work a DS-TE mode, either IETF mode or non-IETF mode.

[Configuring a DS-TE Bandwidth Constraints Model](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0303.html)

If CT bandwidth preemption is allowed, the Russian dolls model (RDM) is recommended to efficiently use bandwidth resources. If CT bandwidth preemption is not allowed, the MAM is recommended.

[Configuring Link Bandwidth](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0305.html)

You can configure link bandwidth to limit the bandwidth for a DS-TE tunnel.

[Configuring Tunnel Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0306.html)

Before creating a DS-TE tunnel, create a tunnel interface and configure tunnel attributes in the view of the tunnel interface.

[Configuring an RSVP CR-LSP and Specifying Bandwidth Values](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0308.html)

When configuring an RSVP CR-LSP and specifying its bandwidth values, ensure that the sum of CT bandwidth values does not exceed the sum of BC bandwidth values.

[(Optional) Configuring a TE-Class Mapping Table](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0304.html)

Configuring the same TE-class mapping table on the whole DS-TE domain is recommended. Otherwise, LSPs may be incorrectly established.

[(Optional) Configuring CBTS](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_te-p2p_cfg_0001_new.html)

Service class can be set for packets that MPLS TE tunnels allow to pass through.

[Verifying the DS-TE Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0310.html)

After configuring DS-TE, you can verify DS-TE information and CT information of a tunnel.