Configuring Static BFD for IPv6 Static Routes
=============================================

Static BFD for IPv6 static routes enables devices to fast detect link changes, improving network reliability.

#### Usage Scenario

To use BFD sessions to provide link detection for IPv6 static routes on the public network, you can bind IPv6 static routes to BFD sessions. One IPv6 static route can be bound to one BFD session.

Optimal IPv6 static routes are delivered to the forwarding table for packet forwarding. However, IPv6 static routes cannot detect the status of the link to the next hop. You can bind IPv6 static routes to BFD sessions. A BFD session can fast detect changes over a link and inform the routing management system of the changes. The routing management system immediately deletes the static route that is bound to the BFD session from the forwarding table and recalculates another active route. In this manner, fast route convergence is implemented.


#### Pre-configuration Tasks

Before configuring static BFD for IPv6 static routes, complete the following tasks:

* Configure link layer protocol parameters and IP addresses for interfaces and ensure that the link layer protocol on the interfaces is up.

#### Procedure

1. Configure a BFD Session.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**bfd**](cmdqueryname=bfd)
      
      BFD is globally enabled.
   3. Run [**quit**](cmdqueryname=quit)
      
      The system view is displayed.
   4. Run [**bfd**](cmdqueryname=bfd) *session-name* **bind peer-ipv6** *peer-ipv6*
      
      The binding between a BFD session for IPv6 and a peer IPv6 address is created, and the BFD session view is displayed.
   5. Run [**discriminator**](cmdqueryname=discriminator) **local** *discr-value*
      
      The local discriminator of a static BFD session is set.
   6. Run [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value*The remote discriminator of a static BFD session is set.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      For details of optional procedures for configuring a BFD session, see the *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - Network Reliability*.
   7. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
2. Associate an IPv6 static route with a BFD session.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run either of the following commands as required:
      
      * Run [**ipv6 route-static**](cmdqueryname=ipv6+route-static) *dest-ipv6-address* *prefix-length* { *interface-type* *interface-number* [ *nexthop-ipv6-address* ] | **vpn-instance** *vpn-instance-name* *nexthop-ipv6-address* | *nexthop-ipv6-address* } [ **preference** *preference* | **tag** *tag* ] \* **track** **bfd-session** *cfg-name* [ **description** *text* ]
        
        A BFD session is bound to an IPv6 static route on the public network.
      * Run [**ipv6 route-static vpn-instance**](cmdqueryname=ipv6+route-static+vpn-instance) *vpn-source-name* *dest-ipv6-address* *prefix-length* { *interface-type* *interface-number* [ *nexthop-ipv6-address* ] | **vpn-instance** *vpn-destination-name* [ *nexthop-ipv6-address* ] | *nexthop-ipv6-address* [ **public** ] } [ **preference** *preference* | **tag** *tag* ]\* **track** **bfd-session** *cfg-name* [ **description** *text* ]
        
        A static BFD session is bound to an IPv6 static route on the VPN network.
   3. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.

#### Verifying the Configuration

After configuring static BFD for IPv6 static routes, verify the configuration.

* Run the [**display bfd session**](cmdqueryname=display+bfd+session) { **all** | **discriminator** *discr-value* } [ **verbose** ] command to check information about BFD sessions.
* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) | **include** **bfd** command to check configurations of BFD for IPv6 static routes.
  
  Information about a BFD session can be viewed only after parameters of the BFD session are set and the BFD session is established.
  
  If a BFD session has been established, the status of the BFD session is up. Run the [**display current-configuration**](cmdqueryname=display+current-configuration) | **include** **bfd** command in the system view, and you can see that the BFD session has been bound to a static route.