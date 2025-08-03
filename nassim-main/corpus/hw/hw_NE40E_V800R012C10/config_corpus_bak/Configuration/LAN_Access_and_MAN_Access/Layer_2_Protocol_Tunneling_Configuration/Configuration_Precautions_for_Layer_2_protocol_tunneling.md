Configuration Precautions for Layer 2 protocol tunneling
========================================================

Configuration_Precautions_for_Layer_2_protocol_tunneling

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| The L2PT BPDU and BPDU tunnel functions are mutually exclusive:  1. The values of <group-mac> in the l2protocol-tunnel group-mac <group-mac> and bpdu-tunnel stp group-mac <group-mac> commands in the system view cannot be the same.  2. The l2protocol-tunnel stp enable and bpdu-tunnel enable commands are mutually exclusive in the interface view. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When STP/RSTP/MSTP is not enabled on a Layer 2 interface, the default action to be taken on BPDUs/BPDU08s is discard. When STP/RSTP/MSTP is enabled on a Layer 2 interface, the default action to be taken on BPDUs/BPDU08s is send.  1. When STP is disabled on a Layer 2 main interface, the VLAN service cannot forward BPDU/BPDU08s.  2. After STP is disabled on a Layer 2 main interface, sub-interfaces of the interface cannot forward BPDU/BPDU08s if VLL/VPLS/BD/EVPN services are configured on the sub-interfaces.  3. When STP is disabled on a Layer 2 main interface, the L2PT function for BPDUs is unavailable on both the main interface and its sub-interfaces.  It is advised to run the stp bpdu bridge enable command in the system view. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After the STP, LACP, LLDP, and ETOAM services are enabled, the transparent transmission function of the corresponding protocol does not take effect. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When STP/RSTP/MSTP is disabled on a main interface, the default action to be taken on protocol packets with the destination MAC address 0180-C200-0008 is discard.  It is advised to run the stp bpdu bridge enable command in the system view. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When STP/RSTP/MSTP is not enabled on a main interface and a common sub-interface accesses VPLS/VLL, the default action for protocol packets with the destination MAC address of 0180-C200-0000 is discard.  It is advised to run the stp bpdu bridge enable command in the system view. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When STP/RSTP/MSTP is not enabled on a main interface and the main interface accesses VPLS/VLL, the default action for protocol packets with the destination MAC address of 0180-C200-0000 is discard.  It is advised to run the stp bpdu bridge enable command in the system view. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |