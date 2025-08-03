Configuring HQoS in Common 8-CoS Mode
=====================================

HQoS in common 8-CoS mode ensures that service traffic is scheduled based on their priorities.

#### Context

When a user has multiple services with different priorities, traffic needs to be uniformly scheduled based on service priorities. Each user has a maximum of eight service flows, that is, eight flow queues (FQs) with different priorities. They are BE, AF1, AF2, AF3, AF4, EF, CS6, and CS7. By default, the system performs PQ scheduling on the FQs with the priorities of EF, CS6, and CS7. The system defaults the FQs with the priorities of BE, AF1, AF2, AF3, and AF4 to WFQ. The scheduling weight proportion is 10:10:10:15:15. You can also configure priorities and scheduling parameters for FQs based on network requirements.


#### Pre-configuration Tasks

Before configuring HQoS in common 8-CoS mode, complete the following tasks:

* Configure the physical parameters and link attributes of interfaces to ensure that they work properly.
* Configure IP addresses for interfaces.
* Configure IP routes on the device to ensure link connectivity.


[(Optional) Configuring an FQ Profile in Common 8-CoS Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_5043_a.html)

You can configure scheduling parameters and traffic shaping for FQs in common 8-CoS mode based on network requirements.

[(Optional) Configuring a GQ Profile in Common 8-CoS Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_5013_3.html)

After a user group queue (GQ) profile in common 8-CoS mode is configured and applied, the device can send traffic at an even rate.

[(Optional) Configuring a Service Profile](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_5043_5.html)

You can configure a network header length in a service profile to compensate a processed packet with the length, precisely controlling traffic.

[Configuring User Queues Based on a QoS Profile](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_5013_6.html)

A QoS profile is the aggregate of QoS scheduling parameters. You can configure scheduling parameters and bandwidth values for user queues or bind an FQ profile.

[Applying a QoS Profile](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_5013_7.html)

You can define a QoS profile and apply it to interfaces to implement unified scheduling of traffic on these interfaces.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_5013_8.html)

After profile-based HQoS is configured on an interface, you can view information about queue profiles and packet statistics on the interface.