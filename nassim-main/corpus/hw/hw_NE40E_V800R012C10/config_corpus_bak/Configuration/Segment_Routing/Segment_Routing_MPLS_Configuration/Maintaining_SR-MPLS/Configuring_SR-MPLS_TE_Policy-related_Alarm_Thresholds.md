Configuring SR-MPLS TE Policy-related Alarm Thresholds
======================================================

You can configure SR-MPLS TE Policy-related alarm thresholds, enabling the device to generate an alarm when the number of SR-MPLS TE Policies or segment lists reaches the specified threshold. This facilitates O&M.

#### Context

If the number of SR-MPLS TE Policies or segment lists exceeds the upper limit, adding new SR-MPLS TE Policies or segment lists may affect existing services. To prevent this, you can configure alarm thresholds for the number of SR-MPLS TE Policies and the number of segment lists. In this way, when the number of SR-MPLS TE Policies or segment lists reaches the specified threshold, an alarm is generated to notify users to handle the problem.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**segment-routing**](cmdqueryname=segment-routing)
   
   
   
   Segment Routing is enabled, and the Segment Routing view is displayed.
3. Run [**sr-te-policy segment-list-number threshold-alarm**](cmdqueryname=sr-te-policy+segment-list-number+threshold-alarm) **upper-limit** *upperLimitValue* **lower-limit** *lowerLimitValue*
   
   
   
   An alarm threshold is configured for the number of segment lists.
4. Run [**sr-te-policy policy-number threshold-alarm**](cmdqueryname=sr-te-policy+policy-number+threshold-alarm) **upper-limit** *upperLimitValue* **lower-limit** *lowerLimitValue*
   
   
   
   An alarm threshold is configured for the number of SR-MPLS TE Policies.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.