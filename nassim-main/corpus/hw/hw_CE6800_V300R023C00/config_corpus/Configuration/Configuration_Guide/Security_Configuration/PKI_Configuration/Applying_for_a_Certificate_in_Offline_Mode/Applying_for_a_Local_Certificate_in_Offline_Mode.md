Applying for a Local Certificate in Offline Mode
================================================

Applying for a Local Certificate in Offline Mode

#### Prerequisites

You have completed the preconfiguration for a local certificate application. For details, see [Preconfiguration for Certificate Application](security_pki_cfg_0041.html).


#### Context

You can apply for a local certificate offline. To do this, you need to first generate a certificate enrollment request file on the device, and then send the file to the CA in out-of-band mode (for example, by disk or email).


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a PKI realm and enter its view, or enter the view of an existing PKI realm.
   
   
   ```
   [pki realm](cmdqueryname=pki+realm) realm-name
   ```
   
   
   
   By default, the system has a PKI realm named **default**. This realm can be modified but cannot be deleted.
   
   A PKI realm is locally available. It is unavailable to CAs or other devices. Each PKI realm has its own parameter settings.
3. Specify the PKI entity that applies for a certificate.
   
   
   ```
   [entity](cmdqueryname=entity) entity-name
   ```
   
   
   
   The PKI entity specified by *entity-name* must have been created using the [**pki entity**](cmdqueryname=pki+entity) command.
4. Configure the key pair used to apply for a certificate in offline mode as required.
   * This command is added to configure the RSA key pair used in offline certificate application.
     ```
     [rsa local-key-pair](cmdqueryname=rsa+local-key-pair) key-name
     ```
   * This command is added to configure the SM2 key pair used in offline certificate application.
     ```
     [sm2 local-key-pair](cmdqueryname=sm2+local-key-pair) key-name
     ```
5. Configure the digest algorithm used to sign certificate enrollment requests.
   
   
   ```
   [enrollment-request signature message-digest-method](cmdqueryname=enrollment-request+signature+message-digest-method) { md5 | sha1| sha-256 | sha-384 | sha-512 | sm3 }
   ```
   
   
   
   By default, the digest algorithm used to sign certificate enrollment requests is SHA-256.
   
   The digest algorithm used on a PKI entity must be the same as that used on the CA server. Note that the MD5 and SHA1 algorithms are insecure, so you are advised to use the more secure SHA2 algorithms (SHA-256, SHA-384, and SHA-512).
   
   In a PKI realm, if the SM2 key pair is used to apply for a certificate in offline mode, the digest algorithm used to sign certificate enrollment requests must be configured as SM3. If the RSA key pair is used to apply for a certificate in offline mode, the digest algorithm used to sign certificate enrollment requests cannot be configured as SM3. Otherwise, offline certificate application fails.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   For security purpose,you are not advised to use the weak security algorithm or weak security protocols provided by this feature. If you need to use the weak security algorithm or protocols, run the **install feature-software WEAKEA** command to install the weak security algorithm or protocol feature package WEAKEA. By default, the device provides the weak security algorithm or protocol feature package WEAKEA. For details about how to install or uninstall the feature package, see "Upgrade Maintenance Configuration" in Configuration Guide > System Management Configuration.
6. **Optional:** Configure the certificate public key usage attribute.
   
   
   ```
   [key-usage](cmdqueryname=key-usage) { signature | cipher }
   [quit](cmdqueryname=quit)
   ```
7. Configure the file format in which the device stores the certificate and certificate enrollment request in the system view.
   
   
   ```
   [pki file-format](cmdqueryname=pki+file-format) { der | pem }
   ```
   
   
   
   By default, the device stores the certificate and certificate enrollment request into a PEM file.
8. Set parameters to save certificate enrollment information into a file in PKCS#10 format.
   
   
   ```
   [pki enroll-certificate](cmdqueryname=pki+enroll-certificate) realm realm-name pkcs10 [ filename filename ] [ password password ]
   ```
   
   
   
   The challenge password used on a PKI entity must be the same as that configured on the CA server. If the CA server does not require a challenge password, this challenge password does not need to be configured.
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
10. Enable the device to send the certificate enrollment request file to the CA in out-of-band mode (for example, by disk or email) to apply for a local certificate.

#### Verifying the Configuration

* Run the [**display pki realm**](cmdqueryname=display+pki+realm) [ *realm-name* ] command to check the PKI realm information.
* Run the [**display pki cert-req**](cmdqueryname=display+pki+cert-req) **filename** *file-name* command to check the content of the certificate enrollment request file.