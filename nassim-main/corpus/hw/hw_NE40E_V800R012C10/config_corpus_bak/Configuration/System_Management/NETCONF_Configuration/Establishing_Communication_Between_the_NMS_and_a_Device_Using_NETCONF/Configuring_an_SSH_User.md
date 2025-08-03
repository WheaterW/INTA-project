Configuring an SSH User
=======================

When specifying a secure shell protocol (SSH) as the transport protocol of NETCONF, you must configure an SSH user, configure the SSH server to generate a local key pair, configure a user authentication mode, and specify a service type for the SSH user.

#### Context

SSH users support the all, RSA, DSA, ECC, SM2, X509v3-SSH-RSA, password, password-RSA, password-ECC, password-DSA, password-SM2, and password-X509v3-RSA authentication modes.

If the authentication mode of an SSH user is RSA, DSA, SM2, or ECC, a local RSA, DSA, SM2, or ECC key pair must be generated on both the server and client. In addition, the server needs to edit the public key of the client locally. After the editing, the public key is bound to the local user.

[Table 1](#EN-US_TASK_0139427569__en-us_task_0172359819_tab_1) compares the RSA, DSA, SM2, X509v3-SSH-RSA, and ECC algorithms.

**Table 1** RSA, DSA, SM2, X509v3-SSH-RSA, and ECC algorithms
| Algorithm | Application Scenarios |
| --- | --- |
| RSA/DSA | An asymmetric public key encryption algorithm, which improves encryption efficiency and simplifies key management. This algorithm allows the server to check whether the SSH user, public key, and digital signature are valid. User authentication succeeds only if all of them are the same as those configured on the server. |
| ECC | An asymmetric encryption algorithm similar to RSA and DSA. Compared with the RSA and DSA algorithms, the ECC algorithm has the following advantages:  * Provides the same security with a shorter key length than the RSA algorithm. * Features a shorter computing process and higher processing speed. * Requires less storage space. * Requires lower bandwidth. |
| SM2 | SM2 is an ECC-based asymmetric encryption algorithm. |
| X509v3-SSH-RSA | The X509v3-SSH-RSA algorithm is based on a PKI certificate and features better scalability and higher security. A PKI certificate must be bound to the user and server. |


[Table 2](#EN-US_TASK_0139427569__en-us_task_0172359819_table338718267498) describes the application scenarios of various authentication modes.

**Table 2** Application scenario of each authentication type
| Authentication Mode | Application Scenarios |
| --- | --- |
| RSA authentication and DSA authentication | RSA and DSA are public key encryption systems and asymmetric encryption algorithms. They can effectively improve the encryption efficiency and simplify key management. The server checks whether the SSH user, public key, and digital signature are valid. User authentication succeeds only if all of them are the same as those configured on the server. |
| ECC authentication | Like RSA authentication, the server first checks the validity of the SSH user and whether the public key and the digital signature are valid. If all of them are consistent with those configured on the server, user authentication succeeds. User authentication succeeds only if all of them are the same as those configured on the server. Compared with RSA authentication, ECC authentication has the following advantages:  * Provides the same security with a shorter key length. * Features a shorter computing process and higher processing speed. * Requires less storage space. * Requires lower bandwidth. |
| Password authentication | On the server, the AAA module assigns each authorized user a password for login. The server has the mapping between usernames and passwords. When a user requests to access the server, the server authenticates the username and password. If either of them fails to be authenticated, the access request of the user is denied.  NOTE:  You are advised to select public key authentication instead of password authentication as the client identity authentication mode. |
| password-RSA, password-DSA, password-ECC, password-SM2, or password-x509v3-rsa authentication | An SSH server authenticates a client by checking both the public key and the password, and returns an authentication success result only when both the public key and the password are consistent with those configured on the server. |
| SM2 authentication | SM2 is a standard encryption algorithm. The server checks whether the SSH user, the public key assigned to the user, and the digital signature of the user are valid. User authentication succeeds only if all of them are the same as those configured on the server. |
| X509v3-SSH-RSA authentication | The X509v3-SSH-RSA algorithm is based on a PKI certificate and features better scalability and higher security. |
| All authentication | The SSH server authenticates a client by checking the public key or password. The client can be authenticated when either the public key or password meets the requirement. |

![](../../../../public_sys-resources/note_3.0-en-us.png) 

For security purposes, you are advised not to use the RSA algorithm with a key length of less than 3072 bits for SSH user authentication. Using the ECC authentication algorithm for higher security is recommended.

The user level depends on the authentication mode and configuration selected by the access user.

* If password authentication is used for SSH users, the SSH user level is the same as that configured in the AAA view.
* If public key authentication or PKI certificate authentication is used for SSH users and the [**ssh authorization-type default**](cmdqueryname=ssh+authorization-type+default) {**aaa** | **root** } command has been run to set the user authorization mode to AAA, the SSH user level is determined by the level configured in the AAA view based on the specified authorization mode.
  + If the authorization mode is AAA, the user level is the one configured in the AAA view.
  + If the authorization type is root, the user level is the one configured in the VTY user interface.
* If public key authentication or PKI certificate authentication is used for SSH users but the [**ssh authorization-type default**](cmdqueryname=ssh+authorization-type+default) { **aaa** | **root** } command has not been run to set a user authorization mode, the SSH user level is determined by the level configured in the AAA view.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. If password authentication is configured for the SSH user, create a local user with the same name as the SSH user in the AAA view and set the local user access type to SSH. Perform the following steps to configure the local user:
   1. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   2. Run [**local-user**](cmdqueryname=local-user) *user-name* **password** [ **cipher** *password* | **irreversible-cipher** *irreversible-cipher-password* ]
      
      
      
      A local username and password are configured.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * The new password is at least eight characters long and contains at least two of the following types: upper-case letters, lower-case letters, digits, and special characters, except the question mark (?) and space.
      * For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password.
   3. Run [**local-user**](cmdqueryname=local-user) *user-name* **user-group manage-ug**
      
      
      
      The local user is configured with administrator rights.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Although a user without management rights can create a NETCONF connection, the user has limited permissions to NETCONF operations.
   4. Run [**local-user**](cmdqueryname=local-user) *user-name* **service-type** **ssh**
      
      
      
      The local user access type is set to SSH.
      
      
      
      You can specify an access type to allow only users configured with the specified access type to log in to the device.
   5. Run [**local-user**](cmdqueryname=local-user) *user-name* **password expire** *days*
      
      
      
      The period after which a password expires is configured for the local user.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      To harden network security, administrators can run the [**local-user password expire**](cmdqueryname=local-user+password+expire) command to configure the period after which a password expires.
      
      When the password is changed, the system resets the period.
      
      The command applies only to local users. After a password expires, reconfigure a new password for users. Otherwise, users fail to log in.
   6. Run [**user-password expire**](cmdqueryname=user-password+expire) *expire-days* **prompt** *prompt-days*
      
      
      
      The password expiration time and the number of days in advance the system prompts the administrator to change the password are configured.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      To prevent account stealing due to unchanged passwords, run the **user-password expire** command to set the password validity period and the period for advance warning before the password expires.
      
      Only a level-3 or higher-level administrator can run the command.
      
      * The command applies only to administrators. The system prompts the administrator to change the password N days before the password expires.
      * If the administrator does not change the password till the password expires, the administrator is denied access to the device.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit from the AAA view.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In addition to local users, server users can also log in to the NMS through NETCONF. If a server user logs in to the NMS through NETCONF, a user group or user level needs to be configured on the AAA server. For details about the configuration, see the configuration guide provided by the associated vendor.
3. (Optional) Run either of the following commands to create a key pair:
   
   
   * If the user requirements for system security are not high, run the [**rsa local-key-pair create**](cmdqueryname=rsa+local-key-pair+create) command to configure a local RSA key pair or run the [**dsa local-key-pair create**](cmdqueryname=dsa+local-key-pair+create) command to configure a local DSA key pair.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To ensure high security, do not use the RSA algorithm whose length is less than 3072 digits or DSA algorithm.
   * If you have high requirements for the system security, run the [**ecc local-key-pair create**](cmdqueryname=ecc+local-key-pair+create) command to create a local ECC key pair.
4. Perform any of the operations listed in [Table 3](#EN-US_TASK_0139427569__en-us_task_0172359819_tab_dc_vrp_basic_cfg_004002) based on the SSH user authentication mode to be configured.
   
   
   
   **Table 3** Configuring an SSH user authentication mode
   | Item | Operation | Remarks |
   | --- | --- | --- |
   | Configure password authentication. | Run the [**ssh user**](cmdqueryname=ssh+user) *user-name* **authentication-type** **password** command. | If local or HWTACACS authentication is used and only a few users need to be authenticated, use password authentication. |
   | Configure RSA authentication. | 1. Run the [**ssh user**](cmdqueryname=ssh+user) *user-name* **authentication-type** **rsa** command to configure RSA authentication. | - |
   | 2. Run the [**rsa peer-public-key**](cmdqueryname=rsa+peer-public-key) *key-name* **encoding-type** *enc-type* command to enter the RSA public key view. | - |
   | 3. Run the [**public-key-code begin**](cmdqueryname=public-key-code+begin) command to enter the public key edit view. | - |
   | 4. Enter *hex-data* to edit the public key.  NOTE:  Before editing the public key, you need to use the SSH client software to generate the RSA key pair on the SSH client. The following uses the PuTTYGen.exe software as an example. For the configuration procedure, see Step 1 in [Using STelnet to Log In to a Server](dc_vrp_basic_cfg_0135.html). Copy all the public keys generated in Step 1.c here.  When editing the public key generated by PuTTY, set the encoding mode in Step 2 to **openssh** through the [**rsa peer-public-key**](cmdqueryname=rsa+peer-public-key) *key-name* **encoding-type** **openssh** command. | * In the public key edit view, the public key must be a hexadecimal string in the public key format. This key is randomly generated by the SSH client software. For detailed operations, see the help document for the SSH client software. * After entering the public key edit view, you can send the RSA public key generated on the SSH client to the SSH server. Specifically, copy and paste the RSA public key to the device functioning as the SSH server. |
   | 5. Run the [**public-key-code end**](cmdqueryname=public-key-code+end) command to exit the public key edit view. | - |
   | 6. Run the [**peer-public-key end**](cmdqueryname=peer-public-key+end) command to exit the public key view and return to the system view. | * A public key can be generated only after a valid *hex-data* complying with the public key format is entered and the [**peer-public-key end**](cmdqueryname=peer-public-key+end) command is run. * If you run the [**peer-public-key end**](cmdqueryname=peer-public-key+end) command after *key-name* specified in Step 2 is deleted in another view, the system displays a message, indicating that the key does not exist. The system then returns to the system view. |
   | 7. Run the [**ssh user**](cmdqueryname=ssh+user) *user-name* **assign** **rsa-key** *key-name* command to allocate an RSA public key to the SSH user. | - |
   | Configure DSA authentication. | 1. Run the [**ssh user**](cmdqueryname=ssh+user) *user-name* **authentication-type** **dsa** command to configure DSA authentication. | - |
   | 2. Run the [**dsa peer-public-key**](cmdqueryname=dsa+peer-public-key) *key-name* **encoding-type** *enc-type* command to enter the DSA public key view. | - |
   | 3. Run the [**public-key-code begin**](cmdqueryname=public-key-code+begin) command to enter the public key edit view. | - |
   | 4. Enter *hex-data* to edit the public key.  NOTE:  Before editing a public key, use the SSH client software to generate a DSA key pair on the SSH client. The following uses the PuTTYGen.exe software as an example to describe how to generate an RSA key pair. For the configuration procedure, see Step 1 in [Using STelnet to Log In to a Server](dc_vrp_basic_cfg_0135.html). Copy all the public keys generated in Step 1.c here.  When editing the public key generated by PuTTY, set the encoding mode in Step 2 to **openssh** through the [**dsa peer-public-key**](cmdqueryname=dsa+peer-public-key) *key-name* **encoding-type** **openssh** command. | * In the public key edit view, the public key must be a hexadecimal string in the public key format. This key is randomly generated by the SSH client software. For detailed operations, see the help document for the SSH client software. * After entering the public key edit view, you can send the DSA public key generated on the SSH client to the SSH server. Specifically, copy and paste the DSA public key to the device functioning as the SSH server. |
   | 5. Run the [**public-key-code end**](cmdqueryname=public-key-code+end) command to exit the public key edit view. | - |
   | 6. Run the [**peer-public-key end**](cmdqueryname=peer-public-key+end) command to exit the public key view and return to the system view. | * A public key can be generated only after a valid *hex-data* complying with the public key format is entered and the [**peer-public-key end**](cmdqueryname=peer-public-key+end) command is run. * If you run the [**peer-public-key end**](cmdqueryname=peer-public-key+end) command after *key-name* specified in Step 2 is deleted in another view, the system displays a message, indicating that the key does not exist. The system then returns to the system view. |
   | 7. Run the [**ssh user**](cmdqueryname=ssh+user) *user-name* **assign** **dsa-key** *key-name* command to allocate a DSA public key to the SSH user. | - |
   | Configure ECC authentication. | 1. Run the [**ssh user**](cmdqueryname=ssh+user) *user-name* **authentication-type** **ecc** command to configure ECC authentication. | - |
   | 2. Run the [**ecc peer-public-key**](cmdqueryname=ecc+peer-public-key) *key-name* [ **encoding-type** *enc-type* ] command to enter the ECC public key view. | - |
   | 3. Run the [**public-key-code begin**](cmdqueryname=public-key-code+begin) command to enter the public key edit view. | - |
   | 4. Enter *hex-data* to edit the public key.  NOTE:  Before editing a public key, use the SSH client software to generate an ECC key pair on the SSH client. The following uses the PuTTYGen.exe software as an example to describe how to generate an RSA key pair. For the configuration procedure, see Step 1 in [Using STelnet to Log In to a Server](dc_vrp_basic_cfg_0135.html). Copy all the public keys generated in Step 1.c here.  When editing the public key generated by PuTTY, set the encoding mode in Step 2 to **openssh** through the [**ecc peer-public-key**](cmdqueryname=ecc+peer-public-key) *key-name* **encoding-type** **openssh** command. | * In the public key edit view, the public key must be a hexadecimal string in the public key format. This key is randomly generated by the SSH client software. For detailed operations, see the help document for the SSH client software. * After entering the public key edit view, you can send the ECC public key generated on the SSH client to the SSH server. Specifically, copy and paste the ECC public key to the device functioning as the SSH server. |
   | 5. Run the [**public-key-code end**](cmdqueryname=public-key-code+end) command to exit the public key edit view. | - |
   | 6. Run the [**peer-public-key end**](cmdqueryname=peer-public-key+end) command to exit the public key view and return to the system view. | * A public key can be generated only after a valid *hex-data* complying with the public key format is entered and the [**peer-public-key end**](cmdqueryname=peer-public-key+end) command is run. * If you run the [**peer-public-key end**](cmdqueryname=peer-public-key+end) command after *key-name* specified in Step 2 is deleted in another view, the system displays a message, indicating that the key does not exist. The system then returns to the system view. |
   | 7. Run the [**ssh user**](cmdqueryname=ssh+user) *user-name* **assign** **ecc-key** *key-name* command to allocate an ECC public key to the SSH user. | - |
   | Configure SM2 authentication. | 1. Run the [**ssh server publickey**](cmdqueryname=ssh+server+publickey) **sm2** command to enable the public key algorithm for the SSH server. | - |
   | 2. Run the [**ssh user**](cmdqueryname=ssh+user) *user-name* **authentication-type** **sm2** command to configure SM2 authentication. | - |
   | 3. Run the [**sm2 peer-public-key**](cmdqueryname=sm2+peer-public-key) *key-name* command to enter the SM2 public key view. | - |
   | 4. Run the [**public-key-code begin**](cmdqueryname=public-key-code+begin) command to enter the public key edit view. | - |
   | 5. Enter *hex-data* to edit the public key. | * In the public key edit view, the public key must be a hexadecimal string in the public key format. This key is randomly generated by the SSH client software. For detailed operations, see the help document for the SSH client software. * After entering the public key edit view, you can send the SM2 public key generated on the SSH client to the SSH server. Specifically, copy and paste the SM2 public key to the device functioning as the SSH server. |
   | 6. Run the [**public-key-code end**](cmdqueryname=public-key-code+end) command to exit the public key edit view. | - |
   | 7. Run the [**peer-public-key end**](cmdqueryname=peer-public-key+end) command to exit the public key view and return to the system view. | * A public key can be generated only after a valid *hex-data* complying with the public key format is entered and the [**peer-public-key end**](cmdqueryname=peer-public-key+end) command is run. * If you run the [**peer-public-key end**](cmdqueryname=peer-public-key+end) command after *key-name* specified in Step 2 is deleted in another view, the system displays a message, indicating that the key does not exist. The system then returns to the system view. |
   | 8. Run the [**ssh user**](cmdqueryname=ssh+user) *user-name* **assign** **sm2-key** *key-name* command to allocate an SM2 public key to the SSH user. | - |
   | Configure X509v3-SSH-RSA authentication. | 1. Run the [**ssh user**](cmdqueryname=ssh+user) *user-name* **authentication-type** **x509v3-rsa** command to configure X509v3-SSH-RSA authentication. | - |
   | 2. Run the [**ssh user**](cmdqueryname=ssh+user) *user-name* **assign** **pki** *pki-name* command to allocate a PKI certificate to the SSH user. | - |
5. (Optional) Configure the SSH server parameters. For details, see [2](dc_vrp_basic_cfg_0042.html#EN-US_TASK_0172359831__step_dc_vrp_basic_cfg_004201)
6. Run [**ssh user**](cmdqueryname=ssh+user) *user-name* **service-type** { **snetconf** | **all** }
   
   
   
   The service type of an SSH user is set to SNETCONF.
7. (Optional) Run [**ssh server rsa-key min-length**](cmdqueryname=ssh+server+rsa-key+min-length) *min-length-val*
   
   
   
   The minimum length of the RSA public key is specified.
8. (Optional) Run [**ssh user**](cmdqueryname=ssh+user) *user-name*[**cert-verify-san enable**](cmdqueryname=cert-verify-san+enable)
   
   
   
   SAN/CN verification for the SSH user is configured.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.