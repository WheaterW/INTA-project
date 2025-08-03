Configuring DHCPv4 Proxy
========================

Configuring_DHCPv4_Proxy

#### Usage Scenario

To guarantee the security of a DHCPv4 server, you need to enable DHCPv4 proxy when the DHCPv4 packet sent from the NE40E to a user does not contain the DHCPv4 server IP address.

DHCPv4 proxy can be used in the scenario shown in [Figure 1](#EN-US_TASK_0172373788__fig_dc_ne_ipv4_address_cfg_016801).

* The DHCPv4 server can receive DHCPv4 Discovery and Request packets that are forwarded by the NE40E and carry the IP address of the NE40E as the source address.
* The user can receive the DHCPv4 Offer packet with the source address being the IP address of the NE40E and obtain an IP address allocated by the DHCPv4 server to access the network.

**Figure 1** Networking diagram of DHCPv4 proxy

  
![](figure/en-us_image_0257534283.png)  




#### Pre-configuration Tasks

[Configure a DHCPv4 server group.](dc_ne_ipv4_address_cfg_0033.html)


[Enabling DHCPv4 Proxy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0169.html)

To improve DHCPv4 server security, the NE40E is required not to contain real DHCPv4 server addresses in DHCPv4 packets sent to users. To meet this requirement, configure DHCPv4 proxy.