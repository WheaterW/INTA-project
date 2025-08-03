Configuring TCP-AO Authentication
=================================

This section describes how to configure BGP TCP Authentication Option (TCP-AO) authentication to check the integrity of packets and prevent TCP replay attacks.

#### Context

The TCP-AO is used to authenticate received and to-be sent packets during TCP session establishment and data exchange. It supports packet integrity check to prevent TCP replay attacks. After creating a TCP-AO, run the **peer tcp-ao policy** command in the BGP view and specify the peer that needs to reference the TCP-AO and the TCP-AO name. This enables the BGP session to be encrypted. Such configuration is applicable to networks that require high security. Different peers can reference the same TCP-AO.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**tcp ao**](cmdqueryname=tcp+ao)*tcpaoname* command to create a TCP-AO and enter the TCP-AO policy view.
3. Run the [**binding keychain**](cmdqueryname=binding+keychain)*kcName* command to bind the TCP-AO to a keychain.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before performing this step, complete [configuring basic keychain functions](dc_vrp_keychain_cfg_0005.html) in [Pre-configuration Tasks](dc_vrp_bgp_cfg_3062.html#EN-US_TASK_0172366284__context137663429214038) to create a keychain.
4. Run the [**key-id**](cmdqueryname=key-id) *keyId* command to create a key ID for the TCP-AO and enter the TCP-AO key ID view.
5. Run the [**send-id**](cmdqueryname=send-id+receive-id) *sndId* **receive-id***rcvId* command to configure send-id and receive-id for the Key ID.
6. Run the [**quit**](cmdqueryname=quit) command to return to the upper-level view.
7. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
8. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
9. Run the [**peer**](cmdqueryname=peer) *ipv4-address* [**as-number**](cmdqueryname=as-number) *as-number* command to specify the IP address of a peer and the number of the AS where the peer resides.
10. Run the [**peer**](cmdqueryname=peer+tcp-ao+policy) *ipv4-address* **tcp-ao policy** *tcp-ao-name* command to configure TCP-AO authentication for the TCP connection to be set up between BGP peers.
    
    
    
    The value of the *tcp-ao-name* parameter must be set to the TCP-AO created in step 2.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    For the same peer, the authentication modes TCP-AO, MD5, and keychain are mutually exclusive.
11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.