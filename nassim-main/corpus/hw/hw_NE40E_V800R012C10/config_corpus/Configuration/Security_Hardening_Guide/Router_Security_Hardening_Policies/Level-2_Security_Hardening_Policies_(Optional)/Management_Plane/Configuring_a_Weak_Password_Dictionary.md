Configuring a Weak Password Dictionary
======================================

You can load a weak password dictionary for a device to verify newly configured weak passwords. Creating weak passwords is not allowed, thereby reducing the risk of brute force cracking.

#### Security Policy

* A weak password dictionary file can be loaded.
* A weak password dictionary file can be unloaded.
* The list of weak passwords can be queried.

#### Attack Methods

An attacker attacks the device and use the administrator rights to clear the weak password dictionary.


#### Configuration and Maintenance Methods

* Load a weak password dictionary file.
  ```
  <HUAWEI> load security weak-password-dictionary wkpass.txt
  ```
* Unload a weak password dictionary file.
  ```
  <HUAWEI> unload security weak-password-dictionary
  ```

#### Configuration and Maintenance Suggestions

* You are advised to upload the weak password dictionary file to the device and load it as required.
* You are advised to periodically update the weak password dictionary file to reduce risks.

#### Verifying the Security Hardening Result

Run the **display security weak-password-dictionary** command to query the list of weak passwords.