(Optional) Configuring a Cipher Suite for an SSL Policy
=======================================================

(Optional) Configuring a Cipher Suite for an SSL Policy

#### Context

A cipher suite is a set of encryption algorithms used by a server and client during SSL communication. In the initial SSL handshake process, the client sends a cipher suite containing its supported algorithms to the server. The server then selects an algorithm from the received cipher suite based on its own configurations. This algorithm is used in subsequent communications.

Each encryption algorithm in the cipher suite contains the following information:

* Key exchange algorithm: determines how the server and client authenticate each other. An asymmetric encryption algorithm is used to generate a session key because it does not transmit significant data. Key exchange algorithms include RSA, Diffie-Hellman, and ECDHE.
* Signature algorithm: used to sign the CA certificate. Signature algorithms include RSA and DSS.
* Encryption algorithm: used to encrypt data to be transmitted. Both symmetric and asymmetric encryption algorithms are available. However, asymmetric encryption algorithms are rarely used as they consume too many resources and are limited in terms of the length of data that can be transmitted. Usually, an encryption algorithm name contains the key length and encryption mode, such as GCM and CBC. Encryption algorithms include AES\_128, AES\_256, AES\_128\_CBC, AES\_256\_CBC, AES\_128\_GCM, AES\_256\_GCM, and ChaCha20-Poly1305.
* Message integrity check algorithm: used to check the integrity of messages. Message integrity check algorithms include SHA, SHA256, and SHA384.

For example, a cipher suite supports the encryption algorithm **tls12\_ck\_rsa\_aes\_128\_cbc\_sha**. This algorithm is based on the **TLS** protocol, and uses **RSA** for key exchange, **AES\_128\_CBC** (with a key length of 128 bits and encryption mode of CBC) for data encryption, and **SHA** for message integrity check.

