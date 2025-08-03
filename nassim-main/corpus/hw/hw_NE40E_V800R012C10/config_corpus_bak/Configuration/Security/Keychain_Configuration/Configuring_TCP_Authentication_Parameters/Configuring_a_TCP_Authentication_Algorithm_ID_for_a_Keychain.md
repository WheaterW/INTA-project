Configuring a TCP Authentication Algorithm ID for a Keychain
============================================================

Configuring_a_TCP_Authentication_Algorithm_ID_for_a_Keychain

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**keychain**](cmdqueryname=keychain) *keychain-name*
   
   
   
   The keychain view is displayed.
3. Run [**tcp-algorithm-id**](cmdqueryname=tcp-algorithm-id) { **hmac-md5** | **hmac-sha-256** | **hmac-sha1-12** | **hmac-sha1-20** | **md5** | **sha-1** | **sha-256** | **aes-128-cmac** | **sm3** | **hmac-sha-384** | **hmac-sha-512** } *algorithm-id*
   
   
   
   A TCP authentication algorithm ID is configured.
   
   
   
   A TCP authentication algorithm ID is an integer ranging from 1 to 63.
   
   For security purposes, the MD5 and SHA-1 algorithms are not recommended.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

A TCP authentication algorithm ID indicates the algorithm type used in TCP authentication.