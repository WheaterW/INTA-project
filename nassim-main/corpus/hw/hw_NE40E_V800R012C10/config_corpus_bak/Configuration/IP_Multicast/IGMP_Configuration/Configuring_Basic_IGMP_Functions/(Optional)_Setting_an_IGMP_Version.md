(Optional) Setting an IGMP Version
==================================

Interfaces that connect multicast devices to the same user network segment must run the same IGMP version. Otherwise, these multicast devices fail to communicate.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**igmp version**](cmdqueryname=igmp+version) *VersionValue*
   
   
   
   An IGMP version is set for the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.