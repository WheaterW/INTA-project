Using STelnet to Log In to Another Device
=========================================

You can use STelnet to log in to an SSH server from an SSH client to configure and manage the server.

#### Context

You can log in to an SSH server from an SSH client without the need of specifying a listening port number only when the listening port number of the server is 22. Otherwise, a listening port number must be specified.

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
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
6. According to the status of the connection between the SSH client and server and the type of the source IP address, run one of the following commands in the user or system view:
   
   
   * If the Layer 3 network connection is normal and the source address is an IPv4 one:
     
     Run the [**stelnet**](cmdqueryname=stelnet)[ **-a***source-ip-address* ] [ **-force-receive-pubkey** ] *host-ip-address* [ *server-port* ] [ [ **prefer\_kex***prefer\_kex* ] | [ **prefer\_ctos\_cipher***prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac***prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac***prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress zlib** ] | [ **prefer\_stoc\_compress zlib** ] | [ **-vpn-instance***vpn-instance-name* ] | [ **-ki***interval* ] | [ **-kc***count* ] | [ **identity-key***identity-key-type* ] | [ **user-identity-key***user-key* ] ] \* command to use STelnet to log in to the SSH server through the specified IPv4 address.
   * If the Layer 3 network connection is normal and the source address is an IPv6 one:
     
     Run the [**stelnet ipv6**](cmdqueryname=stelnet+ipv6)[ **-a** *source-ipv6-address* ] [ **-force-receive-pubkey** ] *host-ipv6-address* [ [ **public-net** | **-vpn-instance** *vpn-instance-name* ] | [ **-oi** { *interface-name* | *interface-type* *interface-number* } ] | [ *server-port* ] | [ **prefer\_kex** *prefer\_kex* ] | [ **prefer\_ctos\_cipher***prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac***prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac***prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress zlib** ] | [ **prefer\_stoc\_compress zlib** ] | [ **-ki** *interval* ] | [ **-kc** *count* ] | [ **identity-key***identity-key-type* ] | [ **user-identity-key***user-key* ] ] \* command to use STelnet to log in to the SSH server through the specified IPv6 address.
   * If the Layer 3 network connection is abnormal, the Layer 2 link is normal, and the source address is an IPv4 one:
     
     Run the [**stelnet -tunnel lldp**](cmdqueryname=stelnet+-tunnel+lldp)**-a***source-ip-address***-i** { *interface-type**interface-number* | *interface-name* } *host-ip-address*[ *server-port* ] [ [ **prefer\_kex** *prefer\_kex* ] | [ **prefer\_ctos\_cipher***prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac***prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac***prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress zlib** ] | [ **prefer\_stoc\_compress zlib** ] | [ **-ki** *interval* ] | [ **-kc** *count* ] | [ **identity-key***identity-key-type* ] | [ **user-identity-key***user-key* ] ] \* command to use STelnet to log in to the SSH server through the IPv4 address.
   * If the Layer 3 network connection is abnormal, the Layer 2 link is normal, and the source address is an IPv6 one:
     
     Run the [**stelnet ipv6 -tunnel lldp**](cmdqueryname=stelnet+ipv6+-tunnel+lldp)**-a***s**ource-ipv6-address***-i** { *interface-type**interface-number* | *interface-name* } *host-ipv6-address*[ *server-port* ] [ [ **prefer\_kex** *prefer\_kex* ] | [ **prefer\_ctos\_cipher***prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac***prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac***prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress zlib** ] | [ **prefer\_stoc\_compress zlib** ] | [ **-ki** *interval* ] | [ **-kc** *count* ] | [ **identity-key***identity-key-type* ] | [ **user-identity-key***user-key* ] ] \* command to use STelnet to log in to the SSH server through the IPv6 address.