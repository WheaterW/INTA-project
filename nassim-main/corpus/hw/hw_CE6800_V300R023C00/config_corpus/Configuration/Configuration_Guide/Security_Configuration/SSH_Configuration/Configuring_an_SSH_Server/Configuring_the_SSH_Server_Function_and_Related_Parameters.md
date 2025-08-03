Configuring the SSH Server Function and Related Parameters
==========================================================

Configuring the SSH Server Function and Related Parameters

#### Context

Configuring the SSH server function and related parameters includes the following tasks: generating a local key pair for the server; enabling the SSH server; and setting server parameters (such as the SSH server port number, interval for updating the SSH server key pair, SSH authentication timeout interval, and maximum number of SSH authentication retries).

![](public_sys-resources/note_3.0-en-us.png) 

* To ensure security, you are advised to periodically change the key.
* To ensure that the SSH algorithm negotiation is successful, the SSH client must support the key exchange algorithm, encryption algorithm, public key algorithm, and HMAC algorithm configured on the SSH server.
* For security purposes, do not use the RSA algorithm whose length is less than 3072 digits. You are advised to use the ECC authentication algorithm instead.


#### Procedure

1. Enter the system view.
   
   
   ```
   system-view
   ```
2. Generate a local key pair.
   
   
   
   **Method 1: Generate a local RSA, DSA, or ECC key pair.**
   
   * Generate a local RSA key pair.
     ```
     [rsa local-key-pair create](cmdqueryname=rsa+local-key-pair+create)
     ```
   * Generate a DSA key pair.
     ```
     [dsa local-key-pair create](cmdqueryname=dsa+local-key-pair+create)
     ```
   * Generate an ECC key pair.
     ```
     [ecc local-key-pair create](cmdqueryname=ecc+local-key-pair+create)
     ```
   
   After a key pair is generated, you can run the [**display**](cmdqueryname=display) [**rsa local-key-pair public**](cmdqueryname=rsa+local-key-pair+public), [**display dsa local-key-pair public**](cmdqueryname=display+dsa+local-key-pair+public), or [**display ecc local-key-pair public**](cmdqueryname=display+ecc+local-key-pair+public) command to view information about the RSA, DSA, or ECC public key in the local key pair.
   
   If you no longer need the local DSA or ECC key pairs, run the **[**dsa local-key-pair destroy**](cmdqueryname=dsa+local-key-pair+destroy)** or [**ecc local-key-pair destroy**](cmdqueryname=ecc+local-key-pair+destroy) command to destroy all the local DSA or ECC key pairs. After this command is run, the file that stores the corresponding keys on the device is cleared. Exercise caution when running this command.
   
   Destroy all the local DSA keys.
   
   **Method 2: Generate a labeled SM2, RSA, DSA, or ECC key pair.**
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   You can generate up to 20 key pairs by using this method. To enhance communication security, rotate between these key pairs at different periods. To limit the maximum number of key pairs that the device can generate, you can run the [**rsa key-pair maximum**](cmdqueryname=rsa+key-pair+maximum), [**dsa key-pair maximum**](cmdqueryname=dsa+key-pair+maximum), or [**ecc key-pair maximum**](cmdqueryname=ecc+key-pair+maximum) command.
   
   1. Generate a labeled RSA, DSA, SM2, or ECC key pair.
      * Generate a labeled RSA key pair.
        ```
        [rsa key-pair label](cmdqueryname=rsa+key-pair+label) label-name [ modulus modulus-bits ]
        ```
      * Generate a labeled DSA key pair.
        ```
        [dsa key-pair label](cmdqueryname=dsa+key-pair+label) label-name [ modulus modulus-bits ]
        ```
      * Generate a labeled ECC key pair.
        ```
        [ecc key-pair label](cmdqueryname=ecc+key-pair+label) label-name [ modulus modulus-bits ]
        ```
      * Generate a labeled SM2 key pair.
        ```
        [sm2 key-pair label](cmdqueryname=sm2+key-pair+label) label-name
        ```
   2. Assign a host key or PKI certificate to the SSH server.
      ```
      [ssh server assign](cmdqueryname=ssh+server+assign) { rsa-host-key key-name | dsa-host-key key-name | ecc-host-key key-name | sm2-host-key key-name | pki key-name } 
      ```
   
   By default, no key or PKI certificate is assigned to an SSH server.
   
   After the key pair is generated, you can run the [**display rsa key-pair**](cmdqueryname=display+rsa+key-pair) [ **brief** | **label** *label-name* ], [**display dsa key-pair**](cmdqueryname=display+dsa+key-pair) [ **brief** | **label** *label-name* ], [**display ecc key-pair**](cmdqueryname=display+ecc+key-pair) [ **brief** | **label** *label-name* ], **[**display sm2 key-pair**](cmdqueryname=display+sm2+key-pair)** [ **brief** | **label** *label-name* ] commands to view information about the labeled RSA, DSA, SM2, or ECC key pair.
