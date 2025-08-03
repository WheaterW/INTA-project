Configuring Centralized MAP-E
=============================

Configuring Centralized MAP-E

#### Centralized Scenario

In a centralized scenario, the MAP-BR and BRAS reside on different devices. The BRAS functions deliver MAP addresses and mapping rules to MAP-CEs in DHCPv6 IA\_PD mode. Router A functioning as the MAP-BR resides on the edge of a MAP domain and allows MAP-CEs to access the public IPv4 network through the IPv6 network that is within the MAP domain. The MAP-CEs use each other's public IPv4 address to communicate through the MAP-BR.

**Figure 1** Centralized MAP-E  
![](images/fig_dc_ne_map_cfg_0030.png)

#### Configuration Roadmap

In the centralized scenario, MAP-E must be configured on the BRAS and MAP-BR.


[Configuring a BRAS](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0043.html)



[Configuring a MAP-BR](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0044.html)



[Verifying the MAP-E Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0020.html)

After configuring basic MAP-E functions, verify the configurations.