Setting the Maximum Number of Multicast Lists that a User Is Allowed to Access at a Time
========================================================================================

A multicast list records multiple multicast addresses, that is, multicast programs. You can set the maximum number of multicast programs that a user is allowed to access at a time.

#### Context

A multicast list records multiple multicast addresses, that is, multicast programs. You can set the maximum number of multicast programs that a user is allowed to access at a time.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
4. Run [**multicast max-list**](cmdqueryname=multicast+max-list) *max-num*
   
   
   
   The maximum number of multicast lists that a user is allowed to access at a time is set.