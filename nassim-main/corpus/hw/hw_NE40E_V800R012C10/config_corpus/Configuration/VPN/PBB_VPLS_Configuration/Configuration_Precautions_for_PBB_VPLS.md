Configuration Precautions for PBB VPLS
======================================

Configuration Precautions for PBB VPLS

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| PBB VPLS does not support load balancing among BGP LSPs. When PBB VPLS recurses to two or more BGP LSPs, only one BGP LSP is selected for traffic forwarding. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| PBB VPLS does not support ECMP or TI-LFA for SR-MPLS TE tunnels. In a scenario where PBB VPLS recurses to SR-MPLS TE tunnels, ECMP or TI-LFA protection does not take effect.  Perform deployment properly. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |