Configuring a Self-signed Certificate
=====================================

Configuring a Self-signed Certificate

#### Context

If a device fails to request a local certificate from the CA, it can generate a self-signed certificate. The generated certificate is saved as a file in storage, implementing simple certificate issuing. You can export the certificate and transfer it to another device. A self-signed certificate is issued by a device to itself and is signed by the initial CA on the device. That is, the certificate issuer is the same as the certificate subject. This type of certificate contains signature information, and it does not require signature application.

![](public_sys-resources/note_3.0-en-us.png) 

The device does not support lifecycle management (such as certificate update and revocation) of its self-signed certificate. To ensure security of the device and certificate, you are advised to replace the self-signed certificate with a local certificate.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a self-signed or unsigned certificate.
   
   
   ```
   [pki create-certificate](cmdqueryname=pki+create-certificate) [ self-signed ] filename file-name
   ```
   
   
   
   During the configuration, you will be prompted to enter the certificate information, such as PKI entity attributes, the certificate file name, the certificate validity period, and the RSA key length.
   
   If the **self-signed** parameter is specified, a self-signed certificate is created. If this parameter is not specified, an unsigned certificate is created. An unsigned certificate, as its name implies, is not signed. It is issued by a device to itself. A signature needs to be obtained from the CA, and the certificate issuer is the CA.
   
   The file format of the created self-signed or unsigned certificate is PEM.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```