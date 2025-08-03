VPN QoS Overview
================

VPN QoS is a mechanism that ensures each type of traffic gets the specified bandwidth by means of bandwidth limiting and queue scheduling. QoS enables different types of traffic to be scheduled based on service classes, enabling important traffic to be preferentially transmitted during traffic congestion.

#### VPN QoS

On the network shown in [Figure 1](#EN-US_CONCEPT_0172371704__fig_dc_vrp_vpn-qos_cfg_0002), a TE tunnel is established between PE1 and PE2.

The data traffic exchanged between the two nodes includes:

* Traffic transmitted over each tunnel
  + VPN traffic, such as VPN1 to VPNn traffic shown in the figure
  + Non-VPN traffic
* Public IP traffic not carried over tunnels

Bandwidth preemption is likely to occur among different types of traffic.

**Figure 1** Network diagram of VPN QoS  
![](images/fig_dc_vrp_vpn-qos_cfg_000201.png)

To ensure service quality, configure bandwidth limiting to ensure that each type of traffic gets the specified bandwidth.