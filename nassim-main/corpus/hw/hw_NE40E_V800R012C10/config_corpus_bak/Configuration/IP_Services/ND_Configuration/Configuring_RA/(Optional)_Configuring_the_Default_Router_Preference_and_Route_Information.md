(Optional) Configuring the Default Router Preference and Route Information
==========================================================================

RA messages that carry the default router preference and route information can be advertised on the local link to help hosts select a proper Router for packet forwarding.

#### Context

If a host is connected to multiple Routers, the host must select a Router to forward packets based on the destination addresses of packets. In this case, the Router can advertise the default router preference and specified route information to the host, allowing the host to select a proper forwarding Router based on the destination addresses of packets.

After receiving the RA messages carrying the route information, the host updates its routing table. When sending packets to another device, the host queries the routing table and selects a proper route to send packets.

When receiving the RA messages that carry the default router preference, the host updates its default router list. When sending packets to another device, if there is no route to be selected, the host queries this list. Then, the host selects a Router with the highest preference on the local link to send packets. If the Router is faulty, the host selects another Router in descending order of preference.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run **ipv6 enable**
   
   
   
   IPv6 is enabled.
4. Run [**ipv6 nd ra preference**](cmdqueryname=ipv6+nd+ra+preference) { **high** | **medium** | **low** }
   
   
   
   A default router preference is configured for RA messages.
5. Run [**ipv6 nd ra route-information**](cmdqueryname=ipv6+nd+ra+route-information) *ipv6-address* *prefix-length* **lifetime** *route-lifetime* [ **preference** { **high** | **medium** | **low** } ]
   
   
   
   Route information is configured for RA messages.