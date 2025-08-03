Configuring TCP Kind of a Keychain
==================================

Configuring_TCP_Kind_of_a_Keychain

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**keychain**](cmdqueryname=keychain) *keychain-name*
   
   
   
   Keychain view is entered
3. Run [**tcp-kind**](cmdqueryname=tcp-kind) *kind-value*
   
   
   
   The TCP kind value for the keychain is configured. The range of the kind-value can be 28 to 255.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configurations are committed.

#### Follow-up Procedure

TCP uses TCP Enhanced Authentication Option for authenticated communication. The kind value used to represent the TCP Enhanced Authentication Option type for a keychain can be configured.