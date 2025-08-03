Configuring BGP4+ Hierarchical Routing
======================================

Configuring BGP4+ Hierarchical Routing

#### Context

In [Figure 1](#EN-US_TASK_0000001130622398__fig15656118122417), DeviceA imports a large number of external routes. To ensure fast route convergence in the case of a device or link failure, BGP4+ hierarchical routing can be deployed on DeviceA, and hierarchical routing convergence can be deployed on other nodes.

**Figure 1** Fault scenario  
![](figure/en-us_image_0000001130782232.png)

#### Prerequisites

Before configuring BGP4+ hierarchical routing, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Procedure

* Configure DeviceA.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create a route-policy node and enter the route-policy view.
     
     
     ```
     [route-policy](cmdqueryname=route-policy+node) route-policy-name matchMode node node
     ```
  3. Exit the route-policy view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  4. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  5. Enter the IPv6 unicast address family view.
     
     
     ```
     [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
     ```
  6. Configure base and hierarchical routes.
     
     
     ```
     [hierarchy-convergence base-route](cmdqueryname=hierarchy-convergence+base-route+hierarchy-route+all) ipv6-address ipv6-mask-length hierarchy-route { all | route-policy policy-name }
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     Base routes and hierarchical routes must be BGP4+ routes.
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure Spine11.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Enter the IPv6 unicast address family view.
     
     
     ```
     [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
     ```
  4. Enable the hierarchical routing convergence function.
     
     
     ```
     [hierarchy-convergence enable](cmdqueryname=hierarchy-convergence+enable)
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

After completing the configuration, perform the following operations to verify it:

* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) *ipv6-address* [ *mask-length* ] command on the peer end to check the BGP IPv6 routing table.