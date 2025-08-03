(Optional) Setting the Maximum Number of Access Users for a Domain
==================================================================

You can set the maximum number of access users for a domain
to facilitate user access management.

#### Context

To guarantee the processing capability of the NE40E, you can limit the total number of access users for a
domain. If the number of users reaches the limit, new access requests
are denied.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
4. Run [**access-limit**](cmdqueryname=access-limit) *max-number*
   
   
   
   The maximum number of access users is specified for the domain.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.