(Optional) Setting the Maximum Number of Sessions for an Account
================================================================

You can set the maximum number of sessions for an account,
so that you can limit the number of sessions allowed for users of
the same user account. Users of the same user account share QoS resources.

#### Context

To guarantee the processing capability of the NE40E, you can limit the maximum number of sessions for an account.
If the number of sessions of an account reaches the limit, new access
requests from this account are denied.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
4. Run [**user-max-session**](cmdqueryname=user-max-session) *max-session-number*
   
   
   
   The maximum number of sessions for an account is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.