Creating Remote LDP Peers on Both Ends of a TE Tunnel
=====================================================

Configure nodes on both ends of a TE tunnel as remote LDP peers.

#### Context

If the destination address of the TE tunnel is not the LSR ID of the egress, the interface with the destination address must be enabled with LDP.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp remote-peer**](cmdqueryname=mpls+ldp+remote-peer) *remote-peer-name*
   
   
   
   The remote MPLS LDP peer view is displayed.
3. Run [**remote-ip**](cmdqueryname=remote-ip) *ip-address*
   
   
   
   An IP address is assigned to the remote LDP peer.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.