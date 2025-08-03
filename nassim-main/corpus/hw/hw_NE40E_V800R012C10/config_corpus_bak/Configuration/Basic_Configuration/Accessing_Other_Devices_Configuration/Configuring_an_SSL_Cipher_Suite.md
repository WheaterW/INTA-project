Configuring an SSL Cipher Suite
===============================

During authentication between the client and server, an encryption algorithm list is provided for SSL algorithm negotiation. This section describes how to configure an SSL cipher suite with supported encryption algorithms. Using secure algorithms enhances system security.

#### Context

During authentication between the client and server, an encryption algorithm list is provided for SSL algorithm negotiation. For a system with high security requirements, you can use encryption algorithms that are more secure to enhance system security.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ssl cipher-suite-list**](cmdqueryname=ssl+cipher-suite-list) *customization-policy-name*
   
   
   
   An SSL cipher suite is created, and the SSL cipher suite view is displayed.
3. Run [**set cipher-suite**](cmdqueryname=set+cipher-suite) { **tls1\_ck\_rsa\_with\_aes\_256\_sha** | **tls1\_ck\_rsa\_with\_aes\_128\_sha** | **tls1\_ck\_dhe\_rsa\_with\_aes\_256\_sha** | **tls1\_ck\_dhe\_dss\_with\_aes\_256\_sha** | **tls1\_ck\_dhe\_rsa\_with\_aes\_128\_sha** | **tls1\_ck\_dhe\_dss\_with\_aes\_128\_sha** | **tls12\_ck\_rsa\_aes\_128\_cbc\_sha** | **tls12\_ck\_rsa\_aes\_256\_cbc\_sha** | **tls12\_ck\_rsa\_aes\_128\_cbc\_sha256** | **tls12\_ck\_rsa\_aes\_256\_cbc\_sha256** | **tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha** | **tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha** | **tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha** | **tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha** | **tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha256** | **tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha256** | **tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha256** | **tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha256** | **tls12\_ck\_rsa\_with\_aes\_128\_gcm\_sha256** | **tls12\_ck\_rsa\_with\_aes\_256\_gcm\_sha384** | **tls12\_ck\_dhe\_rsa\_with\_aes\_128\_gcm\_sha256** | **tls12\_ck\_dhe\_rsa\_with\_aes\_256\_gcm\_sha384** | **tls12\_ck\_dhe\_dss\_with\_aes\_128\_gcm\_sha256** | **tls12\_ck\_dhe\_dss\_with\_aes\_256\_gcm\_sha384** | **tls12\_ck\_ecdhe\_rsa\_with\_aes\_128\_gcm\_sha256** | **tls12\_ck\_ecdhe\_rsa\_with\_aes\_256\_gcm\_sha384**| **tls13\_aes\_128\_gcm\_sha256** | **tls13\_aes\_256\_gcm\_sha384** | **tls13\_chacha20\_poly1305\_sha256** | **tls13\_aes\_128\_ccm\_sha256** }
   
   
   
   Encryption algorithms supported in an SSL cipher suite are configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The following algorithms are not recommended because they are less secure: tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha, tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha256, tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha, tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha256, tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha, tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha256, tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha, tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha256, tls12\_ck\_rsa\_aes\_128\_cbc\_sha, tls12\_ck\_rsa\_aes\_128\_cbc\_sha256, tls12\_ck\_rsa\_aes\_256\_cbc\_sha, tls12\_ck\_rsa\_aes\_256\_cbc\_sha256, tls12\_ck\_rsa\_with\_aes\_128\_gcm\_sha256, tls12\_ck\_rsa\_with\_aes\_256\_gcm\_sha384, tls12\_ck\_ecdhe\_rsa\_with\_aes\_128\_gcm\_sha256, tls12\_ck\_ecdhe\_rsa\_with\_aes\_256\_gcm\_sha384, tls1\_ck\_dhe\_dss\_with\_aes\_128\_sha, tls1\_ck\_dhe\_dss\_with\_aes\_256\_sha, tls1\_ck\_dhe\_rsa\_with\_aes\_128\_sha, tls1\_ck\_dhe\_rsa\_with\_aes\_256\_sha, tls1\_ck\_rsa\_with\_aes\_128\_sha, and tls1\_ck\_rsa\_with\_aes\_256\_sha.
   
   If a weak security algorithm is required, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function first.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.