Configuring First Login to the SSH Server (Enabling First Login on the SSH Client)
==================================================================================

After first login is enabled on an SSH client (SFTP client in this case), the client does not check the validity of the RSA, DSA, SM2, ECC public key for the SSH server when logging in to the SSH server for the first time.

#### Context

After first login is enabled on the SSH client (STelnet client in this case), the client does not check the validity of the RSA, DSA, SM2, ECC public key for the SSH server when logging in to the SSH server for the first time. After the first login, the SSH client automatically saves the RSA, DSA, SM2, ECC public key for subsequent login authentication.

Perform the following steps on the device that functions as an SSH client:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ssh client first-time enable**](cmdqueryname=ssh+client+first-time+enable)
   
   
   
   First login is enabled on the SSH client.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.