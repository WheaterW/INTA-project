Configuring MF Classification-based Traffic Policies for VLAN Packets
=====================================================================

This section describes how to configure MF classification-based traffic policies for VLAN packets.

#### Context

To manage or limit the traffic that goes into or flows in a network according to the class of service, you need to configure QoS traffic policies based on MF classification. That is, you need to provide differentiated services according to the VLAN attributes of packets. In this way, traffic from different users, such as voice services, video services, and data services can be served differently in terms of bandwidth, delay, and precedence. After VLAN QoS is used for the traffic entering the VLAN network, the traffic can either retain its QoS attributes of the previous network, or has its QoS attributes modified according to the configurations of the VLAN. In this manner, the traffic continues to be transmitted in the VLAN.

MF classification-based traffic policies are usually configured on the Router located at the edge of a network, whereas BA classification-based traffic policies are configured on the Router located near the core of a network.


#### Pre-configuration Tasks

Before configuring MF classification-based traffic policies for VLAN packets, you need to complete the following tasks:

* Configure physical parameters for interfaces.
* Configure link layer attributes for interfaces.
* Configure IP addresses for interfaces.


[Configuring Rules for Mapping VLAN Frame Priorities](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0093.html)

This section describes how to configure the rule for mapping VLAN frame priorities.

[Configuring VLAN Priorities](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0094.html)

This section describes how to configure the VLAN priorities.

[Configuring a Traffic Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0095.html)

After defining traffic classifiers and behaviors, you need to configure a traffic policy to associate them.

[Applying a Traffic Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_2050.html)

A class-based policy does not take effect unless it is applied to an interface.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0097.html)

After VLAN QoS is successfully configured, you can view the traffic classifiers, traffic behaviors, binding between traffic classifiers and behaviors in the specified traffic policy, configured traffic policies and their application, and configured queues and their application.