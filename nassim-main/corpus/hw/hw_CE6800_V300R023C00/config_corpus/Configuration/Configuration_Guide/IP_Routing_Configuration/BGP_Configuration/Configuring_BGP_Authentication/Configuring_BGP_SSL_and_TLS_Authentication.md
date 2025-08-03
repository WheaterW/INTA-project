Configuring BGP SSL/TLS Authentication
======================================

Configuring BGP SSL/TLS Authentication

#### Prerequisites

Before configuring SSL/TLS authentication for BGP, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an SSL policy and enter its view.
   
   
   ```
   [ssl policy](cmdqueryname=ssl+policy) policy-name
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   For details about the configuration in the SSL policy view, see "SSL Configuration."
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
5. Configure a peer or peer group as an SSL client or server.
   
   
   ```
   [peer](cmdqueryname=peer+ssl-policy+role+client+server) { group-name | ipv4-address } ssl-policy role { client | server }
   ```
   
   Perform this step on both the client and the server. The configuration on a peer takes precedence over that on a peer group.
6. Apply the SSL policy to the SSL client or server.
   
   
   ```
   [peer](cmdqueryname=peer+ssl-policy+name) { group-name | ipv4-address } ssl-policy name ssl-policy-name
   ```
   
   Perform this step on both the client and the server. The configuration on a peer takes precedence over that on a peer group.
7. Configure SSL/TLS authentication on the SSL server.
   
   
   ```
   [peer](cmdqueryname=peer+ssl-server+certificate) { group-name | ipv4-address } ssl-server certificate
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   This step can be performed only on the server.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) [ *ipv4-address* ] **verbose** command to check authentication information about BGP peers.