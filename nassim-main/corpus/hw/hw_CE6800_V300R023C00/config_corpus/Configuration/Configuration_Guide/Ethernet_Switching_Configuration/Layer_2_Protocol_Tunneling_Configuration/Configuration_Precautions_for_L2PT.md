Configuration Precautions for L2PT
==================================

Configuration Precautions for L2PT

#### License Requirements

L2PT is not under license control.


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-LL-56F (low latency mode)/CE6885-SAN-56F |
| CE8800 series | CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |



#### Feature Requirements

**Table 2** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| For the CE6800 Series:  L2PT delivers ACL rules based on the MAC address and protocol number. LACP and 802.3ah have the same MAC address and protocol number but different sub-protocol numbers. When LACP is enabled, 802.3ah packets are incorrectly sent to the CPU. Similarly, when 802.3ah is enabled, LACP packets are incorrectly sent to the CPU. | CE6800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K |
| For the CE6800 Series:  L2PT does not support MUX VLAN and voice VLAN scenarios. | CE6800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K |
| For the CE6800 Series:  1. The destination MAC addresses of STP, GVRP, and GMRP packets cannot be replaced with the same multicast MAC address.  2. The destination MAC addresses of EFM (802.3ah), LACP, and DLDP packets cannot be replaced with the same multicast MAC address.  3. When Layer 2 protocol tunneling is configured, the following multicast MAC addresses cannot be used to replace the original multicast MAC addresses of Layer 2 protocol packets:  Destination MAC address of BPDUs: 0180-C200-0000 to 0180-C200-002F  MAC addresses of Smart Link packets: 010F-E200-0004  Special multicast MAC addresses: 0100-0CCC-CCCC and 0100-0CCC-CCCD.  Common multicast MAC addresses that have been used on the device | CE6800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K |
| For the CE6800 Series:  When an interface is configured to discard BPDUs, the BPDUs cannot be redirected using a traffic policy. | CE6800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K |
| For the CE6800 Series:  To transparently transmit BPDUs on a physical interface, the outbound interface of the L2PT tunnel cannot be a trunk interface. | CE6800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K |