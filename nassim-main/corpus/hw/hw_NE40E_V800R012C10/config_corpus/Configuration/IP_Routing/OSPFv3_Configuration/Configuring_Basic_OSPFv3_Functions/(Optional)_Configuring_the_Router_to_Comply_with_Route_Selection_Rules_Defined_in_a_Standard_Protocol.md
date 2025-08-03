(Optional) Configuring the Router to Comply with Route Selection Rules Defined in a Standard Protocol
=====================================================================================================

You can configure the Router to comply with the route selection rule defined in RFC 1583 or RFC 5340.

#### Context

RFC 5340 and RFC 1583 define route selection rules differently. After enabling OSPFv3 on a device, you can configure the device to comply with route selection rules defined in either standard protocol as required. By default, a device complies with the route selection rules defined in RFC 5340. If you want the device to comply with the other protocol, you need to configure the device to comply with the rules defined in RFC 1583. Such configurations ensure that all OSPFv3-enabled devices in an AS comply with the same route selection rules defined in the same standard protocol.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ] [ **vpn-instance** *vpnname* ]
   
   
   
   OSPFv3 is enabled, and the OSPFv3 view is displayed.
3. Run [**rfc1583 compatible**](cmdqueryname=rfc1583+compatible)
   
   
   
   The Router is configured to comply with the route selection rule defined in RFC 1583, rather than RFC 5340.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.