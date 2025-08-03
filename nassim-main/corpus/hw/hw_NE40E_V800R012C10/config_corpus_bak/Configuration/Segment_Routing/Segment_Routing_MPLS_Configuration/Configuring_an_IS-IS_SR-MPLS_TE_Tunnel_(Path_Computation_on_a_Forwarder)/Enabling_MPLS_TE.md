Enabling MPLS TE
================

Before configuring an SR-MPLS TE tunnel, you need to enable MPLS TE on each involved node in the SR-MPLS domain.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id*
   
   
   
   An LSR ID is configured for the device.
   
   
   
   Note the following during LSR ID configuration:
   * Configuring LSR IDs is the prerequisite for all MPLS configurations.
   * LSRs do not have default IDs. LSR IDs must be manually configured.
   * Using a loopback interface address as the LSR ID is recommended for an LSR.
3. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
4. (Optional) Run [**mpls te sid selection unprotected-only**](cmdqueryname=mpls+te+sid+selection+unprotected-only)
   
   
   
   The device is enabled to consider only unprotected labels when computing paths for SR-MPLS TE tunnels.
   
   
   
   To enable the device to consider only unprotected labels during SR-MPLS TE tunnel path computation, perform this step.
5. Run [**mpls te**](cmdqueryname=mpls+te)
   
   
   
   MPLS TE is enabled globally.
6. (Optional) Enable interface-specific MPLS TE.
   
   
   
   In scenarios where the controller or ingress performs path computation, interface-specific MPLS TE must be enabled. In static explicit path scenarios, this step can be ignored.
   
   
   
   1. Run [**quit**](cmdqueryname=quit)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
      
      
      
      The view of the interface on which the MPLS TE tunnel is established is displayed.
   3. Run [**mpls**](cmdqueryname=mpls)
      
      
      
      MPLS is enabled on an interface.
   4. Run [**mpls te**](cmdqueryname=mpls+te)
      
      
      
      MPLS TE is enabled on the interface.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.