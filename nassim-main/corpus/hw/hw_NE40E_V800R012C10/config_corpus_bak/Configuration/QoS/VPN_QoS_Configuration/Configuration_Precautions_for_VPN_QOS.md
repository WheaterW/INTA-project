Configuration Precautions for VPN QOS
=====================================

Configuration_Precautions_for_VPN_QOS

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| PBB VSIs do not support VPLS QoS. The commands for PBB VPLS and VPLS QoS are mutually exclusive, and an error message is displayed. Enabling HQoS on an interface is recommended. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Only one outbound interface of an SR-MPLS TE node tunnel supports VPN QoS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| VPLS PW HQoS/VLL PW HQoS does not support load balancing among BGP LSPs. If an HQoS-enabled VPLS/VLL PW recurses to two or more BGP LSPs, only one BGP LSP is selected for traffic forwarding. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| VPN QoS does not support ECMP or TI-LFA for SR-MPLS TE. If VPN QoS recurses to SR-MPLS TE tunnels and ECMP or TI-LFA protection is configured for the tunnels, the protection does not take effect. Proper deployment is recommended. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When the public network tunnel for VPN QoS is a TE tunnel, a TE tunnel change (for example, the TE HSB LSP goes down or up) may cause a small number of VPN packets to be lost. | NE40E-M2 | NE40E-M2K |
| Layer 2 multicast does not support VPLS QoS. Enabling HQoS on an interface is recommended. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| VPN QoS is supported only in the TE-HSB scenario. VPN QoS availability is affected if an active/standby switchover is performed in a non-TE-HSB protection scenario. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |