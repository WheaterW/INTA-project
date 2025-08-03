Verifying and Viewing Initial Certificates
==========================================

Verifying and Viewing Initial Certificates

#### Context

Before a device is delivered, the CA and local certificates are loaded on the device and stored in the NVRAM. These certificates cannot be deleted or modified. The initial certificates, which function as the device identity, are imported to the **default** realm to ensure the security of the device and external communication.

By default, the validity of initial certificates has been verified before a device is delivered. Generally, you do not need to verify initial certificates.


#### Procedure

* Verify the validity of initial certificates.
  
  
  ```
  [pki validate-certificate device slot](cmdqueryname=pki+validate-certificate+device+slot) slot-id
  ```
* View the contents of initial certificates.
  
  
  ```
  [display pki certificate device slot](cmdqueryname=display+pki+certificate+device+slot) slot-id
  ```