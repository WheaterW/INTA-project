Configuring Keychain Authentication
===================================

Configuring Keychain Authentication

#### Prerequisites

Before configuring keychain authentication for BGP, you have completed the following task:

* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Configure keychain authentication.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv4-address | group-name } [keychain](cmdqueryname=keychain) keychain-name
   ```
   
   
   
   You must configure keychain authentication for TCP-based applications on both BGP peers. Note that encryption algorithms and passwords configured for keychain authentication on both peers must be the same; otherwise, a TCP connection cannot be set up between the BGP peers and BGP messages cannot be exchanged.
   
   The keychain specified by *keychain-name* must exist when you configure BGP keychain authentication; otherwise, the TCP connection cannot be established. For keychain configuration details, see "Keychain Configuration" in  Configuration Guide > Security Configuration.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * If keychain authentication is configured in the BGP view, the configuration also takes effect in extended BGP address family views because they use the same TCP connection.
   * BGP MD5 authentication and BGP keychain authentication are mutually exclusive.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) [ *ipv4-address* ] **verbose** command to check authentication information about BGP peers.