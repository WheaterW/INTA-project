IPv4 Multicast Application
==========================

This section describes typical multicast service scenarios on an IPv4 network and the applications of multicast protocols and features in these scenarios. Multicast services should be configured based on the actual network situations and service requirements on your network. This section describes only the deployment of basic service functions.

Before deploying IPv4 multicast services on a network, ensure that IPv4 unicast routes on the network are normal.

#### Multicast in a Single PIM Domain

On a small-scale network shown in [Figure 1](#EN-US_CONCEPT_0000001130781848__fig10488103585717), all devices and hosts are in the same PIM domain, and basic multicast services are deployed.

**Figure 1** Network diagram of the basic multicast service deployment in a PIM domain  
![](figure/en-us_image_0000001594530686.png)

**Table 1** Multicast service deployment in a PIM domain
| Deployment Protocol | Application Location | Purpose |
| --- | --- | --- |
| PIM  (mandatory) | All interfaces of Layer 3 multicast devices in the multicast domain, including all interfaces of DeviceA, DeviceB, and DeviceC.  For detailed configurations, see PIM Configuration. | Sends multicast data from Source to DeviceB and DeviceC, which are connected to multicast receivers. |
| IGMP  (mandatory) | User-side interfaces of Layer 3 multicast devices, including DeviceB and DeviceC  For detailed configurations, see IGMP Configuration. | Allows receiver hosts to join or leave multicast groups, and allows DeviceB and DeviceC to maintain and manage group memberships. |
| IGMP snooping & IGMP Snooping Proxy  (optional) | VLAN on DeviceD between the Layer 3 multicast device and user host.  For details, see Configuring IGMP Snooping. | IGMP snooping listens to IGMP messages exchanged between DeviceB and HostA to create a Layer 2 multicast forwarding table. This allows the Layer 2 device to manage and control the forwarding of multicast data messages on the Layer 2 network.  IGMP snooping proxy allows the Layer 2 device to act as a substitute for DeviceB to send IGMP Query messages and as a substitute for HostA to send IGMP Report and Leave messages. |



#### Multicast Between PIM-SM Domains

A multicast domain can be divided into multiple isolated PIM-SM domains to facilitate the management of multicast resources, including groups, multicast sources, and group members. On the network shown in [Figure 2](#EN-US_CONCEPT_0000001130781848__fig1276418559111), MSDP needs to be deployed to enable the PIM-SM domains to exchange multicast data.

![](public_sys-resources/note_3.0-en-us.png) 

MSDP is not required when PIM-SM uses the SSM model.


**Figure 2** Network diagram of the basic multicast service deployment between PIM-SM domains  
![](figure/en-us_image_0000001595010638.png)

**Table 2** Multicast service deployment between PIM-SM domains
| Deployment Protocol | Application Location | Purpose |
| --- | --- | --- |
| PIM-SM  (mandatory) | All interfaces of Layer 3 multicast devices in the PIM-SM domains, including all interfaces of DeviceA to DeviceF.  For configuration details, see [PIM Configuration](vrp_pim_cfg_0000.html). | Sends multicast data from Source1 and Source2 to DeviceF, which is connected to the multicast receiver. In PIM-SM, the receiver host proactively joins a multicast group, and then multicast data is sent to the receiver host through the RP. |
| IGMP  (mandatory) | User-side interfaces of Layer 3 multicast device DeviceF in the PIM-SM domains.  For configuration details, see [IGMP Configuration](vrp_igmp_cfg_0001.html). | Allows receiver hosts to join or leave multicast groups, and allows DeviceF to maintain and manage group memberships. |
| MSDP  (mandatory) | RPs (DeviceC and DeviceD) in PIM-SM domains.  For configuration details, see [MSDP Configuration](vrp_msdp_cfg_0001.html). | Transmits multicast data between PIM-SM1 and PIM-SM2. Host in PIM-SM2 can receive data from Source1. |
| IGMP snooping & IGMP Snooping Proxy  (optional) | VLAN on DeviceG between the Layer 3 multicast device and user host.  For details, see Configuring IGMP Snooping. | IGMP snooping listens to IGMP messages exchanged between DeviceF and Host to create a Layer 2 multicast forwarding table. This allows the Layer 2 device to manage and control the forwarding of multicast data messages on the Layer 2 network.  IGMP snooping proxy allows the Layer 2 device to act as a substitute for DeviceF to send IGMP Query messages and as a substitute for Host to send IGMP Report and Leave messages. |