**Table 1** Encryption algorithms supported by a cipher suite
| TLS Version | Encryption Algorithm Supported by a Cipher Suite | Description |
| --- | --- | --- |
| TLS1.1, TLS1.2, and TLS1.3 | tls1\_ck\_rsa\_with\_aes\_256\_sha | In this algorithm, RSA is used for key exchange and signature, AES\_256 is used for data encryption, and SHA is used for message integrity check. |
| tls1\_ck\_rsa\_with\_aes\_128\_sha | In this algorithm, RSA is used for key exchange and signature, AES\_128 is used for data encryption, and SHA is used for message integrity check. |
| tls1\_ck\_dhe\_rsa\_with\_aes\_256\_sha | In this algorithm, Diffie-Hellman and RSA are used for key exchange, RSA is used for signature, AES\_256 is used for data encryption, and SHA is used for message integrity check. |
| tls1\_ck\_dhe\_dss\_with\_aes\_256\_sha | In this algorithm, Diffie-Hellman is used for key exchange, DSS is used for signature, AES\_256 is used for data encryption, and SHA is used for message integrity check. |
| tls1\_ck\_dhe\_rsa\_with\_aes\_128\_sha | In this algorithm, Diffie-Hellman is used for key exchange, RSA is used for signature, AES\_128 is used for data encryption, and SHA is used for message integrity check. |
| tls1\_ck\_dhe\_dss\_with\_aes\_128\_sha | In this algorithm, Diffie-Hellman is used for key exchange, DSS is used for signature, AES\_128 is used for data encryption, and SHA is used for message integrity check. |
| TLS1.2 and TLS1.3 | tls12\_ck\_rsa\_aes\_128\_cbc\_sha | In this algorithm, RSA is used for key exchange and signature, AES\_128\_CBC (with a key length of 128 bits and encryption mode of CBC) is used for data encryption, and SHA is used for message integrity check. |
| tls12\_ck\_rsa\_aes\_256\_cbc\_sha | In this algorithm, Diffie-Hellman is used for key exchange, DSS is used for signature, AES\_256\_CBC (with a key length of 256 bits and encryption mode of CBC) is used for data encryption, and SHA is used for message integrity check. |
| tls12\_ck\_rsa\_aes\_128\_cbc\_sha256 | In this algorithm, Diffie-Hellman is used for key exchange, RSA is used for signature, AES\_128\_CBC (with a key length of 256 bits and encryption mode of CBC) is used for data encryption, and SHA256 is used for message integrity check. |
| tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha | In this algorithm, Diffie-Hellman is used for key exchange, RSA is used for signature, AES\_128\_CBC (with a key length of 128 bits and encryption mode of CBC) is used for data encryption, and SHA is used for message integrity check. |
| tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha | In this algorithm, Diffie-Hellman is used for key exchange, DSS is used for signature, AES\_128\_CBC (with a key length of 128 bits and encryption mode of CBC) is used for data encryption, and SHA is used for message integrity check. |
| tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha | In this algorithm, Diffie-Hellman is used for key exchange, DSS is used for signature, AES\_256\_CBC (with a key length of 256 bits and encryption mode of CBC) is used for data encryption, and SHA is used for message integrity check. |
| tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha | In this algorithm, Diffie-Hellman is used for key exchange, RSA is used for signature, AES\_256\_CBC (with a key length of 256 bits and encryption mode of CBC) is used for data encryption, and SHA is used for message integrity check. |
| tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha256 | In this algorithm, Diffie-Hellman is used for key exchange, DSS is used for signature, AES\_128\_CBC (with a key length of 128 bits and encryption mode of CBC) is used for data encryption, and SHA256 is used for message integrity check. |
| tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha256 | In this algorithm, Diffie-Hellman is used for key exchange, RSA is used for signature, AES\_128\_CBC (with a key length of 128 bits and encryption mode of CBC) is used for data encryption, and SHA256 is used for message integrity check. |
| tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha256 | In this algorithm, Diffie-Hellman is used for key exchange, DSS is used for signature, AES\_256\_CBC (with a key length of 256 bits and encryption mode of CBC) is used for data encryption, and SHA256 is used for message integrity check. |
| tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha256 | In this algorithm, Diffie-Hellman is used for key exchange, RSA is used for signature, AES\_256\_CBC (with a key length of 256 bits and encryption mode of CBC) is used for data encryption, and SHA256 is used for message integrity check. |
| tls12\_ck\_rsa\_with\_aes\_128\_gcm\_sha256 | In this algorithm, RSA is used for key exchange and signature, AES\_128\_GCM (with a key length of 128 and encryption mode of GCM) is used for data encryption, and SHA256 is used for message integrity check. |
| tls12\_ck\_rsa\_with\_aes\_256\_gcm\_sha384 | In this algorithm, RSA is used for key exchange and signature, AES\_256\_GCM (with a key length of 256 bits and encryption mode of GCM) is used for data encryption, and SHA384 is used for message integrity check. |
| tls12\_ck\_dhe\_rsa\_with\_aes\_128\_gcm\_sha256 | In this algorithm, Diffie-Hellman is used for key exchange, RSA is used for signature, AES\_128\_GCM (with a key length of 128 bits and encryption mode of GCM) is used for data encryption, and SHA256 is used for message integrity check. |
| tls12\_ck\_dhe\_rsa\_with\_aes\_256\_gcm\_sha384 | In this algorithm, Diffie-Hellman is used for key exchange, RSA is used for signature, AES\_256\_GCM (with a key length of 256 bits and encryption mode of GCM) is used for data encryption, and SHA384 is used for message integrity check. |
| tls12\_ck\_dhe\_dss\_with\_aes\_128\_gcm\_sha256 | In this algorithm, Diffie-Hellman is used for key exchange, DSS is used for signature, AES\_128\_GCM (with a key length of 128 bits and encryption mode of GCM) is used for data encryption, and SHA256 is used for message integrity check. |
| tls12\_ck\_dhe\_dss\_with\_aes\_256\_gcm\_sha384 | In this algorithm, Diffie-Hellman is used for key exchange, DSS is used for signature, AES\_256\_GCM (with a key length of 256 bits and encryption mode of GCM) is used for data encryption, and SHA384 is used for message integrity check. |
| tls12\_ck\_rsa\_aes\_256\_cbc\_sha256 | In this algorithm, RSA is used for key exchange and signature, AES\_256\_CBC (with a key length of 256 bits and encryption mode of CBC) is used for data encryption, and SHA256 is used for message integrity check. |
| tls12\_ck\_ecdhe\_rsa\_with\_aes\_128\_gcm\_sha256 | In this algorithm, ECDHE is used for key exchange, RSA is used for signature, AES\_128\_GCM (with a key length of 128 bits and encryption mode of GCM) is used for data encryption, and SHA256 is used for message integrity check. |
| tls12\_ck\_ecdhe\_rsa\_with\_aes\_256\_gcm\_sha384 | In this algorithm, ECDHE is used for key exchange, RSA is used for signature, AES\_256\_GCM (with a key length of 256 bits and encryption mode of GCM) is used for data encryption, and SHA384 is used for message integrity check. |
| TLS1.3 | tls13\_aes\_128\_gcm\_sha256 | In this algorithm, AES\_128\_GCM (with a key length of 128 bits and encryption mode of GCM) is used for data encryption and SHA256 is used for message integrity check. |
| tls13\_aes\_256\_gcm\_sha384 | In this algorithm, AES\_256\_GCM (with a key length of 256 bits and encryption mode of GCM) is used for data encryption and SHA256 is used for message integrity check. |
| tls13\_chacha20\_poly1305\_sha256 | In this algorithm, ChaCha20-Poly1305 is used for data encryption and SHA256 is used for message integrity check. |
| tls13\_aes\_128\_ccm\_sha256 | In this algorithm, AES\_128\_CCM (with a key length of 128 bits and encryption mode of CCM) is used for data encryption and SHA256 is used for message integrity check. |



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a cipher suite for an SSL policy and enter the customized view of the cipher suite.
   
   
   ```
   [ssl cipher-suite-list](cmdqueryname=ssl+cipher-suite-list) customization-policy-name
   ```
   
   By default, no cipher suite is created for an SSL policy.
