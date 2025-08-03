Configuring BGP Auto FRR
========================

As a protection measure against link faults, BGP Auto FRR is applicable to networks with primary and backup links and services that are sensitive to packet loss and delay.

#### Usage Scenario

As networks evolve continuously, voice, on-line video, and financial services raise increasingly high requirements for real-time performance. Usually, primary and backup links are deployed on a network to ensure the stability of these services. In a traditional forwarding mode, the Router selects a route out of several routes that are bound for the same destination network as the optimal route and delivers the route to the FIB table to guide data forwarding. If the optimal route fails, the Router has to wait for route convergence to be completed before reselecting an optimal route and delivering it to the FIB table. In this case, services are interrupted for a long time, unable to meet service requirements.

As a protection measure against link failures, BGP Auto fast reroute (FRR) is applicable to networks with primary and backup links. With BGP Auto FRR, if the primary link fails, the device rapidly switches services to the backup link without waiting for the completion of route convergence. In this manner, services are interrupted only for a short period of time (subsecond level).

With BGP Auto FRR, if there are multiple valid routes to the same destination network, BGP Auto FRR uses the optimal route as the primary link to forward packets and automatically adds suboptimal route forwarding information to the backup forwarding entry of the optimal route as a backup link. If the primary link fails, the system rapidly responds to the notification that the BGP route is unreachable and switches the forwarding path to the backup link.


#### Pre-configuration Tasks

Before configuring BGP Auto FRR, complete the following tasks:

* [Configure basic BGP functions.](dc_vrp_bgp_cfg_3004.html)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The BGP IPv4 unicast address family view is displayed.
4. Perform either of the following operations to enable BGP Auto FRR for unicast routes:
   * To enable only BGP Auto FRR for unicast routes, run the [**auto-frr**](cmdqueryname=auto-frr) command.
   * To enable BGP Auto FRR for unicast routes and configure the function of preferentially selecting the SRv6 BE path of the primary route as the backup path, run the [**auto-frr best-effort**](cmdqueryname=auto-frr+best-effort) command. If a device is configured to preferentially select the SRv6 BE path of the primary route as the backup path and both the SRv6 TE-Policy and SRv6 BE path of the primary route are available, the device preferentially selects the SRv6 BE path of the primary route as the backup path. That is, the SRv6 BE path of the primary route has a higher priority than the backup route. If the SRv6 TE-Policy of the primary route fails, the forwarding path is rapidly switched to this SRv6 BE path.
5. (Optional) Run [**route-select delay**](cmdqueryname=route-select+delay) *delay-value*
   
   
   
   Delayed route selection is configured. After the primary path recovers, delayed route selection ensures that the device on the primary path performs route selection only after the corresponding forwarding entries on the device are stable. This prevents traffic loss during traffic switchback.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring BGP Auto FRR, verify the configuration.

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+longer-prefixes) [ *network* [ { *mask* | *mask-length* } [ **longer-prefixes** ] ] ] command to check information in the BGP routing table.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table+longer-match+verbose) [ *ip-address* [ *mask* | *mask-length* ] [ **longer-match** ] ] **verbose** command to check backup forwarding entries in the routing table.