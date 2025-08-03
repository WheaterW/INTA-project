Configuring a QPPB Local Policy
===============================

QPPB allows QoS policies to be configured for routes that match the BGP community list, ACL, or BGP AS\_Path list. After the QPPB local policy is applied to the inbound and outbound interfaces of traffic, relevant QoS policies are performed on the traffic.

#### Context

Perform the following operations on a BGP route receiver:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**qppb local-policy**](cmdqueryname=qppb+local-policy) *policy-name*
   
   
   
   A QPPB local policy is created and the QPPB local policy view is displayed.
3. (Optional) Run [**statistics enable**](cmdqueryname=statistics+enable)
   
   
   
   QPPB statistics collection is enabled.
4. (Optional) Run [**service-class outbound enable**](cmdqueryname=service-class+outbound+enable)
5. Run [**qos-local-id**](cmdqueryname=qos-local-id) *qos-local-id* **behavior** *behavior-name*
   
   
   
   A QoS local policy ID is bound to a traffic behavior.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.