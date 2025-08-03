Deleting a Certificate
======================

When a certificate becomes invalid, you can delete it by specifying the file name. If the key is disclosed, you can delete all local certificates, CA certificates, CRL certificates, and remote certificates. Then, apply for new certificates.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Certificates cannot be restored after being deleted. Exercise caution when deleting certificates.



#### Procedure

* Delete a specified certificate file.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**pki delete-certificate**](cmdqueryname=pki+delete-certificate+ca+crl+local+peer+domain+filename) { **ca** | **crl** | **local** | **peer** } [ **domain** *domainName* ] **filename** *file-name* command to delete a specified certificate file from the memory. Running this command does not delete the corresponding file from the CF card.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When you run the [**pki delete-certificate**](cmdqueryname=pki+delete-certificate) command to delete a specified certificate file from the memory, the device first searches for the corresponding file in the CF card. If the device fails to find the file in the CF card, the file cannot be deleted from the memory using this command. In this case, you can run the [**reset pki all-cert**](cmdqueryname=reset+pki+all-cert) command to delete all certificates.
* Run the [**reset pki all-cert**](cmdqueryname=reset+pki+all-cert) command to delete all imported local certificates, CA certificates, and CRL certificates from the memory. Running this command does not delete the corresponding certificate files from the CF card.