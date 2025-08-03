Configuring BGP4+ Authentication
================================

Configuring BGP4+ Authentication

#### Prerequisites

Before configuring BGP4+ authentication, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

BGP4+ supports MD5 authentication and keychain authentication.

* MD5 authentication
  
  BGP4+ uses TCP as the transport protocol and considers a packet valid if the source address, destination address, source port, destination port, and TCP sequence number of the packet are correct. However, most parameters in a packet are easily accessible to attackers. To protect BGP4+ against attacks, configure MD5 authentication for TCP connections established between BGP4+ peers.
  
  To prevent the MD5 password set on the BGP4+ peers from being decrypted, update the MD5 password periodically.
* Keychain authentication
  
  A keychain consists of multiple authentication keys, each of which contains an ID and a password. Each key has a lifecycle, and keys are dynamically selected in a keychain based on the lifecycle of each key. After a keychain with the same rules is configured on the two ends of a BGP4+ connection, the keychains can dynamically select authentication keys to enhance BGP4+ attack defense.

![](public_sys-resources/note_3.0-en-us.png) 

By default, authentication is not configured for BGP4+. Configuring authentication is recommended to ensure system security.

BGP4+ MD5 authentication and BGP4+ keychain authentication are mutually exclusive.

MD5 authentication provides low security. To ensure high security, you are advised to use keychain authentication and a high-security algorithm, such as HMAC-SHA-256.

For security purposes, MD5 is not recommended. If MD5 is required, run the [**install feature-software WEAKEA**](cmdqueryname=install+feature-software+WEAKEA) command first to install the weak security algorithm/protocol feature package WEAKEA.




#### Procedure

1. Configure MD5 authentication.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the BGP view.
      
      
      ```
      [bgp](cmdqueryname=bgp) as-number
      ```
   1. Configure an MD5 authentication password.
      
      
      ```
      [peer](cmdqueryname=peer) { group-name | ipv6-address } [password](cmdqueryname=password+cipher+simple) { cipher | simple } password
      ```
      
      In BGP4+ MD5 authentication, only the MD5 authentication password is set for the TCP connection, and the authentication is performed by TCP. If authentication fails, no TCP connection can be established.
      
      When setting a password, you can select either of the following input modes:
      
      * **cipher** *cipher-password* indicates that a password is set using a ciphertext string.
      * **simple** *simple-password* indicates that a password is set using a simple string.![](public_sys-resources/note_3.0-en-us.png) 
      * It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
      * For security purposes, you are advised to specify the ciphertext mode and to change the password periodically.
   2. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
2. Configure keychain authentication.
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
      [peer](cmdqueryname=peer) { group-name | ipv6-address } [keychain](cmdqueryname=keychain) keychain-name
      ```
      
      Keychain authentication must be configured for TCP-based applications on both BGP4+ peers, and the encryption algorithms and passwords used by keychain authentication on both peers must be the same; otherwise, a TCP connection cannot be set up, and BGP4+ messages cannot be exchanged.
      
      Before configuring BGP4+ keychain authentication, ensure that the keychain specified by *keychain-name* exists; otherwise, the TCP connection cannot be established. For keychain configuration details, see "Keychain Configuration" in  Configuration Guide-Security Configuration.
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```

#### Verifying the Configuration

After completing the configuration, verify it.

* Run the [**display bgp ipv6 peer**](cmdqueryname=display+bgp+ipv6+peer) command to check authentication information about BGP4+ peers.