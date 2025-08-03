Configuring First-Time Login to Another Device Functioning as an SSH Server (with a Public Key Assigned from an SSH Client)
===========================================================================================================================

To allow an SSH client (STelnet client in this case) with first-time authentication disabled to successfully log in to an SSH server for the first time, configure the SSH client to assign an RSA, DSA, SM2, or ECC public key to the SSH server before the login.

#### Context

If first-time authentication is disabled on an SSH client (STelnet client in this case), the client cannot log in to the SSH server because of a failure to check the validity of the RSA, DSA, SM2, or ECC public key on the server. As such, the STelnet client must assign an RSA, DSA, SM2, or ECC public key to the SSH server before logging in to it.

A key pair is created by the SSH server. After the public key in the key pair is transmitted to the STelnet client, the client modifies the key and allocates it to the server, so that the client can successfully perform a validity check on the server.

Perform the following steps on the SSH client:

![](../../../../public_sys-resources/note_3.0-en-us.png) 

For security purposes, you are advised not to use the RSA algorithm with a key length of less than 3072 bits. Using RSA\_SHA2\_256 and RSA\_SHA2\_512 algorithms for higher security is recommended.



#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. (Optional) Run the [**ssh client publickey**](cmdqueryname=ssh+client+publickey) { **dsa** | **ecc** | **rsa** | **sm2** | **rsa\_sha2\_256** | **rsa\_sha2\_512** } \* command to enable the corresponding public key algorithm on the SSH client.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The algorithms specified using **dsa** and **rsa** in the command are weak security algorithms, which are not recommended. To use such an algorithm, run the undo crypto weak-algorithm disable command to enable the weak security algorithm function.
3. Perform any of the following operations based on the selected algorithm:
   
   
   * To enter the RSA public key view, run the [**rsa peer-public-key**](cmdqueryname=rsa+peer-public-key) *key-name* command.
   * To enter the DSA public key view, run the [**dsa peer-public-key**](cmdqueryname=dsa+peer-public-key) *key-name* **encoding-type** *enc-type* command.
   * To enter the ECC public key view, run the [**ecc peer-public-key**](cmdqueryname=ecc+peer-public-key) *key-name* command.
   * To enter the SM2 public key view, run the [**sm2 peer-public-key**](cmdqueryname=sm2+peer-public-key) *key-name* command.
4. Run the [**public-key-code begin**](cmdqueryname=public-key-code+begin) command to access the public key editing view.
5. Enter *hex-data* to edit the public key.
   
   
   
   The public key must be a hexadecimal string complying with the public key format. It is generated randomly on the SSH server.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After entering the public key editing view, you can copy the RSA, DSA, SM2, or ECC public key generated on the server to the SSH client.
6. Run the [**public-key-code end**](cmdqueryname=public-key-code+end) command to exit the public key editing view.
   
   
   
   If the configured public key contains invalid characters or does not comply with encoding rules, an error message is displayed, and the configured public key is discarded. If the configured public key is valid, it is saved to the client's public key chain table.
   
   * If the value of *hex-data* is invalid, key generation fails after you perform this step.
   * If *key-name* specified in [Step 2](#EN-US_TASK_0172360082__step_1) has been deleted in another window, the system displays an error message and returns to the system view when you perform this step.
7. Run the [**peer-public-key end**](cmdqueryname=peer-public-key+end) command to exit the public key view and return to the system view.
8. Perform any of the following operations based on the selected algorithm:
   
   
   * Run the [**ssh client peer**](cmdqueryname=ssh+client+peer) *server-name* **assign rsa-key** *key-name* command to assign an RSA public key to the SSH server.
   * Run the [**ssh client peer**](cmdqueryname=ssh+client+peer) *server-name* **assign dsa-key** *key-name* command to assign a DSA public key to the SSH server.
   * Run the [**ssh client peer**](cmdqueryname=ssh+client+peer) *server-name* **assign ecc-key** *key-name* command to assign an ECC public key to the SSH server.
   * Run the [**ssh client peer**](cmdqueryname=ssh+client+peer) *server-name* **assign sm2-key** *key-name* command to assign an SM2 public key to the SSH server.
9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.