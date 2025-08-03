Obtaining Certificates
======================

To use certificates to authenticate users, an entity needs to obtain local and CA certificates. A local certificate proves the identity of the entity, and a CA certificate proves that the local certificate is issued by a legal CA.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In a two-node cluster scenario, you are advised to set different certificate expiration dates for the active and backup devices to prevent them from being unavailable simultaneously.

To obtain a certificate, perform the following configuration:

* Configure a PKI domain.
  
  Before a certificate is applied for, create a PKI domain and configure entity information in the PKI domain.
  
  A PKI domain is of local significance only. It is unavailable to CAs or other devices. Each PKI domain has its own parameter settings.
* Apply for certificates manually.
  
  After the NE40E generates a certificate request file, send the file to the CA through email, FTP, or disk to apply for certificates.
* Download certificates manually.
  
  After the CA server generates certificates, download the CA and local certificates to the local device through email, FTP, or disk.
* Install certificates.
  
  After obtaining CA and local certificates, install them on the device for them to take effect.

#### Procedure

* Configure a PKI domain.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**pki domain**](cmdqueryname=pki+domain) *domain-name*
     
     A PKI domain is created, and the PKI domain name configuration view is displayed.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) If a non-default key pair is required, perform the following operations:
     1. Run the [**pki cmp session**](cmdqueryname=pki+cmp+session) *session-name* command to create a CMP session and enter the PKI CMP session view.
     2. Run the [**cmp request rsa local-key-pair**](cmdqueryname=cmp+request+rsa+local-key-pair+regenerate) *key-name* [ **regenerate** [ *key-bit* ] ] command to specify a local RSA key pair to be used by CMP requests.
  3. Run [**certificate request entity**](cmdqueryname=certificate+request+entity) *entity-name*
     
     An entity name is specified.
     
     The specified entity name must exist.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Apply for a certificate.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. (Optional) Run [**pki file-format**](cmdqueryname=pki+file-format+der+pem) { **der** | **pem** }
     
     The certificate file format is configured.
  3. Run [**pki request-certificate domain**](cmdqueryname=pki+request-certificate+domain+pkcs10) *domain-name* **pkcs10** [ **signature-algorithm** { **sha2-256** | **sha2-384** | **sha2-512** } ]
     
     A certificate request file named **domain-name.req** is generated.
  4. Apply for a local certificate.
     
     Send the certificate application file to the CA through email, FTP, or disk to apply for a local certificate.
  5. (Optional) Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Download the certificate manually.
* Install the certificate.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**pki import-certificate**](cmdqueryname=pki+import-certificate+ca+local+peer+domain+filename) { **ca** | **local** | **peer** } [ **domain** *domainName* ] **filename** *file-name*
     
     The CA certificate or local certificate is installed.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To ensure high security, you are advised not to import certificates that use the MD5 or SHA1 algorithm. The recommended key length of a certificate is 2048 bits or more.
     
     The default domain of PKI is reserved. For the default domain, you can run the [**pki import-certificate**](cmdqueryname=pki+import-certificate) command to install the downloaded user certificate or run the **pki load** { **preset-ca** | **preset-local** } **domain** **default** command to load the preset CA or local certificate.
  3. (Optional) Run [**pki strict-mode**](cmdqueryname=pki+strict-mode), Strict check is enabled for PKI.