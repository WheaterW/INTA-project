Downloading a CA Certificate
============================

Downloading a CA Certificate

#### Context

When applying for a local certificate, the PKI entity sends the certificate enrollment request to the CA. To improve transmission security, the PKI entity must use the CA's public key to encrypt the certificate enrollment request. Therefore, the PKI entity must download and obtain the CA certificate and then obtain the CA's public key.

A CA certificate can be downloaded using the following methods, which differ in the service types provided by the CA:

* Download the CA certificate from the CMPv2 server to the device storage through CMPv2.
* Download the CA certificate from the server where the certificate is stored to the device storage through LDAP.
* Obtain the CA certificate in out-of-band mode (for example, by disk or email) and then upload it to the device storage.

#### Procedure

* Download a CA certificate through CMPv2.
  
  
  
  For details about how to download a CA certificate through CMPv2, see [Applying for and Updating a Local Certificate in Online Mode Using CMPv2](security_pki_cfg_0046.html).
* Download a CA certificate through LDAP.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [pki ldap-server-template](cmdqueryname=pki+ldap-server-template) template-name attribute attr-value save-name dn dn-value
  [commit](cmdqueryname=commit)
  ```
* Obtain a CA certificate in out-of-band mode.
  
  
  
  After you obtain a CA certificate in out-of-band mode (for example, by disk or email), manually upload it to the device storage. You can also download a CA certificate through the administrator's PC and then upload it to the device storage through FTP or SFTP. SFTP is recommended because it is more secure than FTP.