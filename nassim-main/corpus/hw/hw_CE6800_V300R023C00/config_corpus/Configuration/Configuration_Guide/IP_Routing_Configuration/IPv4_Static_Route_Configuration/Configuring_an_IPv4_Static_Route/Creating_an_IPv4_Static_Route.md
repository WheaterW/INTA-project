Creating an IPv4 Static Route
=============================

Creating an IPv4 Static Route

#### Prerequisites

Before creating an IPv4 static route, you have completed the following task:

* Set data link layer protocol parameters for interfaces to ensure that the data link layer protocol status of the interfaces is up.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an IPv4 static route.
   
   
   * Configure an IPv4 static route on the public network.
     ```
     [ip route-static](cmdqueryname=ip+route-static) ip-address { mask | mask-length } nexthop-address [ preference preference | tag tag ] * [ description text ]
     [ip route-static](cmdqueryname=ip+route-static) ip-address { mask | mask-length }{ interface-name | interface-type interface-number } [ nexthop-address ] [ preference preference | tag tag ] * [ description text ]
     [ip route-static](cmdqueryname=ip+route-static) ip-address { mask | mask-length } vpn-instance vpn-instance-name [ preference preference | tag tag ] * [ description text ]
     [ip route-static](cmdqueryname=ip+route-static) ip-address { mask | mask-length } vpn-instance vpn-instance-name nexthop-address [ preference preference | tag tag ] * [ description text ]
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The CE6885-LL in low latency mode does not support the [**ip route-static**](cmdqueryname=ip+route-static) *ip-address* { *mask* | *mask-length* } **vpn-instance** *vpn-instance-name* [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ] and [**ip route-static**](cmdqueryname=ip+route-static) *ip-address* { *mask* | *mask-length* } **vpn-instance** *vpn-instance-name* *nexthop-address* [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ] command.
   * Configure an IPv4 static route in a VPN instance.
     ```
     [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name destination-address { mask | mask-length }{ interface-type interface-number } [ nexthop-address ] [ preference preference | tag tag ] * [ description text ]
     [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name destination-address { mask | mask-length } nexthop-address [ public ] [ preference preference | tag tag ] * [ description text ]
     [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name destination-address { mask | mask-length } { vpn-instance vpn-destination-name | public } [ preference preference | tag tag ] * [ description text ]
     [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name destination-address { mask | mask-length } vpn-instance vpn-destination-name nexthop-address [ preference preference | tag tag ] * [ description text ]
      
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The CE6885-LL in low-latency mode does not support the [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } { **vpn-instance** *vpn-destination-name* | **public** } [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ], [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } **vpn-instance** *vpn-destination-name* *nexthop-address* [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ] command.
   
   
   
   You can set different preference values for different static routes, facilitating the flexible application of route management policies.
   
   You can configure different tag values for different static routes to classify static routes and implement different routing management policies. For example, a routing protocol can import static routes with a specified tag value through a route-policy.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If you configure a broadcast or NBMA interface as an outbound interface when configuring a static route, you must specify a next-hop address as well.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```