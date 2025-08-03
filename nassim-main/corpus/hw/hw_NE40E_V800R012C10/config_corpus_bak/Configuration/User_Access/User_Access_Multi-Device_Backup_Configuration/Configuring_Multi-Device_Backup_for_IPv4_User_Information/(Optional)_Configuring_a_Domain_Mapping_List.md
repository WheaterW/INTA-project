(Optional) Configuring a Domain Mapping List
============================================

In a hot backup scenario where a domain name is delivered by the RADIUS server or carried in a packet from a user terminal, the backup device must map the domain name into different domain names for different RBSs to ensure resource independency in the RBSs.

#### Procedure

1. Configure a domain mapping list on the master and backup devices.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   3. Run [**domain**](cmdqueryname=domain) *domain-name*
      
      
      
      A domain is created and the AAA domain view is displayed.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run quit
      
      
      
      Return to the AAA domain view.
   6. Run [**domain-map-list**](cmdqueryname=domain-map-list) *domain-map-list-name*
      
      
      
      A domain mapping list is created and the domain mapping list view is displayed.
   7. Run [**domain**](cmdqueryname=domain) *source-domain*-name [**mapping**](cmdqueryname=mapping) *dest-domain*-name [ **extend** ]
      
      
      
      A domain mapping is added to the domain mapping list.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure domain mapping in an RBS.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name*
      
      
      
      The RBS view is displayed.
   3. Run [**domain-map-list**](cmdqueryname=domain-map-list) *domain-map-list-name*
      
      
      
      A domain mapping list is bound to the RBS.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.