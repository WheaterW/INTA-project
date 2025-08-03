Importing the RSA, or SM2 Key Pair and Certificate of Another Device
====================================================================

Importing the RSA, or SM2 Key Pair and Certificate of Another Device

#### Context

On the live network, if a device does not apply for a certificate, you can import the RSA, or SM2 key pair and certificate of another device.


#### Procedure

1. On DeviceA, export its RSA, or SM2 key pair and certificate.
   
   
   ```
   [pki export rsa-key-pair](cmdqueryname=pki+export+rsa-key-pair) keyname [ and-certificate certificate-name ] { pem filename [ aes ] | pkcs12 filename } password password
   [pki export sm2-key-pair](cmdqueryname=pki+export+sm2-key-pair) keyname pem filename [ password password ]
   ```
2. Save the key file in the storage of DeviceA to a PC using a file transfer protocol such as SFTP.
3. Save the key file on the PC to the storage of DeviceB using a file transfer protocol such as SFTP.
4. On DeviceB, import the RSA, or SM2 key pair and certificate of DeviceA.
   
   
   ```
   [pki import rsa-key-pai](cmdqueryname=pki+import+rsa-key-pai)[r](cmdqueryname=r) keyname [ exclude-cert ] { pem | pkcs12 } filename [ exportable ] [ password  password ]
   [pki import sm2-key-pai](cmdqueryname=pki+import+sm2-key-pai)[r](cmdqueryname=r) keyname pem filename [ exportable ] signkey  signkey-name [ certificate  certificate-name ]
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```