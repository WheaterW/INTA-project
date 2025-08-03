Configuring Y.1731 Functions in VPLS Networking
===============================================

This section describes how to configure Y.1731 functions including single-ended frame loss measurement, dual-ended frame loss measurement, one-way frame delay measurement, and two-way frame delay measurement in VPLS networking.

#### Usage Scenario

The VPLS technology implements MP2MP VPN networking, and therefore there may be multiple PWs between devices in the same VSI. As shown in [Figure 1](#EN-US_TASK_0172362078__fig_dc_vrp_cfg_01151901), the PEs are connected through a VPLS network. To collect accurate statistics about frame loss on one end of a PW or an AC in VPLS networking, the performance monitoring functions defined by Y.1731 can be used to monitor links.

**Figure 1** Networking diagram for configuring Y.1731 functions in VPLS networking  
![](images/fig_dc_vrp_cfg_01151901.png)  


#### Pre-configuration Tasks

Before configuring Y.1731 functions in VPLS networking, complete the tasks listed in [Table 1](#EN-US_TASK_0172362078__tab_dc_vrp_cfg_01151901).

**Table 1** Pre-configuration tasks for configuring Y.1731 functions in VPLS networking
| Function | Pre-configuration Tasks |
| --- | --- |
| Configuring Y.1731 functions (single-ended frame loss measurement, dual-ended frame loss measurement, one-way frame delay measurement, and two-way frame delay measurement) for an AC in VPLS networking | * Completing VPLS-related configurations on PEs  For details, see the chapter "VPLS Configuration" in the *NE40E Configuration Guide - VPN*. * Completing VLAN-related configurations on CEs * Completing CFM-related configurations and configuring the MEP type as outward |
| Configuring Y.1731 functions (single-ended frame loss measurement, dual-ended frame loss measurement, one-way frame delay measurement, and two-way frame delay measurement) for a PW in VPLS networking | * Completing VPLS-related configurations on PEs  For details, see the chapter "VPLS Configuration" in the *NE40E Configuration Guide - VPN*. * Completing CFM-related configurations and configuring the MEP type as inward |



[Binding an MA to a VPLS Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011520.html)

Binding an MA to a VPLS network is a prerequisite for configuring single-ended frame loss measurement, dual-ended frame loss measurement, one-way frame delay measurement, or two-way frame delay measurement in VPLS networking.

[Configuring Single-ended Frame Loss Measurement in VPLS Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011521.html)

In VPLS networking, CFM is enabled. CCMs are not used to monitor link connectivity, preventing them from using a lot of network bandwidth resources. If accurate frame loss measurement needs to be performed for a link, single-ended frame loss measurement can be configured to monitor the link quality.

[Configuring Dual-ended Frame Loss Measurement in VPLS Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011522.html)

In VPLS networking, CFM is enabled to monitor link connectivity. If accurate frame loss measurement needs to be performed for a link, dual-ended frame loss measurement can be configured to monitor the quality of the link.

[Configuring One-way Frame Delay Measurement in VPLS Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011523.html)

In VPLS networking, the clock frequencies between the two ends are synchronized and CFM is enabled to monitor link connectivity. If the unidirectional delay measurement needs to be performed for a link, one-way frame delay measurement can be configured to monitor the quality of the link.

[Configuring Two-way Frame Delay Measurement in VPLS Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011524.html)

In VPLS networking, if the clocks of the MEPs at both ends of a link are not synchronized and the requirement for delay measurement is not high, two-way frame delay measurement can be configured for the link.

[Configuring Single-ended SLM in VPLS Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_y1731_cfg_0065.html)

To perform frame loss performance measurement on a point-to-multipoint or multipoint-to-multipoint links, deploy single-ended synthetic loss measurement (SLM) to monitor the link quality.

[Configuring the ETH-Test Function for a VPLS Connection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_y1731_cfg_0066.html)

The ETH-test function is short for Ethernet test signal. ETH-test instances are performed for a unidirectional on-demand service or during an on-demand-service interruption to calculate parameters, including the maximum bandwidth, frame loss ratio, and bit error rate.

[Configuring AIS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011545.html)

Configuring AIS prohibits a MEP in an MD of a higher level from sending the same alarm as that sent by a MEP in an MD of a lower level to the NMS.