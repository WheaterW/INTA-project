Configuring DS-Lite Security
============================

DS-Lite security can be implemented by setting the maximum number of DS-Lite sessions that can be established and the rate at which the first packet is sent to create a flow for a specific user.

#### Usage Scenario

You can deploy the DS-Lite security function to guarantee secure operations of a DS-Lite device and prevent attacks to the system.


#### Pre-configuration Tasks

Before you configure the DS-Lite security function, complete the following tasks:

* Configure basic DS-Lite functions.
* Configure DS-Lite translation for user traffic.


[Setting the Limit on the Number of Forward DS-Lite Sessions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0039.html)

A forward session is established for packets transmitted from the user side to the network side. To prevent individual users from consuming excessive session table resources to cause connection failures of other users, enable the limit on the number of forward DS-Lite sessions.

[Setting the Limit on the Number of Reverse DS-Lite Sessions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0040.html)

A reverse session is established for packets transmitted from the network side to the user side. To prevent network-side devices from consuming excessive session table resources to cause connection failures of other network-side devices, enable the limit on the number of reverse DS-Lite sessions.

[Setting the Limit on the Number of DS-Lite Ports](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0041.html)

To prevent individual users from consuming excessive port resources to cause the connection failure of other users, you can enable the limit on the number of DS-Lite ports. 

[Setting the Maximum Number of Private Network Users Sharing the Same Public IP Address](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0069.html)

In PAT mode, multiple uses can use the same public IP address for access. However, excessive users may lead to network congestion. To address this issue, you can set the maximum number of private network users sharing the same public IP address.

[Setting the Rate at Which Packets Are Sent to Create a Flow for a User](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0044.html)

A device can be configured to dynamically detect the traffic forwarding rate and limit the rate at which user sessions are created so that a certain proportion is maintained between the forwarding rate and the session creation rate.

[Setting the Limit on the Rate at Which the First Packet Is Sent to Create a Flow](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0045.html)

Limiting the rate at which the first packet is sent to create a session prevents users from occupying a large number of CPU resources through first packet attacks, which would otherwise affect common traffic forwarding.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0046.html)

After configuring the DS-Lite security functions, you can run **display** commands to verify the configuration.