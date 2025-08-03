Configuring a Remote LDP Peer
=============================

Before you configure a remote LDP session, specify the name and IP address of the remote peer.

#### Context

A remote LDP session can be established between nonadjacent LSRs or between adjacent LSRs.

A local LDP session and a remote LDP session can be configured together between the same two LSRs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp remote-peer**](cmdqueryname=mpls+ldp+remote-peer) *remote-peer-name*
   
   
   
   A remote MPLS LDP peer is created, and the remote MPLS LDP peer view is displayed.
3. (Optional) Run [**description**](cmdqueryname=description) *description-value*
   
   
   
   The description of a remote peer is configured.
4. Run [**remote-ip**](cmdqueryname=remote-ip) *ip-address*
   
   
   
   The IP address is assigned to the remote MPLS LDP peer.
   
   The remote MPLS LDP peer must use the LSR ID as the IP address.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The IP address of a remote LDP peer must be the LSR ID of the remote LDP peer. If an LDP LSR ID is different from an MPLS LSR ID, the LDP LSR ID is used.
   * Modifying or deleting a configured IP address of a remote peer also deletes the remote LDP session.
5. (Optional) Perform either of the following operations to prevent label distribution to remote LDP peers:
   
   
   * Run [**remote-ip**](cmdqueryname=remote-ip+pwe3) *ip-address* **pwe3**
     
     The device is disabled from distributing labels to a specified remote MPLS LDP peer.
   * Run the following commands to prevent labels from being distributed to all remote MPLS LDP peers.
     1. (Optional) Run [**clear remote-ip pwe3**](cmdqueryname=clear+remote-ip+pwe3)
        
        The explicit configuration of enabling or disabling the ability to distribute labels to a specified remote LDP peer is deleted.
        
        If an explicit configuration has been performed to allow a device to distribute labels to a specified remote LDP peer, to delete the configuration, you can perform this step.
     2. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     3. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
        
        The MPLS-LDP view is displayed.
     4. Run [**remote-peer pwe3**](cmdqueryname=remote-peer+pwe3)
        
        The device is disabled from distributing labels to all remote MPLS LDP peers.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When a remote LDP session provides VPN services, run the preceding commands to prohibit labels from being distributed to the remote MPLS LDP peers, which helps efficiently use system resources. When TE services are transmitted over a backbone network in the LDP over TE scenario, do not perform this configuration.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.