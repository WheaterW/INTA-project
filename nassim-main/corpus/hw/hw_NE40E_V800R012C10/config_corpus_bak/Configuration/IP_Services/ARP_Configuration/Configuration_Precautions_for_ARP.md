Configuration Precautions for ARP
=================================

Configuration_Precautions_for_ARP

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Proxy ARP anyway is mutually exclusive with routed proxy ARP, intra-VLAN proxy ARP, inter-VLAN proxy ARP, and local proxy ARP. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Intra-VLAN proxy ARP determines whether VLAN information meets proxy requirements based on the ARP entries of the source and destination IP addresses. Therefore, if the ARP entry of a destination IP address does not exist, the device broadcasts ARP request packets in the VLAN to learn the ARP entry of the destination IP address. If proxy ARP is enabled on multiple devices on the network but the destination IP address does not exist, the ARP broadcast triggers the same proxy process on other devices. This process repeats, causing a severe broadcast storm. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Inter-VLAN proxy ARP checks whether the VLAN information of both ends meets the proxy requirements based on the ARP entries of the source and destination IP addresses. Therefore, if the ARP entry of a destination IP address does not exist, the device broadcasts ARP requests to all VLANs (for example, all sub-VLANs of a super VLAN) to learn the ARP entry of the destination IP address. If proxy ARP is enabled on multiple switches on the network but the destination IP address does not exist, ARP broadcast triggers the same proxy process on other switches. This process cycles and will cause severe broadcast storms. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Proxy ARP does not take effect on gratuitous ARP packets. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| ARP fast reply supports only the following interface types: Layer 3 Ethernet main interface, Ethernet sub-interface, VLANIF interface, Layer 3 Eth-Trunk interface, Eth-Trunk sub-interface, dot1q VLAN tag termination sub-interface, QinQ VLAN tag termination sub-interface, L2VPN accessing L3VPN VE interface, Eth-Trunk dot1q VLAN tag termination sub-interface, and Eth-Trunk QinQ termination sub-interfaces. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In a dual-device ARP hot backup scenario, sub-interfaces bound to the same RBP cannot be added to the same VLAN. If sub-interfaces are bound to the same RBP and added to the same VLAN, entries cannot be correctly backed up between dual devices.  You are advised to plan services properly. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |