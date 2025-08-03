Configuring UCL-based Traffic Policies
======================================

By configuring UCL-based traffic policies, you can distinguish
between users of different priorities and implement QoS on the traffic
of users. In this manner, the CIR and PIR are guaranteed for users.

#### Usage Scenario

UCL implements user-specific ACL control. During user authentication, to control traffic of some users, for example, to allow or restrict users' access to specific web pages, configure UCL-based traffic policies.

By configuring UCL-based traffic policies on the access device, you can distinguish between users of different priorities and implement QoS on traffic of the users, ensuring the Committed Information Rate (CIR) and Peak Information Rate (PIR) of users. Four types of UCL are defined based on the configuration methods: user-to-network, user-to-user, network-to-network, and network-to-user. If an ACL specifies the source user group (UG), the type of the UCL is user-to-network; if the destination UG is specified, the type of the UCL is network-to-user; if both the source UG and destination UG are specified, the type of the UCL is user-to-user; if neither the source UG or destination UG is specified, the type of the UCL is network-to-network.![](../../../../public_sys-resources/note_3.0-en-us.png) 

UCL rules can be used for IPv4 and IPv6 traffic classification. For IPv6 traffic classification, UCL rules apply only to upstream traffic.




#### Prerequisites

Before configuring UCL-based traffic policies, complete the following tasks:

* Configuring link layer protocol parameters (and IP addresses) for interfaces to ensure that the link layer protocol on the interfaces is Up
* Configuring a routing protocol on the backbone network to realize the IP interworking
* Configuring the access services to enable the users to access the Internet normally


[Configuring a User Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012785.html)

You need to create a user group before configuring UCL-based traffic policies.

[Configuring a Service Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_013877.html)

You need to create a service group before configuring UCL-based traffic policies.

[Configuring a UCL Rule](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012786.html)

You can configure UCLs based on IP bearer protocol types.

[Defining a Traffic Classifier](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012787.html)

Before configuring class-based QoS for the traffic on the network, you need to define a traffic classifier.

[Defining a Traffic Behavior and Configuring Actions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012788.html)

This section describes the traffic behaviors supported by a device and how to configure actions for a traffic behavior.

[Configuring a Traffic Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012789.html)

After defining traffic classifiers and behaviors, you need to configure a traffic policy to associate them.

[Applying UCL-based Traffic Policies](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012790.html)

After the UCL-based traffic policies are applied, the traffic of all online users is classified according to the UCL rules.

[Adding a User Group to a Domain](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012791.html)

Before applying a UCL-based traffic policy to users in a user group, add the user group to a domain.

[Configuring User Priority Mapping in a Domain](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012799.html)

You need to configure the mappings among the user priority, CoS, and color to implement QoS on packets in a domain.

[Verifying the Configuration of UCL-based Traffic Policies](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012793.html)

After UCL-based traffic policies are configured, you can view the information about the traffic policies on a specified interface or all interfaces and statistics about UCL-based traffic policies.