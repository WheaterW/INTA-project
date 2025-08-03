Configuring Traffic Policing Based on MF Classification
=======================================================

This section describes how to configure traffic policing based on MF classification.

#### Usage Scenario

Network congestion, often resulting from users sending a large amount of data, severely affects the running and service quality of a network.

To ensure that a certain amount of bandwidth is retained regardless of whether the network is idle or congested, you can configure an MF classification-based traffic policing policy and then apply it to the inbound interface of the network. In this way, you can control one or more types of packets that enter a network and meet specific conditions, better utilizing limited network resources (losing some data does not severely affect the overall data).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

MF classification enables packets to be classified based on the source address, source port number, protocol number, destination address, and destination port number. It is usually applied at the edge of the network.



#### Pre-configuration Tasks

Before configuring traffic policing based on MF classification, complete the following tasks:

* Configure parameters for physical interfaces.
* Configure link layer attributes for interfaces to ensure their normal operating.
* Configure IP addresses for interfaces.
* Enable a routing protocol for communication between devices.


[Configuring a Traffic Classifier](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0042copy.html)

You need to configure a traffic classifier before configuring class-based QoS. The traffic classifier can be configured based on the ACL rule, IP precedence, MAC address, protocol address, and so on.

[Defining a Traffic Behavior and Configuring Traffic Policing Actions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0010.html)

This section describes how to configure traffic policing actions for different traffic classifiers.

[Defining a Traffic Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0011.html)

After traffic classifiers and traffic behaviors are defined, traffic classifiers and traffic behaviors need to be associated to form traffic policies.

[Applying a Traffic Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0012.html)

A class-based policy does not take effect unless it is applied to an interface.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_0013.html)

After traffic policing based on MF classification is successfully configured, you can check the traffic classifiers, traffic behaviors, bindings between traffic classifiers and behaviors in the specified traffic policy, configured traffic policies and their application, and configured queues and their application.