Configuring Multicast Static Routes
===================================

Configuring Multicast Static Routes

#### Context

Multicast static routes are an important basis for RPF checks. By configuring multicast static routes, you can specify RPF interfaces and RPF neighbors for packets with specific sources.

Multicast static routes provide the following functions, depending on application scenarios:

* Changing RPF routes
  
  If multicast data packets from a specified multicast source need to be received from a specified interface that is not the RPF interface, a multicast static route needs to be configured to specify this interface as the RPF interface. Once configured, a device, when receiving a multicast data packet from the specified source, performs an RPF check on the packet by taking the configured route as the RPF route. Packets that are not sent from the specified interface fail the RPF check.
* Connecting RPF routes
  
  On subnets where unicast routes are blocked, multicast packets cannot be forwarded due to a lack of RPF routes. For example, when two adjacent devices run different routing protocols that do not import routes from each other, packets cannot be forwarded between the two devices because there are no RPF routes. In this case, you can configure multicast static routes to specify RPF interfaces for the RPF check on the devices. Multicast packets can then be forwarded successfully.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the multicast function.
   
   
   ```
   [multicast routing-enable](cmdqueryname=multicast+routing-enable)
   ```
3. Configure a multicast static route.
   
   
   ```
   [ip rpf-route-static](cmdqueryname=ip+rpf-route-static) [ vpn-instance vpn-instance-name ] source-address { mask | mask-length } { rpf-nbr | { interface-name | interface-type interface-number } } [ preference preValue ]
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   When configuring a multicast static route, if the next-hop interface is a P2P interface, you can use the *interface-type* *interface-number* parameter to configure the next-hop interface (namely, the RPF interface) in the command. If the next-hop interface is not a P2P interface, you must specify *rpf-nbr* to configure the next-hop address, that is, the IP address of the RPF neighbor.
   
   After the [**ip rpf-route-static**](cmdqueryname=ip+rpf-route-static) command is run, the multicast static route may not take effect, because outbound interface recursion may fail or the specified interface may be down. Therefore, after the configuration, you are advised to run the [**display multicast routing-table**](cmdqueryname=display+multicast+routing-table) [ **vpn-instance** *vpn-instance-name* ] **static** [ **config** ] [ *prefix* { *mask* | *masklength* } ] command to check whether the route takes effect.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```