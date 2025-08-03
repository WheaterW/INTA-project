Enabling the Function to Recurse Original Next Hops of Multicast Routes to MIGP Shortcuts
=========================================================================================

To ensure that a public network Router can forward multicast traffic normally, enabling the Router to recurse an original next hops of multicast route to an MIGP shortcuts route.

#### Usage Scenario

If both multicast and IGP shortcut-enabled MPLS TE tunnels are configured on a network, the outbound interface of a route calculated by the IGP may not be a physical interface but a TE tunnel interface. If the original next hop of a BGP-advertised route to a multicast source is an IGP shortcut, the device sends Join messages out through a TE tunnel interface along the unicast route to the multicast source. As a result, the devices that are not on the TE tunnel will not receive the Join messages or create multicast forwarding entries.

To resolve this issue, enable the device to recurse original next hops of multicast routes to MIGP shortcuts. Physical interfaces are then used as next-hop outbound interfaces of multicast routes, and multicast forwarding entries can be created.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast recursive-lookup local-mt enable**](cmdqueryname=multicast+recursive-lookup+local-mt+enable)
   
   
   
   Recursion of a multicast route's next hop to an IGP shortcut route is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.