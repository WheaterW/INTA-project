Deleting Certificates
=====================

Deleting Certificates

#### Context

When a local certificate expires or a new certificate is required, delete the existing local certificate from the device memory. The following table lists the commands for deleting certificates from the device memory in the system view.

**Table 1** Commands for deleting certificates
| To... | Run... |
| --- | --- |
| Delete a local certificate from the device memory | [**pki delete-certificate**](cmdqueryname=pki+delete-certificate) **local** { **realm** *realm-name* | **filename** *file-name* } |
| Delete a CA certificate from the device memory | [**pki delete-certificate**](cmdqueryname=pki+delete-certificate) **ca** { **realm** *realm-name* | **filename** *file-name* } |
| Delete an OCSP server certificate from the device memory | [**pki delete-certificate**](cmdqueryname=pki+delete-certificate) **ocsp** { **realm** *realm-name* | **filename** *file-name* } |