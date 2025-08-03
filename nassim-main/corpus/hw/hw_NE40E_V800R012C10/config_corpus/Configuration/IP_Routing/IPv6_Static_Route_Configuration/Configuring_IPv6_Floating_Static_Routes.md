Configuring IPv6 Floating Static Routes
=======================================

Configuring floating static routes helps to implement route backup and improve network reliability.

#### Usage Scenario

If there is a route to a specific destination, you can configure a static route with a low preference to implement route backup, which improves network reliability. This static route with a lower preference is called a floating static route. It is activated to forward packets only when the optimal route fails. When the optimal route recovers, this static route becomes inactive.

Floating static routes are used as follows:

* Two static routes with the same destination address but different priorities are configured, and the one with the lower priority functions as a backup.
* When a route of a dynamic routing protocol to a destination address exists, you can configure a static route to the destination address for data service forwarding temporarily if the dynamic routing protocol restarts.

#### Pre-configuration Tasks

Before configuring IPv6 floating static routes, configure link layer protocol parameters and IP addresses for interfaces and ensure that the status of the link layer protocol on the interfaces is Up.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run either of the following commands as required:
   
   
   * Run [**ipv6 route-static**](cmdqueryname=ipv6+route-static) *dest-ipv6-address* *prefix-length* { *interface-type* *interface-number* [ *nexthop-ipv6-address* ] | **vpn-instance** *vpn-destination-name* [ *nexthop-ipv6-address* ] | *nexthop-ipv6-address* } [ **preference** *preference* | **tag** *tag* ]\* [ **description** *text* ]
     
     An IPv6 floating static route is configured in public network.
   * Run [**ipv6 route-static vpn-instance**](cmdqueryname=ipv6+route-static+vpn-instance) *vpn-source-name* *dest-ipv6-address* *prefix-length* { *interface-type* *interface-number* [ *nexthop-ipv6-address* ] | **vpn-instance** *vpn-destination-name* [ *nexthop-ipv6-address* ] | *nexthop-ipv6-address* [ **public** ] } [ **preference** *preference* | **tag** *tag* ]\* [ **description** *text* ]
     
     An IPv6 floating static route is configured in VPN network.
   * Run [**ipv6 route-static topology**](cmdqueryname=ipv6+route-static+topology) *topology-name* *dest-ipv6-address* *prefix-length* { *interface-type* *interface-number* [ *nexthop-ipv6-address* ] | *nexthop-ipv6-address* } [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]
     
     An IPv6 floating static route is configured in a non-base topology instance.
   
   The **preference** parameter specifies a route priority. The greater the value, the lower the priority. Therefore, make sure that the priority value of the floating static route is greater than that of the optimal route.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

After the configuration is complete, check the configuration results.

* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) *ipv6-address* [ *prefix-length* ] command to check configurations about the optimal IPv6 static route to the specified destination network segment.
* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) | **include** **static** command to check the configurations about the current static route.