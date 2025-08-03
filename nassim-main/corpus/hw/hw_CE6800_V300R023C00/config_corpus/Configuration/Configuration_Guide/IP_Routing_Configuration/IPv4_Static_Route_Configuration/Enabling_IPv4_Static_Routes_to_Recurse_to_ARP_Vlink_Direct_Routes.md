Enabling IPv4 Static Routes to Recurse to ARP Vlink Direct Routes
=================================================================

Enabling IPv4 Static Routes to Recurse to ARP Vlink Direct Routes

#### Context

Static routes cannot recurse to ARP Vlink direct routes by default. However, in some scenarios, static routes need to recurse to ARP Vlink direct routes to prevent a blackhole route from being generated.

![](public_sys-resources/note_3.0-en-us.png) 

A blackhole route has a next hop's outbound interface set to the null or loopback interface. Data packets to be forwarded are discarded once they match a blackhole route.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable a device to recurse static route to ARP Vlink direct routes.
   
   
   ```
   [ip route recursive-lookup arp vlink-direct-route protocol static](cmdqueryname=ip+route+recursive-lookup+arp+vlink-direct-route+protocol+static)
   ```
   
   
   
   By default, static routes cannot recurse to ARP Vlink direct routes.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To enable a static route to recurse only to an ARP Vlink direct route, run both this command and the [**ip route-static**](cmdqueryname=ip+route-static) **recursive-lookup** **host-route** [ **arp-vlink-only** ] command.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check information about the configured IPv4 static route recursing to an ARP Vlink direct route.