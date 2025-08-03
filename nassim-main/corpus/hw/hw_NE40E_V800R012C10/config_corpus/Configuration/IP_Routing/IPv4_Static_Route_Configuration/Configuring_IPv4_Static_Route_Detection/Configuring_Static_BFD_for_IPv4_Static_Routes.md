Configuring Static BFD for IPv4 Static Routes
=============================================

Static BFD for IPv4 static routes enables devices to fast detect link changes, improving network reliability.

#### Usage Scenario

To use BFD sessions to provide link detection for IPv4 static routes on the public network, you can bind IPv4 static routes to BFD sessions. One IPv4 static route can be bound to one BFD session.

Optimal IPv4 static routes are delivered to the forwarding table for packet forwarding. However, IPv4 static routes cannot detect the status of the link to the next hop. You can bind IPv4 static routes to BFD sessions. A BFD session can fast detect changes over a link and inform the routing management system of the changes. The routing management system immediately deletes the IPv4 static route that is bound to the BFD session from the forwarding table and recalculates another active route. In this manner, fast route convergence is implemented.


#### Pre-configuration Tasks

Before configuring static BFD for IPv4 static routes, complete the following tasks:

* Configure parameters of the link layer protocol and IP addresses for interfaces and ensure that the link layer protocol on the interfaces is Up.

#### Procedure

* Configure a BFD Session.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is globally enabled.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     The system view is displayed.
  4. Run [**bfd**](cmdqueryname=bfd) *session-name* **bind** **peer-ip** *peer-ip*
     
     
     
     The binding between a BFD session and a peer IP address is created and the BFD session view is displayed.
  5. Run [**discriminator**](cmdqueryname=discriminator) **local** *discr-value*
     
     
     
     The local discriminator of a static BFD session is set.
  6. Run [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value*
     
     
     
     The remote discriminator of a static BFD session is set.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     For details of optional procedures when configuring BFD session, see the *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - Network Reliability*.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Associating an IPv4 Static Route with a BFD Session.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run either of the following commands as required:
     
     
     + Run [**ip route-static**](cmdqueryname=ip+route-static) *ip-address* { *mask* | *mask-length* } { *nexthop-address* | *interface-type* *interface-number* [ *nexthop-address* ] | **vpn-instance** *vpn-instance-name* *nexthop-address* } **track bfd-session** *cfg-name* [ **description** *text* ]
       
       A BFD session is bound to an IPv4 static route on the public network.
     + Run [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } { *nexthop-address* | *interface-type* *interface-number* [ *nexthop-address* ] | **vpn-instance** *vpn-instance-name* *nexthop-address* } **track bfd-session** *cfg-name* [ **description** *text* ]
       
       A BFD session is bound to an IPv4 static route on the VPN network.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

Run the following commands to check the previous configuration.

* Run the [**display bfd session**](cmdqueryname=display+bfd+session) { **all** | **discriminator** *discr-value* } [ **verbose** ] command to check information about the BFD session.
* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) | **include** **bfd** command to check the configuration of BFD for static routes.
  
  You can check the information about a BFD session only after parameters of the BFD session are set and the BFD session is established.
  
  If a BFD session has been established, the status of the BFD session is Up. Run the [**display current-configuration**](cmdqueryname=display+current-configuration) | **include** **bfd** command in the system view, and you can see that the BFD session has been bound to a static route.