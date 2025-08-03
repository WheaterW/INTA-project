Configuring a Key String for a Key ID
=====================================

Configuring_a_Key_String_for_a_Key_ID

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**keychain**](cmdqueryname=keychain) *keychain-name*
   
   
   
   The keychain view is displayed.
3. Run [**key-id**](cmdqueryname=key-id) *key-id*
   
   
   
   The key ID view is displayed.
4. Run [**key-string**](cmdqueryname=key-string) { **plain** *plain-text* | [ **cipher** ] *plain-cipher-text* }
   
   
   
   A key string is configured for the key ID.
   
   
   
   The key string is the authentication string used in packet sending and receiving.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   It is recommended that the key string be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters excluding question marks (?) and spaces.
   
   For security purposes, you are advised to specify the ciphertext mode. In addition, change the key string periodically.
   
   If no key string is configured for a key ID, the key ID is inactive.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.