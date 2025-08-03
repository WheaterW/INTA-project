Configuring Y.1731 Functions in EVPN Networking
===============================================

This section describes how to configure Y.1731 functions including one-way frame delay measurement, two-way frame delay measurement, Single-ended SLM in EVPN networking.

#### Networking Requirements

Ethernet virtual private network (EVPN) is used for Layer 2 internetworking. EVPN is similar to BGP/MPLS IP VPN. Using extended BGP reachability information, EVPN implements MAC address learning and advertisement between Layer 2 networks at different sites on the control plane instead of on the data plane. To take accurate statistics about frame loss on one end of an AC in EVPN networking, the performance monitoring functions defined by Y.1731 can be used to monitor links.

**Figure 1** Networking diagram for configuring Y.1731 function in EVPN networking  
![](images/fig_dc_vrp_cfg_01151601.png)  


#### Pre-configuration Tasks

Before configuring Y.1731 functions in EVPN networking, complete the tasks listed as following.

* Completing EVPN-related configurations on PEs
* Completing CFM-related configurations on CEs


[Binding an MA to an EVPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011551.html)

Binding an MA to an EVPN is a prerequisite for configuring one-way frame delay measurement, two-way frame delay measurement.

[Configuring Single-ended Frame Loss Measurement in EVPN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_y1731_cfg_0082.html)

In EVPN networking scenarios where CFM is enabled, if CCMs are not used for link connectivity monitoring to minimize their impact on the network, you can configure single-ended frame loss measurement to measure frame loss rates and monitor link quality.

[Configuring Dual-ended Frame Loss Measurement in EVPN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_y1731_cfg_0083.html)

In EVPN networking where CFM is enabled to monitor link connectivity, if accurate frame loss measurement needs to be performed for a link, configure dual-ended frame loss measurement to monitor the quality of the link.

[Configuring One-way Frame Delay Measurement in EVPN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011553.html)

In EVPN networking, the clock frequencies between the two ends are synchronized and CFM is enabled to monitor link connectivity. If the unidirectional delay measurement needs to be performed for a link, one-way frame delay measurement can be configured to monitor the quality of the link.

[Configuring Two-way Frame Delay Measurement in EVPN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011552.html)

In EVPN networking, the clock frequencies between the two ends are not synchronized and CFM is enabled to monitor link connectivity. If the bidirectional delay measurement needs to be performed for a link, two-way frame delay measurement can be configured to monitor the quality of the link.

[Configuring Single-ended SLM in EVPN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011554.html)

To perform frame loss performance measurement on a point-to-multipoint or multipoint-to-multipoint links, deploy single-ended synthetic loss measurement (SLM) to monitor the link quality.

[Configuring the ETH-Test Function for an EVPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011555.html)

The ETH-test function is short for Ethernet test signal. ETH-test instances are performed for a unidirectional on-demand service or during an on-demand-service interruption to calculate parameters, including the maximum bandwidth, frame loss ratio, and bit error rate.

[Configuring AIS in EVPN Networking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011556.html)

Configuring AIS prohibits a MEP in an MD of a higher level from sending the same alarm as that sent by a MEP in an MD of a lower level to the NMS.

[Configuring the ETH-LCK Function for EVPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_011557.html)

The ETH-LCK function notifies the server-layer (sub-layer) MEP of an administrative lock event. Then the data sent to the MEP is interrupted.