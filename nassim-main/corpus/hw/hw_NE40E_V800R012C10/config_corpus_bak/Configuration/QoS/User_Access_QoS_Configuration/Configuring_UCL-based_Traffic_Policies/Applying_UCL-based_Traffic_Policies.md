Applying UCL-based Traffic Policies
===================================

After the UCL-based traffic policies are applied, the traffic of all online users is classified according to the UCL rules.

#### Context

In VS mode, this configuration task is supported only by the admin VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* { **inbound** | **outbound** }
   
   
   
   A traffic policy is applied to online users.
   
   After the UCL-based traffic policy is applied in the system view, the traffic of all online users is classified according to the UCL.
   
   When traffic policies are configured in both the system view and the interface view, on the network side, the traffic policies that are configured in the interface view take effect, whereas on the user side, UCL-based traffic policies take effect.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * You can run the [**traffic-policy match-type destination-user inbound**](cmdqueryname=traffic-policy+match-type+destination-user+inbound) command to configure the UCL-based traffic policy to take effect.
   * You can run the [**traffic-policy match-type interface-acl**](cmdqueryname=traffic-policy+match-type+interface-acl) command to configure the ACL-based traffic policy to take effect.
     
     In VS mode, this configuration task is supported only by the admin VS.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.