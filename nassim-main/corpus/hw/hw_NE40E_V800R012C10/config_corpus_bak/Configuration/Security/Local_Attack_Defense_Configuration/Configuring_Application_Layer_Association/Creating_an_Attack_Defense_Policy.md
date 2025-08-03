Creating an Attack Defense Policy
=================================

All local attack defense features must be added to an attack defense policy. These features take effect after the attack defense policy is applied to the interface board.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
   
   
   
   An attack defense policy is created.
3. (Optional) Run [**description**](cmdqueryname=description) *text*
   
   
   
   The description of the attack defense policy is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

You must run the [**cpu-defend-policy**](cmdqueryname=cpu-defend-policy) command on the interface board to apply the attack defense policy to the interface board. In this manner, the configured attack defense policy can take effect.