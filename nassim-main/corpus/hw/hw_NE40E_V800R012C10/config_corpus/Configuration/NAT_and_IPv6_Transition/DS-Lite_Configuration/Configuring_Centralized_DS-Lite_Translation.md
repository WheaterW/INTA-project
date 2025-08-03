Configuring Centralized DS-Lite Translation
===========================================

Before configuring centralized DS-Lite for user traffic, familiarize yourself with the applicable environment, complete the pre-configuration tasks, and obtain the data required for the configuration.

#### Usage Scenario

After configuring basic DS-Lite functions and user group information, you can apply a DS-Lite traffic diversion policy in the inbound direction of the user traffic to distribute the user traffic to a DS-Lite service board. You can also apply a DS-Lite translation policy to translate the private IPv6 address in a data packet into a public IPv4 address, allowing the user to access public network services.


#### Pre-configuration Tasks

Before configuring centralized DS-Lite for user traffic, configure basic DS-Lite functions.


[Configuring a DS-Lite Traffic Diversion Policy on an Inbound Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0024.html)

A DS-Lite traffic diversion policy is configured on an inbound interface so that user traffic can be processed using DS-Lite.

[Configuring a DS-Lite Translation Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0025.html)

You can configure DS-Lite translation policies to determine whether to implement ACL-based filtering of the traffic introduced to a service board and to redistribute the traffic to different DS-Lite address pools for DS-Lite translation.

[Verifying the Centralized DS-Lite Translation Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0026.html)

After configuring a DS-Lite translation policy, you can run **display** commands to verify the configuration.