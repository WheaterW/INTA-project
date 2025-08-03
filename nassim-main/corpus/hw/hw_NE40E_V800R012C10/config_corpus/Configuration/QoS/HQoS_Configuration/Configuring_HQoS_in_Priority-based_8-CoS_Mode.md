Configuring HQoS in Priority-based 8-CoS Mode
=============================================

HQoS in priority-based 8-CoS mode allows you to configure priority mappings, traffic shaping parameters, and scheduling weights for FQs based on network requirements.

#### Context

When a user has multiple services with different priorities, traffic needs to be uniformly scheduled based on service priorities. Each user has a maximum of eight service flows, that is, eight FQs with different priorities. They are BE, AF1, AF2, AF3, AF4, EF, CS6, and CS7.

**Table 1** Default settings of an FQ profile
| FQ | Priority | Weight |
| --- | --- | --- |
| BE | 3 | 10 |
| AF1 | 2 | 10 |
| AF2 | 2 | 10 |
| AF3 | 1 | 10 |
| AF4 | 1 | 10 |
| CS6 | 0 | 10 |
| CS7 | 0 | 10 |
| EF | 0 | 10 |



#### Pre-configuration Tasks

Before configuring HQoS in priority-based 8-CoS mode, complete the following tasks:

* Configure the physical parameters and link attributes of interfaces to ensure that they work properly.
* Configure IP addresses for interfaces.
* Configure IP routes on the device to ensure link connectivity.


[Configuring an FQ Profile in Priority-based 8-CoS Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_5011_1.html)

You can configure priorities, scheduling parameters, and traffic shaping parameters for FQs based on network requirements.

[Configuring a GQ Profile in Priority-based 8-CoS Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_5011_3.html)

You can configure a shaping value and token bucket depth for a priority-based GQ.

[(Optional) Configuring a Service Profile](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_5011_5.html)

You can configure a network header length in a service profile to compensate a processed packet with the length, precisely controlling traffic.

[Configuring User Queues Based on a QoS Profile](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_5011_6.html)

A QoS profile is the aggregate of QoS scheduling parameters. You can configure scheduling parameters and bandwidth values for user queues or bind an FQ profile.

[Applying a QoS Profile](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_5011_7.html)

You can define a QoS profile and apply it to interfaces to implement unified scheduling of traffic on these interfaces.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_50173.html)

After HQoS in priority-based 8-CoS mode is configured on an interface, you can view information about queues and packet statistics on the interface.