Enabling SSL/TLS Authentication for BGP
=======================================

SSL/TLS authentication can be configured to encrypt BGP messages, ensuring data transmission security.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ssl policy**](cmdqueryname=ssl+policy) *policy-name*
   
   
   
   An SSL policy is created, and the SSL policy view is displayed.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
5. To configure SSL/TLS authentication for BGP, perform the following steps (no sequential order) on the client and server (the priority of the configuration on a peer is higher than that of the configuration on the peer group):
   
   
   * To configure a peer or peer group as an SSL client or server, run the [**peer**](cmdqueryname=peer+ssl-policy+role+client+server) { *group-name* | *ipv4-address* } **ssl-policy** **role** { **client** | **server** } command.
   * To apply the SSL policy to the SSL client or server, run the [**peer**](cmdqueryname=peer+ssl-policy+name) { *group-name* | *ipv4-address* } **ssl-policy** **name** *ssl-policy-name* command.
   * To enable SSL/TLS authentication, run the [**peer**](cmdqueryname=peer+ssl-server+certificate) { *group-name* | *ipv4-address* } **ssl-server** **certificate** command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     This operation can be performed only on the server.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

Run the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) [ *ipv4-address* ] **verbose** command to check the authentication information of BGP peers.