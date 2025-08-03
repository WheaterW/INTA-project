Configuring BGP EVPN Peer Relationships
=======================================

You can configure BGP EVPN peer relationships between PEs or between PEs and ASBRs as required to exchange EVPN routes between the PEs. Additionally, you can configure BGP RRs to minimize the number of peer relationships, saving network resources.

#### Procedure

* Configure BGP EVPN peers.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If a BGP RR needs to be configured on the network, establish BGP EVPN peer relationships between all the PEs and the RR.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     BGP is enabled, and its view is displayed.
  3. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** *as-number*
     
     
     
     The remote PE is specified as the peer.
  4. (Optional) Run [**peer**](cmdqueryname=peer+connect-interface) *ipv4-address* **connect-interface** *interface-type* *interface-number* [ *ipv4-source-address* ]
     
     
     
     A source interface and a source IP address are specified to set up a TCP connection between the BGP peers.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If loopback interfaces are used to establish a BGP connection, it is recommended that the [**peer connect-interface**](cmdqueryname=peer+connect-interface) command be run on both ends to ensure correct connection. If this command is run on only one end, the BGP connection may fail to be established.
  5. (Optional) Run [**peer**](cmdqueryname=peer+ebgp-max-hop) *ipv4-address* [**ebgp-max-hop**](cmdqueryname=ebgp-max-hop) [ *hop-count* ]
     
     
     
     The maximum allowable number of hops is set for an EBGP EVPN connection.
     
     
     
     Generally, EBGP EVPN peers are directly connected. If they are not directly connected, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command to allow the EBGP EVPN peers to establish a multi-hop TCP connection.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If loopback interfaces are used for an EBGP EVPN connection, the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command must be run, with the *hop-count* value greater than or equal to 2. If this configuration is absent, the EBGP EVPN connection fails to be established.
  6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* or [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP VPN instance IPv4/IPv6 address family view is displayed.
  7. Run [**import-route**](cmdqueryname=import-route) { **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** | **ospfv3** *process-id* | **ripng** *process-id* } [ **med** *med* | **route-policy** *route-policy-name* ] \*
     
     
     
     The device is enabled to import non-BGP routing protocol routes into the BGP-VPN instance IPv4/IPv6 address family. To advertise host IP routes, only enable the device to import direct routes. To advertise the routes of the network segment where a host resides, configure a dynamic routing protocol (such as OSPF) to advertise the network segment routes. Then enable the device to import routes of the configured routing protocol.
  8. Run [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn)
     
     
     
     The device is configured to advertise IP prefix routes. This type of route can be used to advertise host IP routes as well as the routes on the subnet where the device resides.
  9. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the BGP-VPN instance IPv4/IPv6 address family view.
  10. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
  11. Run [**peer**](cmdqueryname=peer+enable) { *ipv4-address* | *group-name* } **enable**
      
      
      
      The device is enabled to exchange EVPN routes with a peer or peer group.
  12. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
  13. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
  14. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* (Optional) Configure an RR. To minimize the number of BGP EVPN peers on the network, deploy an RR.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     BGP is enabled, and its view is displayed.
  3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
     
     
     
     The BGP-EVPN address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+reflect-client) { *ipv4-address* | *group-name* } [**reflect-client**](cmdqueryname=reflect-client)
     
     
     
     The RR and its client are configured.
     
     
     
     The Router where the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command is run functions as the RR, and the specified peer or peer group functions as a client.
  5. (Optional) Run [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients)
     
     
     
     Route reflection between clients through the RR is disabled.
     
     
     
     If the clients of an RR have established full-mesh connections with each other, run the [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command to disable route reflection between clients through the RR to reduce the link cost. The [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command applies only to RRs.
  6. (Optional) Run [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) { *cluster-id-value* | *cluster-id-ipv4* }
     
     
     
     A cluster ID is configured for the RR.
     
     
     
     If a cluster has multiple RRs, run this command to set the same cluster ID for these RRs to prevent routing loops.
     
     The [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) command applies only to RRs.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.