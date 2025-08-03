Configuring Y.1731 Functions in BD EVPN Networking
==================================================

This section describes how to configure Y.1731 functions including one-way frame delay measurement, two-way frame delay measurement, and single-ended SLM in BD EVPN networking.

#### Usage Scenario

Ethernet virtual private network (EVPN) is used for Layer 2 internetworking. EVPN is similar to BGP/MPLS IP VPN. Using extended BGP reachability information, EVPN implements MAC address learning and advertisement between Layer 2 networks at different sites on the control plane instead of on the data plane. To take accurate statistics about frame loss on one end of an AC in BD EVPN networking, the performance monitoring functions defined by Y.1731 can be used to monitor links.

**Figure 1** Configuring Y.1731 functions in BD EVPN networking  
![](images/fig_dc_vrp_cfg_01151601.png)  


#### Pre-configuration Tasks

Before configuring Y.1731 functions in EVPN networking, complete the tasks listed as following.

* Completing BD EVPN-related configurations on PEs
* Completing CFM-related configurations on CEs


[Binding an MA to a BD](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011571.html)

Binding an MA to a BD is a prerequisite for configuring single-ended frame loss measurement, dual-ended frame loss measurement, one-way frame delay measurement, two-way frame delay measurement in BD EVPN networking.

[Configuring Dual-ended Frame Loss Measurement in BD EVPN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011578.html)

In BD EVPN networking where CFM is enabled to monitor link connectivity, if accurate frame loss measurement needs to be performed for a link, configure dual-ended frame loss measurement to monitor the quality of the link.

[Configuring Single-ended Frame Loss Measurement in BD EVPN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011579.html)

In BD EVPN networking scenarios where CFM is enabled, if CCMs are not used for link connectivity monitoring to minimize their impact on the network, you can configure single-ended frame loss measurement to measure frame loss rates and monitor link quality.

[Configuring One-way Frame Delay Measurement in BD EVPN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011573.html)

In BD EVPN networking, the clock frequencies between the two ends are synchronized and CFM is enabled to monitor link connectivity. If the unidirectional delay measurement needs to be performed for a link, one-way frame delay measurement can be configured to monitor the quality of the link.

[Configuring Two-way Frame Delay Measurement in BD EVPN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011572.html)

In BD EVPN networking, if the clocks of the MEPs at both ends of a link are not synchronized and the requirement for delay measurement is not high, two-way frame delay measurement can be configured for the link.

[Configuring Single-ended SLM in BD EVPN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011574.html)

To perform frame loss performance measurement on a point-to-multipoint or multipoint-to-multipoint links, deploy single-ended synthetic loss measurement (SLM) to monitor the link quality.

[Configuring the ETH-Test Function in BD EVPN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011575.html)

The ETH-test function is short for Ethernet test signal. ETH-test instances are performed for a unidirectional on-demand service or during an on-demand-service interruption to calculate parameters, including the maximum bandwidth, frame loss ratio, and bit error rate.

[Configuring AIS in BD EVPN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011576.html)

Configuring AIS prohibits a MEP in an MD of a higher level from sending the same alarm as that sent by a MEP in an MD of a lower level to the NMS.

[Configuring the ETH-LCK Function in BD EVPN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011577.html)

The ETH-LCK function notifies the server-layer (sub-layer) MEP of an administrative lock event. Then the data sent to the MEP is interrupted.