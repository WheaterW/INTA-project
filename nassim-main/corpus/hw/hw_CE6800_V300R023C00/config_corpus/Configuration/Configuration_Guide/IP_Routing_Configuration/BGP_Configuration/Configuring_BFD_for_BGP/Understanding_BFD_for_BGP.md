Understanding BFD for BGP
=========================

The application of Bidirectional Forwarding Detection (BFD) in BGP enables fast link fault detection. BGP periodically sends Keepalive messages to a peer to monitor its status. This process takes more than one second, and can lead to lengthy fault detection when traffic is transmitted at gigabit rates. As a result, packet loss occurs, and the carrier-grade network requirements for high reliability are not met.

To address this issue, BFD for BGP has been introduced. Specifically, BFD is used to quickly detect faults on links between BGP peers (usually within milliseconds) and notify BGP of the faults, thereby accelerating BGP route convergence.

![](public_sys-resources/note_3.0-en-us.png) 

You are not advised to configure both BFD and BGP GR on the same device. If both are configured and a BFD session detects a fault on an interface, the session exits GR. As a result, traffic forwarded based on GR is interrupted, which may cause network problems.


#### Networking

As shown in [Figure 1](#EN-US_CONCEPT_0000001130783954__fig_dc_vrp_bgp_feature_001501), DeviceA and DeviceB belong to AS 100 and AS 200, respectively. The two BGP devices are directly connected, and an EBGP connection is established between them.

BFD is enabled to detect the link between DeviceA and DeviceB. If the link between DeviceA and DeviceB fails, BFD can quickly detect the fault and notify BGP of the fault.

**Figure 1** Network diagram of BFD for BGP  
![](figure/en-us_image_0000001130784042.png)