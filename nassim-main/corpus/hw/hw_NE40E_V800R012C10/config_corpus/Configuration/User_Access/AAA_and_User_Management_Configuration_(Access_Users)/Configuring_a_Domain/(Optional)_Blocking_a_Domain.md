(Optional) Blocking a Domain
============================

Users cannot access a blocked domain. You can block a domain
if it is not needed.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
4. Run [**block**](cmdqueryname=block)
   
   
   
   The domain is blocked.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.