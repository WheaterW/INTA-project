Configuration Precautions for EVC
=================================

Configuration_Precautions_for_EVC

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| An EVC sub-interface cannot access a BD that has both an EVPN and a VNI configured. When the EVC sub-interface accesses the BD and this BD also has the EVPN and VNI accessed, traffic forwarding may be abnormal. Extract the following configuration models:  1. An EVC accesses a BD, and the BD accesses an EVPN.  2. An EVC accesses a BD, and the BD accesses a VXLAN network.  3. A BD accesses an EVPN and a VXLAN. You do not need to create an EVC to access the BD.  Determine the application scenario and select one from the preceding three scenarios. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When an EVC main interface and an EVC default sub-interface coexist, services on the EVC default sub-interface take effect, but services on the EVC main interface do not take effect.  You are advised to plan services properly. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| MAC address learning in qualify mode in a BD is not supported in the scenario where EVPN interworks with VPLS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Static MAC addresses cannot be learned in qualify mode in a BD. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Learning of the same MAC address in qualify mode in a BD requires the outer VLAN to be unique in the BD after the sub-interface VLAN changes. This ensures that traffic with the same MAC address is isolated between different interfaces. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In EVPN L2 access to L3 scenarios:  L2VE EVC sub-interfaces do not support the default encapsulation type or the flexible access encapsulation type. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |