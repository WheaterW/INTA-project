(Optional) Configuring L2TP HQoS
================================

L2TP HQoS helps refined control over the L2TP service traffic.

#### Usage Scenario

In an L2TP service wholesale scenario, a LAC is responsible only for the service wholesale, whereas an LNS is responsible for service control. An L2TP tunnel is set up between the LAC and the LNS. To implement refined control over L2TP tunnel traffic, HQoS can be performed on the LNS. This prevents service quality deterioration cause by disordered competition over service flows between the LAC and LNS and allows carriers to control the traffic of different services
that enter the backbone network, thereby limiting traffic bursts of different users in tunnels.


#### Pre-configuration Task

Before configuring L2TP HQoS, complete the following tasks:

* Install a tunnel board on the NE40E.
* Configure L2TP for L2TP users to go online.


[Configuring a QoS Profile](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013491.html)

A QoS profile can be configured on an NE40E that functions as an LNS. A QoS profile contains user queue parameters and scheduling parameters. Different QoS applications can use the same QoS profile.

[Applying the QoS Profile to a Domain](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013492.html)

Before applying a QoS profile to a domain on an NE40E that functions as an LNS, ensure that a QoS profile has been created. L2TP user traffic can be scheduled only after the QoS profile is applied.

[Configuring an L2TP HQoS Scheduling Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013493.html)

In an L2TP service wholesale scenario, an LNS is the actual service control point. Therefore, an L2TP HQoS scheduling mode needs to be configured on an NE40E that functions as an LNS.

[Verifying the L2TP HQoS Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013494.html)

Through L2TP group configurations, you can verify the configured QoS profile and scheduling mode of L2TP.