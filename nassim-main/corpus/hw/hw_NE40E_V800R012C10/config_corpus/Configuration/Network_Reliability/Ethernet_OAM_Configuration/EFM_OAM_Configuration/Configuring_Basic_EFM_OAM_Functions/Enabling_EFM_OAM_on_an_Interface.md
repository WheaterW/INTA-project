Enabling EFM OAM on an Interface
================================

Point-to-point EFM link detection can be performed only after EFM OAM is enabled on the interfaces at both ends of a link. Perform the following steps at both ends of a link:

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface at one end of a link is displayed.
3. Run [**efm enable**](cmdqueryname=efm+enable)
   
   
   
   EFM OAM is enabled on the interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before running this command, you must run the [**efm enable**](cmdqueryname=efm+enable) command in the system view to enable EFM OAM globally.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.