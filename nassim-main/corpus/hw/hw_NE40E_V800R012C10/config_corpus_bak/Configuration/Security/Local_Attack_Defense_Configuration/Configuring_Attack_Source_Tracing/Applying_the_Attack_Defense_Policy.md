Applying the Attack Defense Policy
==================================

The configured attack defense policy takes effect only
after being applied to the interface board.

#### Context

The NE40E defines a default attack defense policy.
This policy cannot be modified or deleted. When the NE40E starts, this policy is automatically applied to the interface
board. Configurations in the policy are default configurations of
each feature. To apply a specified attack defense policy to the interface
board, you need to run the [**cpu-defend-policy**](cmdqueryname=cpu-defend-policy) *policy-number* command on the interface board
to bind the policy to be applied to the interface board. If the [**cpu-defend-policy**](cmdqueryname=cpu-defend-policy) *policy-number* command is not used, the
default attack defense policy is applied to the interface board.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**cpu-defend-policy**](cmdqueryname=cpu-defend-policy) *policy-number*
   
   
   
   The attack defense policy
   is applied to the interface board.
   
   You must apply the attack
   defense policy to the interface board; otherwise, the policy does
   not take effect.
   
   The attack defense policy specified by *policy-number* must be a configured one. Otherwise, the policy
   cannot be applied.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.