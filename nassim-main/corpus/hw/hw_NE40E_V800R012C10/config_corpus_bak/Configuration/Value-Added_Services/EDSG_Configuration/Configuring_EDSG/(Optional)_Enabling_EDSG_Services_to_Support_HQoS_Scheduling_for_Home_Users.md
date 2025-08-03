(Optional) Enabling EDSG Services to Support HQoS Scheduling for Home Users
===========================================================================

This section describes how to enable EDSG services to support
HQoS scheduling for home users in a AAA domain.

#### Context

Home users support HQoS, but differentiated traffic statistics
collection and accounting cannot be performed for different user services. To resolve this issue, enable EDSG services to support
HQoS scheduling for home users.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The AAA domain view is displayed.
4. Run [**value-added-service edsg family-schedule**](cmdqueryname=value-added-service+edsg+family-schedule) { **inbound** | **outbound** }
   
   
   
   EDSG services are enabled to support HQoS scheduling for
   home users.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.