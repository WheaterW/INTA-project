Binding a Policy Server to a Domain
===================================

Bind a policy server to a domain so that users are authenticated and accounted by the server.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The AAA domain view is displayed.
4. Run [**radius-server group**](cmdqueryname=radius-server+group) *groupname*
   
   
   
   A RADIUS server group is bound to the domain.
5. Run [**user-group**](cmdqueryname=user-group) *group-name*
   
   
   
   A user group is bound to the domain.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * You can configure a user group using any of the following methods:
     + Configure a user group in a domain.
     + Configure a user group using a DAA service policy template.
     + Deliver a user group through the RADIUS server.
     
     The user group configured using a DAA service policy template has the highest priority, followed by the one delivered by the RADIUS server, and then the one configured in a domain.
   * The DAA service tariff level used by users must be the same as the DAA ACL tariff level planned for the user group to which the users belong.
6. Run [**billing-server type**](cmdqueryname=billing-server+type) { **1** | **2** }
   
   
   
   An accounting server type is configured.