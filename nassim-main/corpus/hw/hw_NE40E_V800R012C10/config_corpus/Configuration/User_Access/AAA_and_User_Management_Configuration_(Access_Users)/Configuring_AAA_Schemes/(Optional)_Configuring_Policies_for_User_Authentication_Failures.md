(Optional) Configuring Policies for User Authentication Failures
================================================================

(Optional) Configuring Policies for User Authentication Failures

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**user-qos cir-zero**](cmdqueryname=user-qos+cir-zero) { *cir-value* | **unlimited** }
   
   
   
   The CIR to be used when the CIR and PIR delivered by the RADIUS server are both 0s is set.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command can be used only when the upstream and downstream CIR and PIR delivered by the RADIUS server are both 0s.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
   
   
   
   The RADIUS server group view is displayed.
6. Run [**radius-attribute qos-profile no-exist-policy**](cmdqueryname=radius-attribute+qos-profile+no-exist-policy) { **online** | **offline** }
   
   
   
   A policy is configured. It determines whether to allow users to keep online when the QoS profile delivered by the RADIUS server is not configured on the NE40E.
7. Run [**radius-attribute policy-name no-exist-policy**](cmdqueryname=radius-attribute+policy-name+no-exist-policy) { **online** | **offline** }
   
   
   
   A policy is configured. It determines whether to allow users to keep online when the policy name carried in the HUAWEI-95 attribute delivered by the RADIUS server is not configured on the NE40E.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.