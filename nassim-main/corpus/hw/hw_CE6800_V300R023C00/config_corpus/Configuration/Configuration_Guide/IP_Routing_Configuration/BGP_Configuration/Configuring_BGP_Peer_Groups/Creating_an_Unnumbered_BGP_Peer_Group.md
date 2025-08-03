Creating an Unnumbered BGP Peer Group
=====================================

Creating an Unnumbered BGP Peer Group

#### Context

BGP is based on TCP/IP and requires IP addresses to establish BGP connections. However, assigning an IP address to each device in a data center scenario requires a large number of IP addresses. To conserve address resources without compromising BGP connections, you can deploy the unnumbered BGP function, which is a port multiplexing technology that allows BGP to be configured without IP addresses. It can not only conserve IP address resources, but also implement automatic neighbor discovery and connection establishment.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Create an unnumbered BGP peer group.
   
   
   ```
   [group](cmdqueryname=group+unnumbered+internal+external) peerGroupName unnumbered { internal | external }
   ```
4. Specify an outbound interface for the unnumbered peer group.
   
   
   ```
   [peer](cmdqueryname=peer+unnumbered-interface) peerGroupName unnumbered-interface { interface-name | IfType IFNum }
   ```
   
   After the [**peer unnumbered-interface**](cmdqueryname=peer+unnumbered-interface) command is run to specify an outbound interface for the unnumbered peer group, the IPv6 link-local address of the outbound interface and the advertisement protocol are used to automatically discover peers and establish BGP sessions with the peers, implementing route distribution.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```