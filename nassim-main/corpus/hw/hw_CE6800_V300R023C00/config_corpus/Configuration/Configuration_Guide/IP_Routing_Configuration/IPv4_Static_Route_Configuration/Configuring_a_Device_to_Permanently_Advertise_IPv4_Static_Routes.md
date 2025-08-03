Configuring a Device to Permanently Advertise IPv4 Static Routes
================================================================

Configuring a Device to Permanently Advertise IPv4 Static Routes

#### Context

In existing static route implementation, if a static route-related link fails, the static route is withdrawn from the routing table, routes are re-converged, and traffic is switched to another path. Permanent advertisement for static routes is designed to lock traffic to a specific path even if a link failure occurs.

After the permanent advertisement attribute is configured for IPv4 static routes, static routes that have not been advertised before the function is enabled are advertised to the routing table and participate in route selection. Specifically, the following two cases may be included:

* An outbound interface is specified for a static route and assigned an IP address. In this situation, once permanent advertisement is enabled, the static route is advertised to the routing table, regardless of whether the outbound interface is up.
* No outbound interface is specified for a static route. In this situation, once permanent advertisement is enabled, the static route is advertised to the routing table, no matter whether the static route can obtain an outbound interface in route recursion.

![](public_sys-resources/note_3.0-en-us.png) 

After permanent advertisement is enabled, static routes are retained in the IP routing table, regardless of route reachability. If the actual path is unreachable, traffic may be lost.


**Figure 1** Network diagram of permanent advertisement for IPv4 static routes  
![](figure/en-us_image_0000001176662541.png)

On the network shown in [Figure 1](#EN-US_TASK_0000001130622968__fig1889612327416), DeviceA, DeviceB, and DeviceC belong to network 1, network 2, and network 3, respectively. There are two links (link A and link B) between DeviceA and DeviceB. Network 1 requires that service traffic be forwarded directly to network 2 along link A, without passing through network 3.

A single-hop External Border Gateway Protocol (EBGP) peer relationship needs to be established between DeviceA and DeviceB. On DeviceA, a static route is configured, with the destination address set to the BGP peer DeviceB's address and the outbound interface set to a local interface directly connected to DeviceB.

Traffic is forwarded along link A. If permanent advertisement for static routes is not configured and link A fails, the dynamic routing protocol automatically calculates a route over link B and switches traffic to link B.

If permanent advertisement for static routes is configured, traffic is forwarded through link A, regardless of whether link A is reachable. If link A fails, traffic fails to be forwarded. You can ping the destination address carried in a static route to check the reachability of the static route.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an IPv4 static route and enable permanent advertisement for it.
   
   
   
   Configure a public-network IPv4 static route and enable permanent advertisement for it.
   
   
   
   ```
   [ip route-static](cmdqueryname=ip+route-static) ip-address { mask | mask-length }{ nexthop-address | vpn-instance vpn-instance-name nexthop-address } permanent
   [ip route-static](cmdqueryname=ip+route-static) ip-address { mask | mask-length } interface-type interface-number nexthop-address permanent
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The CE6885-LL in low latency mode does not support [**ip route-static**](cmdqueryname=ip+route-static) *ip-address* { *mask* | *mask-length* } { *nexthop-address* | **vpn-instance** *vpn-instance-name* *nexthop-address* } **permanent**.
   
   Configure an IPv4 static route in a VPN instance and enable permanent advertisement for it.
   
   ```
   [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name destination-address { mask | mask-length } { interface-name | interface-type interface-number } nexthop-address permanent
   [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name destination-address { mask | mask-length } vpn-instance vpn-destination-name nexthop-address permanent
   [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name destination-address { mask | mask-length } nexthop-address permanent
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The CE6885-LL in low latency mode does not support [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } { *interface-name* | *interface-type* *interface-number* } *nexthop-address* **permanent**, [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } ****vpn-instance**** **vpn-destination-name* *nexthop-address** **permanent**, or [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } *nexthop-address* **permanent**.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check information about routes with permanent advertisement enabled in the IPv4 routing table.