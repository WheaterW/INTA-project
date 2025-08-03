Configuring a Certificate Whitelist to Implement Access Control
===============================================================

Configuring a Certificate Whitelist to Implement Access Control

#### Prerequisites

Certificate whitelist files need to be stored in advance under the **flash:/pki/public** directory of the device.


#### Context

A certificate whitelist contains common names (CNs) or serial numbers (SNs) of base station certificates. When the local device receives a certificate authentication request from the peer device and if the CN or SN of the peer certificate is whitelisted on the local device, the certificate authentication succeeds.

To make the PKI certificate whitelist check function take effect, import certificate whitelist files to the device memory.


#### Procedure

* Import a certificate whitelist file to the device memory.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [pki import whitelist](cmdqueryname=pki+import+whitelist) filename file-name
  [commit](cmdqueryname=commit)
  ```
* Delete a certificate whitelist file.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [pki delete whitelist](cmdqueryname=pki+delete+whitelist) filename file-name
  [commit](cmdqueryname=commit)
  ```

#### Verifying the Configuration

Run the [**display pki whitelist**](cmdqueryname=display+pki+whitelist) { **all** | **filename** *file-name* } command to check the content of certificate whitelist files on the device.