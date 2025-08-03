Overview of EVC
===============

Overview_of_EVC

#### Definition

Ethernet virtual connection (EVC), proposed by the Metro Ethernet Forum (MEF), defines a unified Layer 2 service transport and configuration model. According to MEF, an EVC can be associated with two or more user network interfaces on an Internet service provider (ISP) network. In the EVC model, bridge domains (BDs) are used to isolate user networks.

EVC can be regarded as a template for Ethernet services, not a specific service or technology.


#### Purpose

[Figure 1](#EN-US_CONCEPT_0172363333__en-us_concept_0172352454_fig_dc_vrp_feature_evc_000101) shows the service model supported by the NE40E.

**Figure 1** Service model of the NE40E  
![](figure/en-us_image_0000001485470809.png)

The service model of the NE40E has limitations, which are described in [Table 1](#EN-US_CONCEPT_0172363333__en-us_concept_0172352454_tab_1). To address the limitations in [Table 1](#EN-US_CONCEPT_0172363333__en-us_concept_0172352454_tab_1), the EVC model is implemented on the NE40E, as shown in [Figure 2](#EN-US_CONCEPT_0172363333__en-us_concept_0172352454_fig_dc_vrp_feature_evc_000102).

**Figure 2** EVC model  
![](figure/en-us_image_0000001435751216.png)

[Table 1](#EN-US_CONCEPT_0172363333__en-us_concept_0172352454_tab_1) provides a comparison between the traditional service model and the EVC model supported by the NE40E.

**Table 1** Comparison between the traditional service model and the EVC model supported by the NE40E
| Service Object | Traditional Service Model | EVC Model |
| --- | --- | --- |
| Service access points | Sub-interfaces and Layer 2 interfaces, which have various types and require different configurations. | EVC Layer 2 sub-interfaces only. Configurations are unified on the Layer 2 sub-interfaces. The configurations include traffic encapsulation types, traffic behaviors, traffic policies, and traffic forwarding modes. Traffic encapsulation types and behaviors can be combined flexibly so that different services can be transmitted through different EVC Layer 2 sub-interfaces. |
| Broadcast domain | * Global virtual local area network (VLAN) for traditional Layer 2 services.  In a metro Ethernet network, VLANs are used to prevent broadcast storms. The VLAN tag field defined in IEEE 802.1Q has 12 bits and identifies only a maximum of 4096 VLANs, which is insufficient for identifying a great number of users in the metro Ethernet.  QinQ was developed to address the shortage of VLAN ID resources. However, QinQ must be used with the VPLS to provide local switching services, and QinQ cannot implement local switching services and Layer 3 packet termination services at the same time. * Virtual switching instance (VSI) for VPLS services:    + After a VSI is sold as a whole to a customer, the customer has to plan VLANs and traffic within the VSI.   + When VLAN services are carried within a VSI, the VLANs are not isolated, posing security risks. If the same MAC address exists in multiple VLANs of a VSI, MAC address flapping occurs, affecting services. | BD:  * A BD supports local switching of VLAN/QinQ services. * Different BDs can carry services from the same VSI, with the services being differentiated using BD IDs. BDs are isolated from each other, and MAC address learning is based on BDs. This ensures broadcast domain isolation and prevents MAC address flapping in a VSI. |
| Layer 2 forwarding | * VLAN Trunk: transmits global VLAN services. * PW: transmits L2VPN services. | - |
| Layer 3 access | * VLANIF interface: terminates Layer 2 packets and provides Layer 3 access.  A VLANIF interface terminates single-tagged packets rather than double-tagged packets before providing Layer 3 access. * L2VE and L3VE sub-interfaces bound to a VE group: terminates L2VPN services and provides L3VPN access, respectively.  A dot1q or QinQ VLAN tag termination sub-interface removes tags from Layer 2 packets and forwards the packets to a Layer 3 network. In this situation, the L2VE and L3VE sub-interfaces must be bound to the same VE group. This configuration is not as simple as the VLANIF interface configuration. | BDIF interface: terminates Layer 2 services and provides Layer 3 access. |



#### Benefits

EVC unifies the Ethernet service model and configuration model, simplifies configuration management, improves O&M efficiency, and enhances service access scalability.