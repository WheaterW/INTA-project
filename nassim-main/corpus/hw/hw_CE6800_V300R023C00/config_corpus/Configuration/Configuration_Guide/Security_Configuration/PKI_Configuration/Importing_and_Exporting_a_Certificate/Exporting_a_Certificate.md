Exporting a Certificate
=======================

Exporting a Certificate

#### Context

The CA certificate, local certificate, and OCSP server certificate of a device can be exported for use on another device. You can run the commands in "Procedure" to export certificates to the device storage, and then transfer the certificates to another device through FTP or SFTP.


#### Procedure

* In the system view, export the CA certificate.
  
  
  ```
  [pki export-certificate](cmdqueryname=pki+export-certificate) ca realm realm-name { pem | pkcs12 }
  [commit](cmdqueryname=commit)
  ```
* In the system view, export the default CA certificate.
  
  
  ```
  [pki export-certificate default](cmdqueryname=pki+export-certificate+default) ca filename file-name
  [commit](cmdqueryname=commit)
  ```
* In the system view, export the local certificate.
  
  
  ```
  [pki export-certificate](cmdqueryname=pki+export-certificate) local realm realm-name { pem | pkcs12 }
  [commit](cmdqueryname=commit)
  ```
* In the system view, export the OCSP server certificate.
  
  
  ```
  [pki export-certificate](cmdqueryname=pki+export-certificate) ocsp realm realm-name { pem | pkcs12 }
  [commit](cmdqueryname=commit)
  ```