(Optional) Configuring the Device to Use the Inner IPv4 Address of Each IPv4-in-IPv6 Packet to Match IPv4 UCLs of EDSG Services
===============================================================================================================================

You can configure this function to allow IPv4-in-IPv6 packets to use inner IPv4 addresses to match IPv4 UCLs of EDSG services.

#### Context

By default, the device uses the outer IPv6 header in each IPv4-in-IPv6 packet to match EDSG services. To allow EDSG rate limiting and accounting based on inner IPv4 addresses, perform the following steps to configure the device to use inner IPv4 addresses to match IPv4 UCLs of EDSG services,


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**value-added-service edsg centralized-ds-lite**](cmdqueryname=value-added-service+edsg+centralized-ds-lite)
   
   
   
   The function to use the inner IPv4 address of each IPv4-in-IPv6 packet to match EDSG services is configured.