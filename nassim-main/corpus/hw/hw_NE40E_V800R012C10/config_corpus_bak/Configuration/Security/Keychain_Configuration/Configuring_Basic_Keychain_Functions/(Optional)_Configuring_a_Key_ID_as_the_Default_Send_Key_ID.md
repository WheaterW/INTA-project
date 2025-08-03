(Optional) Configuring a Key ID as the Default Send Key ID
==========================================================

(Optional)_Configuring_a_Key_ID_as_the_Default_Send_Key_ID

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**keychain**](cmdqueryname=keychain) *keychain-name*
   
   
   
   The keychain view is displayed.
3. Run [**key-id**](cmdqueryname=key-id) *key-id*
   
   
   
   The key ID view is displayed.
4. Run [**default send-key-id**](cmdqueryname=default+send-key-id)
   
   
   
   The key ID is configured as the default send key ID.
   
   
   
   In a keychain, only one key ID can be configured as the default send key ID.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.