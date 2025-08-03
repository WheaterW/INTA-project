(Optional) Configuring User Group Load Balancing in a Domain
============================================================

User group load balancing in a domain allows the traffic of users that go online through the domain to be distributed to different devices based on the user group weight.

#### Context

Only one user group that is not bound to any NAT instances can exist in a domain. In centralized CGN scenarios, load balancing requires user groups that are not bound to any NAT instances. User group load balancing in a domain allows the traffic of users that go online through the domain to be distributed to different centralized CGN devices based on the user group weight.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**access user-group-list**](cmdqueryname=access+user-group-list) *list-name*
   
   
   
   A user group load balancing group is created, and its view is displayed.
3. Run [**user-group**](cmdqueryname=user-group) *group-name* [ **weight** *weight* ]
   
   
   
   A user group with a weight is added to the user group load balancing group.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   The system view is displayed.
5. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
6. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The AAA domain view is displayed.
7. Run [**access user-group-list**](cmdqueryname=access+user-group-list) *list-name*
   
   
   
   The user group load balancing group is bound to the domain.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.