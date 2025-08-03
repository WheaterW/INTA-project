(Optional) Configuring Graceful Shutdown
========================================

The graceful shutdown function can be enabled to help traffic migrate in seamless switching scenarios, which reduces the upgrade and maintenance expenses on an entire device.

#### Procedure

1. Configure graceful shutdown in the MPLS view.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**mpls**](cmdqueryname=mpls)
      
      
      
      The MPLS view is displayed.
   3. Run [**mpls te**](cmdqueryname=mpls+te)
      
      
      
      MPLS TE is globally enabled.
   4. Run [**mpls rsvp-te**](cmdqueryname=mpls+rsvp-te)
      
      
      
      RSVP-TE is enabled.
   5. Run [**mpls rsvp-te graceful-shutdown**](cmdqueryname=mpls+rsvp-te+graceful-shutdown)
      
      
      
      Graceful shutdown is enabled.
   6. (Optional) Run [**mpls rsvp-te timer graceful-shutdown**](cmdqueryname=mpls+rsvp-te+timer+graceful-shutdown) *graceful-shutdown-time*
      
      
      
      A graceful shutdown timeout period is set.
      
      
      
      During graceful shutdown, if the RSVP LSP rerouting request fails within the specified graceful shutdown timeout period after a rerouting request message is sent, the RSVP LSP will be directly deleted.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure graceful shutdown in the interface view.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
      
      
      
      The interface view is displayed.
   3. Run [**mpls**](cmdqueryname=mpls)
      
      
      
      MPLS is enabled on the interface.
   4. Run [**mpls te**](cmdqueryname=mpls+te)
      
      
      
      MPLS TE is enabled on the interface.
   5. Run [**mpls rsvp-te graceful-shutdown**](cmdqueryname=mpls+rsvp-te+graceful-shutdown)
      
      
      
      Graceful shutdown is enabled.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.