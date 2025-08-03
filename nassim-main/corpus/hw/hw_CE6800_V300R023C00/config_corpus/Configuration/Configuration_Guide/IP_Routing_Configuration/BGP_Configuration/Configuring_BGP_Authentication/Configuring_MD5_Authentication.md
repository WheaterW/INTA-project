Configuring MD5 Authentication
==============================

Configuring MD5 Authentication

#### Prerequisites

Before configuring MD5 authentication for BGP, you have completed the following task:

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
3. Configure an MD5 authentication password.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv4-address | group-name } [password](cmdqueryname=password+cipher+simple) { cipher cipher-password | simple simple-password }
   ```
   
   When setting a password, you can select either of the following input modes:
   
   * **cipher** *cipher-password* indicates that a password is set using a ciphertext string.
   * **simple** *simple-password* indicates that a password is set using a cleartext string.![](public_sys-resources/note_3.0-en-us.png) 
   * It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
   * To prevent high security risks, you are advised to select the ciphertext mode. To ensure device security, change the password periodically.
   * If MD5 authentication is configured in the BGP view, the configuration also takes effect in extended BGP address family views because they use the same TCP connection.
   * BGP MD5 authentication and BGP keychain authentication are mutually exclusive.
   * For security purposes, MD5 is not recommended. If MD5 is required, run the [**install feature-software WEAKEA**](cmdqueryname=install+feature-software+WEAKEA) command first to install the weak security algorithm/protocol feature package WEAKEA.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) [ *ipv4-address* ] **verbose** command to check authentication information about BGP peers.