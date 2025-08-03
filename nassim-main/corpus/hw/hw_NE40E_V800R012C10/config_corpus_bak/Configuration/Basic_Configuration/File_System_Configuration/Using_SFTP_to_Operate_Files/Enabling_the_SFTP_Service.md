Enabling the SFTP Service
=========================

Before using SFTP to access a device, enable the SFTP service on the device.

#### Context

Perform the following steps on the device to be used as an SSH server:

![](../../../../public_sys-resources/note_3.0-en-us.png) 

For security purposes, you are advised not to use the RSA algorithm with a key length of less than 3072 bits. Using RSA\_SHA2\_256 and RSA\_SHA2\_512 algorithms for higher security is recommended.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**ssh server publickey**](cmdqueryname=ssh+server+publickey) { **dsa** | **ecc** | **rsa** | **sm2** | **x509v3-ssh-rsa** | **rsa\_sha2\_256** | **rsa\_sha2\_512** } \*
   
   
   
   Public key encryption algorithms are configured for the SSH server.
3. (Optional) Configure the maximum number of key pairs. Perform any of the following operations based on the user requirements for system performance:
   
   
   * Run the [**rsa key-pair maximum**](cmdqueryname=rsa+key-pair+maximum) *max-keys* command to configure the maximum number of RSA key pairs that can be created.
   * Run the [**dsa key-pair maximum**](cmdqueryname=dsa+key-pair+maximum) *max-keys* command to configure the maximum number of DSA key pairs that can be created.
   * Run the [**ecc key-pair maximum**](cmdqueryname=ecc+key-pair+maximum) *max-keys* command to configure the maximum number of ECC key pairs that can be created.
4. (Optional) Select either of the following methods to create a key pair for an SSH server.
   
   
   * Method 1
     + If the user requirements for system security are not high, run the [**rsa local-key-pair create**](cmdqueryname=rsa+local-key-pair+create) command to configure a local RSA key pair or run the [**dsa local-key-pair create**](cmdqueryname=dsa+local-key-pair+create) command to configure a local DSA key pair.
     + If the user requirements for system security are high, run the [**ecc local-key-pair create**](cmdqueryname=ecc+local-key-pair+create) command to configure a local ECC key pair.
   * Method 2
     + If the user requirements for system security are not high, run the [**rsa key-pair label**](cmdqueryname=rsa+key-pair+label) *label-name* [ **modulus** *modulus-bits* ] command to configure a local RSA key pair or run the [**dsa key-pair label**](cmdqueryname=dsa+key-pair+label) *label-name* [ **modulus** *modulus-bits* ] command to configure a local DSA key pair.
     + If the user requirements for system security are high, run the [**ecc key-pair label**](cmdqueryname=ecc+key-pair+label) *label-name* [ **modulus** *modulus-bits* ] command to create a local ECC key pair , run the [**sm2 key-pair label**](cmdqueryname=sm2+key-pair+label) *label-name* [ **modulus** *modulus-bits* ] command to create local SM2 key pair .
     
     After keys are generated, run the [**ssh server assign**](cmdqueryname=ssh+server+assign) { **rsa-host-key** | **dsa-host-key** | **ecc-host-key** | **sm2-host-key**  } *key-name* command to assign a key pair to an SSH server.
     
     If the authentication mode is set to x509v3-ssh-rsa, run the [**ssh server assign**](cmdqueryname=ssh+server+assign) **pki** *pki-name* command to configure a PKI certificate for the SSH server.
5. Perform any of the following operations based on the SFTP service type:
   
   
   * Run the [**sftp server enable**](cmdqueryname=sftp+server+enable) command to enable the SFTP service.
   * Run the [**sftp ipv4 server enable**](cmdqueryname=sftp+ipv4+server+enable) command to enable the IPv4 SFTP service.
   * Run the [**sftp ipv6 server enable**](cmdqueryname=sftp+ipv6+server+enable) command to enable the IPv6 SFTP service.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   SSH uses port 22 to listen to packets. If the TCP listening function is disabled on the port, running this command will enable the TCP listening function for IPv4 and IPv6 on the port.
