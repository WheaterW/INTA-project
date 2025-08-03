Configuring Multicast Services on a VLAN Tag Termination Sub-interface
======================================================================

With the wide use of multicast services on the Internet, you need to deploy sub-interfaces for QinQ/dot1q VLAN tag termination to process the user packets carrying a single tag or double tags for multicast services. In this manner, the UPE can maintain information about the outbound interface of multicast packets according to the established multicast forwarding table to ensure the normal communications between hosts and the multicast source.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_CONCEPT_0172363271__fig_dc_vrp_qinq_cfg_003902), Layer 2 multicast and Layer 3 multicast services are deployed.

* Layer 2 multicast
  
  After being bound to a Virtual Switching Instance (VSI) and enabled with Internet Group Management Protocol (IGMP) snooping, the sub-interface for QinQ/dot1q VLAN tag termination can listen IGMP messages exchanged between the multicast device and hosts, and therefore can learn which interfaces have multicast receivers. In this case, multicast packets are transmitted on the Layer 2 network in multicast mode rather than broadcast mode, and consequently received only by members of the multicast group.
* Layer 3 multicast
  
  When multicast protocol packets with double tags are sent to the upper-layer network through the UPE, you need to configure a sub-interface for QinQ VLAN tag termination or sub-interface for dot1q VLAN tag termination on the UPE to support IGMP. In this way, a multicast group member forwarding table and a routing table can be created on the UPE. When multicast protocol packets sent from the user side pass through the UPE, the UPE can identify the packets and send them to the corresponding multicast source based on the service tag. Based on the established multicast forwarding table, the UPE can replicate and deliver multicast packets correctly.
  
  Here, Layer 3 multicast mainly refers to IGMP.

**Figure 1** Networking diagram of the multicast service on termination sub-interfaces  
![](figure/en-us_image_0000001591626218.png)

#### Pre-configuration Tasks

Before configuring the sub-interface for VLAN tag termination to access the multicast service, complete the following tasks:

* Ensuring that devices are correctly connected and that the physical interfaces of each device are in the Up state.
* Configuring the correct VLANs of users to enable the packets received by the sub-interface for VLAN tag termination to carry one or double tags.


[Configuring a VLAN Tag Termination Sub-interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0040.html)

A VLAN tag termination sub-interface can be a dot1q VLAN tag termination sub-interface or a QinQ VLAN tag termination sub-interface. In dot1q/QinQ termination, a device identifies whether a packet has one tag or two tags. The device then forwards the packet after stripping one or both tags or discards the packet.

[Configuring Multicast Services](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0041.html)

After a dot1q or QinQ VLAN tag termination sub-interface is configured, configure multicast services for the sub-interface so user hosts of this sub-interface can communicate with multicast sources.

[Verifying the Multicast Service Configuration on the VLAN Tag Termination Sub-interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0042.html)

After configuring multicast services on a dot1q or QinQ VLAN tag termination sub-interface, verify the configuration.