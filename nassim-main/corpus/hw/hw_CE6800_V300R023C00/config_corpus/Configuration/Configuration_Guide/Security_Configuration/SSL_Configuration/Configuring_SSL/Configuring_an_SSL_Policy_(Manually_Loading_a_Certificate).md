Configuring an SSL Policy (Manually Loading a Certificate)
==========================================================

Configuring an SSL Policy (Manually Loading a Certificate)

#### Prerequisites

Before loading a trusted-CA file to an SSL policy, you have completed the following task:

Apply for a certificate from a CA for the client or server and upload the certificate to the **security** sub-directory of the system directory.


#### Context

SSL uses data encryption, identity authentication, and message integrity check mechanisms to ensure security of TCP-based application layer protocols. An SSL policy can be applied to application layer protocols to provide secure connections.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an SSL policy and enter the SSL policy view.
   
   
   ```
   [ssl policy](cmdqueryname=ssl+policy) policy-name
   ```
   
   By default, no SSL policy is configured.
3. (Optional) Set the elliptic curve parameter for the ECDHE algorithm.
   
   
   ```
   [ecdh group](cmdqueryname=ecdh+group) { nist | curve | brainpool } *
   ```
   
   By default, the elliptic curve parameters of the ECDHE algorithm are Curve and Brainpool.
4. (Optional) Configure a minimum SSL version for the SSL policy.
   
   
   ```
   [ssl minimum version](cmdqueryname=ssl+minimum+version) { tls1.1 | tls1.2 | tls1.3 }
   ```
   
   By default, the minimum version used by an SSL policy is TLS1.2.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * SSL policies support three SSL versions: TLS1.1, TLS1.2, and TLS1.3. TLS1.3 ensures the highest security, followed by TLS1.2 and TLS1.1. TLS1.2 and TLS1.3 are recommended.
   * The **tls1.1** parameter in this command can be used only after the weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.
5. Load a digital certificate for the SSL policy.
   
   By default, no digital certificate is loaded for the SSL policy.![](public_sys-resources/note_3.0-en-us.png) 
   * For enhanced security, you are advised to use more secure certificates. To be specific, RSA/DSA certificates have a key length of 3072 bits or greater, and ECC certificates have a key length of 256 bits or greater. Additionally, the certificate's hash algorithm is SHA-256 or a later version.
   * The **install feature-software WEAKEA** command needs to be run if the key length of the RSA/DSA certificate is less than 2048 bits, the key length of the ECC certificate is less than 256 bits, or the hash algorithm of the certificate is SHA1, SHA-224, MD4, or MD5.
   * Load a PEM digital certificate for the SSL policy.
     ```
     [certificate load pem-cert](cmdqueryname=certificate+load+pem-cert) certFile key-pair keyType key-file keyFile auth-code [ cipher authCode ]
     ```
   * Load a PEM certificate chain for the SSL policy.
     ```
     [certificate load pem-chain](cmdqueryname=certificate+load+pem-chain) certFile key-pair keyType key-file keyFile auth-code [ cipher authCode ]
     ```
   * Load a PFX digital certificate for the SSL policy.
     
     Format 1:
     
     ```
     [certificate load pfx-cert](cmdqueryname=certificate+load+pfx-cert) certFile key-pair keyType key-file keyFile auth-code [ cipher authCode ]
     ```
     Format 2:
     ```
     [certificate load pfx-cert](cmdqueryname=certificate+load+pfx-cert) certFile key-pair keyType mac [ cipher macCode auth-code cipher authCode ] 
     ```
6. (Optional) Load a certificate revocation list (CRL) for the SSL policy.
   
   
   ```
   [crl load](cmdqueryname=crl+load) crlType crlFile
   ```
   
   By default, no CRL is loaded for the SSL policy.
7. (Optional) Load a trusted-CA file for the SSL policy.
   
   
   
   By default, no trusted-CA file is loaded for the SSL policy.
   
   The trusted-CA file is used to verify validity of the digital certificate sent by the server. A maximum of four trusted-CA files can be loaded for an SSL policy.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * Perform this step if the identity of the peer needs to be authenticated.
   * For enhanced security, you are advised to use more secure certificates. To be specific, RSA/DSA certificates have a key length of 3072 bits or greater, and ECC certificates have a key length of 256 bits or greater. Additionally, the certificate's hash algorithm is SHA-256 or a later version.
   * The **install feature-software WEAKEA** command needs to be run if the key length of the RSA/DSA certificate is less than 2048 bits, the key length of the ECC certificate is less than 256 bits, or the hash algorithm of the certificate is SHA1, SHA-224, MD4, or MD5.
   * Load an ASN1 trusted-CA file for the SSL policy.
     ```
     [trusted-ca load asn1-ca](cmdqueryname=trusted-ca+load+asn1-ca) caFile
     ```
   * Load a PEM trusted-CA file for the SSL policy.
     ```
     [trusted-ca load pem-ca](cmdqueryname=trusted-ca+load+pem-ca) caFile
     ```
   * Load a PFX trusted-CA file for the SSL policy.
     ```
     [trusted-ca load pfx-ca](cmdqueryname=trusted-ca+load+pfx-ca) caFile auth-code [ cipher authCode ]
     ```
8. (Optional) Bind a cipher suite to the SSL policy.
   
   
   ```
   [binding cipher-suite-customization](cmdqueryname=binding+cipher-suite-customization) customization-name
   ```
   
   By default, no cipher suite is bound to an SSL policy. In this case, all encryption algorithms can be used.
   
   The cipher suite to be bound to the SSL policy must have been configured. For details, see [(Optional) Configuring a Cipher Suite for an SSL Policy](galaxy_ssl_cfg_0010.html).
9. (Optional) Set the certificate expiration alarm threshold and the interval for checking certificate expiration alarms.
   
   
   ```
   [quit](cmdqueryname=quit)
   [ssl certificate alarm-threshold](cmdqueryname=ssl+certificate+alarm-threshold) early-alarm time check-interval check-period
   ```
   
   By default, the certificate expiration alarm threshold is 90 days, and the interval for checking certificate expiration alarms is 24 hours.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```