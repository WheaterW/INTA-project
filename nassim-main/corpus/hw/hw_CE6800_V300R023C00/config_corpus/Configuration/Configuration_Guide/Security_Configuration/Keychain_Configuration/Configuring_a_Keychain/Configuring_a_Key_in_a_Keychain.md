Configuring a Key in a Keychain
===============================

Configuring a Key in a Keychain

#### Context

After a keychain is created, you need to create and configure one or more keys as required for the keychain.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of a created keychain.
   
   
   ```
   [keychain](cmdqueryname=keychain) keychain-name
   ```
3. Create a key and enter the key view.
   
   
   ```
   [key-id](cmdqueryname=key-id) key-id
   ```
4. Configure the authentication algorithm of the key.
   
   
   ```
   [algorithm](cmdqueryname=algorithm) { md5 | sha-1 | hmac-md5 | hmac-sha1-12 | hmac-sha1-20 | hmac-sha-256 | sha-256 | sm3 | hmac-sha-384 | hmac-sha-512 }
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   MD5, HMAC-MD5, and SHA-1 algorithms are not recommended since they are less secure.
   
   Parameters ****md5**, **sha-1**,** **hmac-md5**, **hmac-sha1-12**, and **hmac-sha1-20** in this command can be used only after the weak security algorithm/protocol feature package is installed.
   
   For security purpose,you are not advised to use the weak security algorithm or weak security protocols provided by this feature. If you need to use the weak security algorithm or protocols, run the **install feature-software WEAKEA** command to install the weak security algorithm or protocol feature package WEAKEA. By default, the device provides the weak security algorithm or protocol feature package WEAKEA. For details about how to install or uninstall the feature package, see "Upgrade Maintenance Configuration" in Configuration Guide > System Management Configuration.
5. Configure the authentication key string of the key.
   
   
   ```
   [key-string](cmdqueryname=key-string) { plain-cipher-text | plain plain-text | cipher plain-cipher-text }
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   It is recommended that the password complies with the password complexity rule: The password is at least eight characters long and contains at least two of the following: uppercase letters, lowercase letters, digits, and special characters (excluding question marks and spaces).
   
   For security purposes, the **cipher** mode is recommended to ensure that the configured key string is displayed in ciphertext in the configuration file.
6. Configure the send lifetime of the key based on the configured keychain time mode, as described in [Table 1](#EN-US_TASK_0000001176742375__table33415683610).
   
   
   
   The lifetime of a key depends on clock synchronization.
   
   **Table 1** Configuring the send lifetime of a key
   | Keychain Time Mode | Command |
   | --- | --- |
   | **absolute** | [**send-time**](cmdqueryname=send-time) *start-time* *start-date* { **duration** { *duration-value* | **infinite** } | { **to** *end-time* *end-date* } } |
   | **periodic** **daily** | [**send-time daily**](cmdqueryname=send-time+daily) **start-time** **to** **end-time** |
   | **periodic** **weekly** | [**send-time day**](cmdqueryname=send-time+day) { **start-day** **to** **end-day** | **start-day** *&<1-7>* } |
   | **periodic** **monthly** | [**send-time date**](cmdqueryname=send-time+date) { **start-date** **to** **end-date** | **start-date** *&<1-31>* } |
   | **periodic** **yearly** | [**send-time month**](cmdqueryname=send-time+month) { **start-month** **to** **end-month** | **start-month** *&<1-12>* } |
7. Configure the accept lifetime of the key based on the configured keychain time mode, as described in [Table 2](#EN-US_TASK_0000001176742375__table1739263013719).
   
   
   
   The lifetime of a key depends on clock synchronization.
   
   **Table 2** Configuring the accept lifetime of a key
   | Keychain Time Mode | Command |
   | --- | --- |
   | **absolute** | [**receive-time**](cmdqueryname=receive-time) *start-time* *start-date* { **duration** { *duration-value* | **infinite** } | { **to** *end-time* *end-date* } } |
   | **periodic** **daily** | [**receive-time daily**](cmdqueryname=receive-time+daily) **start-time** **to** **end-time** |
   | **periodic** **weekly** | [**receive-time day**](cmdqueryname=receive-time+day) { **start-day** **to** **end-day** | **start-day** *&<1-7>* } |
   | **periodic** **monthly** | [**receive-time date**](cmdqueryname=receive-time+date) { **start-date** **to** **end-date** | **start-date** *&<1-31>* } |
   | **periodic** **yearly** | [**receive-time month**](cmdqueryname=receive-time+month) { **start-month** **to** **end-month** | **start-month** *&<1-12>* } |
8. (Optional) Configure the key as the default send key.
   
   
   ```
   [default send-key-id](cmdqueryname=default+send-key-id)
   ```
   
   Each keychain can have only one default send key.
9. (Optional) Configure the length of the digest after being encrypted using an authentication algorithm.
   
   
   ```
   [digest-length](cmdqueryname=digest-length) { hmac-sha1-20 | hmac-sha-256 | sha-256 } length
   ```
   
   The default digest length after encryption varies depending on the authentication algorithm:
   
   * HMAC-SHA1-20: 20 bytes
   * HMAC-SHA-256: 32 bytes
   * SHA-256: 32 bytes
10. Exit the key view.
    
    
    ```
    [quit](cmdqueryname=quit)
    ```
11. Exit the keychain view.
    
    
    ```
    [quit](cmdqueryname=quit)
    ```
12. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```