6. (Optional) Run [**ssh server cipher**](cmdqueryname=ssh+server+cipher) { **des\_cbc** | **3des\_cbc** | **aes128\_cbc** | **aes192\_cbc** | **aes256\_cbc** | **aes128\_ctr** | **aes192\_ctr** | **aes256\_ctr** | **arcfour128** | **arcfour256** | **aes128\_gcm** | **aes256\_gcm** | **blowfish\_cbc** | **sm4\_cbc** | **sm4\_gcm** } \*
   
   
   
   Encryption algorithms are configured for the SSH server.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are advised to use secure algorithms aes192\_ctr, aes128\_gcm, aes256\_gcm, aes128\_ctr and aes256\_ctr.
   
   The **des\_cbc**, **3des\_cbc**, **aes128\_cbc**, **aes256\_cbc**, **arcfour128**, **arcfour256**, **blowfish\_cbc**, **aes192\_cbc**, and **sm4\_cbc** algorithms in the command are weak security algorithms and are not recommended. To configure these algorithms, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function. To avoid security risks, you are advised to use a more secure algorithm.
7. (Optional) Run [**ssh server hmac**](cmdqueryname=ssh+server+hmac) { **md5** | **md5\_96** | **sha1** | **sha1\_96** | **sha2\_256** | **sha2\_256\_96** | **sha2\_512** | **sm3** } \*
   
   
   
   HMAC authentication algorithms are configured for the SSH server.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are advised to use HMAC algorithms sha2\_256 and sha2\_512.
   
   The algorithms specified using **md5**, **md5\_96**, **sha1**, **sha1\_96**, and **sha2\_256\_96** in the command are weak security algorithms, which are not recommended. To use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function. To avoid security risks, you are advised to use a more secure algorithm.
8. (Optional) Run [**ssh server key-exchange**](cmdqueryname=ssh+server+key-exchange) { **dh\_group14\_sha1** | **dh\_group1\_sha1** | **dh\_group\_exchange\_sha1** | **dh\_group\_exchange\_sha256** | **dh\_group16\_sha512** | **ecdh\_sha2\_nistp256** | **ecdh\_sha2\_nistp384** | **ecdh\_sha2\_nistp521** | **sm2\_kep** | **curve25519\_sha256** } \*
   
   
   
   A key exchange algorithm list is configured for the SSH server.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are advised to use curve25519\_sha256 as the key exchange algorithm.
   
   The algorithms specified using **dh\_group\_exchange\_sha1**, **dh\_group1\_sha1**, and **dh\_group14\_sha1** in the command are weak security algorithms, which are not recommended. To use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function. To avoid security risks, you are advised to use a more secure algorithm.
9. (Optional) Run [**ssh server dh-exchange min-len**](cmdqueryname=ssh+server+dh-exchange+min-len) *min-len*
   
   
   
   The minimum key length supported during Diffie-hellman-group-exchange key exchange with the SSH client is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the SSH client supports the Diffie-hellman-group-exchange key exchange algorithm with a length greater than 1024 bits, you are advised to run the [**ssh server dh-exchange min-len**](cmdqueryname=ssh+server+dh-exchange+min-len) command to set the minimum key length to 3072 bits to improve security.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

* Perform any of the following operations to view information about the locally generated key pair:
  + Run the [**display rsa key-pair**](cmdqueryname=display+rsa+key-pair) [ **brief** | **label** *label-name* ] command to view the RSA key pair information.
  + Run the [**display dsa key-pair**](cmdqueryname=display+dsa+key-pair) [ **brief** | **label** *label-name* ] command to view the DSA key pair information.
  + Run the [**display ecc key-pair**](cmdqueryname=display+ecc+key-pair) [ **brief** | **label** *label-name* ] command to view the ECC key pair information.
  + Run the [**display sm2 key-pair**](cmdqueryname=display+sm2+key-pair) [ **brief** | **label** *label-name* ] command to view the SM2 key pair information.
* After a local key pair is generated, perform any of the following operations to view the public key information in the key pair:
  + Run the [**display rsa local-key-pair public**](cmdqueryname=display+rsa+local-key-pair+public) command to view the RSA public key information.
  + Run the [**display dsa local-key-pair public**](cmdqueryname=display+dsa+local-key-pair+public) command to view the DSA public key information.
  + Run the [**display ecc local-key-pair public**](cmdqueryname=display+ecc+local-key-pair+public) command to view the ECC public key information.