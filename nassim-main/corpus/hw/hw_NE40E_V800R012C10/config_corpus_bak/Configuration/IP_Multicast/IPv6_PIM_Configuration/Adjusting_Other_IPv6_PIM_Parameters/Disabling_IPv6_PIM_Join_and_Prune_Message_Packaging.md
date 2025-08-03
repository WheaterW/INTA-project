Disabling IPv6 PIM Join/Prune Message Packaging
===============================================

Sending IPv6 Protocol Independent Multicast (PIM) Join/Prune messages in a package increases the rate at which the IPv6 PIM Join/Prune messages are sent.

#### Context

The efficiency for sending IPv6 PIM Join/Prune messages in a package is higher than that for separately sending a large number of IPv6 PIM Join/Prune messages. By default, a device sends IPv6 PIM Join/Prune messages in a package. Because the size of an IPv6 PIM Join/Prune message package is large, devices that have poor performance cannot receive the IPv6 PIM Join/Prune message package. To prevent packet discarding, disable the IPv6 PIM Join/Prune message packaging function.

Perform the following steps on the Router that runs IPv6 Protocol Independent Multicast Sparse Mode (PIM-SM):


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
   
   
   
   The IPv6 PIM view is displayed.
3. Run [**join-prune triggered-message-cache disable**](cmdqueryname=join-prune+triggered-message-cache+disable)
   
   
   
   The real-time IPv6 Join/Prune message packaging function is disabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.