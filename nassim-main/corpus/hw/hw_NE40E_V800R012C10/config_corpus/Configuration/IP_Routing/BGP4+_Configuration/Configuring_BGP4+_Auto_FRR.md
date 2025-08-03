Configuring BGP4+ Auto FRR
==========================

As a protection measure against link faults, BGP4+ Auto Fast Reroute (FRR) is applicable to the network topology with primary and backup links. BGP4+ Auto FRR is applicable to services that are very sensitive to packet loss and delays.

#### Usage Scenario

As networks evolve continuously, voice, on-line video, and financial services raise increasingly high requirements for real-time performance. Usually, primary and backup links are deployed on a network to ensure the stability of these services. In a traditional forwarding mode, the Router selects a route out of several routes that are bound for the same destination network as the optimal route and delivers the route to the FIB table to guide data forwarding. If the optimal route fails, the Router has to wait for route convergence to be completed before reselecting an optimal route and delivering it to the FIB table. In this case, services are interrupted for a long time, unable to meet service requirements.

As a protection measure against link failures, BGP Auto fast reroute (FRR) is applicable to networks with primary and backup links. With BGP Auto FRR, if the primary link fails, the device rapidly switches services to the backup link without waiting for the completion of route convergence. In this manner, services are interrupted only for a short period of time (subsecond level).

With BGP Auto FRR, if there are multiple valid routes to the same destination network, BGP Auto FRR uses the optimal route as the primary link to forward packets and automatically adds suboptimal route forwarding information to the backup forwarding entry of the optimal route as a backup link. If the primary link fails, the system rapidly responds to the notification that the BGP route is unreachable and switches the forwarding path to the backup link.


#### Pre-configuration Tasks

Before configuring BGP4+ Auto FRR, complete the following tasks:

* Configure static route or an IGP to ensure that IP routes between routers are reachable.
* [Configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family+unicast) **unicast**
   
   
   
   The BGP-IPv6 unicast address family view is displayed.
4. Perform either of the following operations to enable BGP4+ Auto FRR for unicast routes:
   * To enable only BGP4+ Auto FRR for unicast routes, run the [**auto-frr**](cmdqueryname=auto-frr) command.
   * To enable BGP4+ Auto FRR for unicast routes and configure the function of preferentially selecting the SRv6 BE path of the primary route as the backup path, run the [**auto-frr best-effort**](cmdqueryname=auto-frr+best-effort) command.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table+longer-match+verbose) *ipv6-address* *prefix-length* [ **longer-match** ] [ **verbose** ] command to check the backup forwarding information in the routing table.