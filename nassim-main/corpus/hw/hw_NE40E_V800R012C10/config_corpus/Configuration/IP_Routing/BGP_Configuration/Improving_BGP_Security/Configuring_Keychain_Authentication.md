Configuring Keychain Authentication
===================================

After a keychain with the same rules is configured on the two ends of a BGP connection, the keychain can dynamically select the authentication keys to enhance BGP attack defense.

#### Procedure

* Configuring Keychain Authentication.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**keychain**](cmdqueryname=keychain) *keychain-name*
     
     
     
     Keychain authentication is configured.
     
     To ensure the setup of a TCP connection and BGP exchange between on both ends of a BGP connection, configure keychain authentication specified for TCP-based applications and the same password and encryption algorithms on both ends.
     
     *keychain-name* specified in this command must exist; otherwise, the TCP connection cannot be established. For keychain configuration details, see the "Keychain Configuration" chapter in *HUAWEI NE40E-M2 series Configuration Guide - Security*.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + When this command is used in the BGP view, it is also applicable to the extended address family view because they use the same TCP connection.
     + BGP MD5 authentication and BGP keychain authentication are mutually exclusive.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

Run the following command to check the previous configuration.

Run the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) [ *ipv4-address* ] **verbose** command to view the authentication information about BGP peers.