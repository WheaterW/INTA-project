Configuring a Keychain
======================

Configuring a Keychain

#### Context

To implement TCP-AO on a device, a TCP-AO needs to be associated with the authentication algorithm, authentication key string, and lifetime of a key in a keychain. Therefore, before configuring a TCP-AO, you need to configure a keychain and a key for the keychain.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**keychain**](cmdqueryname=keychain) *keychain-name* **mode** { **absolute** | **periodic** { **daily** | **weekly** | **monthly** | **yearly** } } command to create a keychain and enter its view.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When creating a keychain, a time mode must be specified. However, if the desired keychain has been created, you can directly run the [**keychain**](cmdqueryname=keychain) *keychain-name* command to enter the keychain view, without specifying a time mode.
3. Run the [**receive-tolerance**](cmdqueryname=receive-tolerance) { *value* | **infinite** } command to set a tolerance time for the keychain.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   By default, the tolerance time is 0, indicating no tolerance.
   
   You are advised to set the tolerance time to prevent packet loss caused by clock jitters. The recommended setting is 5 minutes.
4. (Optional) Run the [**time mode**](cmdqueryname=time+mode) { **lmt** | **utc** } command to set a time mode for the keychain.
5. Run the [**key-id**](cmdqueryname=key-id) *key-id* command to create a key and enter the key ID view.
6. Run the [**algorithm**](cmdqueryname=algorithm) { **md5** | **sha-1** | **hmac-md5** | **hmac-sha1-12** | **hmac-sha1-20** | **hmac-sha-256** | **sha-256** | **sm3** | **aes-128-cmac** | **hmac-sha-384** | **hmac-sha-512** } command to configure an authentication algorithm for the key.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are advised not to specify **md5** or **sha-1**.
7. Run the [**key-string**](cmdqueryname=key-string) { *plain-cipher-text* | **plain** *plain-text* | **cipher** *plain-cipher-text* } command to configure an authentication key string (a character string used for encryption) for the key.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters excluding question marks (?) and spaces.
   
   For security purposes, you are advised to use the **cipher** mode. In this mode, the configured key is displayed in ciphertext in the configuration file.
8. Run any of the following commands to configure a lifetime for the key:
   
   
   
   **Table 1** Configuring a lifetime for the key
   | Time Mode of the Keychain | Command for Configuring a Lifetime for a Key |
   | --- | --- |
   | Absolute time mode: **absolute** | [**send-time**](cmdqueryname=send-time) *start-time* *start-date* { **duration** { *duration-value* | **infinite** } | { **to** *end-time* *end-date* } } |
   | Periodic mode (daily): **periodic** **daily** | [**send-time daily**](cmdqueryname=send-time+daily) **start-time** **to** **end-time** |
   | Periodic mode (weekly): **periodic** **weekly** | [**send-time day**](cmdqueryname=send-time+day) { **start-day** **to** **end-day** | **start-day** *&<1-7>* } |
   | Periodic mode (monthly): **periodic** **monthly** | [**send-time date**](cmdqueryname=send-time+date) { **start-date** **to** **end-date** | **start-date** *&<1-31>* } |
   | Periodic mode (yearly): **periodic** **yearly** | [**send-time month**](cmdqueryname=send-time+month) { **start-month** **to** **end-month** | **start-month** *&<1-12>* } |
9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.