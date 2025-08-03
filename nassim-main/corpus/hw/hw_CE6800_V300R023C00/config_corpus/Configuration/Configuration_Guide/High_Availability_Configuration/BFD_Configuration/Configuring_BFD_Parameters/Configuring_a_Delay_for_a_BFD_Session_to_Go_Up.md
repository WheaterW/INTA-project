Configuring a Delay for a BFD Session to Go Up
==============================================

Configuring a Delay for a BFD Session to Go Up

#### Context

On a live network, some devices switch traffic only when a BFD session is in the Up state. If a routing protocol goes up later than an interface, no route is available for switching traffic back, leading to traffic loss. To resolve this problem, configure a delay to compensate for the time difference caused when the routing protocol goes up after the interface, preventing traffic loss.


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable BFD globally and enter the global BFD view.
   ```
   [bfd](cmdqueryname=bfd) 
   ```
3. Configure a delay for a BFD session to go up.
   ```
   [delay-up](cmdqueryname=delay-up) seconds
   ```
   
   The default delay is 0s.
4. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```