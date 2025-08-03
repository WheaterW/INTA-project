Configuring SBFD for SR-MPLS TE Tunnel
======================================

This section describes how to configure SBFD to detect SR-MPLS TE tunnel faults.

#### Usage Scenario

If SBFD for SR-MPLS TE tunnel detects a fault on the primary tunnel, traffic is rapidly switched to the backup tunnel, which minimizes the impact on traffic.


#### Pre-configuration Tasks

Before configuring SBFD for SR-MPLS TE tunnel, complete the following task:

* Configure an SR-MPLS TE tunnel.
* Run the [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id* command to configure an LSR ID and ensure that the route from the peer to the local address specified using *lsr-id* is reachable.

#### Procedure

* Configure an SBFD initiator.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally.
     
     You can set BFD parameters only after running the [**bfd**](cmdqueryname=bfd) command to enable global BFD.
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
  7. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
     
     
     
     The SR-MPLS TE tunnel interface view is displayed.
  8. Run [**mpls te bfd tunnel enable seamless**](cmdqueryname=mpls+te+bfd+tunnel+enable+seamless)
     
     
     
     SBFD for SR-MPLS TE tunnel is enabled.
     
     
     
     After the configuration is complete, the SBFD initiator automatically establishes an SBFD session destined for the destination address of an SR-MPLS TE tunnel.
  9. (Optional) Configure an IS-IS SBFD source address.
     
     
     
     In IS-IS multi-process scenarios, you can configure source addresses for SBFD sessions in different IS-IS processes.
     
     By default, MPLS LSR IDs are used to create SBFD sessions. During SBFD deployment, only an LSR ID can be used as the source of an SBFD session, but the source belongs to only one IS-IS process. As a result, in the multi-process scenarios, LSR ID-based host routes must be imported in route import mode. Otherwise, SBFD cannot take effect. If IS-IS process isolation prevents route import, the device must support SBFD session establishment using different sources in different IS-IS processes.
     
     1. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
        
        The IS-IS view is displayed.
     3. Run [**cost-style**](cmdqueryname=cost-style) { **wide** | **compatible** | **wide-compatible** }
        
        The IS-IS wide metric is configured.
     4. Run [**segment-routing mpls**](cmdqueryname=segment-routing+mpls)
        
        IS-IS SR-MPLS is enabled.
     5. Run [**segment-routing sbfd source-address**](cmdqueryname=segment-routing+sbfd+source-address) *ip-address*
        
        An SBFD source address is configured.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure the SBFD reflector.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally.
     
     You can set BFD parameters only after running the [**bfd**](cmdqueryname=bfd) command to enable global BFD.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**sbfd**](cmdqueryname=sbfd)
     
     
     
     SBFD is enabled globally, and the SBFD view is displayed.
  5. Run [**reflector discriminator**](cmdqueryname=reflector+discriminator) { *unsigned-integer-value* | *ip-address-value* }
     
     
     
     The discriminator of an SBFD reflector is configured.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After you configure SBFD for SR-MPLS TE tunnel, run the [**display bfd session**](cmdqueryname=display+bfd+session) { **all** | **discriminator** *discr-value* } [ **verbose** ] command to check information about the SBFD session that monitors an SR-MPLS TE tunnel.