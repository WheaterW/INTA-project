Configuring an SSL Policy
=========================

Configuring an SSL Policy

#### Context

Before configuring HTTPS, you need to deploy an SSL policy on the device, and load the corresponding digital certificate. An SSL policy contains the SSL parameters used during device startup, and only takes effect after it is associated with an application layer protocol (such as HTTP).

![](public_sys-resources/note_3.0-en-us.png) 

* For enhanced security, you are advised to use more secure certificates. To be specific, RSA/DSA certificates have a key length of 3072 bits or greater, and ECC certificates have a key length of 256 bits or greater. Additionally, the certificate's hash algorithm is SHA-256 or a later version.
* The **install feature-software WEAKEA** command needs to be run if the key length of the RSA/DSA certificate is less than 2048 bits, the key length of the ECC certificate is less than 256 bits, or the hash algorithm of the certificate is SHA1, SHA-224, MD4, or MD5.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an SSL policy and enter the SSL policy view.
   
   
   ```
   [ssl policy](cmdqueryname=ssl+policy) policy-name
   ```
3. Load a certificate for the SSL policy. The format must be the same as that of the certificate loaded on the HTTPS server.
   * Load a PEM digital certificate for the SSL policy.
     ```
     [certificate load](cmdqueryname=certificate+load) pem-cert certFile key-pair keyType key-file keyFile auth-code [ cipher authCode ]
     ```
   * Load a PFX digital certificate for the SSL policy.
     ```
     [certificate load](cmdqueryname=certificate+load) pfx-cert certFile key-pair keyType mac [ cipher macCode auth-code cipher authCode ]
     [certificate load](cmdqueryname=certificate+load) pfx-cert certFile key-pair keyType key-file keyFile auth-code [ cipher authCode ]
     ```
   * Load a PEM certificate chain for the SSL policy.
     ```
     [certificate load](cmdqueryname=certificate+load) pem-chain certFile key-pair keyType key-file keyFile auth-code [ cipher authCode ]
     ```
4. Load a trusted-CA file for the SSL policy. The format must be the same as that of the trusted-CA file loaded on the HTTPS server.
   * Load a PEM trusted-CA file for the SSL policy.
     ```
     [trusted-ca load](cmdqueryname=trusted-ca+load) pem-ca caFile
     ```
   * Load a PFX trusted-CA file for the SSL policy.
     ```
     [trusted-ca load](cmdqueryname=trusted-ca+load) pfx-ca caFile auth-code [ cipher authCode ]
     ```
   * Load an ASN1 trusted-CA file for the SSL policy.
     ```
     [trusted-ca load](cmdqueryname=trusted-ca+load) asn1-ca caFile
     ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```