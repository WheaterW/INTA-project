Using SFTP to Log In to Another Device Functioning as an SSH Server
===================================================================

You can log in to an SSH server from an SSH client through SFTP.

#### Context

Similar to the commands used to enable an SSH client to log in to an SSH server through STelnet, the commands used to enable an SSH client to log in to an SSH server through SFTP allow you to specify a source address and select the key exchange algorithm, encryption algorithm, and HMAC algorithm.

Perform the following steps on the device that functions as an SSH client:


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. (Optional) Run the [**ssh client cipher**](cmdqueryname=ssh+client+cipher) { **des\_cbc** | **3des\_cbc** | **aes128\_cbc** | **aes192\_cbc** | **aes256\_cbc** | **aes128\_ctr** | **aes192\_ctr** | **aes256\_ctr** | **arcfour128** | **arcfour256** | **aes128\_gcm** | **aes256\_gcm** | **sm4\_cbc** | **sm4\_gcm** } \* command to configure encryption algorithms for the SSH client.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are advised to use secure algorithms AES128\_CTR, AES256\_CTR, AES192\_CTR, AES128\_GCM, and AES256\_GCM.
   
   The algorithms specified using **des\_cbc**, **3des\_cbc**, **aes128\_cbc**, **aes256\_cbc**, **arcfour128**, **arcfour256**, **aes192\_cbc**, and **sm4\_cbc** in the command are weak security algorithms, which are not recommended. To use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function. To avoid security risks, you are advised to use a more secure algorithm.
3. (Optional) Run the [**ssh client hmac**](cmdqueryname=ssh+client+hmac) { **md5** | **md5\_96** | **sha1** | **sha1\_96** | **sha2\_256** | **sha2\_256\_96** | **sha2\_512** | **sm3** } \* command to configure HMAC authentication algorithms for the SSH client.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are advised to use HMAC algorithms SHA2\_256 and SHA2\_512.
   
   The algorithms specified using **md5**, **md5\_96**, **sha1**, **sha1\_96**, and **sha2\_256\_96** in the command are weak security algorithms, which are not recommended. To use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function. To avoid security risks, you are advised to use a more secure algorithm.
4. (Optional) Run the [**ssh client key-exchange**](cmdqueryname=ssh+client+key-exchange) { **dh\_group14\_sha1** | **dh\_group1\_sha1** | **dh\_group\_exchange\_sha1** | **dh\_group\_exchange\_sha256** | **dh\_group16\_sha512** | **ecdh\_sha2\_nistp256** | **ecdh\_sha2\_nistp384** | **ecdh\_sha2\_nistp521** | **sm2\_kep** | **curve25519\_sha256** } \* command to configure a key exchange algorithm list for the SSH client.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are advised to use curve25519\_sha256 as the key exchange algorithm.
   
   The algorithms specified using **dh\_group\_exchange\_sha1**, **dh\_group1\_sha1**, and **dh\_group14\_sha1** in the command are weak security algorithms, which are not recommended. To use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function. To avoid security risks, you are advised to use a more secure algorithm.
5. Perform either of the following operations based on the network protocol:
   
   
   * For IPv4:
     
     Run the [**sftp**](cmdqueryname=sftp) [ **-a** *source-ip-address* ] [ **-force-receive-pubkey** ] *host-ip-address* [ *port-number* ] [ [ **prefer\_kex***prefer\_kex* ] | [ **prefer\_ctos\_cipher***prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac***prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac***prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress zlib** ] | [ **prefer\_stoc\_compress zlib** ] | [ **public-net** | **-vpn-instance***vpn-instance-name* ] | [ **-ki***interval* ] | [ **-kc***count* ] | [ **identity-key***identity-key-type* ] | [ **user-identity-key***user-key* ] ] \* command to log in to the SSH server using the specified IPv4 address through SFTP and enter the SFTP client view.
   * For IPv6:
     
     Run the [**sftp ipv6**](cmdqueryname=sftp+ipv6) [ **-force-receive-pubkey** ] [ **-a** *source-ipv6-address* ] *host-ipv6-address* [ [ [ **-vpn-instance** *vpn-instance-name* ] | **public-net** ] | [ **-oi** { *interface-name* | *interface-type* *interface-number* } ] [ *port-number* ] | [ **prefer\_kex** { *prefer\_kex* } ] | [ **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress** **zlib** ] | [ **prefer\_stoc\_compress** **zlib** ] | [ **-ki** *interval* ] | [ **-kc** *count* ] | [ **identity-key** *identity-key-type* ] | [ **user-identity-key** *user-key* ] ]\* command to log in to the SSH server using the specified IPv6 address through SFTP and enter the SFTP client view.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.