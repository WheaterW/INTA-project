Configuring MF Classification-based Traffic Policies for VXLAN Packets
======================================================================

This section describes how to configure MF classification-based traffic policies for VXLAN packets.

#### Context

MF classification-based traffic policies can be configured to provide differentiated services for VXLAN packets based on parameters of the packets, such as the DSCP value, protocol type, IP address, and port number, to meet services' requirements on bandwidth and delay.

MF classification-based traffic policies are usually configured on the Router located at the edge of a network, whereas BA classification-based traffic policies are configured on the Router located near the core of a network.


#### Pre-configuration Tasks

Before configuring MF classification-based traffic policies for VXLAN packets, complete the following tasks:

* Configure a VXLAN tunnel.
* Bind a VNI to a BD/VPN.


[Configuring a Traffic Classifier](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0127.html)

You need to configure a traffic classifier before configuring class-based QoS. The traffic classifier can be configured based on the ACL rule, IP precedence, and so on.

[Defining a Traffic Behavior and Configuring Actions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0128.html)

This section describes the traffic behaviors supported by a device and how to configure actions for a traffic behavior.

[Configuring a Traffic Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0129.html)

After defining traffic classifiers and behaviors, you need to configure a traffic policy to associate them.

[Applying a Traffic Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0130.html)

A class-based traffic policy takes effect only after being applied to a BD/VPN.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0132.html)

After MF classification-based traffic policies for VXLAN packets are successfully configured, you can check the traffic classifiers, traffic behaviors, bindings between traffic classifiers and behaviors in the specified traffic policy, configured traffic policies and their application, as well as configured queues and their application.