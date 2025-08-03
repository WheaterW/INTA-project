Configuring IPv6 Peers
======================

Devices can exchange BGP4+ routing information only after the IPv6 peer relationship is established among them.

#### Context

Because BGP4+ uses TCP connections, the IPv6 addresses for peers must be specified when you configure BGP4+. A BGP4+ peer may not be a neighboring Router, and a BGP4+ peer relationship can be created by using a logical link. Using the addresses of loopback interfaces to set up BGP4+ peer relationships can improve the stability of BGP4+ connections and is recommended.

The devices in the same AS establish IBGP peer relationships, and the devices of different ASs establish EBGP peer relationships.


#### Procedure

* Configure IBGP peers.
  
  
  
  Perform the following steps on the Routers between which an IBGP peer relationship needs to be set up:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *peerGroupName* } [**as-number**](cmdqueryname=as-number) *as-number*
     
     
     
     The address of the remote peer and the AS to which the remote peer belongs are configured.
     
     The number of the AS where the specified peer resides must be the same as that of the local AS.
     
     The IP address of the specified peer can be one of the following types:
     
     + IPv6 address of an interface on a directly connected peer
     + IP address of a routable loopback interface on the peer
     + IPv6 address of a sub-interface on a directly connected peer
     + Link-local address of an interface on a directly connected peer
     
     If the specified peer IPv6 address is the address of a loopback interface, you need to configure the local interface for the BGP4+ connection to ensure that the peer relationship is correctly established.
  4. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } [**connect-interface**](cmdqueryname=connect-interface) *interface-type* *interface-number* [ *ipv6-source-address* ]
     
     
     
     The source interface and source address for establishing a TCP connection are specified. To improve the reliability and stability of a BGP4+ connection to be established through loopback interfaces, you need to specify the local interface to be used to establish this BGP4+ connection.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When establishing multiple peer relationships between two Routers through multiple links, you are advised to run the [**peer connect-interface**](cmdqueryname=peer+connect-interface) command to specify the interface for establishing each BGP4+ connection.
     
     If the source interface used by the local end to establish a BGP4+ session is configured with multiple IP addresses, the [**peer connect-interface**](cmdqueryname=peer+connect-interface) command must be run to specify the source address. This ensures the correct connection between the two ends.
  5. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } [**listen-only**](cmdqueryname=listen-only)
     
     
     
     The local peer (group) is configured to accept connection requests, but not to send connection requests.
     
     After this command is run, the existing peer relationship is interrupted. The local peer will wait for a connection request from the remote peer to reestablish a peer relationship. This command enables only one peer to send connection requests, preventing a connection request conflict.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     This command can only be run on one of two peers. If this command is run on both peers, the connection between them cannot be reestablished.
  6. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } [**description**](cmdqueryname=description) *description-text*
     
     
     
     The description of the peer is configured.
     
     You can simplify network management by configuring the descriptions of peers.
  7. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  8. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } [**enable**](cmdqueryname=enable)
     
     
     
     The IPv6 peer is enabled.
     
     After configuring a BGP4+ peer in the BGP view, you also need to enable the peer in the IPv6 unicast address family view.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure EBGP peers.
  
  
  
  Perform the following steps on the Routers between which an EBGP peer relationship needs to be set up:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. (Optional) Run [**router-id allow-same enable**](cmdqueryname=router-id+allow-same+enable)
     
     
     
     The peers with the same router ID are allowed to establish EBGP connections.
  4. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } [**as-number**](cmdqueryname=as-number) *as-number*
     
     
     
     The IPv6 address of the remote peer and the AS to which the remote peer belongs are configured.
     
     The number of the AS where the specified peer resides must be different from that of the local AS.
     
     The IP address of the specified peer can be one of the following types:
     
     + IPv6 address of an interface on a directly connected peer
     + IP address of a routable loopback interface on the peer
     + IPv6 address of a sub-interface on a directly connected peer
     + Link-local address of an interface on a directly connected peer
     
     If the specified peer IP address is a loopback interface address or a local-link address, you need to configure the local interface for the BGP4+ connection to ensure that the peer relationship is correctly established.
  5. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } [**connect-interface**](cmdqueryname=connect-interface) *interface-type* *interface-number* [ *ipv6-source-address* ]
     
     
     
     The source interface and source address for establishing a TCP connection are specified.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When establishing multiple peer relationships between two Routers through multiple links, you are advised to run the [**peer connect-interface**](cmdqueryname=peer+connect-interface) command to specify the interface for establishing each BGP4+ connection.
  6. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } [**ebgp-max-hop**](cmdqueryname=ebgp-max-hop) [ *hop-count* ]
     
     
     
     The maximum number of hops is configured for establishing an EBGP connection.
     
     Generally, a direct physical link must be available between EBGP peers. If such a link does not exist, the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command must be used to allow EBGP peers to establish a TCP connection over multiple hops.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If loopback interfaces are used to establish an EBGP peer relationship, the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command must be run with *hop-count* greater than or equal to 2; otherwise, the peer relationship cannot be established.
  7. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } [**listen-only**](cmdqueryname=listen-only)
     
     
     
     The local peer (group) is configured to accept connection requests, but not to send connection requests.
     
     After this command is run, the existing peer relationship is interrupted. The local peer will wait for the connection request from the remote peer to reestablish a peer relationship. This command enables only one peer to send connection requests, preventing a connection request conflict.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     This command can only be run on one of two peers. If this command is run on both peers, the connection between them cannot be reestablished.
  8. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } [**description**](cmdqueryname=description) *description-text*
     
     
     
     The description of the peer is configured.
     
     You can simplify network management by configuring the descriptions of peers.
  9. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  10. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } [**enable**](cmdqueryname=enable)
      
      
      
      The IPv6 peer is enabled.
      
      After configuring a BGP4+ peer in the BGP view, you also need to enable the peer in the IPv6 unicast address family view.
  11. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *peerGroupName* } **peer-as-check**
      
      
      
      The device is configured not to advertise the routes learned from an EBGP peer to the peers in the same AS with the EBGP peer.
      
      
      
      By default, after receiving a route from an EBGP peer (for example, in AS 200), the local device (for example, in AS 100) advertises the route to other EBGP peers in AS 200. After the [**peer peer-as-check**](cmdqueryname=peer+peer-as-check) command is run on the device, the device does not advertise the routes received from an EBGP peer to other EBGP peers in the same AS with this EBGP peer. This reduces BGP memory and CPU consumption and speeds up route convergence in case of route flapping.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.