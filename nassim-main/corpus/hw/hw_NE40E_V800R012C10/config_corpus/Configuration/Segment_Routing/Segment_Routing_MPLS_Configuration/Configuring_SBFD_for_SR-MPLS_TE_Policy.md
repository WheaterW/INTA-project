Configuring SBFD for SR-MPLS TE Policy
======================================

This section describes how to configure seamless bidirectional forwarding detection (SBFD) for SR-MPLS TE Policy.

#### Usage Scenario

SBFD for SR-MPLS TE Policy can quickly detect segment list faults. If all the segment lists of a candidate path are faulty, SBFD triggers a hot-standby candidate path switchover to minimize the impact on services.


#### Pre-configuration Tasks

Before configuring SBFD for SR-MPLS TE Policy, complete the following tasks:

* Configure an SR-MPLS TE Policy.
* Run the [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id* command to configure an LSR ID and ensure that the route from the peer to the local address specified using *lsr-id* is reachable.

#### Procedure

* Configure an SBFD initiator.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally.
     
     BFD can be configured only after this function is enabled globally using the [**bfd**](cmdqueryname=bfd) command.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**sbfd**](cmdqueryname=sbfd)
     
     
     
     SBFD is enabled globally, and the SBFD view is displayed.
  5. (Optional) Run [**destination ipv4**](cmdqueryname=destination+ipv4) *ip-address* [**remote-discriminator**](cmdqueryname=remote-discriminator) *discriminator-value*
     
     
     
     The mapping between the SBFD reflector IP address and discriminator is configured.
     
     
     
     On the device functioning as an SBFD initiator, if the mapping between the SBFD reflector IP address and discriminator is configured using the [**destination ipv4 remote-discriminator**](cmdqueryname=destination+ipv4+remote-discriminator) command, the initiator uses the configured discriminator to negotiate with the reflector in order to establish an SBFD session. If such a mapping is not configured, the SBFD initiator uses the reflector IP address as a discriminator by default to complete the negotiation.
     
     This step is optional. If it is performed, the value of *discriminator-value* must be the same as that of *unsigned-integer-value* in the [**reflector discriminator**](cmdqueryname=reflector+discriminator) command configured on the reflector.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. Run [**segment-routing**](cmdqueryname=segment-routing)
     
     
     
     SR is enabled globally and the Segment Routing view is displayed.
  8. Configure SBFD for SR-MPLS TE Policy.
     
     
     
     SBFD for SR-MPLS TE Policy supports both global configuration and single-policy configuration. You can select either of the two modes.
     
     + Global configuration
       
       1. Run [**sr-te-policy seamless-bfd enable**](cmdqueryname=sr-te-policy+seamless-bfd+enable)
          
          SBFD is enabled for all SR-MPLS TE Policies.
       2. (Optional) Run [**sr-te-policy seamless-bfd**](cmdqueryname=sr-te-policy+seamless-bfd) { **min-rx-interval** *receive-interval* | **min-tx-interval** *transmit-interval* | **detect-multiplier** *multiplier-value* } \*
          
          SBFD parameters are set for the SR-MPLS TE Policies.
          
          ![](../../../../public_sys-resources/note_3.0-en-us.png) 
          
          In the SBFD scenario, the **min-rx-interval** *receive-interval* parameter will not take effect.
     + Single-policy configuration
       
       1. Run [**sr-te policy**](cmdqueryname=sr-te+policy) *policy-name*
          
          The SR-MPLS TE Policy view is displayed.
       2. Run [**seamless-bfd**](cmdqueryname=seamless-bfd) { **enable** | **disable** }
          
          SBFD is enabled or disabled for the SR-MPLS TE Policy.
       3. Run [**quit**](cmdqueryname=quit)
          
          Return to the SR view.
     
     If an SR-MPLS TE Policy has both global configuration and single-policy configuration, the single-policy configuration takes effect.
  9. (Optional) Run [**sr-te-policy delete-delay**](cmdqueryname=sr-te-policy+delete-delay) *delete-delay-value*
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure an SBFD reflector.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally.
     
     
     
     BFD can be configured only after this function is enabled globally using the [**bfd**](cmdqueryname=bfd) command.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**sbfd**](cmdqueryname=sbfd)
     
     
     
     SBFD is enabled globally, and the SBFD view is displayed.
  5. Run [**reflector discriminator**](cmdqueryname=reflector+discriminator) { *unsigned-integer-value* | *ip-address-value* }
     
     
     
     A discriminator is configured for the SBFD reflector.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After SBFD for SR-MPLS TE Policy is configured, run the [**display sr-te policy**](cmdqueryname=display+sr-te+policy) [ [**endpoint**](cmdqueryname=endpoint) *ipv4-address* **color** *color-value* | **policy-name** *name-value* ] command to check SBFD status.