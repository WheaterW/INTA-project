Enabling Recursion of IPv6 Static Routes to ND Vlink Direct Routes
==================================================================

Enabling Recursion of IPv6 Static Routes to ND Vlink Direct Routes

#### Context

By default, IPv6 static routes cannot be recursed to ND Vlink direct routes. In some scenarios, however, you need to enable recursion of IPv6 static routes to ND Vlink direct routes to prevent blackhole routes.

![](public_sys-resources/note_3.0-en-us.png) 

A blackhole route is a route whose next-hop outbound interface is a null or loopback interface. Data packets to be forwarded are discarded once they match a blackhole route.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable recursion of IPv6 static routes to ND Vlink direct routes.
   
   
   ```
   [ipv6 route recursive-lookup nd vlink-direct-route protocol static](cmdqueryname=ipv6+route+recursive-lookup+nd+vlink-direct-route+protocol+static)
   ```
   
   
   
   By default, IPv6 static routes cannot be recursed to ND Vlink direct routes.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   This command is usually used together with the **recursive-lookup** **host-route** parameter in the [**ipv6 route-static**](cmdqueryname=ipv6+route-static) command to configure IPv6 static routes to be recursed only to ND Vlink direct routes.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check information about recursion of IPv6 static routes to ND Vlink direct routes.