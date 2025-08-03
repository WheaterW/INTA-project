(Optional) Configuring a MAP Rule
=================================

By default, Huawei devices use an RFC-compliant mapping rule for MAP-E conversion. If such a device functions as a MAP BR and works with peripheral devices that use the IETF draft-compliant mapping rule to complete MAP-E conversion, configure the Huawei device to use a mapping rule that complies with the IETF draft.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**map-e instance**](cmdqueryname=map-e+instance) *map-e-instance-name* [ **id** *id* ]
   
   
   
   The MAP-E instance view is displayed.
3. Run [**map-version draft**](cmdqueryname=map-version+draft)
   
   
   
   The mapping rule that complies with the IETF draft is used for MAP-E conversion.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.