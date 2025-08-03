Setting a Master Key
====================

A master key is used by a device to encrypt data, safeguarding data transmission. A fixed default master key is provided before device delivery. In actual network environments, the default master key may be stolen or cracked. Administrators can manually change master keys as required to improve data security.

#### Security Policy

* You can change the default master key to a user-defined master key, improving data security.
* You can clear a user-defined master key to restore the default master key.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If an administrator forgets a user-defined master key configured on a local device, other devices cannot have the same master key configured to communicate with the local device through an encrypted data channel. In this case, attempts to share configuration files between the devices and decrypt data on the devices fail.
* You can query the master key configuration to check whether the default master key or a user-defined master key is used.

#### Attack Methods

An attacker cracks the fixed default master key by analyzing a large number of encrypted data, causing device information leakage.


#### Configuration and Maintenance Methods

* Set a user-defined master key.
  ```
  <HUAWEI> set master-key
  Warning: This operation will automatically save configurations. Are you sure you want to perform it? [Y/N]:y
  Enter a new master key: 
  Confirm the new master key: 
  Warning: Keep the new master key well.
  Enter the user password: 
  Info: Operating, please wait for a moment.....
  Info: Operation succeeded.
  ```
* Enable the automatic update of the master key so that the system periodically generates a new master key, which is a string of 32 characters.
  ```
  <HUAWEI> system-view
  [HUAWEI] set master-key auto-update interval 5
  Warning: If automatic master key update is enabled, the configured master key will be cleared, and the system will automatically generate a master key. The configuration will be automatically saved when the master key is updated. Are you sure you want to continue? [Y/N]:y
  ```
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In scenarios where the automatic update of the master key is enabled, if you run the [**set master-key**](cmdqueryname=set+master-key) command to manually configure a master key, the system displays a message indicating that this operation will disable the automatic update.
* Clear historical master keys.
  ```
  <HUAWEI> clear master-key
  Warning: This operation will delete all historical master keys. Are you sure you want to perform it? [Y/N]:y
  Enter the user password:
  Info: Operating, please wait for a moment...done.
  Info: Operation succeeded.
  ```
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The [**clear master-key**](cmdqueryname=clear+master-key) command cannot clear the historical default master key. Instead, it can clear only historical master keys that are generated automatically or defined by users. After you clear historical master keys, only the configuration file generated based on the current master key can be properly decrypted. This means that the configuration files generated based on other historical master keys cannot be decrypted.

#### Verifying the Security Hardening Result

Run the **display master-key configuration** command to query the type of the master key.


#### Configuration and Maintenance Suggestions

* To ensure data security, you are advised to set a user-defined master key when using a device for the first time, preventing sensitive information leakage.
* To ensure key security, you are advised to periodically update the user-defined master key, preventing the master key from being stolen or cracked.