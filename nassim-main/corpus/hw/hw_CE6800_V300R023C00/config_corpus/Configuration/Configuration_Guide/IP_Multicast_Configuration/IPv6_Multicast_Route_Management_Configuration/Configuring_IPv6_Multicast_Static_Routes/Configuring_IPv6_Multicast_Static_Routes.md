Configuring IPv6 Multicast Static Routes
========================================

Configuring IPv6 Multicast Static Routes

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the IPv6 multicast function.
   
   
   ```
   [multicast ipv6 routing-enable](cmdqueryname=multicast+ipv6+routing-enable)
   ```
3. Configure a multicast static route.
   
   
   ```
   [ipv6 rpf-route-static](cmdqueryname=ipv6+rpf-route-static) [ vpn-instance vpn-instance-name ] source-address mask-length { rpf-nbr6 | { interface-name | interface-type interface-number } } [ preference preValue ]
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   When configuring a multicast static route, if the next-hop interface is a P2P interface, you can use the *interface-type* *interface-number* parameter to configure the next-hop interface (namely, the RPF interface) in the command. If the next-hop interface is not a P2P interface, you must specify *rpf-nbr6* to configure a next-hop address (IP address of the RPF neighbor).
   
   After the [**ipv6 rpf-route-static**](cmdqueryname=ipv6+rpf-route-static) command is run, the multicast static route may not take effect, because no outbound interface may be unavailable for recursion or the specified interface may be down. Therefore, after this configuration, you are advised to run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **table-name msr** command to check whether the route takes effect.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```