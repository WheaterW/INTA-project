Deleting a Key Pair
===================

When a user's key is disclosed, the corresponding key pair must be deleted, and a new key pair needs to be created.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

After you delete the RSA key pair used by a certificate, the certificate cannot be updated, and the RSA key pair cannot be restored. Exercise caution when deleting a key pair.



#### Procedure

* Run the [**rsa pki local-key-pair**](cmdqueryname=rsa+pki+local-key-pair+destroy) [ *keypair-name* ] **destroy** command to delete a local RSA key pair.
* Run the [**sm2 pki local-key-pair**](cmdqueryname=sm2+pki+local-key-pair+destroy) [ *keypair-name* ] **destroy** command to delete a local SM2 key pair.