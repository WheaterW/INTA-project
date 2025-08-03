Clearing PKI Information
========================

Clearing PKI Information

#### Context

PKI information cannot be restored after it is cleared. Exercise caution when you run the following **reset** commands in the user view.


#### Procedure

* Clear the OCSP response cache.
  
  
  ```
  [reset pki ocsp response cache](cmdqueryname=reset+pki+ocsp+response+cache)
  [commit](cmdqueryname=commit)
  ```
* Clear the OCSP server down information recorded on the device.
  
  
  ```
  [reset pki ocsp server down-information](cmdqueryname=reset+pki+ocsp+server+down-information) [ url [ esc ] url-addr ]
  [commit](cmdqueryname=commit)
  ```
* Clear the CA certificates, CRLs, local certificates, and OCSP responder certificates that have been imported into the memory.
  
  
  ```
  [reset pki global-ca](cmdqueryname=reset+pki+global-ca)
  [commit](cmdqueryname=commit)
  ```
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  This command will delete all CA certificates, CRLs, local certificates, and OCSP responder certificates that have been imported into the device memory. Exercise caution when running this command.