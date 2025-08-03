Controlling Advertisement of L2TP Hot Backup Routes
===================================================

If L2TP hot backup is configured on LACs that work in load balancing mode, advertisement of L2TP hot backup routes can be controlled.

#### Context

LACs use loopback interfaces to establish L2TP tunnels with an LNS. After loopback interfaces are configured for LACs that work in load balancing mode, route advertisement can be controlled as follows:

* Configure a routing policy, in which the route to the loopback IP address of the master LAC has a smaller cost than the route to the loopback IP address of the backup LAC. In this way, the route to the master LAC is preferentially selected. For information about how to configure a routing policy, see [Routing Policy Configuration](../vrp/dc_vrp_route-policy_cfg_0000.html) in *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - IP Routing*.
* This control mode is complex to configure. If a fault occurs and then is rectified on the master LAC, the route to the master LAC cannot be automatically advertised, affecting service reliability. Configure a routing protocol to trust the costs of the imported routes to loopback IP addresses of the LACs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**peer-backup route-cost**](cmdqueryname=peer-backup+route-cost) **auto-advertising**
   
   
   
   The LAC is enabled to control route preference by using the default cost of the route.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

To allow the route to the loopback IP address of the master LAC to be preferentially selected, perform one of the following operations based on the used routing protocol:

* For IS-IS:
  
  Run the [**import-route**](cmdqueryname=import-route) **unr route-policy** *route-policy-name* command.
* For OSPF:
  
  Run the [**import-route**](cmdqueryname=import-route) **unr route-policy** *route-policy-name* command.
* For BGP:
  
  Run the [**import-route**](cmdqueryname=import-route) **unr route-policy** *route-policy-name* command.

To allow a routing protocol to trust the costs of imported routes to loopback IP addresses, perform one of the following operations based on the used routing protocol:

* If IS-IS is used to import direct routes, run the [**import-route**](cmdqueryname=import-route) **direct inherit-cost** command in the IS-IS view.
* If OSPF is used to import direct routes, run the following commands in the OSPF view:
  1. [**default**](cmdqueryname=default) **cost inherit-metric**
  2. [**import-route**](cmdqueryname=import-route) **direct**
* If the [**network**](cmdqueryname=network) command is used to import routes into the OSPF routing table, run the [**ospf cost**](cmdqueryname=ospf+cost) **inherit** command in the view of the loopback interface view.
* If BGP is used to import direct routes, run the [**import-route**](cmdqueryname=import-route) **direct** command in the BGP view.

(Optional) Run the [**l2tp-tunnel source**](cmdqueryname=l2tp-tunnel+source) **loopback** *loopback-num* command to configure a source L2TP tunnel interface in the RBS view so that the source interface route bound to the RBS is updated based on the link status on the network side.