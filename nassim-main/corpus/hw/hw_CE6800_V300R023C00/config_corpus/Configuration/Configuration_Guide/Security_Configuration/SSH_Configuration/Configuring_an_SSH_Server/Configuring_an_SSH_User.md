Configuring an SSH User
=======================

Configuring an SSH User

#### Context

Configuring an SSH user includes the following tasks: creating an SSH user and configuring an authentication mode for the SSH user. The authentication modes supported by the device include RSA, password, password-rsa, DSA, password-dsa, ECC, password-ecc, password-x509v3-rsa, x509v3-rsa, sm2, password-sm2, and all.

* password-rsa: The password authentication and RSA authentication requirements must be met.
* password-dsa: The password authentication and DSA authentication requirements must be met.
* password-ecc: The password authentication and ECC authentication requirements must be met.
* password-x509v3-rsa: The password authentication and X509V3-SSH-RSA authentication requirements must be met.
* password-sm2: The password authentication and SM2 authentication requirements must be met.
* all: The requirements of any one of the authentication modes must be met.

![](public_sys-resources/note_3.0-en-us.png) 

For security purposes, do not use the RSA algorithm whose length is less than 3072 digits. You are advised to use the ECC authentication algorithm instead.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an SSH user.
   
   
   ```
   [ssh user](cmdqueryname=ssh+user) user-name
   ```
   
   By default, no SSH user is created.