3. Enable the public key algorithm for the SSH server.
   
   
   ```
   [ssh server publickey](cmdqueryname=ssh+server+publickey) { dsa | ecc | rsa | x509v3-ssh-rsa | rsa_sha2_256 | rsa_sha2_512 | sm2 | x509v3-rsa2048-sha256 } *
   ```
   
   By default:
   
   * When a device starts with the factory defaults, the RSA\_SHA2\_256 and RSA\_SHA2\_512 public key algorithms are enabled, whereas the SM2, RSA, ECC, DSA, X509-RSA-SHA2-256, and X509-SSH-RSA public key algorithms are disabled.
   * When a device starts with a configuration file which does not contain the **ssh server publickey** command configuration, the ECC, RSA, RSA\_SHA2\_256, RSA\_SHA2\_512, and DSA public key algorithms are enabled, but not X509-SSH-RSA, SM2, and X509-RSA-SHA2-256.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Parameters **dsa**, **rsa**, and **x509v3-ssh-rsa** in the command can be used only after the weak security algorithm/protocol feature package is installed by running the **install feature-software WEAKEA** command.
   
   To log in to the device using public key authentication, ensure that the public key algorithms enabled for the SSH server are the same as those configured for SSH users using the [**ssh user authentication-type**](cmdqueryname=ssh+user+authentication-type) command. Otherwise, login to the device fails.
4. Enable the SSH server function.
   
   
   * Enable the STelnet server function on the device.
     ```
     [stelnet](cmdqueryname=stelnet) [ ipv4 | ipv6 ] server enable
     ```
     
     By default, the STelnet service is disabled.
   * Enable the SFTP server function on the device.
     ```
     [sftp](cmdqueryname=sftp) [ ipv4 | ipv6 ] server enable
     ```
     
     By default, the SFTP service is disabled.
   * Enable the SCP server function on the device.
     ```
     [scp](cmdqueryname=scp) [ ipv4 | ipv6 ] server enable
     ```
     
     By default, the SCP service is disabled.
5. Configure the port number of the SSH server.
   
   
   ```
   [ssh](cmdqueryname=ssh) [ ipv4 | ipv6 ] server port port-number
   ```
   
   By default, the port number of an SSH server is 22.
   
   If a new port number is configured, the SSH server disconnects from all SSH clients and uses the new port number to establish connections. This is more secure as it prevents attackers from connecting to the server straight through the standard SSH port.
6. Enable the keepalive function on the SSH server.
   
   
   ```
   [undo ssh server keepalive disable](cmdqueryname=undo+ssh+server+keepalive+disable)
   ```
   
   By default, the keepalive function is enabled on an SSH server.
   
   When this function is enabled, the SSH server will respond to keepalive packets sent from the SSH client. If the SSH client does not receive any keepalive response packets from the SSH server, the client will disconnect from the server. This ensures that server resources are not wasted due to the client repeatedly attempting to reconnect.
