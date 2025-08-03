Configuring IPv6 IS-IS to Import External Routes
================================================

Configuring IPv6 IS-IS to Import External Routes

#### Prerequisites

Before configuring IPv6 IS-IS to import external routes, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

If a border device of an IPv6 IS-IS routing domain is configured to advertise the default route through IS-IS, all traffic destined beyond the routing domain is forwarded by this border device because the other devices in the domain do not have external routes. As a result, this border device will be overloaded. In addition, if multiple border devices are deployed in the IPv6 IS-IS routing domain, the selected routes to other routing domains may not be optimal. To address these issues, configure the border devices to import external routes so that all the other devices in the local routing domain can learn all, or some, of the external routes from the border devices.

If the other IPv6 IS-IS devices in the local routing domain require only some of the external routes, you can configure an export policy for the border devices to advertise only the required external routes.

![](public_sys-resources/notice_3.0-en-us.png) 

IS-IS and other dynamic routing protocols such as OSPF and BGP often import routes from each other. If no routing policy is configured or a routing policy is incorrectly configured on a device where IS-IS, OSPF, and BGP import routes from each other, a Layer 3 routing loop may occur due to a route selection result change. As a result, services are compromised. For details about the cause of the routing loop, see [Understanding Routing Loop Detection for Routes Imported to IS-IS](vrp_isis_ipv4_cfg_0051.html).



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Configure IPv6 IS-IS to import external routes.
   
   
   * Configure IPv6 IS-IS to import external routes and set a cost for the imported routes.
     ```
     [ipv6 import-route](cmdqueryname=ipv6+import-route) { direct | static | { ospfv3 | ripng | isis } [ process-id ] | bgp [ permit-ibgp ] } [ cost cost | tag tag | { route-policy route-policy-name } | [ level-1 | level-2 | level-1-2 ] ] 
     ```
   * Configure the device to import external routes and retain their original costs.
     ```
     [ipv6 import-route](cmdqueryname=ipv6+import-route) { { ospfv3 | ripng | isis } [ process-id ] | bgp [ permit-ibgp ] | direct } inherit-cost [ tag tag | route-policy route-policy-name | [ level-1 | level-2 | level-1-2 ] ] 
     ```
     
     The protocol from which routes are imported cannot be **static**.
4. (Optional) Configure IPv6 IS-IS to advertise only some imported external routes to the IS-IS routing domain.
   
   
   
   By default, IS-IS advertises all imported external routes to an IS-IS routing domain. To advertise only some imported external routes to the IS-IS routing domain, perform this step.
   
   
   
   ```
   [ipv6 filter-policy](cmdqueryname=ipv6+filter-policy) { acl6-number | acl6-name acl6-name-string | ipv6-prefix ipv6-prefix-name | route-policy route-policy-name } { export [ direct | static | ripng process-id | bgp | ospfv3 process-id | isis process-id ] }
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the **display isis route** [ *process-id* | **vpn-instance** *vpn-instance-name* ] **ipv6** [ **verbose** | [ **level-1** | **level-2** ] | *ipv6-address* [ *prefix-length* ] ] command to check IPv6 IS-IS routing information.