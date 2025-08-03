Configuring Basic DS-Lite Functions
===================================

This section describes how to configure basic DS-Lite functions.

#### Usage Scenario

Basic DS-Lite functions are prerequisites for DS-Lite configurations, including enhanced DS-Lite configurations. The configuration of basic DS-Lite functions includes the following operations:

* Create a DS-Lite address pool. You can define a public network IPv4 address range for a DS-Lite address pool, and assign it to the specified DS-Lite instance, enabling conversions between a private IPv4 address and a public IPv4 address.
* (Optional) Create DS-Lite policy templates: To enable a RADIUS server to issue DS-Lite configuration policies, you can predefine a DS-Lite template on a device, and define some NAT configuration policies, for example, a limit on the number of DS-Lite sessions in the template. When the RADIUS server issues a template name to the device, the device finds the configured DS-Lite template and applies it to the specified DS-Lite instance.


#### Prerequisites

Before you configure basic NAT functions, complete the following tasks:

* Verify that a service board is working properly.
* Run the [**license active**](cmdqueryname=license+active) **file-name** command to load the DS-Lite function license.
* Configure data link layer protocol parameters and IP addresses for interfaces so that the data link layer protocol on each interface can go Up.


[Binding a Service Board to a DS-Lite Instance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0011.html)

Only after a DS-Lite instance is created and bound to a DS-Lite board, can a device direct packets to the DS-Lite board and run DS-Lite to process the packets. 

[Creating a DS-Lite Tunnel](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0012.html)

This section describes how to configure a DS-Lite tunnel. A DS-Lite tunnel allows users with private IPv4 addresses to pass through IPv6-only carrier networks.

[Creating a DS-Lite Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0013.html)

A DS-Lite address pool can be created so that you can define a public IPv4 address segment for a DS-Lite address pool and assign the address pool to a specific DS-Lite instance before the instance translates between private and public IPv4 addresses.

[(Optional) Configuring an IP Address of a Next Hop to Which a Route Is Redirected](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0010.html)

This section describes how to set the IP address of a next hop to which a route is redirected.

[(Optional) Configuring a DS-Lite Port Allocation Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0014.html)

Configuring a port allocation mode helps manage port resources.

[(Optional) Configuring DS-Lite ECMP and Trunk Load Balancing](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_00015.html)

If multiple next hops are used to forward user packets destined for the same destination, configure a proper hash algorithm and its harsh factor to implement equal cost multi-path (ECMP) and trunk load balancing on a DS-Lite network.

[Verifying the Basic DS-Lite Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0017.html)

After configuring basic DS-Lite functions, verify the configuration.