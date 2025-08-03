Creating a Key-id in a Keychain
===============================

Creating_a_Key-id_in_a_Keychain

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is entered.
2. Run [**keychain**](cmdqueryname=keychain) *keychain-name*
   
   
   
   The keychain view is entered.
3. Run [**key-id**](cmdqueryname=key-id) *key-id*
   
   
   
   Key-id is created and key-id view is entered.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To configure a key-id in a keychain, a unique
   id within the keychain is required. This id should be an integer and
   the value ranges from 0 to 63.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configurations are
   committed.