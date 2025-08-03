Setting SSH Client Parameters
=============================

Setting SSH Client Parameters

#### Context

SSH client parameters include the interval for sending keepalive packets and the maximum number of keepalive packets sent by the SSH client.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the interval for sending keepalive packets on the SSH client.
   
   
   ```
   [ssh client keepalive-interval](cmdqueryname=ssh+client+keepalive-interval) seconds
   ```
   
   By default, the interval is 0 seconds, indicating that the SSH client does not send keepalive packets.
   
   If the interval for sending keepalive packets is set to 0 seconds, the configured maximum number of keepalive packets does not take effect.
   
   If the SSH client does not receive any data packets from the server within a certain period, the client will keep sending keepalive packets to the server after the period elapses, until the number of sent keepalive packets reaches the upper limit. If the client does not receive any keepalive response packet from the server, the client will disconnect from the server.
3. Set the maximum number of keepalive packets that can be sent by the SSH client.
   
   
   ```
   [ssh client keepalive-maxcount](cmdqueryname=ssh+client+keepalive-maxcount) count
   ```
   
   By default, the maximum number of keepalive packets that can be sent by an SSH client is 3.
   
   
   
   If the SSH client does not receive any data packets from the server within a certain period, the client will keep sending keepalive packets to the server after the period elapses, until the number of sent keepalive packets reaches the upper limit. If the client does not receive any keepalive response packet from the server, the client will disconnect from the server.
4. (Optional) Configure a key exchange algorithm list for the SSH client.
   
   
   ```
   [ssh client key-exchange](cmdqueryname=ssh+client+key-exchange) { dh_group_exchange_sha256 | dh_group_exchange_sha1 | dh_group1_sha1 | ecdh_sha2_nistp256 | ecdh_sha2_nistp384 | ecdh_sha2_nistp521 | sm2_kep | dh_group14_sha1 | dh_group16_sha512 | curve25519_sha256 } *
   ```
   
   By default, the SSH client uses dh\_group\_exchange\_sha256, dh\_group16\_sha512, and curve25519\_sha256.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * For security purposes, you are advised to use the curve25519\_sha256 key exchange algorithm.
   * Parameters **dh\_group\_exchange\_sha1**, **dh\_group1\_sha1**, **sm2\_kep**, and **dh\_group14\_sha1** in the command can be used only after the weak security algorithm/protocol feature package is installed using the **install feature-software WEAKEA** command.
5. (Optional) Configure the condition for renegotiating the SSH session key.
   
   
   ```
   [ssh client rekey](cmdqueryname=ssh+client+rekey) { data-limit data-limit | max-packet max-packet | time minutes } *
   ```
   To improve transmission security, the SSH client can initiate key renegotiation. If renegotiation fails, the SSH connection is terminated. By default, the SSH client triggers key renegotiation only when at least one of the following conditions is met:
   * The total data volume of packets transmitted using the current key reaches 1000 megabytes.
   * The total number of sent and received packets reaches 2147483648.
   * An SSH connection lasts for 60 minutes.
6. (Optional) Configure an encryption algorithm list for the SSH client.
   
   
   ```
   [ssh client cipher](cmdqueryname=ssh+client+cipher) { des_cbc | 3des_cbc | aes128_cbc | aes256_cbc | aes128_ctr | aes256_ctr | arcfour128 | arcfour256 | aes192_cbc | aes192_ctr | aes128_gcm | aes256_gcm | sm4_cbc | sm4_gcm } *
   ```
   By default:
   * When a device starts with no configuration, the SSH client supports the following encryption algorithms: AES256\_GCM, AES128\_GCM, AES256\_CTR, AES192\_CTR, and AES128\_CTR.
   * When a device functioning as an SSH client starts with a configuration file which does not contain the [**ssh client cipher**](cmdqueryname=ssh+client+cipher) command configuration, the SSH client supports the following encryption algorithms: AES128\_CTR, AES256\_CTR, AES192\_CTR, AES128\_GCM, and AES256\_GCM.
   ![](public_sys-resources/note_3.0-en-us.png) 
   * For security purposes, you are advised to use the following encryption algorithms: AES256\_GCM, AES128\_GCM, AES256\_CTR, AES192\_CTR, and AES128\_CTR.
   * Parameters **des\_cbc**, **3des\_cbc**, **aes128\_cbc**, **aes256\_cbc**, **arcfour128**, **arcfour256**, **aes192\_cbc**, and **sm4\_cbc** in the command can be used only after the weak security algorithm/protocol feature package is installed using the **install feature-software WEAKEA** command.
7. (Optional) Configure an authentication algorithm list for the SSH client.
   
   
   ```
   [ssh client hmac](cmdqueryname=ssh+client+hmac) { md5 | md5_96 | sha1 | sha1_96 | sha2_256 | sha2_256_96 | sha2_512 | sm3 } *
   ```
   By default:
   * When a device starts with no configuration, the SSH client supports the following HMAC authentication algorithms: SHA2\_512 and SHA2\_256.
   * When a device starts with a configuration file which does not contain the [**ssh client hmac**](cmdqueryname=ssh+client+hmac) configuration, the SSH client supports the following HMAC authentication algorithms: MD5, MD5\_96, SHA2\_512, SHA1, SHA1\_96, SHA2\_256, and SHA2\_256\_96.
   ![](public_sys-resources/note_3.0-en-us.png) 
   * For security purposes, you are advised to use the following HMAC algorithms: SHA2\_256 and SHA2\_512.
   * Parameters **md5**, **md5\_96**, **sha1**, **sha1\_96**, and **sha2\_256\_96** in the command can be used only after the weak security algorithm/protocol feature package is installed using the **install feature-software WEAKEA** command.
8. (Optional) Configure the DSCP priority of SSH packets.
   
   
   ```
   [ssh client dscp](cmdqueryname=ssh+client+dscp) value
   ```
   
   By default, the DSCP priority of SSH packets is 48.
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```