(Optional) Configuring the Traffic Direction to Which the Domain User Traffic Quota Applies
===========================================================================================

The user traffic quota can be configured to apply to upstream
or downstream traffic in the AAA domain view.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The AAA domain view is displayed.
4. Run [**user volume-quota apply**](cmdqueryname=user+volume-quota+apply) { **inbound** | **outbound** }
   
   
   
   The traffic direction to which the user traffic quota applies
   is specified.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.