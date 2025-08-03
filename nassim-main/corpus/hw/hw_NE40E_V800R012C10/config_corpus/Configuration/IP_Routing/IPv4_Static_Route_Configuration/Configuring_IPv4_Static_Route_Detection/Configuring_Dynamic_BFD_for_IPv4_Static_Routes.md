Configuring Dynamic BFD for IPv4 Static Routes
==============================================

Dynamic BFD for IPv4 static routes enables devices to fast detect link changes, improving network reliability.

#### Usage Scenario

To use BFD sessions to provide link detection for IPv4 static routes on the public network, you can bind IPv4 static routes to BFD sessions. One IPv4 static route can be bound to one BFD session.

Optimal IPv4 static routes are delivered to the forwarding table for packet forwarding. However, IPv4 static routes cannot detect the status of the link to the next hop. You can bind IPv4 static routes to BFD sessions. A BFD session can fast detect changes over a link and inform the routing management system of the changes. The routing management system immediately deletes the IPv4 static route that is bound to the BFD session from the forwarding table and recalculates another active route. In this manner, fast route convergence is implemented.


#### Pre-configuration Tasks

Before configuring dynamic BFD for IPv4 static routes, configure parameters of the link layer protocol and IP addresses for interfaces and ensure that the link layer protocol on the interfaces is Up.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   Global BFD is enabled on the local device.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Running the [**undo bfd**](cmdqueryname=undo+bfd) command will delete the parameters of the BFD session bound to the static route. As a result, the static route status may change, and services may be interrupted.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. (Optional) Run [**ip route-static default-bfd**](cmdqueryname=ip+route-static+default-bfd) [ **min-rx-interval** *min-rx-interval* ] [ **min-tx-interval** *min-tx-interval* ] [ **detect-multiplier** *multiplier* ] \*
   
   
   
   Global BFD parameters are configured for IPv4 static routes.
5. Run [**ip route-static bfd**](cmdqueryname=ip+route-static+bfd) [ *interface-type* *interface-number* | **vpn-instance** *vpn-instance-name* ] *nexthop-address* [ **local-address** *address* ] [ **min-rx-interval** *min-rx-interval* ] [ **min-tx-interval** *min-tx-interval* ] [ **detect-multiplier** *multiplier* ] \*
   
   
   
   BFD parameters are set for a specified IPv4 static route.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If *interface-type* *interface-number* is not set, **local-address** *address* must be specified.
   
   If *interface-type* *interface-number* is specified, the BFD session monitors the active status of the corresponding link on the specified interface. If **local-address** *address* is specified, the BFD session monitors the active status of the corresponding link.
   
   If none of **min-rx-interval**, **min-tx-interval**, or **detect-multiplier** is specified, the default values of the global BFD parameters are used.
6. Run either of the following commands as required:
   
   
   * Run [**ip route-static**](cmdqueryname=ip+route-static) *ip-address* { *mask* | *mask-length* } { *nexthop-address* | *interface-type* *interface-number* [ *nexthop-address* ] | **vpn-instance** *vpn-instance-name* *nexthop-address* } **bfd** **enable** [ **description** *text* ]
     
     A public network IPv4 static route is bound to a BFD session.
   * Run [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } { *nexthop-address* | *interface-type* *interface-number* [ *nexthop-address* ] | **vpn-instance** *vpn-instance-name* *nexthop-address* } **bfd** **enable** [ **description** *text* ]
     
     A VPN network IPv4 static route is bound to a BFD session.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The outbound interface and next hop IP address specified when binding the IPv4 static route to a BFD session must be the same as those specified when configuring BFD parameters for the IPv4 static route.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After completing the configuration, perform the following operations to verify the configuration:

* Run the [**display bfd session**](cmdqueryname=display+bfd+session) { **all** | **discriminator** *discr-value* } [ **verbose** ] command to check detailed BFD session information.
* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) | **include** **bfd** command to check configurations of BFD for static routes.
  
  You can check the information about a BFD session only after parameters of the BFD session are set and the BFD session is established.
  
  If a BFD session has been established, the status of the BFD session is Up. Run the [**display current-configuration**](cmdqueryname=display+current-configuration) | **include** **bfd** command in the system view, and you can view that the BFD session has been bound to a static route.