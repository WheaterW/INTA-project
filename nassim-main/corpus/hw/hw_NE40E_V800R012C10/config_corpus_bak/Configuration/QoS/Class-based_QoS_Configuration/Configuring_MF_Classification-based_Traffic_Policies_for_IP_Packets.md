Configuring MF Classification-based Traffic Policies for IP Packets
===================================================================

This section describes how to configure MF classification-based traffic policies for IP packets.

#### Usage Scenario

As networks rapidly develop and services become increasingly diversified, multiple service flows share the same network resource. In some scenarios, incoming or ongoing traffic on a network needs to be classified and managed. For example, voice, video, and data services must be allocated different bandwidths because they have different requirements on delay, and traffic from different users must be distinguished and allocated different bandwidths and priorities. BA classification-based traffic policies fail to meet such requirements.

MF classification-based traffic policies can be configured to provide differentiated services for IP packets based on parameters of the packets, such as the DSCP value, protocol type, IP address, and port number, to meet services' requirements on bandwidth and delay.

MF classification-based traffic policies are usually configured on the Router located at the edge of a network, whereas BA classification-based traffic policies are configured on the Router located near the core of a network.


#### Pre-configuration Tasks

Before configuring MF classification-based traffic policies for IP packets, you need to complete the following tasks:

* Configure the physical parameters of interfaces.
* Configure the link layer attributes of interfaces.
* Configure IP addresses for interfaces.
* Enable the routing protocol for communication between devices at the network layer.


[Configuring a Traffic Classifier](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0042.html)

You need to configure a traffic classifier before configuring class-based QoS. The traffic classifier can be configured based on the ACL rule, IP precedence, MAC address, protocol address, and so on.

[Defining a Traffic Behavior and Configuring Actions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0043.html)

This section describes the traffic behaviors supported by a device and how to configure actions for a traffic behavior.

[Configuring a Traffic Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0044.html)

After defining traffic classifiers and behaviors, you need to configure a traffic policy to associate them.

[Applying a Traffic Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0045.html)

A class-based policy does not take effect unless it is applied to an interface.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0047.html)

After class-based QoS is successfully configured, you can check the traffic classifiers, traffic behaviors, bindings between traffic classifiers and behaviors in the specified traffic policy, configured traffic policies and their application, as well as configured queues and their application.