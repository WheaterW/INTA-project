Enabling the STelnet Server Function
====================================

Enabling_the_STelnet_Server_Function

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

For security purposes, you are advised not to use the RSA algorithm with a key length of less than 3072 bits. Using RSA\_SHA2\_256 and RSA\_SHA2\_512 algorithms for higher security is recommended.



#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. (Optional) Run the [**ssh server publickey**](cmdqueryname=ssh+server+publickey) { **dsa** | **ecc** | **rsa** | **sm2** | **x509v3-ssh-rsa** | **rsa\_sha2\_256** | **rsa\_sha2\_512** } \* command to configure public key encryption algorithms for the SSH server.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The algorithms specified using **dsa** and **rsa** in the command are weak security algorithms, which are not recommended. To use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function.
3. (Optional) Configure the maximum number of key pairs. Perform any of the following operations based on the key in use:
   
   
   * Run the [**rsa key-pair maximum**](cmdqueryname=rsa+key-pair+maximum) *max-keys* command to configure the maximum number of RSA key pairs that can be created.
   * Run the [**dsa key-pair maximum**](cmdqueryname=dsa+key-pair+maximum) *max-keys* command to configure the maximum number of DSA key pairs that can be created.
   * Run the [**ecc key-pair maximum**](cmdqueryname=ecc+key-pair+maximum) *max-keys* command to configure the maximum number of ECC key pairs that can be created.
4. (Optional) Create an SSH server key pair through either of the following methods:
   
   
   * Method 1
     + If you do not have high requirements on system security, run the [**rsa local-key-pair create**](cmdqueryname=rsa+local-key-pair+create) command to create a local RSA key pair or the [**dsa local-key-pair create**](cmdqueryname=dsa+local-key-pair+create) command to create a local DSA key pair.
     + If you have high requirements on system security, run the [**ecc local-key-pair create**](cmdqueryname=ecc+local-key-pair+create) command to create a local ECC key pair.
     
     After a local key pair is generated, run any of the following commands to check the public key in the key pair:
     
     + Run the [**display rsa local-key-pair public**](cmdqueryname=display+rsa+local-key-pair+public) command to check the public key in the local RSA key pair.
     + Run the [**display dsa local-key-pair public**](cmdqueryname=display+dsa+local-key-pair+public) command to check the public key in the local DSA key pair.
     + Run the [**display ecc local-key-pair public**](cmdqueryname=display+ecc+local-key-pair+public) command to check the public key in the local ECC key pair.
   * Method 2
     + If you do not have high requirements on system security, run the [**rsa key-pair label**](cmdqueryname=rsa+key-pair+label) *label-name* command to create a local RSA key pair or the [**dsa key-pair label**](cmdqueryname=dsa+key-pair+label) *label-name* command to create a local DSA key pair.
     + If you have high requirements on system security, run the [**ecc key-pair label**](cmdqueryname=ecc+key-pair+label) *label-name* [ **modulus** *modulus-bits* ] command to create a local ECC key pair or the [**sm2 key-pair label**](cmdqueryname=sm2+key-pair+label) *label-name* command to create a local SM2 key pair.
     
     After the key pair is generated, run the [**ssh server assign**](cmdqueryname=ssh+server+assign) { **rsa-host-key** | **dsa-host-key** | **ecc-host-key** | **sm2-host-key** } *label-name* command to assign the key pair to the SSH server.
     
     If the authentication mode is set to X509v3-SSH-RSA, run the [**ssh server assign**](cmdqueryname=ssh+server+assign) **pki** *key-name* command to configure a PKI certificate for the SSH server.
     
     To check key pair information, perform any of the following operations as required:
     + Run the [**display rsa key-pair**](cmdqueryname=display+rsa+key-pair) [ **brief** | **label** *label-name* ] command to check RSA key pair information.
     + Run the [**display dsa key-pair**](cmdqueryname=display+dsa+key-pair) [ **brief** | **label** *label-name* ] command to check DSA key pair information.
     + Run the [**display ecc key-pair**](cmdqueryname=display+ecc+key-pair) [ **brief** | **label** *label-name* ] command to check ECC key pair information.
     + Run the [**display sm2 key-pair**](cmdqueryname=display+sm2+key-pair) [ **brief** | **label** *label-name* ] command to check SM2 key pair information.
