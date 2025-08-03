Configuring SBFD for SR-MPLS TE LSP
===================================

This section describes how to configure SBFD to detect SR-MPLS TE LSP faults.

#### Usage Scenario

If SBFD for SR-MPLS TE LSP detects a fault on the primary LSP, traffic is rapidly switched to the backup LSP, which minimizes the impact on traffic.


#### Pre-configuration Tasks

Before configuring SBFD for SR-MPLS TE LSP, complete the following task:

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
  8. Run [**mpls te bfd enable**](cmdqueryname=mpls+te+bfd+enable) **seamless**
     
     
     
     SBFD for SR-MPLS TE LSP is enabled.
     
     
     
     After the configuration is complete, the SBFD initiator automatically establishes an SBFD session destined for the destination address of an SR-MPLS TE tunnel.
  9. (Optional) Run [**mpls te reverse-lsp binding-sid**](cmdqueryname=mpls+te+reverse-lsp+binding-sid) **label** *label-value*
     
     
     
     A label is configured for the SR-MPLS TE tunnel used for BFD return packets. This label must be the binding SID of the tunnel.
     
     
     
     Before running this command, ensure that the [**mpls te binding-sid label**](cmdqueryname=mpls+te+binding-sid+label) *label-value* command has been run on the ingress of the reverse SR-MPLS TE tunnel.
     
     In SBFD for SR-MPLS TE LSP scenarios, SBFD packets from the initiator to the reflector are forwarded along an SR-MPLS TE LSP, whereas the return packets from the reflector to the initiator are forwarded along a multi-hop IP path. To allow the return packets to be forwarded also along an LSP, run the [**mpls te reverse-lsp binding-sid**](cmdqueryname=mpls+te+reverse-lsp+binding-sid) command.
     
     Both the forward and reverse SR-MPLS TE tunnels may have a primary LSP and a backup LSP. After the [**mpls te reverse-lsp binding-sid**](cmdqueryname=mpls+te+reverse-lsp+binding-sid) command is run, the SBFD packet sent by the initiator carries the primary/backup LSP flag. If the SBFD packet sent by the initiator is forwarded through the primary LSP of the forward tunnel, the SBFD return packet sent by the reflector is forwarded through the primary LSP of the reverse tunnel. If the SBFD packet sent by the initiator is forwarded through the backup LSP of the forward tunnel, the SBFD return packet sent by the reflector is forwarded through the backup LSP of the reverse tunnel.
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

After you configure SBFD for SR-MPLS TE LSP, run the [**display bfd session**](cmdqueryname=display+bfd+session) { **all** | **discriminator** *discr-value* } [ **verbose** ] command to check information about the SBFD session that monitors an SR-MPLS TE tunnel.