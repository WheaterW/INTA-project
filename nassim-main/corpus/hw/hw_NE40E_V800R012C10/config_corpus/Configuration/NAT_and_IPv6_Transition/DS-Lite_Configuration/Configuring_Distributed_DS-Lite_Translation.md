Configuring Distributed DS-Lite Translation
===========================================

This section describes the applicable environment, pre-configuration tasks, and data preparation for configuring distributed DS-Lite translation.

#### Usage Scenario

After configuring basic DS-Lite functions and user group information, you can apply a DS-Lite traffic diversion policy in the inbound direction of the user traffic to distribute the user traffic to a DS-Lite service board. You can also apply a DS-Lite translation policy to translate the private IPv4 address in a packet into a public IPv4 address, allowing the user to access public network services. DS-Lite translation for user traffic is used only in distributed DS-Lite when a service board is installed on a BRAS.


#### Pre-configuration Tasks

Before configuring distributed DS-Lite translation, configure basic DS-Lite functions.


[Configuring DS-Lite User Group Information](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0019.html)

In a distributed DS-Lite scenario, a DS-Lite device identifies user traffic from each CPE by checking user identities. Therefore, DS-Lite user group information must be configured on the DS-Lite device.

[Configuring a DS-Lite Traffic Diversion Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0020.html)

You can configure a DS-Lite traffic diversion policy to distribute user traffic to DS-Lite service boards for translation.

[Configuring a DS-Lite Translation Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0021.html)

You can configure DS-Lite translation policies to determine whether to implement ACL-based filtering of the traffic introduced to a service board and to redistribute the traffic to different DS-Lite address pools for DS-Lite translation.

[Verifying the DS-Lite Translation Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0022.html)

After configuring a DS-Lite translation policy, you can run **display** commands to verify the configuration.