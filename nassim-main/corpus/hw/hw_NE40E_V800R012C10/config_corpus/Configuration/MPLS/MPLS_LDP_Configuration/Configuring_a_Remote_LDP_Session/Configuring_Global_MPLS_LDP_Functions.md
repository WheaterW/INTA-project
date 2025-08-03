Configuring Global MPLS LDP Functions
=====================================

Global LDP must be enabled on each node before LDP services can be configured in an MPLS domain.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id*
   
   
   
   An LSR ID is set for the local node.
   
   
   
   When configuring an LSR ID, note the following:
   * LSR IDs must be set before you run other MPLS commands.
   * LSR IDs can only be manually configured, and do not have default values.
   * Using the address of a loopback interface as the LSR ID is recommended.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     Running the [**undo mpls**](cmdqueryname=undo+mpls) command deletes all MPLS configurations, including established LDP sessions and LSPs.
3. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   MPLS is enabled globally, and the MPLS view is displayed.
4. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   MPLS LDP is enabled globally, and the MPLS-LDP view is displayed.
5. (Optional) Run [**lsr-id**](cmdqueryname=lsr-id) *lsr-id*
   
   
   
   The LSR ID is set for an LDP instance.
   
   An MPLS LSR ID is usually used as the LSR ID of an LDP instance. When VPN instances are used, such as a BGP/MPLS VPN, if the VPN address space and public network address space overlap, set LSR IDs for LDP instances so that TCP connections for LDP sessions can be properly established.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.