5. Run the [**stelnet server enable**](cmdqueryname=stelnet+server+enable) command to enable the STelnet server function.
   
   
   
   Disabling the STelnet server function on the SSH server will disconnect all clients from the server.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The standard listening port number of the SSH protocol is 22. If the TCP listening function is disabled on the port, running the command will enable this function for IPv4 and IPv6 on the port.
6. (Optional) Run the [**ssh server security-banner disable**](cmdqueryname=ssh+server+security-banner+disable) command to disable the risk warning function triggered when the SSH server uses an insecure algorithm.
7. (Optional) Run the [**ssh server cipher**](cmdqueryname=ssh+server+cipher) { **des\_cbc** | **3des\_cbc** | **aes128\_cbc** | **aes192\_cbc** | **aes256\_cbc** | **aes128\_ctr** | **aes192\_ctr** | **aes256\_ctr** | **arcfour128** | **arcfour256** | **aes128\_gcm** | **aes256\_gcm** | **blowfish\_cbc** | **sm4\_cbc** | **sm4\_gcm** } \* command to configure encryption algorithms for the SSH server.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are advised to use secure algorithms aes192\_ctr, aes128\_gcm, aes256\_gcm, aes128\_ctr and aes256\_ctr.
   
   The algorithms specified using **des\_cbc**, **3des\_cbc**, **aes128\_cbc**, **aes256\_cbc**, **arcfour128**, **arcfour256**, **blowfish\_cbc**, **aes192\_cbc**, and **sm4\_cbc** in the command are weak security algorithms, which are not recommended. To use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function. To avoid security risks, you are advised to use a more secure algorithm.
8. (Optional) Run the [**ssh server hmac**](cmdqueryname=ssh+server+hmac) { **md5** | **md5\_96** | **sha1** | **sha1\_96** | **sha2\_256** | **sha2\_256\_96** | **sha2\_512** | **sm3** } \* command to configure HMAC authentication algorithms for the SSH server.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are advised to use HMAC algorithms SHA2\_256 and SHA2\_512.
   
   The algorithms specified using **md5**, **sha1**, and **sm3** in the command are weak security algorithms, which are not recommended. To use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function. To avoid security risks, you are advised to use a more secure algorithm.
9. (Optional) Run the [**ssh server key-exchange**](cmdqueryname=ssh+server+key-exchange) { **dh\_group14\_sha1** | **dh\_group1\_sha1** | **dh\_group\_exchange\_sha1** | **dh\_group\_exchange\_sha256** | **dh\_group16\_sha512** | **ecdh\_sha2\_nistp256** | **ecdh\_sha2\_nistp384** | **ecdh\_sha2\_nistp521** | **sm2\_kep** | **curve25519\_sha256** } \* command to configure a key exchange algorithm list for the SSH server.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are advised to use curve25519\_sha256 as the key exchange algorithm.
   
   The algorithms specified using **dh\_group\_exchange\_sha1**, **dh\_group1\_sha1**, and **dh\_group14\_sha1** in the command are weak security algorithms, which are not recommended. To use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function. To avoid security risks, you are advised to use a more secure algorithm.
10. (Optional) Run the [**ssh server dh-exchange min-len**](cmdqueryname=ssh+server+dh-exchange+min-len) *min-len* command to configure the minimum key length supported during Diffie-hellman-group-exchange key exchange with the SSH client.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    If the SSH client supports the Diffie-hellman-group-exchange key exchange algorithm with a length greater than 1024 bits, you are advised to run the [**ssh server dh-exchange min-len**](cmdqueryname=ssh+server+dh-exchange+min-len) command to set the minimum key length to 3072 bits to improve security.
11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.