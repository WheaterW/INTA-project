Configuring an Administrative Tag for SRv6 Locator Routes
=========================================================

In scenarios such as inter-AS SRv6 locator route import, an administrative tag can be configured for SRv6 locator routes to facilitate route filtering and prevent routing loops.

#### Context

The SRv6 Locator TLV can carry the 32-bit Administrative Tag sub-TLV, which is used to set an administrative tag for SRv6 locator routes. During inter-AS SRv6 locator route import, you can set an administrative tag for SRv6 locator routes and use a route-policy to filter these routes based on the administrative tag, thereby preventing routing loops.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable) **topology ipv6**
   
   
   
   IPv6 is enabled for the IS-IS process.
4. Run [**segment-routing ipv6 default-tag**](cmdqueryname=segment-routing+ipv6+default-tag) *tag-value*
   
   
   
   An administrative tag is configured for SRv6 locator routes.
   
   After the configuration is complete and the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) command is run in the IS-IS view to enable the device to advertise SRv6 locator routes, the advertised routes carry the administrative tag.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.