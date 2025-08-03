Configuring a BGP Peer
======================

Devices can exchange BGP routing information only after the BGP peer relationship is established.

#### Context

BGP peers use TCP to establish connections. Therefore, you need to specify the IP addresses of the peers when configuring BGP. A BGP peer may not be a neighboring node, and the BGP peer relationship can be created through logical links. To enhance the stability of BGP connections, using loopback interface addresses to establish connections is recommended.

The devices in the same AS establish IBGP peer relationships, and the devices of different ASs establish EBGP peer relationships.


#### Procedure

* Configure an IBGP peer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer+as-number) { *ipv4-address* | *peerGroupName* } [**as-number**](cmdqueryname=peer+as-number) *as-number*
     
     
     
     The IP address of the peer and the number of the AS where the peer resides are specified.
     
     
     
     The number of the AS where the specified peer resides must be the same as that of the local AS.
     
     The IP address of the peer can be one of the following types:
     
     + IP address of the peer's interface that is directly connected to the local device
     + IP address of a sub-interface on a directly connected peer
     + IP address of a reachable loopback interface on the peer
  4. (Optional) Run [**peer**](cmdqueryname=peer+connect-interface) { *ipv4-address* | *peerGroupName* } [**connect-interface**](cmdqueryname=peer+connect-interface) *interface-type* *interface-number* [ *ipv4-source-address* ]
     
     
     
     The source interface and source address are specified for establishing a TCP connection with the specified BGP peer.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the IP address of a loopback interface or a sub-interface is used to establish a BGP connection, you are advised to run the [**peer connect-interface**](cmdqueryname=peer+connect-interface) command at both ends of the connection to ensure that the connection is correctly established. If this command is run on only one end, the BGP connection may fail to be established.
     
     If the source interface used by the local end to establish a BGP session is configured with multiple IP addresses, the [**peer connect-interface**](cmdqueryname=peer+connect-interface) command must be run to specify the source address. This ensures the correct connection between the two ends.
  5. (Optional) Run [**peer**](cmdqueryname=peer+description) { *ipv4-address* | *peerGroupName* } [**description**](cmdqueryname=peer+description) *description-text*
     
     
     
     A description is configured for the peer.
     
     
     
     To simplify network management, you can configure a description for a specified peer.
  6. (Optional) Run [**peer**](cmdqueryname=peer+tcp-mss) { *ipv4-address* | *peerGroupName* } [**tcp-mss**](cmdqueryname=peer+tcp-mss) *tcp-mss-number*
     
     
     
     A TCP MSS value used during TCP connection establishment with a peer or peer group is configured.
     
     
     
     This configuration ensures that TCP packets can still be segmented properly based on the specified TCP MSS in cases where the path MTU is unavailable, thereby improving network performance.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an EBGP peer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. (Optional) Run [**router-id allow-same enable**](cmdqueryname=router-id+allow-same+enable)
     
     
     
     The peers with the same router ID are allowed to establish EBGP connections.
  4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *peerGroupName* } [**as-number**](cmdqueryname=as-number) *as-number*
     
     
     
     A peer IP address and the number of the AS where the peer resides are specified.
     
     
     
     The number of the AS where the specified peer resides must be different from that of the local AS.
     
     The IP address of the peer can be one of the following types:
     
     + IP address of the peer's interface that is directly connected to the local device
     + IP address of a sub-interface on a directly connected peer
     + IP address of a reachable loopback interface on the peer
  5. (Optional) Run [**peer**](cmdqueryname=peer+connect-interface) { *ipv4-address* | *peerGroupName* } [**connect-interface**](cmdqueryname=peer+connect-interface) *interface-type* *interface-number* [ *ipv4-source-address* ]
     
     
     
     The source interface and source address are specified for establishing a TCP connection with the specified BGP peer.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the IP address of a loopback interface or a sub-interface is used to establish a BGP connection, you are advised to run the [**peer connect-interface**](cmdqueryname=peer+connect-interface) command at both ends of the connection to ensure that the connection is correctly established. If this command is run on only one end, the BGP connection may not be established.
  6. (Optional) Run [**peer**](cmdqueryname=peer+ebgp-max-hop) { *ipv4-address* | *peerGroupName* } [**ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) [ *hop-count* ]
     
     
     
     The maximum number of hops allowed over an EBGP connection is set.
     
     
     
     In most cases, EBGP peers are directly connected through a physical link. If you want to establish an EBGP peer relationship between indirectly connected peers, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command to set the maximum number of hops allowed over the TCP connection.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If loopback interfaces are used to establish an EBGP connection, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command, where the value of *hop-count* must be greater than or equal to 2. Otherwise, the EBGP peer relationship cannot be established.
  7. (Optional) Run [**peer**](cmdqueryname=peer+description) { *ipv4-address* | *peerGroupName* } [**description**](cmdqueryname=peer+description) *description-text*
     
     
     
     A description is configured for the peer.
     
     
     
     To simplify network management, you can configure a description for a specified peer.
  8. (Optional) Run [**peer**](cmdqueryname=peer+peer-as-check) { *ipv4-address* | *peerGroupName* } [**peer-as-check**](cmdqueryname=peer+peer-as-check)
     
     
     
     The device is configured not to advertise the routes learned from an EBGP peer to the peers in the same AS with the EBGP peer.
     
     
     
     By default, after receiving a route from an EBGP peer (for example, in AS 200), the local device (for example, in AS 100) advertises the route to other EBGP peers in AS 200. After the [**peer peer-as-check**](cmdqueryname=peer+peer-as-check) command is run on the device, the device does not advertise the routes received from an EBGP peer to other EBGP peers in the same AS with this EBGP peer. This reduces BGP memory and CPU consumption and speeds up route convergence in case of route flapping.
  9. (Optional) Run [**peer**](cmdqueryname=peer+tcp-mss) { *ipv4-address* | *peerGroupName* } [**tcp-mss**](cmdqueryname=peer+tcp-mss) *tcp-mss-number*
     
     
     
     A TCP MSS value used during TCP connection establishment with a peer or peer group is configured.
     
     
     
     This configuration ensures that TCP packets can still be segmented properly based on the specified TCP MSS in cases where the path MTU is unavailable, thereby improving network performance.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.