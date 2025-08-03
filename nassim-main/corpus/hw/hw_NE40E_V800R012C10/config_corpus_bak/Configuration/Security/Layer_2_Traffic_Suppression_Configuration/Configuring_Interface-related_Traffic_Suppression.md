Configuring Interface-related Traffic Suppression
=================================================

This section describes how to configure interface-related traffic suppression.

#### Usage Scenario

In addition to user traffic management and bandwidth allocation, an Ethernet requires broadcast, multicast, and unknown unicast traffic to be suppressed to ensure the secure transmission of unicast traffic and properly utilize bandwidth resources.

Most networks require unicast traffic to be much heavier than broadcast traffic. If broadcast traffic is not suppressed, forwarding a large volume of such traffic consumes numerous bandwidth resources, reducing network performance and even causing a communication interruption.


#### Pre-configuration Tasks

Before configuring Layer 2 traffic suppression, complete the following task:

* Connect interfaces and set their physical parameters to ensure that the physical status of the interfaces is up.


[Configuring Interface-based Traffic Suppression](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_traff-supress_cfg_5004.html)

This section describes how to configure interface-based traffic suppression in order to reduce the traffic burden on a network.

[Configuring Sub-interface-based Traffic Suppression](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_traff-supress_cfg_5501.html)

This section describes how to configure sub-interface-based traffic suppression in order to reduce the traffic burden on a network.

[Configuring Interface- and VLAN-based Traffic Suppression](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_traff-supress_cfg_5007.html)

This section describes how to configure interface- and VLAN-based traffic suppression in order to reduce the traffic burden on a network.