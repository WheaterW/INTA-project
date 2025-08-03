Keychain Fundamentals (for Non-TCP Applications)
================================================

A keychain itself manages just the encryption and authentication keys, and only takes effect when used in applications.

An application needs to bind a keychain before using keychain authentication. For example, if an application binds KeychainA, the application can use the keys in KeychainA for encryption and decryption.

#### Encryption Process

**Figure 1** Encryption process for a non-TCP application using keychain authentication  
![](figure/en-us_image_0000001176742381.png)
![](public_sys-resources/note_3.0-en-us.png) 

If an application does not obtain an active send key from the keychain, the application cannot use keychain authentication when sending packets. That is, packets are sent without being encrypted.



#### Decryption Process

**Figure 2** Decryption process for a non-TCP application using keychain authentication  
![](figure/en-us_image_0000001130782718.png)
![](public_sys-resources/note_3.0-en-us.png) 

* The purpose of the decryption process is not to decrypt packets; rather, the device re-encrypts packets and checks whether the new encryption result is the same as the received old decryption result. If so, the decryption is successful.
* Keychain authentication in IS-IS is special. During the decryption, an IS-IS application does not provide a key ID. Instead, the keychain searches all active accept keys and uses the one with the same algorithm for decryption.