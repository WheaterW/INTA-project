Configuring a BGP4+ Peer
========================

Configuring a BGP4+ Peer

#### Context

As BGP4+ peer relationships are established over TCP connections, you need to specify the IPv6 addresses of peers when configuring them. A BGP4+ peer may not be a neighboring device, and BGP4+ peer relationships can be established through logical links. To enhance the stability of BGP4+ connections, using loopback interface addresses is recommended for the connections.

Devices in the same AS establish IBGP peer relationships, whereas devices from different ASs establish EBGP peer relationships.


#### Procedure

* Configure an IBGP peer.
  
  
  
  Perform the following steps on the devices between which an IBGP peer relationship needs to be set up:
  
  
  
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Specify the IPv6 address of a peer and the number of the AS where the peer resides.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv6-address | group-name } [as-number](cmdqueryname=as-number) as-number
     ```
     
     The number of the AS where the specified peer resides must be the same as that of the local AS.
     
     The IPv6 address of the specified peer can be one of the following:
     
     + IPv6 address of the peer's interface that directly connects to the local device
     + Address of a routing-reachable loopback interface on the peer
     + IPv6 address of a sub-interface on the peer's interface that directly connects to the local device
     + Link-local address of the peer's interface that directly connects to the local device
  4. (Optional) Specify the source interface and source address for TCP connection establishment.
     
     
     ```
     [peer](cmdqueryname=peer+connect-interface) ipv6-address connect-interface { interface-name | ipv6-source-address | interface-type interface-number | interface-name ipv6-source-address | interface-type interface-number ipv6-source-address }
     ```
     ```
     [peer](cmdqueryname=peer+connect-interface) group-name connect-interface { interface-name | ipv4-source-addr | ipv6-source-addr | interface-type interface-number | interface-name ipv4-source-addr | interface-name ipv6-source-addr | interface-type interface-number ipv4-source-addr | interface-type interface-number ipv6-source-addr }
     ```
     
     
     
     In most cases, BGP4+ uses the physical interface directly connected to the peer as the interface for a TCP connection.
     
     To increase the reliability and stability of a BGP4+ connection, you can specify a device's loopback interface as the local interface used for the BGP4+ connection. As a result, when redundant links exist on the network, the BGP4+ connection will not be terminated due to failure of a specific interface or link.
  5. (Optional) Configure the device to only listen for connection requests from the specified peer, and not to initiate connection requests.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv6-address | group-name } [listen-only](cmdqueryname=listen-only)
     ```
     
     After this command is run on the local device, the existing peer relationship is terminated, and the device waits for a connection request from the specified peer to re-establish a peer relationship. This configuration can prevent conflicts in connection requests.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     This command can be run only on one end. If it is run on both ends, the connection between both ends cannot be established.
  6. (Optional) Configure a description for the specified peer.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv6-address | group-name } [description](cmdqueryname=description) description-text
     ```
     
     To simplify network management, you can configure a description for a specified peer.
  7. Enter the IPv6 unicast address family view.
     
     
     ```
     [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
     ```
  8. Enable the IPv6 peer.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv6-address | group-name } [enable](cmdqueryname=enable)
     ```
     
     After configuring a BGP4+ peer in the BGP view, enable the peer in the IPv6 unicast address family view.
  9. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure an EBGP peer.
  
  
  
  Perform the following steps on the devices between which an EBGP peer relationship needs to be set up:
  
  
  
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. (Optional) Allow EBGP connections to be established between peers with the same router ID.
     
     
     ```
     [router-id allow-same enable](cmdqueryname=router-id+allow-same+enable)
     ```
  4. Specify the IPv6 address of a peer and the number of the AS where the peer resides.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv6-address | group-name } [as-number](cmdqueryname=as-number) as-number
     ```
     
     The number of the AS where the specified peer resides must be different from that of the local AS.
     
     The IPv6 address of the specified peer can be one of the following:
     
     + IPv6 address of the peer's interface that directly connects to the local device
     + Address of a routing-reachable loopback interface on the peer
     + IPv6 address of a sub-interface on the peer's interface that directly connects to the local device
     + Link-local address of the peer's interface that directly connects to the local device
     
     If the IP address of a specified BGP4+ peer is a loopback interface address or a link-local address, the source interface used for the BGP4+ connection must be specified to ensure that the peer relationship can be established correctly.
  5. Set the maximum number of hops allowed over an EBGP connection.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv6-address | group-name } [ebgp-max-hop](cmdqueryname=ebgp-max-hop) [ hop-count ]
     ```
     
     In most cases, a directly connected physical link must be available between EBGP peers. To establish an EBGP peer relationship between indirectly connected devices, you need to run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command to set the maximum number of hops allowed over the EBGP connection.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     If loopback interfaces are used to establish an EBGP peer relationship, the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command (*hop-count* â¥ 2) must be run. Otherwise, the peer relationship cannot be established.
  6. (Optional) Specify the source interface and source address for TCP connection establishment.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv6-address | group-name } [connect-interface](cmdqueryname=connect-interface) interface-type interface-number ipv6-source-address
     ```
     
     In most cases, BGP4+ uses the physical interface directly connected to the peer as the interface for a TCP connection.
     
     To increase the reliability and stability of a BGP4+ connection, you can specify a device's loopback interface as the local interface used for the BGP4+ connection. As a result, when redundant links exist on the network, the BGP4+ connection will not be terminated due to failure of a specific interface or link.
  7. (Optional) Configure the device to only listen for connection requests from the specified peer, and not to initiate connection requests.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv6-address | group-name } [listen-only](cmdqueryname=listen-only)
     ```
     
     After this command is run on the local device, the existing peer relationship is terminated, and the device waits for a connection request from the specified peer to re-establish a peer relationship. This configuration can prevent conflicts in connection requests.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     This command can be run only on one end. If it is run on both ends, the connection between both ends cannot be established.
  8. (Optional) Configure a description for the specified peer.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv6-address | group-name } [description](cmdqueryname=description) description-text
     ```
     
     To simplify network management, you can configure a description for a specified peer.
  9. Enter the IPv6 unicast address family view.
     
     
     ```
     [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
     ```
  10. Enable the IPv6 peer.
      
      
      ```
      [peer](cmdqueryname=peer) { ipv6-address | group-name } [enable](cmdqueryname=enable)
      ```
      
      After configuring a BGP4+ peer in the BGP view, enable the peer in the IPv6 unicast address family view.
  11. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```