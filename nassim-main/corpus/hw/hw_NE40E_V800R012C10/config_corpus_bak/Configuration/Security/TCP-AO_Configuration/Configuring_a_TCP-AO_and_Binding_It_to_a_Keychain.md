Configuring a TCP-AO and Binding It to a Keychain
=================================================

Configuring_a_TCP-AO_and_Binding_It_to_a_Keychain

#### Prerequisites

A keychain has been configured.


#### Context

To implement TCP-AO on a device, a TCP-AO needs to be associated with the authentication algorithm, authentication key string, and lifetime of a key in a keychain. Therefore, during TCP-AO configuration, you need to bind the TCP-AO to an existing keychain.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**tcp ao**](cmdqueryname=tcp+ao) *tcpaoname* command to create a TCP-AO and enter the TCP-AO Policy view.
3. Run the [**binding keychain**](cmdqueryname=binding+keychain) **kcName** command to bind the TCP-AO to an existing keychain.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After being bound to a keychain, a TCP-AO can be associated with the authentication algorithm, authentication key string, and lifetime of a key in the keychain.
   
   Multiple TCP-AOs can be bound to the same keychain to reduce the configuration workload and implement centralized management of multiple TCP-AO keys.
4. (Optional) Run the [**accept-mismatch enable**](cmdqueryname=accept-mismatch+enable) command to configure the local end to permit received TCP connection setup request packets that do not carry the TCP-AO option.
5. Run the [**key-id**](cmdqueryname=key-id) *KeyId* command to create a key ID for the TCP-AO and enter the TCP-AO key ID view.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The key ID specified in this step must be the same as a key ID configured in the bound keychain. Otherwise, the authentication algorithm, authentication key string, and lifetime of the keychain fail to be associated with the TCP-AO.
6. Run the [**send-id**](cmdqueryname=send-id) *sndId* **receive-id** r*cvId* command to configure the send-id and receive-id for the key ID.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   **send-id** and **receive-id** determine the KeyID (SendKeyID) and RNextKeyID (ReceiveKeyID) of a TCP-AO to be carried in a TCP packet header. Their combination represents the currently active key.
   
   For example, Key1 (SendKeyID=1, ReceiveKeyID=2) indicates that the local end uses the authentication algorithm and key in Key1 for encryption. The peer end selects the authentication algorithm and key in Key1 (SendKeyID=2, ReceiveKeyID=1) based on ReceiveKeyID=2 in the received packet to decrypt the packet.
7. (Optional) Run the [**option-authentication disable**](cmdqueryname=option-authentication+disable) command to disable the options in TCP packet headers from participating in the MAC calculation for a TCP-AO.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A TCP packet header can contain multiple optional options. TCP-AO (Kind=29) is a type of option.
   
   You can run this command to include or exclude TCP packet headers' options during the MAC calculation for a TCP-AO.
   
   Note: The TCP-AO option is excluded during the MAC calculation for a TCP-AO even if the function to include the options in TCP packet headers is enabled.
8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.