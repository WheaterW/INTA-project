Attack Source Tracing Does Not Take Effect
==========================================

Attack Source Tracing Does Not Take Effect

#### Fault Symptom

The configured attack source tracing function does not take effect.


#### Possible Causes

Possible causes are as follows:

* The attack defense policy is not applied.
* A large rate threshold is set, resulting in failure of the attack source tracing function to identify attack packets.


#### Procedure

1. Run the **[**display current-configuration**](cmdqueryname=display+current-configuration)** command to check whether the attack defense policy is applied.
   * If the command output contains **[**cpu-defend-policy**](cmdqueryname=cpu-defend-policy)**, the attack defense policy has been applied. In this case, go to [2](#EN-US_CONCEPT_0000001563756857__li44745162116).
   * If the command output does not contain **cpu-defend-policy**, the attack defense policy is not applied. In this case, you need to run the [**cpu-defend-policy**](cmdqueryname=cpu-defend-policy) command in the system view to apply the attack defense policy.
2. Check whether a high rate threshold is set for attack source tracing.
   
   Run the [**display auto-defend configuration**](cmdqueryname=display+auto-defend+configuration) command to check the value of the **auto-defend threshold** field. If the value is large, run the [**auto-defend threshold**](cmdqueryname=auto-defend+threshold) command in the attack defense policy view to reduce the value.