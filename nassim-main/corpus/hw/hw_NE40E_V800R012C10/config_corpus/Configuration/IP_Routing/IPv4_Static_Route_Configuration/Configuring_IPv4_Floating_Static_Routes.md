Configuring IPv4 Floating Static Routes
=======================================

Configuring IPv4 floating static routes helps to implement route backup and improve network reliability.

#### Usage Scenario

If there is a route to a specific destination, you can configure a static route with a low preference to implement route backup, which improves network reliability. This static route with a lower preference is called a floating static route. It is activated to forward packets only when the optimal route fails. When the optimal route recovers, this static route becomes inactive.

Floating static routes are used as follows:

* Two static routes with the same destination address but different priorities are configured, and the one with the lower priority functions as a backup.
* When a route of a dynamic routing protocol to a destination address exists, you can configure a static route to the destination address for data service forwarding temporarily if the dynamic routing protocol restarts.

#### Pre-configuration Tasks

Before configuring IPv4 floating static routes, configure link layer protocol parameters and IP addresses for interfaces and ensure that the status of the link layer protocol on the interfaces is Up.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run either of the following commands as required:
   
   
   * To configure an IPv4 floating static route on the public network, run the [**ip route-static**](cmdqueryname=ip+route-static) *ip-address* { *mask* | *mask-length* } { *nexthop-address* | *interface-type* *interface-number* [ *nexthop-address* ] | **vpn-instance** *vpn-instance-name* *nexthop-address* } [ **preference** *preference* | **tag** *tag* ]\* [ **description** *text* ] command.
   * To configure an IPv4 floating static route on a VPN, run the [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } { *nexthop-address* | *interface-type* *interface-number* [ *nexthop-address* ] | **vpn-instance** *vpn-instance-name* *nexthop-address* } [ **preference** *preference* | **tag** *tag* ]\* [ **description** *text* ] command.
   * To configure an IPv4 floating static route in a topology instance, run the [**ip route-static topology**](cmdqueryname=ip+route-static+topology) *topology-name* *ip-address* { *mask* | *mask-length* } { *nexthop-address* | *interface-type* *interface-number* [ *nexthop-address* ] } [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ] command.
   
   
   
   The **preference** parameter specifies a route priority. The greater the value, the lower the priority. Therefore, make sure that the priority value of the floating static route is greater than that of the primary route.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

After the configuration is complete, check the configuration results.

* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) *ip-address* [ *mask* | *mask-length* ] command to check configurations about the optimal IPv4 static route to the specified destination network segment.
* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) | **include** **static** command to check the configurations about the current static route.