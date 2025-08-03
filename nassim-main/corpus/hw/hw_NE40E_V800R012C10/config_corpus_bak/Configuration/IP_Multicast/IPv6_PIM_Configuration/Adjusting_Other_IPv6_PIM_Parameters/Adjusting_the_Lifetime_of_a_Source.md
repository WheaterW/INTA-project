Adjusting the Lifetime of a Source
==================================

A multicast device starts a timer for each (S, G) entry. If the multicast device does not receive any multicast packets from a multicast source within the specified lifetime of the multicast source, the multicast device considers that the (S, G) entry invalid, and the multicast source stops sending multicast data to the multicast group.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
   
   
   
   The IPv6 PIM view is displayed.
3. Run [**source-lifetime**](cmdqueryname=source-lifetime) *interval*
   
   
   
   Lifetime is configured for sources.
   
   After receiving a multicast packet from a source S, the Router resets the timer. If the timer times out, the (S, G) entry is considered invalid.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.