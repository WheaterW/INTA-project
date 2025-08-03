Disabling Join/Prune Message Packaging
======================================

Sending PIM Join/Prune messages in a package increases the transmission rate.

#### Context

The efficiency for sending PIM Join/Prune messages in a package is higher than that for separately sending a large number of PIM Join/Prune messages. By default, a device sends PIM Join/Prune messages in a package. Because the size of a PIM Join/Prune message package is large, devices that have poor performance cannot receive the PIM Join/Prune message package. To prevent packets from being discarded, disable the Join/Prune message packaging function.

Perform the following steps on the Router that runs Protocol Independent Multicast Sparse Mode (PIM-SM):


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The PIM view is displayed.
3. Run [**join-prune triggered-message-cache disable**](cmdqueryname=join-prune+triggered-message-cache+disable)
   
   
   
   The real-time Join/Prune message packaging function is disabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.