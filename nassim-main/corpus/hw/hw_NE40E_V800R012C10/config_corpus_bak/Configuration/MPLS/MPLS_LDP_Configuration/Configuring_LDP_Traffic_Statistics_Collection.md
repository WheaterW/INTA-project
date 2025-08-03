Configuring LDP Traffic Statistics Collection
=============================================

LDP traffic information on the ingress and transit nodes of an LSP can be queried only after LDP traffic statistics collection is configured.

#### Usage Scenario

To obtain LDP LSP traffic statistics, configure LDP traffic statistics collection.

LDP traffic statistics collection collects only forwarded traffic data. Therefore, LDP traffic statistics collection can be configured only on the ingress and transit nodes.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

LDP traffic statistics collection enables the ingress or a transit node to collect statistics only about outgoing LDP LSP traffic with the destination IP address mask of 32 bits.



#### Pre-configuration Tasks

Before configuring LDP statistics collection, [configure an LDP LSP](dc_vrp_ldp-p2p_cfg_0015.html).


[Enabling LDP Traffic Statistics Collection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0091.html)

To check LDP LSP traffic statistics, enable LDP LSP statistics collection on the ingress and transit nodes.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0092.html)

After configuring LDP statistics collection, check traffic statistics on the ingress and transit nodes.