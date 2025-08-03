Installing a CA Certificate
===========================

Installing a CA Certificate

#### Context

After the CA certificate is downloaded, the device automatically stores the CA certificate in **flash:/pki/public**.

After obtaining a CA certificate in out-of-band mode (for example, by disk or email), you need to upload the CA certificate to the specified storage directory on the device. Before installing a CA certificate, you need to upload the CA certificate to **flash:/pki/public**.

After the CA certificate is saved to the specified directory, you also need to import it to the device memory. After the device restarts, the system automatically loads the certificate.

![](public_sys-resources/note_3.0-en-us.png) 

To prevent a certificate installation failure, ensure that the CA certificate file size does not exceed 1 MB.

By default, the PKI realm named **default** exists. The **default** realm can be modified but cannot be deleted.



#### Procedure

1. **Optional:** Enter the user view and download the CA certificate to the **flash:/pki/public** directory.
   
   
   
   If you obtain the CA certificate in out-of-band mode and upload it to the device storage through FTP or SFTP, perform this step. SFTP is recommended because it is more secure than FTP.
   
   
   
   ```
   [cd pki](cmdqueryname=cd+pki)
   [cd public](cmdqueryname=cd+public)[/](cmdqueryname=%2F)
   [ftp 172.16.104.110](cmdqueryname=ftp+172.16.104.110)
   Trying 172.16.104.110...
   Press CTRL+K to abort
   Connected to 172.16.104.110.
   220 FTP service ready.
   User(172.16.104.110:(none)):ftpuser
   331 Password required for ftpuser
   Enter password:
   230 User logged in.
   [get ca.cer](cmdqueryname=get+ca.cer)
   200 Port command okay.
   150 Opening ASCII mode data connection for temp1.c.
   226 Transfer complete.
   FTP: 4 byte(s) received in 8.190 second(s) .48byte(s)/sec.
   ```
2. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
3. **Optional:** Import the initial CA certificate to the **default** realm.
   
   
   ```
   [pki import-certificate](cmdqueryname=pki+import-certificate) default_ca realm default
   ```
   
   The initial CA certificate has been saved to the NVRAM before the device is delivered. To use the initial CA certificate, run this command to load the certificate to the **default** realm. The initial CA certificate can be deleted. After it is deleted, you can import other CA certificates to the **default** realm. However, **default\_ca.cer** is the name reserved for the initial CA certificate. An imported certificate cannot be named **default\_ca.cer**. To restore the initial CA certificate after it is deleted, run this command to load the certificate to the **default** realm.
4. Create a PKI realm.
   
   
   ```
   [pki realm](cmdqueryname=pki+realm) realm-name
   [quit](cmdqueryname=quit)
   ```
5. Import the CA certificate to the device memory.
   
   
   ```
   [pki import-certificate](cmdqueryname=pki+import-certificate) ca [ [ realm realm-name ] { der | pkcs12 | pem } ] filename file-name [ cert-name cert-name ] [ no-check-hash-alg ] [ no-check-same-name ]
   ```
6. **Optional:** Set the number of days in advance you are notified that the CA certificate in the memory is about to expire.
   
   
   ```
   [pki set-certificate expire-prewarning](cmdqueryname=pki+set-certificate+expire-prewarning) day
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display pki certificate**](cmdqueryname=display+pki+certificate) **ca** [ **realm** *realm-name* | **filename** *file-name* ] command to check the CA certificate that has been loaded on the device.