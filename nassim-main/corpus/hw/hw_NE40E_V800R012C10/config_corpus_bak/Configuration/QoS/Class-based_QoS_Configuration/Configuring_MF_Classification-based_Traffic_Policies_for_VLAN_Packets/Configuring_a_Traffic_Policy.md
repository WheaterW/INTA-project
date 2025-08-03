Configuring a Traffic Policy
============================

After defining traffic classifiers and behaviors, you need to configure a traffic policy to associate them.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
   
   
   
   A traffic policy is defined and its view is displayed.
3. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name* [ **precedence** *precedence-value* ]
   
   
   
   A traffic classifier is associated with a traffic behavior in the traffic policy, and a matching priority is configured.
4. (Optional) Run [**step**](cmdqueryname=step) *step-value*
   
   
   
   The step between sub-policies is configured.
5. (Optional) Run [**statistics enable**](cmdqueryname=statistics+enable)
   
   
   
   The statistics collection function is enabled for the traffic policy.
   
   
   
   By default, the statistics collection function is disabled for a traffic policy to conserve memory resources. To view statistics about a traffic policy, you can enable the statistics collection function for it.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.