Downloading a Local Certificate
===============================

Downloading a Local Certificate

#### Context

A device downloads its local certificate using one of following methods, depending on the service type provided by the CA server:

* LDAP mode: The device's local certificate is downloaded from the server where the certificate is stored using LDAP. After the download is completed, the device automatically saves the local certificate to the **flash:/pki/public** directory on the device.
* Out-of-band mode: The device's local certificate is downloaded in out-of-band mode (for example, by disk or email) and then uploaded to the device storage.


#### Procedure

* Download the local certificate through LDAP.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [pki ldap-server-template](cmdqueryname=pki+ldap-server-template) template-name attribute attr-value save-name dn dn-value
  [commit](cmdqueryname=commit)
  ```
* Download the local certificate in out-of-band mode (for example, by disk or email).
  
  
  
  After you obtain the local certificate in out-of-band mode, manually upload it to the device storage. You can also download the local certificate through the management PC and then upload it to the device storage through FTP SFTP.

#### Verifying the Configuration

* Run the [**display pki credential-storage-path**](cmdqueryname=display+pki+credential-storage-path) command to check the default directory where a certificate is stored.
* Run the [**dir**](cmdqueryname=dir) command in the user view to check the local certificate file in the device storage.