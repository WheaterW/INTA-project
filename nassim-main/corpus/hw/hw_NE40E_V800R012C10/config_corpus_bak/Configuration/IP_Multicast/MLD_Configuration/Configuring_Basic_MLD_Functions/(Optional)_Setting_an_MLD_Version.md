(Optional) Setting an MLD Version
=================================

Interfaces that connect multicast devices to the same user network segment must run the same MLD version; otherwise, these multicast devices fail to communicate.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**mld version**](cmdqueryname=mld+version) *version*
   
   
   
   An MLD version is set for the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.