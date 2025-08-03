Configuring LDP TCP-AO Authentication
=====================================

This section describes how to configure LDP TCP-AO authentication to check the integrity of LDP packets and prevent TCP replay attacks.

#### Pre-configuration Tasks

A TCP-AO is used to authenticate received and to-be sent packets during TCP session establishment and data exchange. It supports packet integrity check to prevent TCP replay attacks. After creating a TCP-AO, specify the peer that needs to reference the TCP-AO and the name of the TCP-AO in the MPLS LDP view. This enables the TCP-AO to be referenced, and the LDP session to be encrypted. You can specify multiple peers to reference the same TCP-AO.

A TCP-AO uses the passwords configured in the bound keychain, and these passwords can be automatically switched based on the configuration. However, the configuration process is complex and applies to networks with high security requirements.

Before configuring LDP keychain authentication for a TCP connection, complete the following task:

* [Configure a global keychain.](dc_vrp_keychain_cfg_0000.html)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**tcp ao**](cmdqueryname=tcp+ao)*tcpaoname*
   
   
   
   A TCP-AO is created, and its view is displayed.
3. Run [**binding keychain**](cmdqueryname=binding+keychain)*kcName*
   
   
   
   The TCP-AO is bound to a keychain.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before performing this step, complete "Configuring Keychain Authentication Globally" in [Pre-configuration Tasks](dc_vrp_ldp-p2p_cfg_0055.html#EN-US_CONCEPT_0172368529__section_dc_vrp_ldp-p2p_cfg_005502) to create a keychain.
4. Run [**key-id**](cmdqueryname=key-id) *keyId*
   
   
   
   A key ID is created for the TCP-AO, and the TCP-AO key ID view is displayed.
5. Run [**send-id**](cmdqueryname=send-id+receive-id) *sndId* **receive-id***rcvId*
   
   
   
   send-id and receive-id are configured for the key ID.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   The upper-level view is displayed.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
9. Run [**authentication tcp-ao**](cmdqueryname=authentication+tcp-ao+peer+name) **peer***peer-id* **name** *tcpao-name*
   
   
   
   TCP-AO authentication is enabled for LDP.
   
   
   
   The value of *tcpaoname* must be the same as that of the TCP-AO created in Step 2.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For the same peer, the authentication modes TCP-AO, MD5, and keychain are mutually exclusive.
   
   Configuring LDP TCP-AO authentication may cause the reestablishment of LDP sessions.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.