3. Configure an authentication mode for the SSH user.
   
   
   ```
   [ssh user](cmdqueryname=ssh+user) user-name authentication-type { password | rsa | password-rsa | all | dsa | password-dsa | ecc | password-ecc | sm2 | password-sm2 | password-x509v3-rsa | x509v3-rsa }
   ```
   
   By default, no authentication type is configured for an SSH user.
   
   If no SSH user is configured using the [**ssh user**](cmdqueryname=ssh+user) *user-name* command, run the [**ssh authentication-type default password**](cmdqueryname=ssh+authentication-type+default+password) command to configure password authentication as the default authentication mode. In this case, you only need to configure AAA users. This helps to simplify the configuration if there are a large number of users.
   
   * The password authentication mode is implemented based on AAA. When the password, password-rsa, password-x509v3-rsa, password-dsa, password-ecc, or password-sm2 mode is used to log in to the device, you need to create a local user in the AAA view with the same name as the SSH user.
   * If an SSH user is authenticated using the RSA, DSA, SM2, or ECC authentication mode, both the server and client need to generate the local RSA, DSA, SM2, or ECC key pair (for details, see [Configuring the SSH Server Function and Related Parameters](galaxy_ssh_cfg_0009.html)) and have each other's public key configured locally.
   
   Configure the authentication mode based on the preceding configuration. For details, see [Table 1](#EN-US_TASK_0000001513153334__table946042985217).
   
   **Table 1** Configuration in different authentication modes
   | Authentication Mode | Configuration Notes |
   | --- | --- |
   | password | Create an AAA user with the same username as the SSH user. For details, see [Table 2](#EN-US_TASK_0000001513153334__login034E5BF9). |
   | RSA, DSA, ECC, or SM2 authentication | Configure the device to generate a local RSA, DSA, SM2, or ECC key pair. For details, see [Table 3](#EN-US_TASK_0000001513153334__login03552A29). |
   | password-rsa, password-dsa, password-sm2, or password-ecc authentication | Create an AAA user with the same username as the SSH user and generate a local RSA, DSA, SM2, or ECC key pair. For details, see [Table 2](#EN-US_TASK_0000001513153334__login034E5BF9) and [Table 3](#EN-US_TASK_0000001513153334__login03552A29). |
   | x509v3-rsa | Bind the SSH user to the PKI realm. For details, see [Table 4](#EN-US_TASK_0000001513153334__table1953610297348). |
   | password-x509v3-rsa | Create an AAA user with the same username as the SSH user and bind the AAA user to the PKI realm. For details, see [Table 2](#EN-US_TASK_0000001513153334__login034E5BF9) and [Table 4](#EN-US_TASK_0000001513153334__table1953610297348). |
   
   
   **Table 2** Creating a local user with the same name as the SSH user in the AAA view
   | Step | Command | Description |
   | --- | --- | --- |
   | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
   | Enter the AAA view. | [**aaa**](cmdqueryname=aaa) | - |
   | Configure the local username and password. | [**local-user**](cmdqueryname=local-user) *user-name* **password** **irreversible-cipher** *password* | For security purposes, change the password periodically. |
   | Configure a service type for the local user. | [**local-user**](cmdqueryname=local-user) *user-name* **service-type ssh** | - |
   | Configure a privilege level for the local user. | [**local-user**](cmdqueryname=local-user) *user-name* **privilege level** *level* | - |
   | Return to the system view. | [**quit**](cmdqueryname=quit) | - |
   | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
   
   
   **Table 3** Configuring the local RSA, DSA, SM2, or ECC key for the SSH user
   | Step | Command | Description |
   | --- | --- | --- |
   | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
   | Configure an authentication type for the SSH connection. | [**ssh authorization-type default**](cmdqueryname=ssh+authorization-type+default) { **aaa** | **root** } | By default, the authentication type of the SSH connection is AAA. When the authentication type is AAA, only the password authentication mode can be configured. If the public key authentication mode is used, perform either of the following operations: * Run this command with the authentication type set to **root**. * In the AAA view, create a local user with the same name as the SSH user. |
   | Enter the RSA, SM2, DSA, or ECC public key view. | [**rsa peer-public-key**](cmdqueryname=rsa+peer-public-key) *key-name* [ **encoding-type** *enc-type* ]  or  [**dsa peer-public-key**](cmdqueryname=dsa+peer-public-key) *key-name* **encoding-type** *enc-type*  or  [**ecc peer-public-key**](cmdqueryname=ecc+peer-public-key) *key-name* [ **encoding-type** *enc-type* ]  or  **[**sm2 peer-public-key**](cmdqueryname=sm2+peer-public-key)** *key-name* | - |
   | Enter the public key editing view. | [**public-key-code begin**](cmdqueryname=public-key-code+begin) | - |
   | Edit the public key. | *hex-data* | * The public key must be a hexadecimal character string in the public key encoding format, and generated by SSH client software. For detailed operations, see the help documentation for the SSH client software. * You need to enter the RSA, DSA, SM2, or ECC public key on the device functioning as the SSH server. |
   | Exit the public key editing view. | [**public-key-code end**](cmdqueryname=public-key-code+end) | * If *hex-data* is invalid, the key cannot be generated after you run this command. * If the key specified by *key-name* has been deleted in another view, the system displays a message indicating that the key does not exist and directly returns to the system view when you run this command. |
   | Return to the system view from the public key view. | [**peer-public-key end**](cmdqueryname=peer-public-key+end) | - |
   | Assign an RSA, DSA, SM2, or ECC public key to the SSH user. | [**ssh user**](cmdqueryname=ssh+user) *user-name* **assign** { **rsa-key** | **dsa-key** | **ecc-key** | **sm2-key**} *key-name* | - |
   | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
   
   
   **Table 4** Binding a PKI realm to the SSH user
   | Step | Command | Description |
   | --- | --- | --- |
   | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
   | Bind a PKI realm to the SSH user. | [**ssh user**](cmdqueryname=ssh+user) *user-name* **assign** **pki** *pki-name* | Assign a PKI certificate to the SSH server.  The prerequisite is that PKI has been configured. |
   | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
4. Configure a service type for the SSH user.
   
   
   ```
   [ssh user](cmdqueryname=ssh+user) user-name service-type { all | { sftp | stelnet | snetconf }*}
   ```
   
   By default, no service type is configured for an SSH user.
5. (Optional) Configure SAN/CN verification for the SSH user.
   
   
   ```
   [ssh user](cmdqueryname=ssh+user) user-name cert-verify-san enable
   ```
   
   By default, the device does not check whether the CN or SAN in the certificate contains the realm name of the authentication user.
   
   After a PKI realm is bound to the SSH user, the system checks whether the Subject Alternative Name (SAN) or common name (CN) in the PKI certificate contains the realm name of the authentication user to enhance security.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```