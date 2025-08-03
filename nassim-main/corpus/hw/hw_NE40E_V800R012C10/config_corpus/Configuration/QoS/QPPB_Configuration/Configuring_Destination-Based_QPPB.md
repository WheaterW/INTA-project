Configuring Destination-Based QPPB
==================================

Destination-based QPPB differentiates routes to different destinations and associates differentiated QoS policies with them.

#### Usage Scenario

QPPB is applicable to both IBGP and EBGP and can be configured for one or more ASs.

As shown in [Figure 1](#EN-US_TASK_0172371435__fig_dc_ne_qos_cfg_202901), traffic is transmitted from provider B (AS 200) and provider C (AS 300) to provider D (AS 400) through provider A (AS 100). Providers B and C function as BGP route senders and provider A functions as a BGP route receiver. Based on the traffic control policies that are signed between providers A and D, provider A needs to limit the rate of the traffic sent to provider D.

Providers B and C advertise BGP routes carrying the community attribute to provider A. After receiving the BGP routes, provider A matches the routes with the community list, ACL list, or AS\_Path list, and associates QoS policy IDs with QoS behaviors for the routes. Destination-based QPPB is enabled on the provider A interface that allows traffic to pass through. Therefore, QPPB local policies are applied to all traffic that passes through provider A.

Destination-based QPPB is applicable to both incoming and outgoing traffic on a device.

**Figure 1** Networking diagram for destination-based QPPB configuration  
![](images/fig_dc_ne_qos_cfg_202901.png)  


#### Pre-configuration Tasks

Before configuring QPPB, complete the following tasks:

* Configure basic BGP functions.
* Configure local network routes advertised by BGP.
* Configure interfaces for setting up a BGP connection.


[Configuring Routing Policies on a BGP Route Sender](../../../../software/nev8r10_vrpv8r16/user/ne/adc_ne_qos_cfg_2030.html)

This section describes how to configure a route-policy on a route sender.

[Configuring Routing Policies on a BGP Route Receiver](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_2040.html)

This section describes how to configure routing policies on a BGP route receiver.

[Configuring Traffic Behaviors on a Route Receiver](../../../../software/nev8r10_vrpv8r16/user/ne/adc_ne_qos_cfg_2032.html)

You can configure different traffic behaviors for different traffic classifiers on a BGP receiver to implement differentiated services.

[Configuring a QPPB Local Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_2041.html)

QPPB allows QoS policies to be configured for routes that match the BGP community list, ACL, or BGP AS\_Path list. After the QPPB local policy is applied to the inbound and outbound interfaces of traffic, relevant QoS policies are implemented on the traffic.

[Applying a QPPB Local Policy to an Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_2036.html)

After a QPPB local policy is applied to an interface, the associated traffic behavior is performed for the packets that meet the matching rule.

[Checking the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/adc_ne_qos_cfg_2035.html)

After QPPB is configured, you can view QPPB information.