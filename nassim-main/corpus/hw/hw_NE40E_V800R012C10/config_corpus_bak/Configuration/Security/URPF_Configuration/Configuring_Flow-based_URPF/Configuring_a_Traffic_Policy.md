Configuring a Traffic Policy
============================

After being classified, the traffic must be associated
with the traffic behavior. In this manner, a traffic policy can be
formed.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
   
   
   
   A traffic policy is defined and the traffic policy view is displayed.
   
   *policy-name* defined by users cannot be the
   one pre-defined by the system. For details on traffic policies, see *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - QoS*.
3. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name*
   
   
   
   The traffic behavior
   is specified for the specified traffic class in the traffic policy.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Traffic of the same class cannot match two
   traffic behaviors at the same time.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.