3. Configure encryption algorithms supported by the cipher suite for the SSL policy.
   
   
   ```
   [set cipher-suite](cmdqueryname=set+cipher-suite) { tls1_ck_rsa_with_aes_256_sha | tls1_ck_rsa_with_aes_128_sha | tls1_ck_dhe_rsa_with_aes_256_sha | tls1_ck_dhe_dss_with_aes_256_sha | tls1_ck_dhe_rsa_with_aes_128_sha | tls1_ck_dhe_dss_with_aes_128_sha | tls12_ck_rsa_aes_128_cbc_sha | tls12_ck_rsa_aes_256_cbc_sha | tls12_ck_rsa_aes_128_cbc_sha256 | tls12_ck_rsa_aes_256_cbc_sha256 | tls12_ck_dhe_dss_aes_128_cbc_sha | tls12_ck_dhe_rsa_aes_128_cbc_sha | tls12_ck_dhe_dss_aes_256_cbc_sha | tls12_ck_dhe_rsa_aes_256_cbc_sha | tls12_ck_dhe_dss_aes_128_cbc_sha256 | tls12_ck_dhe_rsa_aes_128_cbc_sha256 | tls12_ck_dhe_dss_aes_256_cbc_sha256 | tls12_ck_dhe_rsa_aes_256_cbc_sha256 | tls12_ck_rsa_with_aes_128_gcm_sha256 | tls12_ck_rsa_with_aes_256_gcm_sha384 | tls12_ck_dhe_rsa_with_aes_128_gcm_sha256 | tls12_ck_dhe_rsa_with_aes_256_gcm_sha384 | tls12_ck_dhe_dss_with_aes_128_gcm_sha256 | tls12_ck_dhe_dss_with_aes_256_gcm_sha384 | tls12_ck_ecdhe_rsa_with_aes_128_gcm_sha256 | tls12_ck_ecdhe_rsa_with_aes_256_gcm_sha384| tls13_aes_128_gcm_sha256 | tls13_aes_256_gcm_sha384 | tls13_chacha20_poly1305_sha256 | tls13_aes_128_ccm_sha256 }
   ```
   
   By default, no encryption algorithm is configured in the cipher suite for an SSL policy.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   For security purpose,you are not advised to use the weak security algorithm or weak security protocols provided by this feature. If you need to use the weak security algorithm or protocols, run the **install feature-software WEAKEA** command to install the weak security algorithm or protocol feature package WEAKEA. By default, the device provides the weak security algorithm or protocol feature package WEAKEA. For details about how to install or uninstall the feature package, see "Upgrade Maintenance Configuration" in Configuration Guide > System Management Configuration.
   
   
   The following table lists the commands that can be used only after the weak security algorithm/protocol feature package is installed.
   
   | Command | Parameters Available Only After Feature Package Installation |
   | --- | --- |
   | **set cipher-suite** | **tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha, tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha256, tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha, tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha256, tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha, tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha256, tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha, tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha256, tls12\_ck\_rsa\_aes\_128\_cbc\_sha, tls12\_ck\_rsa\_aes\_128\_cbc\_sha256, tls12\_ck\_rsa\_aes\_256\_cbc\_sha, tls12\_ck\_rsa\_aes\_256\_cbc\_sha256, tls12\_ck\_rsa\_with\_aes\_128\_gcm\_sha256, tls12\_ck\_rsa\_with\_aes\_256\_gcm\_sha384, tls1\_ck\_dhe\_dss\_with\_aes\_128\_sha, tls1\_ck\_dhe\_dss\_with\_aes\_256\_sha, tls1\_ck\_dhe\_rsa\_with\_aes\_128\_sha, tls1\_ck\_dhe\_rsa\_with\_aes\_256\_sha, tls1\_ck\_rsa\_with\_aes\_128\_sha, tls1\_ck\_rsa\_with\_aes\_256\_sha** |
   | **ssl minimum version** | **tls1.1** |
   
   
   SSL provides a handshake mechanism that allows a client and a server to establish a session, authenticate each other's identity, and negotiate the key and cipher suite. It is recommended that a cipher suite of TLS1.2 or a later version be used during communication. In TLS versions, when the symmetric encryption algorithm in CBC mode is used, data may be subject to a plaintext-recovery attack, causing disclosure of encrypted data. Therefore, you are not advised to use the CBC mode for data encryption in TLS versions.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```