7. (Optional) Configure extended attributes for the SSH server.
   
   
   1. Configure a key exchange algorithm list for the SSH server.
      ```
      [ssh server key-exchange](cmdqueryname=ssh+server+key-exchange) { dh_group_exchange_sha256 | dh_group_exchange_sha1 | dh_group1_sha1 | ecdh_sha2_nistp256 | ecdh_sha2_nistp384 | ecdh_sha2_nistp521 | sm2_kep | dh_group14_sha1 | dh_group16_sha512 | curve25519_sha256 } *
      ```
      
      By default, the SSH server uses dh\_group\_exchange\_sha256, dh\_group16\_sha512, and curve25519\_sha256.
      
      The client and server negotiate the key exchange algorithm for packet transmission. During this negotiation, the server compares the key exchange algorithm list sent by the client with its own, and selects the first algorithm that appears on both lists for packet transmission. If there are no matches, the negotiation fails.
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      * For security purposes, you are advised to use the curve25519\_sha256 key exchange algorithm.
      * Parameters **dh\_group\_exchange\_sha1**, **dh\_group1\_sha1**, **sm2\_kep**, and **dh\_group14\_sha1** in the command can be used only after the weak security algorithm/protocol feature package is installed using the **install feature-software WEAKEA** command.
   2. Configure the condition for renegotiating the SSH session key.
      ```
      [ssh server rekey](cmdqueryname=ssh+server+rekey) { data-limit data-limit | max-packet max-packet | time minutes } *
      ```
      To improve transmission security, the SSH server can initiate key renegotiation. If renegotiation fails, the SSH connection is terminated. By default, the SSH server triggers key renegotiation only when at least one of the following conditions is met:
      * The total data volume of packets transmitted using the current key reaches 1000 megabytes.
      * The total number of sent and received packets reaches 2147483648.
      * An SSH connection lasts for 60 minutes.
   3. Set the minimum key length supported during diffie-hellman-group-exchange key exchange between the SSH server and client.
      ```
      [ssh server dh-exchange min-len](cmdqueryname=ssh+server+dh-exchange+min-len) min-len
      ```
      By default, the minimum supported key length is 3072 bits when the SSH server uses the diffie-hellman-group-exchange key to exchange with clients. You are advised to set the minimum key length to 3072 bits to improve security.![](public_sys-resources/note_3.0-en-us.png) 
      
      Security risks exist if the minimum key length of the diffie-hellman-group-exchange algorithm is less than or equal to 2048 bits. In this case, you need to run the **install feature-software WEAKEA** command to install the weak security algorithm/protocol feature package (WEAKEA). You are advised to set the minimum key length to 3072 bits. This command takes effect for both IPv4 and IPv6 SSH servers.
   4. Configure an encryption algorithm list for the SSH server.
      ```
      [ssh server cipher](cmdqueryname=ssh+server+cipher) { des_cbc | 3des_cbc | aes128_cbc | aes256_cbc | aes128_ctr | aes256_ctr | arcfour128 | arcfour256 | aes192_cbc | aes192_ctr | aes128_gcm | aes256_gcm | blowfish_cbc | sm4_cbc | sm4_gcm } *
      ```
      By default, an SSH server supports the following encryption algorithms: AES128\_CTR, AES256\_CTR, AES192\_CTR, AES128\_GCM, and AES256\_GCM.![](public_sys-resources/note_3.0-en-us.png) 
      * For security purposes, you are advised to use the following encryption algorithms: AES256\_GCM, AES128\_GCM, AES256\_CTR, AES192\_CTR, and AES128\_CTR.
      * Parameters **blowfish\_cbc**, **des\_cbc**, **3des\_cbc**, **aes128\_cbc**, **aes256\_cbc**, **arcfour128**, **arcfour256**, **aes192\_cbc**, and **sm4\_cbc** in the command can be used only after the weak security algorithm/protocol feature package is installed using the **install feature-software WEAKEA** command.
   5. Configure an authentication algorithm list for the SSH server.
      ```
      [ssh server hmac](cmdqueryname=ssh+server+hmac) { md5 | md5_96 | sha1 | sha1_96 | sha2_256 | sha2_256_96 | sha2_512 | sm3 } *
      ```
      
      By default, an SSH server uses the HMAC authentication algorithm SHA2\_256 or SHA2\_512.
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      * For security purposes, you are advised to use the following HMAC algorithms: SHA2\_512 and SHA2\_256.
      * Parameters **md5**, **md5\_96**, **sha1**, **sha1\_96**, and **sha2\_256\_96** in the command can be used only after the weak security algorithm/protocol feature package is installed using the **install feature-software WEAKEA** command.
   6. Disable the function that triggers a warning when the SSH server uses an insecure algorithm.
      ```
      [ssh server security-banner disable](cmdqueryname=ssh+server+security-banner+disable)
      ```
      
      By default, the function that triggers a warning when the SSH server uses an insecure algorithm is enabled.
   7. Set the interval for updating a key pair.
      ```
      [ssh server rekey-interval](cmdqueryname=ssh+server+rekey-interval) hours
      ```
      
      By default, the interval for updating the key pair of an SSH server is 0, indicating that the key pair is never updated.
      
      After the interval for updating the SSH server key pair is set using this command, the SSH server will automatically update the key pair at the specified interval, thereby enhancing security.
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      
      Only SSH1.X supports this configuration.
   8. Set the SSH authentication timeout interval.
      ```
      [ssh server timeout](cmdqueryname=ssh+server+timeout) seconds
      ```
      
      By default, the SSH authentication timeout interval is 60 seconds.
      
      If you have not logged in successfully within the SSH authentication timeout interval, the current connection is terminated to ensure security.
   9. Set the maximum number of SSH authentication retries.
      ```
      [ssh server authentication-retries](cmdqueryname=ssh+server+authentication-retries) times
      ```
      
      By default, a maximum of three SSH authentication retries are supported.
      
      The number of SSH authentication retries is limited to prevent unauthorized access.
   10. Enable compatibility with earlier SSH versions.
       ```
       [ssh server compatible-ssh1x enable](cmdqueryname=ssh+server+compatible-ssh1x+enable)
       ```
       
       By default, the SSH server's compatibility with earlier versions is disabled.
       
       ![](public_sys-resources/note_3.0-en-us.png) 
       
       This command can be used only after the weak security algorithm/protocol feature package is installed using the **install feature-software WEAKEA** command.
   11. Configure an ACL.
       ```
       [ssh](cmdqueryname=ssh) [ ipv6 ] server acl { acl-number | acl-name }
       ```
       
       By default, no ACL is configured.
       
       An ACL is configured to determine which clients can log in to the current device through SSH.
   12. Set the minimum length of the RSA public key allowed for SSH server authentication.
       ```
       [ssh server rsa-key min-length](cmdqueryname=ssh+server+rsa-key+min-length) min-length-val
       ```
       
       By default, the minimum length of the RSA public key allowed for SSH server authentication is 512 bits.
