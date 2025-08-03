Configuring Y.1731 Functions in VLL Networking
==============================================

This section describes how to configure Y.1731 functions, including single-ended frame loss measurement, dual-ended frame loss measurement, one-way frame delay measurement, and two-way frame delay measurement in VLL networking.

#### Usage Scenario

The VLL technology implements point-to-point VPN networking. As shown in [Figure 1](#EN-US_TASK_0172362057__fig_dc_vrp_cfg_01151301), the PEs are connected through a PW. To collect accurate statistics about frame loss on one end of a PW or an AC in VPLS networking, the performance monitoring functions defined by Y.1731 can be used to monitor links.

**Figure 1** Networking diagram for configuring Y.1731 functions in VLL networking  
![](images/fig_dc_vrp_cfg_01151301.png)  


#### Pre-configuration Tasks

Before configuring Y.1731 functions in VLL networking, complete the tasks listed in [Table 1](#EN-US_TASK_0172362057__tab_dc_vrp_cfg_01151301).

**Table 1** Pre-configuration tasks for configuring Y.1731 functions in VLL networking
| Function | Pre-configuration Tasks |
| --- | --- |
| Configuring Y.1731 functions (single-ended frame loss measurement, dual-ended frame loss measurement, one-way frame delay measurement, and two-way frame delay measurement) for an AC in VLL networking | * Completing VLL-related configurations on PEs  For details, see the chapter "VLL Configuration" in the *NE40E Configuration Guide - VPN*. * Completing VLAN-related configurations on CEs * Completing CFM-related configurations and configuring the MEP type as outward |
| Configuring Y.1731 functions (single-ended frame loss measurement, dual-ended frame loss measurement, one-way frame delay measurement, and two-way frame delay measurement) for a PW in VLL networking | * Completing VLL-related configurations on PEs  For details, see the chapter "VLL Configuration" in the *NE40E Configuration Guide - VPN*. * Completing CFM-related configurations and configuring the MEP type as inward |



[Binding an MA to a VLL](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011514.html)

Binding an MA to a VLL is a prerequisite for configuring single-ended packet loss measurement, dual-ended packet loss measurement, one-way packet delay measurement, two-way packet delay measurement.

[Configuring Single-ended Frame Loss Measurement in VLL Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011515.html)

In VLL networking, CFM is enabled. CCMs are not used to monitor link connectivity, preventing them from using a lot of network bandwidth resources. If frame loss measurement needs to be performed for a link, single-ended frame loss measurement can be configured to monitor the link quality.

[Configuring Dual-ended Frame Loss Measurement in VLL Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011516.html)

In VLL networking, CFM is enabled to monitor link connectivity. If accurate frame loss measurement needs to be performed for a link, dual-ended frame loss measurement can be configured to monitor the quality of the link.

[Configuring One-way Frame Delay Measurement in VLL Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011517.html)

In VLL networking, the clock frequencies between the two ends are synchronized and CFM is enabled to monitor link connectivity. If the unidirectional delay measurement needs to be performed for a link, one-way frame delay measurement can be configured to monitor the quality of the link.

[Configuring Two-way Frame Delay Measurement in VLL Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011518.html)

In VLL networking, the clock frequencies between the two ends are not synchronized and CFM is enabled to monitor link connectivity. If the bidirectional delay measurement needs to be performed for a link, two-way frame delay measurement can be configured to monitor the quality of the link.

[Configuring Single-ended SLM in VLL Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_y1731_cfg_0062.html)

This section describes how to configure single-ended synthetic loss measurement (SLM) in virtual leased line (VLL) networking. To collect performance statistics for frame loss on point-to-multipoint links or load balancing links of an Eth-Trunk interface, deploy single-ended SLM, which helps monitor link quality.

[Configuring the ETH-Test Function for a VLL](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_y1731_cfg_0063.html)

The ETH-test function is short for Ethernet test signal. ETH-test instances are performed for a unidirectional on-demand service or during an on-demand-service interruption to calculate parameters, including the maximum bandwidth, frame loss ratio, and bit error rate.

[Configuring AIS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011544.html)

Configuring AIS prohibits a MEP in an MD of a higher level from sending the same alarm as that sent by a MEP in an MD of a lower level to the NMS.