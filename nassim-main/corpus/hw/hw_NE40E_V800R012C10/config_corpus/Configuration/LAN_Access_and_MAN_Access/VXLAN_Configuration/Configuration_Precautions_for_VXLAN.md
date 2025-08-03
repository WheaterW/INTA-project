Configuration Precautions for VXLAN
===================================

Configuration Precautions for VXLAN

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| A VXLAN tunnel does not support MTU configuration, and packets cannot be fragmented before entering the VXLAN tunnel. Although packets entering a VXLAN tunnel can be fragmented based on the MTU of the outbound interface, the outbound VXLAN tunnel node can reassemble only a few packets. Therefore, you need to properly plan the MTU of the network-side interface to prevent packets from being fragmented after entering the VXLAN tunnel. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Restrictions of EVPN control plane of VXLAN networks are as follows:  1. BDs, VNIs, and EVPNs support only 1:1 binding.  2. A BD must be bound to a VNI before being bound to an EVPN.  3. VNI peer statistics collection and VNI statistics collection use the same statistical resource and cannot be configured together. Traffic statistics by VNI+peer support only the split-horizon-mode of VNIs, and do not support common VNIs. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Restrictions for VXLAN dual-active access are as follows:  1. Currently, only Eth-Trunk interfaces are supported for active-active reliability.  2. Active-active reliability does not support shutdown of sub-interfaces. (Upstream Eth-Trunk traffic is not switched. As a result, traffic is interrupted.) Downstream local bias pruning is based on the main interface and does not switch the process.)  3. The shutdown bd scenario is not supported.  4. The configurations of active-active interfaces must be the same.  5. Dynamic ESIs are not supported.  6. After MAC FRR is enabled, MAC addresses are deleted because MAC addresses need to be learned in FRR format. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When a VXLAN tunnel is bound to a VNI, the VNI is bound to a BD, and a VBDIF interface is created to function as a Layer 3 gateway, the VXLAN tunnel does not support the multicast function on the VBDIF interface. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| VNI-based HQoS supports only level-3 scheduling (GQ, SQ, and FQ), and does not support DP and VI level scheduling.  Configuring interface-based HQoS is recommended. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Only two VXLANv4 fragments can be reassembled on the same board. Inter-board reassembly is not supported. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| VXLAN tunnels with the same VNI do not support both IPv4 and IPv6.  If IPv4 and IPv6 VXLAN tunnels coexist between two devices:  1. Packets are preferentially transmitted over the IPv4 VXLAN tunnel.  2. Packet loss or excess packets may occur during tunnel switching. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| IPv6 VXLAN tunnels do not support packet redundancy avoidance during BUM traffic switchback. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After a BD accesses a VSI or VXLAN, Layer 2 sub-interfaces cannot be bound to the BD. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| VXLAN does not meet DHCP snooping requirements. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After a BD accesses a VSI or VXLAN, a VBDIF interface cannot be created. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| If an EVPN instance has been bound to a BD, the binding relationship between the EVPN instance and VNI cannot be modified or deleted. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| If the number of VXLAN tunnels exceeds the upper limit, new tunnels cannot be created, and an alarm is generated to notify the user of the tunnel creation failure cause. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After a distributed gateway is configured, you need to specify the non-gateway IP address of the local device as the source IP address of ICMP Echo Request packets to be sent when pinging the host address from the gateway. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| A VNI can be bound to only one service instance (BD/VRF/EVPL). | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |