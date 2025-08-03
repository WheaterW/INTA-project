Enabling the Capability of Dynamically Creating BFD Sessions on the Ingress
===========================================================================

You can enable the ingress node to dynamically create BFD sessions on a TE tunnel either globally or on a specified tunnel interface.

#### Context

Perform either of the following operations:

* [Enable MPLS TE BFD globally](#EN-US_TASK_0172368263__step_dc_vrp_cfg_00380901) if most TE tunnels on the ingress need to dynamically create BFD sessions.
* [Enable MPLS TE BFD on a tunnel interface](#EN-US_TASK_0172368263__step_dc_vrp_cfg_00380902) if some TE tunnels on the ingress need to dynamically create BFD sessions.

#### Procedure

* Enable MPLS TE BFD globally on the ingress.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls te bfd enable**](cmdqueryname=mpls+te+bfd+enable)
     
     
     
     The capability of dynamically creating BFD sessions is enabled on the TE tunnel.
     
     
     
     After this command is run in the MPLS view, dynamic BFD for TE LSP is enabled on all tunnel interfaces, excluding the interfaces on which dynamic BFD for TE LSP is blocked.
  4. (Optional) Block the capability of dynamically creating BFD sessions for TE LSP on the tunnel interfaces of the TE tunnels that do not need dynamic BFD for TE LSP.
     
     
     + Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
       
       The TE tunnel interface view is displayed.
     + Run [**mpls te bfd block**](cmdqueryname=mpls+te+bfd+block)
       
       The capability of dynamically creating BFD sessions on the tunnel interface is blocked.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable MPLS TE BFD on a tunnel interface of the ingress.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
     
     
     
     The TE tunnel interface view is displayed.
  3. Run [**mpls te bfd enable**](cmdqueryname=mpls+te+bfd+enable)
     
     
     
     The capability of dynamically creating BFD sessions is enabled on the TE tunnel.
     
     The command configured in the tunnel interface view takes effect only on the current tunnel interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.