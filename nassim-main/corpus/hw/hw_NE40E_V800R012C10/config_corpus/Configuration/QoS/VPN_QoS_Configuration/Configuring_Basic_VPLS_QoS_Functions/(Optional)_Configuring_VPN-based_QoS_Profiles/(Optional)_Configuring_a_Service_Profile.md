(Optional) Configuring a Service Profile
========================================

Applying a service profile to an interface and configuring precision compensation achieve precise flow control by compensating for a processed packet with a preconfigured length.

#### Context

Perform the following steps on the router.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**service-template**](cmdqueryname=service-template) *service-template-name*
   
   
   
   The view of a user-defined service profile is displayed.
   
   The service profile specified in this command must be a globally configured one rather than a board-specific service profile.
3. Run [**network-header-length**](cmdqueryname=network-header-length) *network-header-length* { **inbound** | **outbound** }
   
   
   
   A precision compensation length is set for the service profile.
   
   After packets enter the device, there is a difference between the length of a processed packet and the original packet. To achieve precise traffic control, configure a precision compensation length to compensate for the processed packet.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.