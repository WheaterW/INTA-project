Configuring Headend-based Fault Detection for SRv6 TE Policies
==============================================================

This section describes how to configure headend-based fault detection for SRv6 TE Policies.

#### Usage Scenario

An SRv6 TE Policy selects a forwarding path from the candidate paths that are either delivered by a controller or manually configured. Currently, SBFD for SRv6 TE Policy is not allowed in some scenarios. As such, if the segment list of a candidate path in an SRv6 TE Policy fails, the headend cannot quickly detect the fault. The SRv6 TE Policy can be updated only after the controller detects a topology change and re-converges the topology.

If the controller or the connection between the controller and headend fails, the SRv6 TE Policy cannot detect the fault or perform a candidate path switchover. This may cause traffic loss. To speed up traffic switching in the case of a fault, headend-based fault detection is introduced. With this function, if a segment list fails, the headend sets the segment list to down, triggering path or service switching in the SRv6 TE Policy.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In the SRv6 SRH, 16-bit compressed SIDs with the **node-length** value of 0 do not support fault detection or enhanced fault detection.

If fault detection is enabled, the verification result is Up regardless of whether 16-bit compressed SIDs with the **node-length** value of 0 are reachable.



#### Pre-configuration Tasks

Before configuring headend-based fault detection for SRv6 TE Policies, complete the following tasks:

* Configure SRv6 TE Policies.
* Run the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name* command in the IS-IS view to enable IS-IS SRv6.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
   
   
   
   The SRv6 view is displayed.
3. Run [**srv6-te-policy path verification**](cmdqueryname=srv6-te-policy+path+verification) [ **specified-sid** ] **enable**
   
   
   
   Headend-based fault detection is enabled for all SRv6 TE Policies.
   
   
   
   After the **specified-sid** parameter is configured, only SIDs with the verification flag in a segment list are verified.
4. (Optional) Run [**srv6-te-policy suppress-flapping disable**](cmdqueryname=srv6-te-policy+suppress-flapping+disable)
   
   
   
   Flap suppression is disabled for all SRv6 TE Policies.
   
   
   
   Enabling this function suppresses frequent SID status changes. If the SID status becomes unreachable, the associated segment list goes down immediately. However, if the SID status becomes reachable, the device needs to determine whether flap suppression is required. If it is required, the device updates the SID status to reachable after a delay and then updates the segment list status.
   
   If flap suppression is not required, run the [**srv6-te-policy suppress-flapping disable**](cmdqueryname=srv6-te-policy+suppress-flapping+disable) command to disable this function for all SRv6 TE Policies.
5. Run [**srv6-te policy**](cmdqueryname=srv6-te+policy) *name-value*
   
   
   
   The SRv6 TE Policy view is displayed.
6. Run [**path verification**](cmdqueryname=path+verification) { [ **specified-sid** ] **enable** | **disable** }
   
   
   
   Headend-based fault detection is configured for the SRv6 TE Policy.
   
   
   
   If an SRv6 TE Policy has both global and single-policy configurations, the single-policy configuration takes precedence.
   
   
   
   After the **specified-sid** parameter is configured, only SIDs with the verification flag in a segment list are verified.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring headend-based fault detection for SRv6 TE Policies, verify the configuration.

* Run the [**display srv6-te policy**](cmdqueryname=display+srv6-te+policy) [ **endpoint** *endpoint-ip* **color** *color-value* | **policy-name** *name-value* | **binding-sid** *binding-sid* ] command to check SRv6 TE Policy details.
* Run the [**display srv6-te policy source-sid**](cmdqueryname=display+srv6-te+policy+source-sid) [ *sid-value* | **end** | **end-x** ] command to check details about the End and End.X SIDs collected from the IS-IS LSDB, including the IS-IS process and level information about the SIDs.
* Run the [**display srv6-te policy sid statistics**](cmdqueryname=display+srv6-te+policy+sid+statistics) [ **isis** **process** *process-id* { **level-1** | **level-2** | **level-1-2** } ] command to check the numbers of End and End.X SIDs collected from the IS-IS LSDB.
* Run the [**display srv6-te policy last-down-reason**](cmdqueryname=display+srv6-te+policy+last-down-reason) { **endpoint** *endpoint-ip* **color** *color-value* | **policy-name** *name-value* | **binding-sid** *binding-sid* } command to check records about events where SRv6 TE Policies or segment lists in SRv6 TE Policies go down.