Configuring a Method for IPv6 IS-IS to Process Equal-Cost Routes
================================================================

Configuring a Method for IPv6 IS-IS to Process Equal-Cost Routes

#### Prerequisites

Before configuring the method for IPv6 IS-IS to process equal-cost routes, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

When multiple redundant links exist on an IPv6 IS-IS network, multiple equal-cost routes may exist. IPv6 IS-IS load balancing can be configured to improve link utilization and prevent network congestion caused by link overload. IPv6 IS-IS load balancing evenly distributes traffic among multiple equal-cost paths. [Figure 1](#EN-US_TASK_0000001562825921__fig238461885815) shows the typical networking for load balancing.

**Figure 1** Typical networking of IPv6 IS-IS load balancing  
![](figure/en-us_image_0000001514168328.png)

* DeviceA, DeviceB, DeviceC, and DeviceD run IS-IS for IP interworking.
* DeviceA, DeviceB, DeviceC, and DeviceD all belong to area 10 and are Level-2 routing devices.
* Without load balancing, traffic from DeviceA is always transmitted along the optimal route obtained using the SPF algorithm, which may cause load imbalance. If load balancing is enabled on DeviceA, traffic to DeviceD is balanced between DeviceB and DeviceC, which relieves the load on the link of the optimal route.

Load balancing can be implemented per packet or per flow. IPv6 IS-IS supports load balancing among routes in either the same process or different processes.

Load balancing improves link utilization on a network, but traffic is forwarded randomly, which may affect service traffic management. To resolve this issue, you can configure a weight for each equal-cost route to indicate a priority and specify the maximum number of routes for load balancing. In this case, the specified number of routes with high priorities are preferentially selected for load balancing, with others functioning as backups. This solution does not require any modification on the original configuration. In addition, this solution ensures network reliability and facilitates service traffic management.


#### Procedure

* Configure IPv6 IS-IS load balancing.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) [ process-id ]
     ```
  3. Enable IPv6 for the IS-IS process.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  4. Configure the maximum number of equal-cost routes for load balancing.
     
     
     ```
     [ipv6 maximum load-balancing](cmdqueryname=ipv6+maximum+load-balancing) number
     ```
     
     By default, load balancing is supported, and a maximum of 64 equal-cost routes can participate in load balancing.
     
     When the number of equal-cost routes is greater than the number specified in the [**ipv6 maximum load-balancing**](cmdqueryname=ipv6+maximum+load-balancing) command, valid routes are selected for load balancing based on the following criteria:
     1. Route weight: Routes with small weight values (high priority) are selected for load balancing.
     2. Next-hop system ID: If routes have the same weight, those with small system IDs are selected for load balancing.
     3. Outbound interface index: If routes have the same weight and system ID, those with small outbound interface indexes are selected for load balancing.
     4. Next-hop IP address: If the weights, next-hop system IDs, and local outbound interface indexes of the routes are the same, their next-hop IP addresses are compared. The routes with high IP addresses are selected for load balancing.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure weights for equal-cost IPv6 IS-IS routes.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) [ process-id ]
     ```
  3. Enable IPv6 for the IS-IS process.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  4. Configure a weight for an equal-cost IPv6 IS-IS route.
     
     
     ```
     [ipv6 nexthop](cmdqueryname=ipv6+nexthop) ip-address weight weight-value
     ```
     
     
     
     By default, no weight is set for equal-cost IPv6 IS-IS routes. The lower the *weight-value*, the higher the priority.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

* Run the **display isis route** [ *process-id* | **vpn-instance** *vpn-instance-name* ] **ipv6** [ **verbose** | [ **level-1** | **level-2** ] | *ipv6-address* [ *prefix-length* ] ] command to check IPv6 IS-IS routing information.
* Run the **display isis lsdb** [ **verbose** | { **level-1** | **level-2** } | { **local** | *lspid* | **is-name** *isname* } ] [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check IS-IS LSDB information.