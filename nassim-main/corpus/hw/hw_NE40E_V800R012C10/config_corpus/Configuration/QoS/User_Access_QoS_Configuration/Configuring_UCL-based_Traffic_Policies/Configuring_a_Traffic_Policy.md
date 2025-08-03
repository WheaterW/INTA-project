Configuring a Traffic Policy
============================

After defining traffic classifiers and behaviors, you need to configure a traffic policy to associate them.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
   
   
   
   A traffic policy is defined and its view is displayed.
3. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name* [ **precedence** *precedence-value* ]
   
   
   
   A traffic classifier and behavior are specified in the traffic policy, and a matching precedence is set.
4. (Optional) Run [**statistics enable**](cmdqueryname=statistics+enable)
   
   
   
   The statistics collection function is enabled for the traffic policy.
5. (Optional) Run [**share-mode**](cmdqueryname=share-mode)
   
   
   
   The shared mode is specified for the traffic policy.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) By default, the statistics collection function is disabled for a traffic policy. This helps conserve memory resources. To check statistics about a traffic policy, you can run the [**statistics enable**](cmdqueryname=statistics+enable) command to enable the statistics collection function for it. By default, the shared mode is used for a traffic policy.
   * After a traffic policy is applied to an interface, you cannot modify its shared or unshared mode. To perform such a modification, you must remove the traffic policy on the interface first.
   * Although a shared traffic policy is applied to different interfaces, only summarized statistics are displayed. In this case, per-interface statistics cannot be distinguished.
   * After an unshared traffic policy is applied to different interfaces, per-interface statistics are displayed.
   * Statistics on inbound and outbound traffic are separately collected, regardless of whether a traffic policy is shared or unshared.
6. (Optional) Run [**step**](cmdqueryname=step) *step-value*
   
   
   
   A step between policies is configured.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.