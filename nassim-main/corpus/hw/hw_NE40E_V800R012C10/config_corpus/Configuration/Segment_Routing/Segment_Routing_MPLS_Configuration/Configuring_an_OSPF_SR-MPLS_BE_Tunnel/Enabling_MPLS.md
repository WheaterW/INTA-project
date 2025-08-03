Enabling MPLS
=============

Enabling MPLS on each node in an SR-MPLS domain is the prerequisites for configuring an SR-MPLS BE tunnel.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id*
   
   
   
   An LSR ID is configured for the local node.
   
   
   
   Note the following during LSR ID configuration:
   * Configuring LSR IDs is the prerequisite for all MPLS configurations.
   * LSRs do not have default IDs. LSR IDs must be manually configured.
   * Using the address of a loopback interface as the LSR ID is recommended for an LSR.
3. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   MPLS is enabled globally.
   
   
   
   Because SR-MPLS uses the MPLS forwarding plane, it requires MPLS to be enabled globally and on specific interfaces.
   
   To avoid the complex configuration of enabling MPLS on interfaces one by one, an optimization has been made, so that MPLS can be automatically enabled on IGP-enabled interfaces if Segment Routing has been enabled for the IGP.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.