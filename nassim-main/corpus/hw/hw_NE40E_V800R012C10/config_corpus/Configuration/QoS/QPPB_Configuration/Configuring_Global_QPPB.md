Configuring Global QPPB
=======================

Global QPPB allows packets of the same type to be scheduled using the same traffic policy.

#### Usage Scenario

In [Figure 1](#EN-US_TASK_0172371420__fig_dc_ne_qos_cfg_202901), multiple interfaces on Device A receive packets of the same attribute and need to forward them to Device D. Customers require that the packets of the same attribute be scheduled using the same traffic policy.

**Figure 1** Networking for global QPPB configuration  
![](images/fig_dc_ne_qos_cfg_202901.png)  


#### Pre-configuration Tasks

Before configuring global QPPB, complete the following tasks:

* Configure basic BGP functions.
* Configure BGP to advertise local routes.
* Configure the interfaces used to establish BGP connections.


[Configuring Routing Policies on a BGP Route Sender](../../../../software/nev8r10_vrpv8r16/user/ne/g-dc_ne_qos_cfg_2030.html)

This section describes how to configure a route-policy on a route sender.

[Configuring Routing Policies on a BGP Route Receiver](../../../../software/nev8r10_vrpv8r16/user/ne/g-dc_ne_qos_cfg_2031.html)

This section describes how to configure routing policies on a BGP route receiver.

[Configuring a Global Traffic Policy and Enabling Global QPPB](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_8002.html)

A global traffic policy must be configured for global QPPB implementation.