8. Configure the source interface or source IP address for the SSH server.
   
   
   
   By default, no source interface or source IPv6 address is specified for an SSH server.
   
   * Configure the SSH server to use a specified interface as the source interface.
     
     ```
     [ssh server-source](cmdqueryname=ssh+server-source) -i interface-type interface-number
     ```
     
     By default, no source interface is configured for an SSH server.
   * Configure the SSH server to use all valid interfaces as the source interface.
     
     ```
     [ssh server-source](cmdqueryname=ssh+server-source) all-interface
     ```
   * Configure a source IPv6 address for the SSH server.
     
     ```
     [ssh ipv6 server-source](cmdqueryname=ssh+ipv6+server-source) -a ipv6-address [ -vpn-instance vpn-instance-name ]
     ```
     
     By default, no source interface or source IPv6 address is specified for an SSH server.
   * Configure the SSH server to use all valid interfaces using IPv6 addresses as the IPv6 source interface.
     
     ```
     [ssh ipv6 server-source](cmdqueryname=ssh+ipv6+server-source) all-interface
     ```![](public_sys-resources/note_3.0-en-us.png) 
   
   After the **ssh server-source** **all-interface** or **ssh ipv6 server-source** **all-interface** command is run, users can log in to the SSH server from all valid interfaces, posing system security risks. Exercise caution while running these two commands.
9. Configure the maximum number of connections that can be established between a single IP address and the SSH server.
   
   
   ```
   [ssh server ip-limit-session](cmdqueryname=ssh+server+ip-limit-session) limit-session-num
   ```
   
   By default, a maximum of 256 connections can be established on the SSH server using a single IP address.
10. Enable keyboard-interactive authentication on the SSH server.
    
    
    ```
    [ssh server authentication-type keyboard-interactive enable](cmdqueryname=ssh+server+authentication-type+keyboard-interactive+enable)
    ```
    
    By default, keyboard-interactive authentication is enabled on an SSH server.
    
    If an SSH user logs in to a device using password card authentication, keyboard-interactive authentication must be enabled for this user.
11. (Optional) Enable the client IP address locking function on the SSH server.
    
    
    ```
    [undo ssh server ip-block disable](cmdqueryname=undo+ssh+server+ip-block+disable)
    ```
    
    By default, the client IP address locking function is enabled on an SSH server.
    
    * When this function is enabled, locked IP addresses fail to pass authentication and are displayed in the [**display ssh server ip-block list**](cmdqueryname=display+ssh+server+ip-block+list) command output.
    * If this function is disabled, the [**display ssh server ip-block list**](cmdqueryname=display+ssh+server+ip-block+list) command does not display any previously locked IP addresses or IP addresses that fail to pass authentication.![](public_sys-resources/note_3.0-en-us.png) 
    
    If an SSH user fails authentication six consecutive times within 5 minutes, the user's IP address will be locked for 5 minutes. To unlock the IP address before the locking period elapses, run the [**activate ssh server ip-block ip-address**](cmdqueryname=activate+ssh+server+ip-block+ip-address) *ip-address* [ **vpn-instance** *vpn-name* ] command.
12. (Optional) Configure alarm generation and clearance thresholds as a number of SSH server login failures within a specified period.
    
    
    ```
    [ssh server login-failed threshold-alarm](cmdqueryname=ssh+server+login-failed+threshold-alarm) upper-limit report-times lower-limit resume-times period period-time
    ```
    
    By default, an alarm is generated when 30 or more login failures occur within 5 minutes, and the alarm is cleared when the number of login failures within 5 minutes falls below 20.
13. (Optional) Configure the DSCP priority of SSH packets.
    
    
    ```
    [ssh server dscp](cmdqueryname=ssh+server+dscp) value
    ```
    
    By default, the DSCP priority of SSH packets is 48.
14. (Optional) Enable the local port forwarding service on the SSH server.
    
    
    ```
    [ssh server tcp forwarding enable](cmdqueryname=ssh+server+tcp+forwarding+enable)
    ```
    
    By default, the local port forwarding service is disabled on the SSH server.
15. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```