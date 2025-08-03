Creating an ICCP Redundancy Group
=================================

Creating_an_ICCP_Redundancy_Group

#### Context

ICCP establishes reliable ICCP channels over LDP sessions for different devices to transmit information. One or more PEs in the same administrative domain form an RG to protect services and use established ICCP sessions to communicate with each other.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id*
   
   
   
   An LSR ID is set for the local node.
3. Run **[**mpls**](cmdqueryname=mpls)**
   
   
   
   MPLS is enabled globally, and the MPLS view is displayed.
4. Run **[**mpls ldp**](cmdqueryname=mpls+ldp)**
   
   
   
   LDP is enabled globally, and the MPLS LDP view is displayed.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**mpls ldp remote-peer**](cmdqueryname=mpls+ldp+remote-peer) *remote-peer-name*
   
   
   
   A remote MPLS LDP peer is created, and its view is displayed.
7. Run [**remote-ip**](cmdqueryname=remote-ip) *ip-address*
   
   
   
   An IP address is configured for the remote MPLS LDP peer.
8. Run **[**iccp redundancy group**](cmdqueryname=iccp+redundancy+group)** **groupId**
   
   
   
   An ICCP redundancy group is created.
9. Run **[**peer-ip**](cmdqueryname=peer-ip)** **ip-address**
   
   
   
   A peer IP address is configured for the ICCP redundancy group, which is then bound to an LDP session.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The peer address of the ICCP redundancy group is the IP address of the remote MPLS LDP peer, which is the LSR ID of the remote device configured using the [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) command. IP address 0.X.X.X, 127.X.X.X, or one greater than or equal to 224.0.0.0 cannot be configured.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.