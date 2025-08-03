Configuring a VRRP Group to Track a Route Monitoring Group
==========================================================

This section describes how to configure a VRRP group to track a route monitoring group. By tracking a route monitoring group, the VRRP group can perform a master/backup switchover after a specified number of routes in the route monitoring group are withdrawn or deactivated. This shortens the duration of traffic interruptions.

#### Prerequisites

Before configuring a VRRP group to track a route monitoring group, you have configured a route monitoring group as described in [Configuring a Route Monitoring Group](dc_vrp_cfg_route_rmg_0005.html).


#### Context

To prevent the loss of service traffic resulting from the withdrawal or deactivation of an uplink route, configure a VRRP group to track the uplink route. Note that a VRRP group can track only one VRRP-disabled route. This means that the configuration workload is very heavy if there are many such routes to track.

To reduce the configuration workload, you can add multiple VRRP-disabled routes to a route monitoring group, and then enable a VRRP group to track the route monitoring group. When the rate of route failures within the route monitoring group reaches a specified threshold, the VRRP group performs a master/backup switchover to ensure reliable service transmission.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface where the VRRP group resides is displayed.
3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **track** **route-monitor-group** *route-monitor-group-name* **failure-ratio** *failure-ratio-value* [ **link** | [ **reduced** *priority-value* ] ]
   
   
   
   The VRRP group is configured to track a route monitoring group. If the rate of route failures on the access or network side reaches a specified threshold, the VRRP group performs a master/backup switchover.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.