Configuring Y.1731 Functions in VLAN Networking
===============================================

This section describes how to config Y.1731 functions including single-ended frame loss measurement, dual-ended frame loss measurement, one-way frame delay measurement, two-way frame delay measurement, AIS, and multicast MAC ping in VLAN networking.

#### Usage Scenario

On the VLAN networking shown in [Figure 1](#EN-US_TASK_0172362095__fig_dc_vrp_cfg_01152501), the Y.1731 functions can be used to monitor links between the CEs.

**Figure 1** Typical Y.1731 deployment scenario  
![](images/fig_dc_vrp_cfg_01152501.png)  


#### Pre-configuration Tasks

Before configuring Y.1731 functions in VLAN networking, complete the following tasks:

* Completing VLAN-related configurations on the peer MEPs
* Completing CFM-related configurations on the peer MEPs and configuring the type of the peer MEPs as outward


[Binding an MA to a VLAN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011526.html)

Binding an MA to a VLAN is a prerequisite for configuring single-ended frame loss measurement, dual-ended frame loss measurement, one-way frame delay measurement, or two-way frame delay measurement in VLAN networking.

[Configuring Single-ended Frame Loss Measurement in VLAN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011527.html)

In VLAN networking, CFM is enabled. CCMs are not used to monitor link connectivity, preventing them from using a lot of network bandwidth resources. If accurate frame loss measurement needs to be performed for a link, single-ended frame loss measurement can be configured to monitor the link quality.

[Configuring Dual-ended Frame Loss Measurement in VLAN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011528.html)

In VLAN networking, if CFM is enabled to monitor link connectivity, and accurate frame loss measurement needs to be performed for a link, dual-ended frame loss measurement can be configured to monitor the quality of the link.

[Configuring One-way Frame Delay Measurement in VLAN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011529.html)

In VLAN networking, the clock frequencies between the two ends are synchronized and CFM is enabled to monitor link connectivity. If the unidirectional delay measurement needs to be performed for a link, one-way frame delay measurement can be configured to monitor the quality of the link.

[Configuring Two-way Frame Delay Measurement in VLAN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011530.html)

In VLAN networking, the clock frequencies between the two ends are not synchronized and CFM is enabled to monitor link connectivity. If the bidirectional delay measurement needs to be performed for a link, two-way frame delay measurement can be configured to monitor the quality of the link.

[Configuring Single-ended SLM in VLAN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_y1731_cfg_0068.html)

This section describes how to configure single-ended synthetic loss measurement (SLM) in virtual local area network (VLAN) networking. To collect performance statistics for frame loss on point-to-multipoint or multipoint-to-multipoint links, deploy single-ended SLM, which helps monitor link quality.

[Configuring the ETH-Test Function for a VLAN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_y1731_cfg_0069.html)

The ETH-test function is short for Ethernet test signal. ETH-test instances are performed for a unidirectional on-demand service or during an on-demand-service interruption to calculate parameters, including the maximum bandwidth, frame loss ratio, and bit error rate.

[Configuring AIS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011546.html)

Configuring AIS prohibits a MEP in an MD of a higher level from sending the same alarm as that sent by a MEP in an MD of a lower level to the NMS.

[Enabling the ETH-BN Receiving Function for a VLAN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_y1731_cfg_0078.html)

When routing devices connect to microwave devices, enable the ETH-BN receiving function to implement association with the microwave bandwidth.