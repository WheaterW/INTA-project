Moving Overwritten Files to the Recycle Bin
===========================================

Moving Overwritten Files to the Recycle Bin

#### Context

Overwritten files are permanently deleted by default and cannot be restored. If you want to restore overwritten files in case new files are unavailable, enable the function of moving these files to the recycle bin.

This function applies only to the following scenarios:

* The existing CRL has been overwritten using the [**pki import-crl**](cmdqueryname=pki+import-crl) command.
* The existing certificates have been overwritten using the [**pki enroll-certificate**](cmdqueryname=pki+enroll-certificate), [**pki create-certificate**](cmdqueryname=pki+create-certificate), [**pki export-certificate**](cmdqueryname=pki+export-certificate), [**pki export-certificate default**](cmdqueryname=pki+export-certificate+default), or [**pki import-certificate peer**](cmdqueryname=pki+import-certificate+peer) command.
* The existing RSA key pair has been overwritten using the [**pki import rsa-key-pair**](cmdqueryname=pki+import+rsa-key-pair) or [**pki export rsa-key-pair**](cmdqueryname=pki+export+rsa-key-pair) command.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the function of moving overwritten files to the recycle bin.
   
   
   ```
   [pki recycle-bin enable](cmdqueryname=pki+recycle-bin+enable)
   ```
   
   
   
   By default, overwritten files are deleted permanently.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```