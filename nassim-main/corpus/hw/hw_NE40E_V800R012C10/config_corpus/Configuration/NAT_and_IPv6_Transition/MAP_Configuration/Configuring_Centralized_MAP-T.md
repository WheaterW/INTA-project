Configuring Centralized MAP-T
=============================

Configuring Centralized MAP-T

#### Centralized Scenario

In a centralized scenario, the MAP-BR and BRAS reside on different devices. The BRAS delivers MAP addresses and mapping rules to MAP-CEs in DHCPv6 IA\_PD mode. Router A functioning as the MAP-BR resides on the edge of a MAP domain and accesses the public IPv4 network through the IPv6 network that is within the MAP domain. The MAP-CEs use each other's public IPv4 address to communicate through the MAP-BR.

**Figure 1** Centralized MAP-T  
![](images/fig_dc_ne_map_cfg_0030.png)

#### Configuration Roadmap

In the centralized scenario, MAP-T must be configured on the BRAS and MAP-BR.


[Configuring a BRAS](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0039.html)



[Configuring a MAP-BR](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0040.html)



[Verifying the MAP-T Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_map_cfg_0012.html)

After configuring basic MAP-T functions, verify the configurations.