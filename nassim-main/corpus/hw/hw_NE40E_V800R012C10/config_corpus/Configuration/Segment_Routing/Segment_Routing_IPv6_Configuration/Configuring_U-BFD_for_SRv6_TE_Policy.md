Configuring U-BFD for SRv6 TE Policy
====================================

This section describes how to configure unaffiliated bidirectional forwarding detection (U-BFD) for SRv6 TE Policy.

#### Usage Scenario

SBFD for SRv6 TE Policy requires you to configure the mapping between the reflector's IPv6 address and discriminator on the headend of the involved SRv6 TE Policy and configure the same reflector discriminator on the endpoint of the policy. If these requirements are not met, SBFD loopback packets cannot be constructed. In addition, you must ensure that the configured reflector discriminator is globally unique to avoid possible SBFD errors.

In inter-AS SRv6 TE Policy scenarios, the preceding constraints on the reflector discriminator make network planning inconvenient. To address this issue, U-BFD for SRv6 TE Policy is introduced.

U-BFD for SRv6 TE Policy can quickly detect segment list faults. If all the segment lists of a candidate path are faulty, U-BFD triggers a hot-standby candidate path switchover to minimize the impact on services.

The global configuration takes effect for all SRv6 TE Policies, whereas the single-policy configuration takes effect only for the specified SRv6 TE Policy.


#### Pre-configuration Tasks

Before configuring U-BFD for SRv6 TE Policy, complete the following tasks:

* Configure an SRv6 TE Policy.
* Run the [**te ipv6-router-id**](cmdqueryname=te+ipv6-router-id)*ipv6Addr* command to configure a global TE IPv6 router ID.

#### Procedure

1. Run **[**system-view**](cmdqueryname=system-view)**
   
   
   
   The system view is displayed.
2. Run **[**bfd**](cmdqueryname=bfd)**
   
   
   
   BFD is enabled globally.
   
   
   
   BFD-related configuration can be performed only after BFD is enabled globally using the **bfd** command.
3. Run **[**quit**](cmdqueryname=quit)**
   
   
   
   Return to the system view.
4. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
   
   
   
   The SRv6 view is displayed.
5. Configure U-BFD for SRv6 TE Policy.
   * Global configuration
     1. Run the [**srv6-te-policy bfd unaffiliated enable**](cmdqueryname=srv6-te-policy+bfd+unaffiliated+enable) [ **reverse-path binding-sid** ] command to enable U-BFD for all SRv6 TE Policies.
        
        The **reverse-path binding-sid** parameter enables U-BFD return packets to be forwarded over an SRv6 TE Policy.
     2. (Optional) Run the [**srv6-te-policy bfd**](cmdqueryname=srv6-te-policy+bfd) { **min-tx-interval** *tx-value* | **detect-multiplier** *detectmulti-value* } \* command to configure U-BFD parameters for the SRv6 TE Policies.
     3. (Optional) Run the [**srv6-te-policy bfd**](cmdqueryname=srv6-te-policy+bfd) { **min-tx-interval** *backup-tx-value* | **detect-multiplier** *backup-detectmulti-value* } \* **backup-path** command to configure U-BFD parameters for the backup candidate paths of the SRv6 TE Policies.
     4. (Optional) Run the [**srv6-te-policy bfd switch-delay**](cmdqueryname=srv6-te-policy+bfd+switch-delay) *delay-interval* command to configure a BFD switching delay for the SRv6 TE Policies.
     5. (Optional) Run the [**srv6-te-policy bfd**](cmdqueryname=srv6-te-policy+bfd) **no-bypass** [ **preferred** ] command to enable the BFD no-bypass function for the SRv6 TE Policies.
        
        After this function is enabled, U-BFD for SRv6 TE Policy packets do not transit local protection paths such as TI-LFA and TE FRR paths.
        
        For example, in TE FRR protection, if the current SID is unreachable, the SRv6 TE Policy uses the next-layer SID for forwarding. If this SID is still unreachable, the SRv6 TE Policy forwards the packet using the lower-layer SID until the destination IPv6 address of the packet changes to the TE IPv6 router ID of the headend. In this case, the BFD packets are looped back to the headend, and the BFD status remains up, which is inconsistent with the actual forwarding status of the SRv6 TE Policy. As such, you are advised to enable the BFD no-bypass function in U-BFD for SRv6 TE Policy scenarios.
        
        If the **preferred** parameter is specified and an SRv6 TE Policy has a backup path, BFD packets on the primary path are not transmitted over local protection paths such as TI-LFA and TE FRR paths. If the primary path fails, BFD goes down, and traffic is then switched to the backup path. BFD packets on the backup path can be transmitted over local protection paths to ensure service continuity.
   * Single-policy configuration
     1. Run the [**srv6-te policy**](cmdqueryname=srv6-te+policy) *policy-name* command to enter the SRv6 TE Policy view.
     2. Run the [**bfd unaffiliated**](cmdqueryname=bfd+unaffiliated) **enable** [ **reverse-path binding-sid** ] or [**bfd**](cmdqueryname=bfd) **disable** command to set the status of the U-BFD function for the SRv6 TE Policy.
        
        The **reverse-path binding-sid** parameter enables U-BFD return packets to be forwarded over an SRv6 TE Policy.
     3. (Optional) Run the [**bfd**](cmdqueryname=bfd) { **min-tx-interval** *tx-value* | **detect-multiplier** *detectmulti-value* } \* command to configure U-BFD parameters for the SRv6 TE Policy.
     4. (Optional) Run the [**bfd**](cmdqueryname=bfd) { **min-tx-interval** *backup-tx-value* | **detect-multiplier** *backup-detectmulti-value* } \* **backup-path** command to configure U-BFD parameters for the backup candidate paths of the SRv6 TE Policy.
     5. (Optional) Run the [**bfd**](cmdqueryname=bfd) { **no-bypass** [ **preferred** ] | **bypass** } command to set the status of the U-BFD bypass function for the SRv6 TE Policy.
        
        If you do not want the U-BFD packets of the SRv6 TE Policy to transit local protection paths such as TI-LFA and TE FRR paths, select the **no-bypass** parameter. Otherwise, select the **bypass** parameter.
        
        If you specify both the **no-bypass** and **preferred** parameters, the traffic forwarded over an SRv6 TE Policy is not preferentially transmitted over local protection paths. If an SRv6 TE Policy has a backup path, BFD packets on the primary path are not transmitted over local protection paths such as TI-LFA and TE FRR paths. If the primary path fails, BFD goes down, and traffic is then switched to the backup path. BFD packets on the backup path can be transmitted over local protection paths to ensure service continuity.
6. (Optional) Run **[**srv6-te-policy switch-delay**](cmdqueryname=srv6-te-policy+switch-delay)** **switchDelay** **[**delete-delay**](cmdqueryname=delete-delay)** **deleteDelay**
   
   
   
   Segment list switching and deletion delays are configured for SRv6 TE Policies.
7. Run **[**commit**](cmdqueryname=commit)**
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring U-BFD for SRv6 TE Policy, run the **[**display srv6-te policy**](cmdqueryname=display+srv6-te+policy)** [****endpoint**** **ipv6-address** ****color**** **color-value** | ****policy-name**** **name-value** ] command to check SRv6 TE Policy-specific U-BFD status.