Configuring IP Hard Pipe
========================

IP hard pipe is a pipe technology that establishes a static
PW over a static bidirectional co-routed LSP to simulate an SDH leased
line. The NE40E strictly isolates soft and hard pipes by reserving hardware
so that the soft and hard pipes do not affect each other when carrying
leased line services of high-value customers, reserving bandwidth
and ensuring low delay for hard pipe services.

#### Usage Scenario

VPWS enables carriers to
provide L2VPN services on an IP hard pipe network over different media,
implementing P2P services over the hard pipe and enhancing leased
line services of high-value customers.


#### Pre-configuration Tasks

Before configuring
IP hard pipe, complete the following tasks:

* Configure static routes or an IGP protocol on PEs and Ps on
  the MPLS backbone network to provide IP connectivity.
* Configure a static bidirectional co-routed CR-LSP.

![](../../../../public_sys-resources/note_3.0-en-us.png) Note the following issues:

* Do not specify the bandwidth for the static bidirectional co-routed
  CR-LSP. This is because an NMS is used to assign bandwidth for CR-LSPs
  in an IP hard pipe scenario.
* The **outgoing-interface** *interface-type* *interface-number* parameter must be configured
  to specify an outbound interface of the static bidirectional co-routed
  CR-LSP.



[Configuring IP Hard Pipe Bandwidth Reservation on a Main Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_ip-hard-pipe_0001.html)

This section describes how to configure IP hard pipe bandwidth reservation on a main interface. The physical interface bandwidth on the public network is divided and allocated to both hard and soft pipes, and the bandwidth of the hard and soft pipes is isolated.

[Configuring a Static Bidirectional Co-routed LSP as a Public Network LSP over Which an IP Hard Pipe Is Established](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ip-hard-pipe_0010.html)

A static bidirectional co-routed LSP can be configured to implement public network service isolation and label forwarding for PW packets transmitted along an IP hard pipe.

[Configuring a Hard-Pipe VPWS PW](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ip-hard-pipe_0005.html)

Configuring a hard-pipe VPWS PW to carry private line services of high-value customers implements P2P services over the hard pipe.

[Configuring the Hard Pipe Function for a VPLS PW](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ip-hard-pipe_0011.html)

Configuring the hard pipe function for an LDP VPLS PW allows P2MP services to be carried over the hard-pipe static PW, enhancing private line services for high-value customers.

[(Optional) Configuring an Alarm Threshold for the Outbound Bandwidth Usage of the Soft Pipe](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_ip-hard-pipe_0005.html)

After the hard pipe is configured on the network-side or AC-side interface, you can configure an alarm threshold for the soft pipe bandwidth usage to monitor the soft pipe load on the device. When the bandwidth usage exceeds the alert or alarm threshold, the device reports an alarm to prompt users to properly plan service traffic or expand device capacity. You can set the alarm threshold and clear alarm threshold as required.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_ip-hard-pipe_0006.html)

After configuring a hard-pipe VPWS/VPLS PW, check the configurations.