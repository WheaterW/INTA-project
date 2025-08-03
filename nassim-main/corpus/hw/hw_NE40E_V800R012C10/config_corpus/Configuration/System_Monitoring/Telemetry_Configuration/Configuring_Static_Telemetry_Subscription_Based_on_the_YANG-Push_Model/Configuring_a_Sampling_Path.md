Configuring a Sampling Path
===========================

When configuring a static telemetry subscription to the sampled data based on the YANG-Push model, you need to create a sampling filter and specify a sampling path.

#### Context

A device functions as a client, and a collector functions as a server. To statically subscribe to the sampled data through the YANG-Push model, you need to configure a source from which to sample the data.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**telemetry ietf**](cmdqueryname=telemetry+ietf)
   
   
   
   The telemetry IETF view is displayed.
3. Run [**filter**](cmdqueryname=filter) *filter-name* [**type**](cmdqueryname=type) [**datastore**](cmdqueryname=datastore)
   
   
   
   A sampling filter is created, and the telemetry IETF sampling filter view is displayed.
4. Run [**xpath**](cmdqueryname=xpath)*xpath-name*
   
   
   
   A telemetry IETF sampling path is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The sampling path must start with a slash (/).
   * A maximum of 64 sampling paths can be configured for a sampling filter. When the number of sampling paths reaches the upper limit, the device displays a message indicating that the maximum number of sampling paths is reached.
   * A sampling path name can be configured for up to 10 sampling filters at the same time. When the number of sampling filters for which a sampling path name is configured reaches the upper limit, the device displays a message indicating that the maximum number of sampling filters is reached.
   * You can configure only the sampling paths for which you have the read permission.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.