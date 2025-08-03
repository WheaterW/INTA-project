Configuring a Key Pair
======================

Before applying for and using a certificate, configure a key pair.

#### Context

Generating a key pair is important for applying for a certificate. A key pair consists of a private key and a public key. The public key is sent by the PKI entity to the CA, and the peer uses this key to encrypt cleartext. In contrast, the private key is retained by the PKI entity, which uses it to digitally sign and decrypt the peer's ciphertext. The private key is encrypted on the device. If the private key is disclosed, the user must delete the old key pair, create a new key pair, and reapply for a certificate.

RSA is a public key encryption algorithm. RSA comes from the surnames of Ron Rivest, Adi Shamir, and Leonard Adleman. RSA key pairs are classified into host key pairs and server key pairs. A server key pair changes periodically on a local server, but a host key pair remains unchanged. A host key pair is required during certificate application.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* If a local existing key pair has been named, it will be overridden when a new key pair is created. If a local existing key pair has been named, delete it before recreating or renaming it.
* After a key pair is deleted or replaced, the existing certificate becomes invalid. To ensure the consistency between a new key pair and the existing certificate, you must apply for a new certificate.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rsa pki local-key-pair**](cmdqueryname=rsa+pki+local-key-pair+create) [ *key-name* ] **create**
   
   
   
   An RSA key pair is created.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If an RSA key pair already exists on the device, you can run the [**pki import rsa-key-pair**](cmdqueryname=pki+import+rsa-key-pair+der+pem+password) *keypair-name* { **der** *key-filename* | **pem** *key-filename* **password** *password-val* } command to import the RSA key pair to the device memory for it to take effect. In this case, you do not need to create an RSA key pair.