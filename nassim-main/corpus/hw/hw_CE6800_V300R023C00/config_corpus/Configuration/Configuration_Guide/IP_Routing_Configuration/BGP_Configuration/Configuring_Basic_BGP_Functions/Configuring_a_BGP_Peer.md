Configuring a BGP Peer
======================

Configuring a BGP Peer

#### Context

As BGP peer relationships are established over TCP connections, you need to specify the IP addresses of peers when configuring them. A BGP peer may not be a neighboring device, and BGP peer relationships can be established through logical links. To enhance the stability of BGP connections, using loopback interface addresses to establish connections is recommended.

Establish IBGP peer relationships between devices in the same AS and EBGP peer relationships between devices in different ASs.

![](public_sys-resources/note_3.0-en-us.png) 

EBGP peers do not support the following features:

* RR
* RPKI
* Best-External
* Add-Path

IBGP peers do not support the following features:

* ebgp-max-hop
* local-as

The **ebgp-max-hop** and **valid-ttl-hops** functions are mutually exclusive.



#### Procedure

* Configure an IBGP peer.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Specify the IP address of a peer and the number of the AS where the peer resides.
     
     
     ```
     [peer](cmdqueryname=peer+as-number) { ipv4-address | ipv6-address | group-name } [as-number](cmdqueryname=as-number) as-number
     ```
     
     The number of the AS where the specified peer resides must be the same as that of the local AS.
     
     The IP address of the peer can be one of the following types:
     
     + IP address of an interface on a directly connected peer
     + IP address of a sub-interface on a directly connected peer
     + IP address of a routable loopback interface on the peer
  4. (Optional) Specify the source interface and source IP address for TCP connection establishment between BGP peers.
     
     
     ```
     [peer](cmdqueryname=peer) ipv4-address [connect-interface](cmdqueryname=connect-interface) { interface-name | ipv4-source-address | interface-type interface-number | interface-name ipv4-source-address | interface-type interface-number ipv4-source-address }
     or
     [peer](cmdqueryname=peer) group-name [connect-interface](cmdqueryname=connect-interface) { interface-name | ipv4-source-addr | ipv6-source-addr| interface-type interface-number | interface-name ipv4-source-addr| interface-name ipv6-source-addr | interface-type interface-number ipv4-source-addr | interface-type interface-number ipv6-source-addr }
     ```
     
     By default, BGP uses the physical interface directly connected to a peer as the local interface of a TCP connection.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     If the IP address of a loopback interface or a sub-interface is used to establish a BGP connection, you are advised to run the [**peer connect-interface**](cmdqueryname=peer+connect-interface) command at both ends of the connection to ensure that the connection is correctly established. If this command is run on only one end, the BGP connection may fail to be established.
  5. (Optional) Set the TCP MSS value used when the local device establishes a TCP connection with the peer.
     
     
     ```
     [peer](cmdqueryname=peer+tcp-mss) { ipv4-address | ipv6-address | group-name } tcp-mss tcp-mss-number
     ```
     
     This configuration ensures that TCP packets can still be fragmented properly based on the specified TCP MSS in cases where the path MTU is unavailable, thereby improving network performance.
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure an EBGP peer.
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
  4. Specify the IP address of a peer and the number of the AS where the peer resides.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv4-address | group-name } [as-number](cmdqueryname=as-number) as-number
     ```
     
     The number of the AS where the specified peer resides must be different from that of the local AS.
     
     The IP address of the peer can be one of the following types:
     
     + IP address of an interface on a directly connected peer
     + IP address of a sub-interface on a directly connected peer
     + IP address of a routable loopback interface on the peer
  5. (Optional) Specify the source interface and source IP address for TCP connection establishment between BGP peers.
     
     
     ```
     [peer](cmdqueryname=peer) ipv4-address [connect-interface](cmdqueryname=connect-interface) { interface-name | ipv4-source-address | interface-type interface-number | interface-name ipv4-source-address | interface-type interface-number ipv4-source-address }
     or
     [peer](cmdqueryname=peer)  group-name [connect-interface](cmdqueryname=connect-interface) { interface-name | ipv4-source-address | ipv6-source-address| interface-type interface-number | interface-name ipv4-source-address| interface-name ipv6-source-address | interface-type interface-number ipv4-source-address | interface-type interface-number ipv6-source-address }
     ```
     
     By default, BGP uses the physical interface directly connected to a peer as the local interface of a TCP connection.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     If the IP address of a loopback interface or a sub-interface is used to establish a BGP connection, you are advised to run the [**peer connect-interface**](cmdqueryname=peer+connect-interface) command at both ends of the connection to ensure that the connection is correctly established. If this command is run on only one end, the BGP connection may fail to be established.
  6. (Optional) Set the maximum number of hops allowed over an EBGP connection.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv4-address | group-name } [ebgp-max-hop](cmdqueryname=ebgp-max-hop) [ hop-count ]
     ```
     
     The default value of *hop-count* is 255.
     
     In most cases, a directly connected physical link must be available between EBGP peers. If you want to establish an EBGP peer relationship between indirectly connected peers, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command to set the maximum number of hops allowed over the EBGP connection.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     If loopback interfaces are used to establish an EBGP connection, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command, where the value of *hop-count* must be greater than or equal to 2. Otherwise, the EBGP peer relationship cannot be established.
  7. (Optional) Configure a description for the specified peer.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv4-address | group-name } [description](cmdqueryname=description) description-text
     ```
     
     To simplify network management, you can configure a description for a specified peer.
  8. (Optional) Set the TCP MSS value used when the local device establishes a TCP connection with the peer.
     
     
     ```
     [peer](cmdqueryname=peer+tcp-mss) { ipv4-address | group-name } tcp-mss tcp-mss-number
     ```
     
     This configuration ensures that TCP packets can still be fragmented properly based on the specified TCP MSS in cases where the path MTU is unavailable, thereby improving network performance.
  9. Enter the IPv4 unicast address family view.
     
     
     ```
     [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
     ```
  10. (Optional) Disable the device from advertising routes learned from an EBGP peer to the peers in the same AS with the EBGP peer.
      
      
      ```
      [peer](cmdqueryname=peer+peer-as-check) { peerIpv4Addr | peerGroupName } peer-as-check
      ```
      
      By default, after receiving a route from an EBGP peer (for example, in AS 200), the local device (for example, in AS 100) advertises the route to other EBGP peers in AS 200. After the [**peer peer-as-check**](cmdqueryname=peer+peer-as-check) command is run on the device, the device does not advertise the routes received from an EBGP peer to other EBGP peers in the same AS with this EBGP peer. This reduces BGP memory and CPU consumption and speeds up route convergence in case of route flapping.
  11. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```