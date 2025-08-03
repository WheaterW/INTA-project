Configuring SBFD for SRv6 TE Policy
===================================

This section describes how to configure seamless bidirectional forwarding detection (SBFD) for SRv6 TE Policy.

#### Usage Scenario

SBFD for SRv6 TE Policy can quickly detect segment list faults. If all the segment lists of a candidate path are faulty, SBFD triggers a hot-standby candidate path switchover to minimize the impact on services.


#### Pre-configuration Tasks

Before configuring SBFD for SRv6 TE Policy, complete the following tasks:

* Configure an SRv6 TE Policy.
* Run the [**te ipv6-router-id**](cmdqueryname=te+ipv6-router-id)*ipv6Addr* command to configure a global TE IPv6 router ID.

#### Procedure

* Configure an SBFD initiator.
  1. Run **[**system-view**](cmdqueryname=system-view)**
     
     
     
     The system view is displayed.
  2. Run **[**bfd**](cmdqueryname=bfd)**
     
     
     
     BFD is enabled globally.
     
     
     
     BFD-related configuration can be performed only after BFD is enabled globally using the **[**bfd**](cmdqueryname=bfd)** command.
  3. Run **[**quit**](cmdqueryname=quit)**
     
     
     
     Return to the system view.
  4. Run **[**sbfd**](cmdqueryname=sbfd)**
     
     
     
     SBFD is enabled globally, and the SBFD view is displayed.
  5. Run **[**destination ipv6**](cmdqueryname=destination+ipv6)** **Ipv6Address** **[**remote-discriminator**](cmdqueryname=remote-discriminator)** *discriminator-value*
     
     
     
     The mapping between the IPv6 address and discriminator of the SBFD reflector is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The IPv6 address of the SBFD reflector must be the same as the endpoint of the corresponding SRv6 TE Policy.
  6. Run **[**quit**](cmdqueryname=quit)**
     
     
     
     Return to the system view.
  7. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
     
     
     
     The SRv6 view is displayed.
  8. Configure SBFD for SRv6 TE Policy.
     
     
     
     SBFD for SRv6 TE Policy supports both global configuration and single-policy configuration. You can select either of the two modes.
     
     + Global configuration
       
       1. Run the [**srv6-te-policy bfd seamless enable**](cmdqueryname=srv6-te-policy+bfd+seamless+enable) [ **reverse-path binding-sid** ] command to enable SBFD for all SRv6 TE Policies.
          
          In SBFD for SRv6 TE Policy scenarios, the **reverse-path binding-sid** parameter enables SBFD return packets to be forwarded over an SRv6 TE Policy. If this parameter is specified, a reverse binding SID needs to be configured for the segment list referenced by the candidate path of the SRv6 TE Policy on the local device, and the corresponding SRv6 TE Policy also needs to be configured on the peer device.
       2. (Optional) Run the [**srv6-te-policy bfd**](cmdqueryname=srv6-te-policy+bfd) { **min-tx-interval** *tx-value* | **detect-multiplier** *detectmulti-value* } \* command to configure SBFD parameters for the SRv6 TE Policies.
       3. (Optional) Run the [**srv6-te-policy bfd**](cmdqueryname=srv6-te-policy+bfd) { **min-tx-interval** *backup-tx-value* | **detect-multiplier** *backup-detectmulti-value* } \* **backup-path** command to configure SBFD parameters for the backup candidate paths of the SRv6 TE Policies.
       4. (Optional) Run the [**srv6-te-policy bfd switch-delay**](cmdqueryname=srv6-te-policy+bfd+switch-delay) *delay-interval* command to configure a BFD switching delay for the SRv6 TE Policies.
       5. (Optional) Run the [**srv6-te-policy bfd**](cmdqueryname=srv6-te-policy+bfd) **no-bypass** [ **preferred** ] command to enable the SBFD no-bypass function for the SRv6 TE Policies.
          
          After this function is enabled, SBFD for SRv6 TE Policy packets do not transit local protection paths such as TI-LFA and TE FRR paths.
          
          In scenarios where SBFD for SRv6 TE Policy is deployed, if the segment lists of the primary candidate path all fail and a local protection path (for example, a TI-LFA or TE FRR path) exists, SBFD remains in the Up state, and data traffic is switched to the TI-LFA or TE FRR path. However, the performance such as the bandwidth/latency of the TI-LFA or TE FRR path may be unstable, preventing the path from meeting the strict SLA requirements of high-value private line services. To resolve this problem, you can enable SBFD traffic to bypass local protection paths. In this way, SBFD goes Down if the segment lists of the primary candidate path all fail, triggering the candidate path to also go Down. As a result, traffic is switched to a backup candidate path or another SRv6 TE Policy.
          
          If the **preferred** parameter is specified and an SRv6 TE Policy has a backup path, BFD packets on the primary path are not transmitted over local protection paths such as TI-LFA and TE FRR paths. If the primary path fails, BFD goes down, and traffic is then switched to the backup path. BFD packets on the backup path can be transmitted over local protection paths to ensure service continuity.
     + Single-policy configuration
       
       1. Run the [**srv6-te policy**](cmdqueryname=srv6-te+policy) *policy-name* command to enter the SRv6 TE Policy view.
       2. Run the [**bfd seamless**](cmdqueryname=bfd+seamless) **enable** [ **reverse-path binding-sid** ] or [**bfd**](cmdqueryname=bfd) **disable** command to set the status of the SBFD function for the SRv6 TE Policy.
          
          In SBFD for SRv6 TE Policy scenarios, the **reverse-path binding-sid** parameter enables SBFD return packets to be forwarded over an SRv6 TE Policy. If this parameter is specified, a reverse binding SID needs to be configured for the segment list referenced by the candidate path of the SRv6 TE Policy on the local device, and the corresponding SRv6 TE Policy also needs to be configured on the peer device.
       3. (Optional) Run the [**bfd**](cmdqueryname=bfd) { **min-tx-interval** *tx-value* | **detect-multiplier** *detectmulti-value* } \* command to configure SBFD parameters for the SRv6 TE Policy.
       4. (Optional) Run the [**bfd**](cmdqueryname=bfd) { **min-tx-interval** *backup-tx-value* | **detect-multiplier** *backup-detectmulti-value* } \* **backup-path** command to configure SBFD parameters for the backup candidate paths of the SRv6 TE Policy.
       5. (Optional) Run the [**bfd**](cmdqueryname=bfd) { **no-bypass** [ **preferred** ] | **bypass** } command to set the status of the SBFD bypass function for the SRv6 TE Policy.
          
          If you do not want the SBFD packets of the SRv6 TE Policy to transit local protection paths such as TI-LFA and TE FRR paths, select the **no-bypass** parameter. Otherwise, select the **bypass** parameter.
          
          If you specify both the **no-bypass** and **preferred** parameters, the traffic forwarded over an SRv6 TE Policy is not preferentially transmitted over local protection paths. If an SRv6 TE Policy has a backup path, BFD packets on the primary path are not transmitted over local protection paths such as TI-LFA and TE FRR paths. If the primary path fails, BFD goes down, and traffic is then switched to the backup path. BFD packets on the backup path can be transmitted over local protection paths to ensure service continuity.
     
     If an SRv6 TE Policy has both global and single-policy configurations, the single-policy configuration takes precedence.
  9. (Optional) Run **[**srv6-te-policy switch-delay**](cmdqueryname=srv6-te-policy+switch-delay)** **switchDelay** **[**delete-delay**](cmdqueryname=delete-delay)** **deleteDelay**
     
     
     
     Segment list switching and deletion delays are configured for SRv6 TE Policies.
  10. Run **[**commit**](cmdqueryname=commit)**
      
      
      
      The configuration is committed.
* Configure an SBFD reflector.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally.
     
     
     
     BFD-related configuration can be performed only after BFD is enabled globally using the [**bfd**](cmdqueryname=bfd) command.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**sbfd**](cmdqueryname=sbfd)
     
     
     
     SBFD is enabled globally, and the SBFD view is displayed.
  5. Run [**reflector discriminator**](cmdqueryname=reflector+discriminator) *unsigned-integer-value*
     
     
     
     A discriminator is configured for the SBFD reflector.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     You can use a 32-bit integer or an IP address as an SBFD discriminator. A device converts discriminators into a uniform form, ensuring that each discriminator is globally unique in a domain.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After configuring SBFD for SRv6 TE Policy, run the **[**display srv6-te policy**](cmdqueryname=display+srv6-te+policy)** [****endpoint**** **ipv6-address** ****color**** **color-value** | ****policy-name**** **name-value** ] command to check SRv6 TE Policy-specific SBFD status.