Configuring a Delay for a BFD Session to Go Up
==============================================

In special scenarios, you can configure a delay for a BFD session to go up to prevent traffic loss caused when a routing protocol goes up later than an interface.

#### Usage Scenario

On a live network, some devices switch traffic only when a BFD session is in the Up state. If a routing protocol goes up later than an interface, no route is available for switching traffic back, leading to traffic loss. To resolve this issue, configure a delay to compensate for the time difference caused when the routing protocol goes up later than the interface.


#### Pre-configuration Tasks

Before configuring a delay for a BFD session to go up, ensure that the Router is running properly.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled globally on the local node, and the BFD view is displayed.
   
   BFD can be configured only after the [**bfd**](cmdqueryname=bfd) command is run globally.
3. Run [**delay-up**](cmdqueryname=delay-up) *seconds*
   
   
   
   A delay for the BFD session to go up is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.