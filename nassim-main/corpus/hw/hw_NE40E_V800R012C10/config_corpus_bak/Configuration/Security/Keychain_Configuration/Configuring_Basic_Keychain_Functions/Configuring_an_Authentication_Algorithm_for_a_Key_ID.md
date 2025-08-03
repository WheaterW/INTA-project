Configuring an Authentication Algorithm for a Key ID
====================================================

Configuring_an_Authentication_Algorithm_for_a_Key_ID

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**keychain**](cmdqueryname=keychain) *keychain-name* **mode** { **absolute** | **periodic** { **daily** | **weekly** | **monthly** | **yearly** } }
   
   
   
   The keychain view is displayed.
3. Run [**key-id**](cmdqueryname=key-id) *key-id*
   
   
   
   The key ID view is displayed.
4. Run [**algorithm**](cmdqueryname=algorithm) { **md5** | **sha-1** | **hmac-md5** | **hmac-sha1-12** | **hmac-sha1-20** | **hmac-sha-256** | **sha-256** | **sm3** | **aes-128-cmac** | **hmac-sha-384** | **hmac-sha-512** }
   
   
   
   An authentication algorithm is configured for the key ID.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The **aes-128-cmac** parameter can be specified only when TCP-AO authentication is bound with the key of a keychain. The AES-128-CMAC algorithm is not applicable to keychain authentication.
   
   If no authentication algorithm is configured, a key ID is inactive.
   
   For security purposes, the HMAC-MD5, MD5, and SHA-1 algorithms are not recommended.
5. (Optional) Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the keychain view.
6. (Optional) Run [**digest-length**](cmdqueryname=digest-length) { **hmac-sha-256** | **sha-256** | **hmac-sha1-20** } *length*
   
   
   
   The digest length of the encryption algorithm is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   By default, the HMAC-SHA1-20 algorithm uses a 20-byte digest for encryption and decryption. You can run the [**digest-length hmac-sha1-20 16**](cmdqueryname=digest-length+hmac-sha1-20+16) command to allow for interworking with an earlier version. By default, the HMAC-SHA-256 and SHA-256 algorithms use a 32-byte digest for encryption and decryption. You can run the [**digest-length hmac-sha-256 16**](cmdqueryname=digest-length+hmac-sha-256+16) or [**digest-length sha-256 16**](cmdqueryname=digest-length+sha-256+16) command to allow for interworking with an earlier version.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.