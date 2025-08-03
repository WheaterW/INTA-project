(Optional) Disabling TTL Decrease by 1
======================================

This section describes how to disable TTL decrease by 1.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast-nat ttl-decrease disable**](cmdqueryname=multicast-nat+ttl-decrease+disable)
   
   
   
   TTL decrease is disabled for multicast packets on the device, so that the TTL value of multicast packets does not decrease by 1 when the multicast packets pass through the device.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.