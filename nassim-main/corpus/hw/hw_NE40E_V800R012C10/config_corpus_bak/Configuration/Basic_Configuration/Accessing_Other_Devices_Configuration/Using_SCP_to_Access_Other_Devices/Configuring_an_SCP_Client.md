Configuring an SCP Client
=========================

After a secure connection is established between an SCP client and server through negotiation, the client can upload files to the server or download files from it.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. (Optional) Run the [**scp client-source**](cmdqueryname=scp+client-source) { **-a** *source-ip-address* [ **public-net** | **-vpn-instance** *vpn-instance-name* ] | **-i** { *interface-type* *interface-number* | *interface-name* } } or [**scp ipv6 client-source**](cmdqueryname=scp+ipv6+client-source) **-a** *ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ] command to configure a source address for the SCP client.
3. (Optional) Run the [**ssh client cipher**](cmdqueryname=ssh+client+cipher) { **des\_cbc** | **3des\_cbc** | **aes128\_cbc** | **aes192\_cbc** | **aes256\_cbc** | **aes128\_ctr** | **aes192\_ctr** | **aes256\_ctr** | **arcfour128** | **arcfour256** | **aes128\_gcm** | **aes256\_gcm** | **sm4\_cbc** | **sm4\_gcm** } \* command to configure encryption algorithms for the SSH client.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are advised to use secure algorithms AES128\_CTR, AES256\_CTR, AES192\_CTR, AES128\_GCM, and AES256\_GCM.
   
   The algorithms specified using **des\_cbc**, **3des\_cbc**, **aes128\_cbc**, **aes256\_cbc**, **arcfour128**, **arcfour256**, **aes192\_cbc**, and **sm4\_cbc** in the command are weak security algorithms, which are not recommended. To use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function. To avoid security risks, you are advised to use a more secure algorithm.
4. (Optional) Run the [**ssh client hmac**](cmdqueryname=ssh+client+hmac) { **md5** | **md5\_96** | **sha1** | **sha1\_96** | **sha2\_256** | **sha2\_256\_96** | **sha2\_512** | **sm3** } \* command to configure HMAC authentication algorithms for the SSH client.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are advised to use HMAC algorithms SHA2\_256 and SHA2\_512.
   
   The algorithms specified using **md5**, **md5\_96**, **sha1**, **sha1\_96**, and **sha2\_256\_96** in the command are weak security algorithms, which are not recommended. To use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function. To avoid security risks, you are advised to use a more secure algorithm.
5. Upload files to the remote SCP server or download files from it.
   
   
   * For IPv4:
     
     Run the [**scp**](cmdqueryname=scp) [ **-a** *source-ip-address* ] [ **-force-receive-pubkey** ] [ **-port** *port-number* | **public-net** | **vpn-instance** *vpn-instance-name* | **identity-key** *identity-key-type* | **user-identity-key** *user-key* | **-r** | **-c** | **-cipher** *cipher* | **-prefer-kex** *prefer-kex* ] \* *source-filename* *destination-filename* or [**scp**](cmdqueryname=scp) { **-i** *interface-name* | *interface-type interface-number* } [ **-force-receive-pubkey** ] [ **-port** *port-number* | **identity-key** *identity-key-type* | **user-identity-key** *user-key* | **-r** | **-c** | **-cipher** *cipher*| **-prefer-kex** *prefer-kex* ] \* *source-filename* *destination-filename* command.
   * For IPv6:
     
     Run the [**scp ipv6**](cmdqueryname=scp+ipv6) [ [ [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* ] | **public-net** ] [ **-force-receive-pubkey** ] [ [ **-port** *server-port* ] | [ **identity-key** *identity-key-type* ] | [ **user-identity-key** *user-key* ] | [ [ **-a** *source-ipv6-address* ] | [ **-oi** { *interface-name* | *interface-type* *interface-number* } ] ] | **-r** | **-c** | [ **-cipher** *cipher* ] | [ **-prefer-kex** { *prefer-kex* } ] ] \* *source-filename* *destination-filename* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are advised not to use the RSA algorithm with a key length of less than 3072 bits for SSH user authentication. Using the ECC authentication algorithm for higher security is recommended.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.