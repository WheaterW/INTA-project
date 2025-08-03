Configuring an Interface to Support PPP
=======================================

Configure an interface to support PPP so that it can implement point-to-point (P2P) traffic transmission.

#### Usage Scenario

PPP is a link layer protocol that transmits network layer packets over P2P links. PPP defines a group of protocols, including LCP and NCP.

* During the LCP negotiation phase, an MRU, negotiation timeout period, and PPP LCP link dead duration are negotiated.
* During the NCP negotiation phase, network layer packet attributes and types are negotiated. For example, during the IPCP negotiation, the IP address of a DNS server will be negotiated.

To monitor link status in real time, configure link status monitoring parameters so that link faults can be identified in time. A PPP link does not require that the peer route and local route be on the same network segment. To avoid incorrect routing information, prohibit the addition of the peer host route to the local routing table of direct routes.


#### Pre-configuration Tasks

Before configuring an interface to support PPP, connect the interface and set physical parameters to ensure that the physical status of the interface is Up.


#### Configuration Procedures

The following flowchart shows how to configure an interface to support PPP.

**Figure 1** Flowchart for configuring an interface to support PPP  
![](images/fig_dc_vrp_ppp_cfg_002701.png)


[Configuring PPP as the Link Layer Protocol of an Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ppp_cfg_0028.html)

Configure PPP as the link layer protocol of an interface for the interface to implement P2P traffic transmission.

[(Optional) Configuring PPP Negotiation Parameters](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ppp_cfg_0029.html)

For a PPP link to be established between two communicating devices that have PPP enabled, configure the following PPP negotiation parameters: MRU, negotiation timeout period, PPP LCP link dead duration, and DNS server IP address.

[(Optional) Configuring PPP Link Status Monitoring](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ppp_cfg_0030.html)

The PPP link status can be effectively monitored using the PPP link status monitoring function.

[(Optional) Prohibiting a Local Device from Adding the Peer Host Route to the Local Routing Table of Direct Routes](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ppp_cfg_0031.html)

To avoid incorrect routing information in the local routing table, you can prohibit a local device from adding the peer host route to the local routing table of direct routes.

[(Optional) Configuring the PPP Link Dampening Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ppp_cfg_0033.html)

To prevent frequent PPP link flapping from causing flapping of the link and network layers, configure the PPP link dampening function.

[Verifying the PPP Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ppp_cfg_0032.html)

After configuring PPP as the link layer protocol, verify the configuration.