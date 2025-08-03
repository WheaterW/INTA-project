Configuration Precautions for LLDP
==================================

Configuration Precautions for LLDP

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| The lldp enable command is mutually exclusive with the link-protocol transport lldp command. Ensure that the lldp enable command is not run in the system view or interface view to enable LLDP when LLDP-based PW transparent transmission is configured on an interface. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In an E-Trunk active-active scenario, only the LLDP neighbor on one side is displayed for an Eth-Trunk sub-interface. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |