Configuration Precautions for ERPS (G.8032)
===========================================

Configuration Precautions for ERPS (G.8032)

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| There is no restriction on the software. To achieve good convergence performance, ITU-T recommends that each ERPS ring contain a maximum of 16 nodes and the total ring length be less than or equal to 1200 km. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| ERPS can be associated only with outward-facing MEPs.  The association does not take effect in other scenarios.  You are advised to ensure that the associated MEP is outward-facing. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| erps vpls-subinterface enable: enables an interface to instruct its VSI-bound sub-interfaces to update ARP and MAC entries after receiving TC packets. This function applies to QinQ mapping1:1, vlan-type dot1q, QinQ stacking, and dot1q termination sub-interfaces. MAC entries in a VSI can be cleared for allowed sub-interface types. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| To enable an interface to instruct its BD-bound sub-interfaces to update ARP and MAC entries after receiving TC packets, run the erps bd-subinterface enable command. This function allows sub-interfaces with single-tagged encapsulation and without policies to update ARP and MAC entries. Allowed sub-interface types clear only MAC address entries and ARP entries in the local BD. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |