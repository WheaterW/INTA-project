Configuring and Binding an SSL Policy
=====================================

SSL policies can be used to protect transmitted data from being tampered with, improving security.

#### Context

Some traditional protocols, such as syslog, do not have security mechanisms. They transmit data in clear text, cannot authenticate communicating devices or prevent transmitted data from being tampered with, exposing data transmission to security risks. SSL provides data encryption, identity authentication, and message integrity check o ensure the security of TCP-based application layer protocols.


#### Procedure

Deploy an SSL policy in the SSL policy view:

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ssl policy**](cmdqueryname=ssl+policy) *policy-name* command to configure an SSL policy and enter the SSL policy view.
3. (Optional) Run the [**ecdh group**](cmdqueryname=ecdh+group) { **nist** | **curve** | **brainpool** }\* command to configure elliptic curve parameters for the ECDHE algorithm.
4. Run the [**ssl minimum version**](cmdqueryname=ssl+minimum+version) { **tls1.1** | **tls1.2** | **tls1.3** } command to configure the minimum version for the SSL policy.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a device configured with TLS 1.0 is upgraded to a version that does not support TLS 1.0, the minimum version supported by the SSL policy is still TLS 1.0. In this case, you can run the [**ssl minimum version**](cmdqueryname=ssl+minimum+version) { **tls1.1** | **tls1.2** | **tls1.3** } command to reconfigure the minimum version for the SSL policy. This process is irreversible.
   
   If a device for which the [**ssl minimum version**](cmdqueryname=ssl+minimum+version) command is not run is upgraded to the target version, the minimum version supported by the SSL policy is TLS 1.1. The default minimum version is TLS 1.2. You can run the [**ssl minimum version**](cmdqueryname=ssl+minimum+version) { **tls1.1** | **tls1.2** | **tls1.3** } command to reconfigure the minimum version for the SSL policy.
5. (Optional) Run the [**ssl verify**](cmdqueryname=ssl+verify) { **basic-constrain** | **key-usage** | **version** { **cert-version3** | **crl-version2** } } [**enable**](cmdqueryname=enable) command to enable certificate verification.
6. (Optional) Run the [**ssl verify certificate-chain minimum-path-length**](cmdqueryname=ssl+verify+certificate-chain+minimum-path-length) *path-length* command to configure the minimum path length for the digital certificate chain.
7. (Optional) Run the [**signature algorithm-list**](cmdqueryname=signature+algorithm-list) { **ecdsa-secp256r1-sha256** | **ecdsa-secp384r1-sha384** | **ecdsa-secp521r1-sha512** | **ed25519** | **ed448** | **rsa-pss-pss-sha256** | **rsa-pss-pss-sha384** | **rsa-pss-pss-sha512** | **rsa-pss-rsae-sha256** | **rsa-pss-rsae-sha384** | **rsa-pss-rsae-sha512** | **rsa-pkcs1-sha256** | **rsa-pkcs1-sha384** | **rsa-pkcs1-sha512** | **ecdsa-sha1** | **ecdsa-sha224** | **rsa-sha1** | **rsa-sha224** | **dsa-sha1** | **dsa-sha224** | **dsa-sha256** | **dsa-sha384** | **dsa-sha512** } \* command to configure signature algorithms supported by SSL handshake.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the number of supported signature algorithms decreases, the SSL handshake may fail due to signature algorithm mismatch. In this case, you can run this command to adjust the supported signature algorithms.
8. (Optional) Run the [**pki-domain**](cmdqueryname=pki-domain)*pki-domain* command to bind a PKI domain to the SSL policy.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * After a PKI domain is bound to an SSL policy, the SSL policy uses the certificates and certificate revocation list (CRL) in the PKI domain.
   * In addition to loading and revoking certificates using PKI, you can also perform the following steps to manually load and revoke certificates.
9. (Optional) Run the [**certificate load**](cmdqueryname=certificate+load) command to load a digital certificate. Currently, the PEM and PFX certificates and the PEM certificate chain are supported. Load a digital certificate or certificate chain as needed.
   * Run the [**certificate load**](cmdqueryname=certificate+load) **pem-cert** *certFile* **key-pair** { **dsa** | **rsa** } **key-file** *keyFile* **auth-code** [ **cipher** *authCode* ] command to load a PEM certificate for the SSL policy.
   * Run the [**certificate load**](cmdqueryname=certificate+load) **pfx-cert** *certFile* **key-pair** { **dsa** | **rsa** } **mac** or [**certificate load**](cmdqueryname=certificate+load) **pfx-cert** *certFile* **key-pair** { **dsa** | **rsa** } { **mac** **cipher** *mac-code* | **key-file** *keyFile* } **auth-code** **cipher** *authCode* command to load a PFX certificate for the SSL policy.
   * Run the [**certificate load**](cmdqueryname=certificate+load) **pem-chain** *certFile* **key-pair** { **dsa** | **rsa** } **key-file** *keyFile* **auth-code** [ **cipher** *authCode* ] command to load a PEM certificate chain for the SSL policy.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Loading a digital certificate is optional for a device but mandatory for an NMS.
10. (Optional) Run the [**crl load**](cmdqueryname=crl+load) *crlType* *crlFile* command to load a digital CRL file.
    
    A maximum of two CRL files can be loaded for an SSL policy.
11. Run the [**trusted-ca load**](cmdqueryname=trusted-ca+load) command to load a trusted-CA file. A maximum of four trusted-CA files can be loaded for an SSL policy.
    * Run the [**trusted-ca load**](cmdqueryname=trusted-ca+load) **pem-ca** *caFile* command to load a trusted-CA file in PEM format for the SSL policy.
    * Run the [**trusted-ca load**](cmdqueryname=trusted-ca+load) **asn1-ca** *caFile* command to load a trusted-CA file in ASN1 format for the SSL policy.
    * Run the [**trusted-ca load**](cmdqueryname=trusted-ca+load) **pfx-ca** *caFile* **auth-code** [ **cipher** *authCode* ] command to load a trusted-CA file in PFX format for the SSL policy.
12. (Optional) Run the [**binding cipher-suite-customization**](cmdqueryname=binding+cipher-suite-customization) *customization-name* command to bind a cipher suite to the SSL policy. Before binding a cipher suite to an SSL policy, ensure that the cipher suite has been configured for the SSL policy. For details, see [Configuring an SSL Cipher Suite](dc_vrp_basic_cfg_0063.html).
13. (Optional) Run the [**cipher-suite exclude**](cmdqueryname=cipher-suite+exclude) **key-exchange****rsa** command to exclude the RSA key exchange algorithm from the SSL policy cipher suite.![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The RSA key exchange algorithm is not recommended on networks that have high security requirements because this algorithm is not secure.
14. (Optional) Run the [**cipher-suite exclude**](cmdqueryname=cipher-suite+exclude) **cipher** **mode** **cbc** command to exclude the CBC encryption algorithm from the SSL policy cipher suite.![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The CBC encryption algorithm is not recommended for networks that have high security requirements because this algorithm is not secure.
15. (Optional) Run the [**cipher-suite exclude**](cmdqueryname=cipher-suite+exclude) **hmac** **sha1** command to exclude the SHA1 digest algorithm from the SSL policy cipher suite.![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The SHA1 digest algorithm is not recommended for networks that have high security requirements because this algorithm is not secure.
16. (Optional) Run the [**diffie-hellman modulus**](cmdqueryname=diffie-hellman+modulus) *modulus-val* command to configure a modulus for the Diffie-Hellman key exchange algorithm.![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    If the modulus length of the Diffie-Hellman key exchange algorithm increases, the SSL handshake may fail when the modulus length is too long. In this case, you can run this command to adjust the modulus length.
17. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
18. (Optional) Run the [**ssl certificate alarm-threshold**](cmdqueryname=ssl+certificate+alarm-threshold) **early-alarm** *time* **check-interval** *check-period* command to configure the certificate expiration alarm threshold and check interval.
19. Run the **bind ssl-policy** command in a service view to bind the SSL policy.
    1. Dual-device backup service
       
       Run the [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name* command to enter the RBS view.
       
       Run the [**bind ssl-policy**](cmdqueryname=bind+ssl-policy) *ssl-policy-name* command to bind an SSL policy.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       In VS mode, this command is supported only by the admin VS.
       
       For detailed dual-device backup service configurations, see [Establishing a Dual-Device Backup Platform](dc_vrp_rbs_cfg_0004.html).
    2. DCN service
       
       Run the [**dcn**](cmdqueryname=dcn) command to enter the DCN view.
       
       Run the [**bind ssl-policy**](cmdqueryname=bind+ssl-policy) *ssl-policy-name* command to bind an SSL policy.
       
       For detailed DCN service configurations, see [Configuring SSL Authentication on a GNE](dc_vrp_dcn_cfg_0048.html).
20. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

Deploy an SSL policy in the DTLS policy view.

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**dtls policy**](cmdqueryname=dtls+policy)*policyName* command to configure a DTLS policy and enter the DTLS policy view.
3. (Optional) Run the [**signature algorithm-list**](cmdqueryname=signature+algorithm-list) { **ecdsa-secp256r1-sha256** | **ecdsa-secp384r1-sha384** | **ecdsa-secp521r1-sha512** | **ed25519** | **ed448** | **rsa-pss-pss-sha256** | **rsa-pss-pss-sha384** | **rsa-pss-pss-sha512** | **rsa-pss-rsae-sha256** | **rsa-pss-rsae-sha384** | **rsa-pss-rsae-sha512** | **rsa-pkcs1-sha256** | **rsa-pkcs1-sha384** | **rsa-pkcs1-sha512** | **ecdsa-sha1** | **ecdsa-sha224** | **rsa-sha1** | **rsa-sha224** | **dsa-sha1** | **dsa-sha224** | **dsa-sha256** | **dsa-sha384** | **dsa-sha512** } \* command to configure signature algorithms supported by SSL handshake.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the number of supported signature algorithms decreases, the SSL handshake may fail due to signature algorithm mismatch. In this case, you can run this command to adjust the supported signature algorithms.
4. (Optional) Run the [**ssl verify**](cmdqueryname=ssl+verify) { **basic-constrain** | **key-usage** } [**enable**](cmdqueryname=enable) command to enable certificate verification.
5. (Optional) Run the [**ssl verify certificate-chain minimum-path-length**](cmdqueryname=ssl+verify+certificate-chain+minimum-path-length) *path-length* command to configure the minimum path length for the digital certificate chain.
6. (Optional) Run the [**binding cipher-suite-customization**](cmdqueryname=binding+cipher-suite-customization) *customization-name* command to bind a cipher suite to the SSL policy. Before binding a cipher suite to an SSL policy, ensure that the cipher suite has been configured for the SSL policy. For details, see [Configuring an SSL Cipher Suite](dc_vrp_basic_cfg_0063.html).
7. (Optional) Run the [**diffie-hellman modulus**](cmdqueryname=diffie-hellman+modulus) *modulus-val* command to configure a modulus for the Diffie-Hellman key exchange algorithm.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the modulus length of the Diffie-Hellman key exchange algorithm increases, the SSL handshake may fail when the modulus length is too long. In this case, you can run this command to adjust the modulus length.
8. (Optional) Run the [**pki-domain**](cmdqueryname=pki-domain)*pki-domain* command to bind a PKI domain to the SSL policy.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After a PKI domain is bound to an SSL policy, the SSL policy uses the certificates and certificate revocation list (CRL) in the PKI domain.
9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.