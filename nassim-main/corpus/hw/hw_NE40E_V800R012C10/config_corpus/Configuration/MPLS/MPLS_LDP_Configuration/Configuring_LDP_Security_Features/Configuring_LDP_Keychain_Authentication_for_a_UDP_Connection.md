Configuring LDP Keychain Authentication for a UDP Connection
============================================================

LDP keychain authentication can be configured to improve the security of a UDP connection used to establish an LDP session. LDP authentication is configured on LSRs at both ends of an LDP session.

#### Pre-configuration Tasks

A remote LDP peer relationship can be established across multiple devices. To enhance the security of Hello message sending and receiving and prevent relationship establishment with unauthorized peers, you can configure LDP keychain authentication for Targeted Hello to improve network security.

Before configuring LDP keychain authentication for a UDP connection, complete the following task:

* [Configure a global keychain.](dc_vrp_keychain_cfg_0000.html)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**authentication udp-remote key-chain**](cmdqueryname=authentication+udp-remote+key-chain+peer+name) **peer** *peer-id* **name** *keychain-name*
   
   
   
   LDP keychain authentication is enabled for Targeted Hello, and the referenced keychain name is specified.
   
   
   
   After the configuration is successful, the configured keychain authentication takes effect on the specified peer. If the authentication fails, the LDP session cannot be established.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command supports only the keychain authentication using a strong encryption algorithm (SHA-256, HMAC-SHA-256, HMAC-SHA-384, HMAC-SHA-512, or SM3) but not a weak encryption algorithm.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.