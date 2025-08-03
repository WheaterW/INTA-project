Configuring BGP RPD
===================

RPD provides a new method of distributing route-policies. It can work with the controller to efficiently and dynamically deploy route-policies.

#### Usage Scenario

In a MAN ingress or IGW scenario, uneven link resource usage or link faults may cause link congestion. To make full use of network bandwidth, you can deploy an inbound traffic optimization solution to adjust route priorities so that traffic is diverted to idle links. In such a scenario, the Router functions as a forwarder, and RPD needs to be deployed on it.

In [Figure 1](#EN-US_TASK_0172366281__fig_dc_vrp_bgp_cfg_410401), an inbound traffic optimization solution is deployed so that traffic from AS 200 to the backbone network is monitored and scheduled in real time. If the link from Device C to Device A is congested, the traffic enters AS 100 through Device B and reaches the backbone network by path of the PE.

**Figure 1** Typical networking of inbound traffic optimization  
![](images/fig_dc_vrp_bgp_cfg_410401.png)

In this scenario, forwarders adjust route attributes based on the traffic optimization policies delivered by the controller. This ensures that routes are advertised based on the traffic optimization policies, which are configured on the controller based on traffic application. The following describes how to perform operations on the local device (forwarder).


#### Pre-configuration Tasks

Before configuring BGP RPD, complete the following tasks:

* [Configure basic BGP functions](dc_vrp_bgp_cfg_3004.html), and establish a connection between the device and the controller to ensure routing reachability between them.

#### Procedure

* Configure basic RPD functions.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**rpd-family**](cmdqueryname=rpd-family)
     
     
     
     RPD is enabled, and the BGP RPD address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+enable) *ipv4-address* **enable**
     
     
     
     The device is enabled to exchange routing information with the specified peer.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     The BGP view is displayed.
  6. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  7. Run [**peer**](cmdqueryname=peer+rpd-policy+export+enable) *ipv4-address* **rpd-policy export enable**
     
     
     
     The RPD export route-policy function is enabled in the IPv4 unicast address family view.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure GR to prevent the traffic interruption caused by a protocol restart.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**graceful-restart**](cmdqueryname=graceful-restart)
     
     
     
     GR is enabled in the BGP view.
  4. Run [**rpd-family**](cmdqueryname=rpd-family)
     
     
     
     The BGP RPD address family view is displayed.
  5. Run [**peer**](cmdqueryname=peer+graceful-restart+static-timer) *ipv4-address* **graceful-restart static-timer** *restart-time*
     
     
     
     GR is enabled in the BGP RPD address family, and a GR restart timer is set.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure router ID-based filtering on non-RRs in the RR scenario so that the non-RRs only accept the RPD routes that match the router ID of the local BGP process. If a large number of RPD routes are accepted, a large number of policy nodes are generated accordingly, which reduces the performance.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**rpd-family**](cmdqueryname=rpd-family)
     
     
     
     The BGP RPD address family view is displayed.
  4. Run [**router-id filter**](cmdqueryname=router-id+filter)
     
     
     
     Router ID-based filtering is enabled.
* (Optional) Configure a delay for the protocol to apply an updated RPD route-policy after the controller notifies the local device of the RPD route update.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**rpd-policy change notify-delay**](cmdqueryname=rpd-policy+change+notify-delay) *delay-time*
     
     
     
     A delay is configured for the RPD route-policy to take effect.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer+rpd+export-policy) *ipv4-address* **rpd export-policy** command to check RPD route-policies.
* Run the [**display bgp rpd routing-table**](cmdqueryname=display+bgp+rpd+routing-table) command to check information about RPD routes.