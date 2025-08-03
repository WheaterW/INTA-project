Configuring IP Services on a VLAN Tag Termination Sub-Interface
===============================================================

IP services include proxy Address Resolution Protocol (ARP), Virtual Router Redundancy Protocol (VRRP), and Dynamic Host Configuration Protocol (DHCP) services. You can deploy IP services on QinQ/dot1q VLAN tag termination sub-interfaces so that users in different VLANs can communicate. This ensures non-stop and reliable connections between the users and the network.

#### Usage Scenario

[Table 1](#EN-US_TASK_0172363255__tab_dc_vrp_qinq_cfg_000801) shows the applications of VLAN tag termination sub-interfaces transmitting IP services.

**Table 1** Application of VLAN tag termination sub-interfaces transmitting IP services
| IP service | Application |
| --- | --- |
| Proxy ARP | A range of VLANs can access the same network segment through VLAN tag termination sub-interfaces. However, if users on the same network segment belong to different VLANs, these users cannot communicate at Layer 2, and rely on IP forwarding at Layer 3 to communicate with each other. You can configure VLAN tag termination sub-interfaces to support proxy ARP so that users from different VLANs can communicate. |
| DHCP | * To assign IP addresses to users on a VLAN tag termination sub-interface, the DHCP server function needs to be enabled on this sub-interface. * If the DHCP client and DHCP server belong to different sub-nets, you need to deploy a DHCP relay agent to forward DHCP request packets from the client to the server so that the client can dynamically obtain IP addresses from the DHCP server.  DHCP relay can be configured on the VLAN tag termination sub-interface to insert tag information into Option82. The tag information provides a reference for the DHCP server in IP address allocation. |
| VRRP | Users may require communication with certain networks at any time. Running VRRP on the VLAN tag termination sub-interfaces ensures reliable communication and provides an active/standby mechanism for dot1q or QinQ users. |


![](../../../../public_sys-resources/note_3.0-en-us.png) 

Proxy ARP, VRRP and DHCP are different types of IP services. Deploy the desired service on the VLAN tag termination sub-interface.

#### Pre-configuration Tasks

Before you configure a VLAN tag termination sub-interface to transmit IP services, plan user VLANs so that packets received by the VLAN tag termination sub-interface carry one or two VLAN tags.



[Configuring a VLAN Tag Termination Sub-interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0009.html)

A virtual local area network (VLAN) tag termination sub-interface can be a dot1q VLAN tag termination sub-interface or a QinQ VLAN tag termination sub-interface. In dot1q/QinQ termination, a device identifies whether a packet has one tag or two tags. The device then forwards the packet after stripping one or both tags or discards the packet.

[Configuring IP Services](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0010.html)

After a VLAN tag termination sub-interface is configured, you need to configure IP services so that users can access IP services using the VLAN tag termination sub-interface.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0011.html)

After configuring IP services on the VLAN tag termination sub-interface, verify the configuration.