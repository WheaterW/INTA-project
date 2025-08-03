Configuring a VLAN Tag Termination Sub-interface to Transmit the VPN Service
============================================================================

Virtual private network (VPN) services are classified into L2VPN services and L3VPN services. You can configure VLAN tag termination sub-interfaces on the PEs for VPN access to enable the interworking between the CEs.

#### Usage Scenario

[Table 1](#EN-US_TASK_0172363261__tab_dc_vrp_qinq_cfg_001201) shows a typical application scenario in which VLAN tag termination sub-interfaces transmit VPN services.

**Table 1** VLAN tag termination sub-interfaces transmitting VPN services
| VPN Service | Application |
| --- | --- |
| L2VPN | When a VLAN tag termination sub-interface is used to access a L2VPN network, this sub-interface needs to be bound to a Virtual Switching Instance (VSI) or virtual private wire service (VPWS) to enable Layer 2 communication. |
| L3VPN | When a VLAN tag termination sub-interface is used to access an L3VPN network, this sub-interface needs to be bound to a VPN instance to enable Layer 3 communication. |

#### Pre-configuration Tasks

Before you configure a VLAN tag termination sub-interface to transmit IP services, plan user VLANs so that packets received by the VLAN tag termination sub-interface carry one or two VLAN tags.



[Configuring a VLAN Tag Termination Sub-interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0013.html)

A virtual local area network (VLAN) tag termination sub-interface can be a dot1q VLAN tag termination sub-interface or a QinQ VLAN tag termination sub-interface. In dot1q/QinQ termination, a device identifies whether a packet has one tag or two tags. The device then forwards the packet after stripping one or both tags or discards the packet.

[(Optional) Configuring a PW-Tag Action](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0057.html)

This section describes how to configure a PW-tag action so that a PE changes the P-Tag of packets to be forwarded over a PW in tagged mode to ensure normal communication with non-Huawei devices on an L2VPN network.

[Configuring VPN Services](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0014.html)

After you configure the VLAN tag termination sub-interface, you need to configure VPN services so as to enable users to communicate with each other over an L2VPN or an L3VPN.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0015.html)

After you configure VPN services on the VLAN tag termination sub-interface, verify the configuration.