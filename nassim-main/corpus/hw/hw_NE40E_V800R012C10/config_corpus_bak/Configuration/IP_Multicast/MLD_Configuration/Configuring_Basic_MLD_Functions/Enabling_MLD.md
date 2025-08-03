Enabling MLD
============

To enable an interface to process user MLD join requests, enable MLD on the interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**mld enable**](cmdqueryname=mld+enable)
   
   
   
   MLD is enabled.
   
   
   
   MLD parameters that are configured on an interface before MLD is enabled on this interface take effect only after the [**mld enable**](cmdqueryname=mld+enable) command is run on the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.