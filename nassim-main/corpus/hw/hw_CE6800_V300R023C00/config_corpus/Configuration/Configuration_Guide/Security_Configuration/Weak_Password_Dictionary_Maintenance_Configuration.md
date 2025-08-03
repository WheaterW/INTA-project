Weak Password Dictionary Maintenance Configuration
==================================================

Weak Password Dictionary Maintenance Configuration

#### Context

A weak password is a simple password that can be easily guessed or cracked within a short period of time. A device provides the weak password dictionary maintenance function to prevent security problems caused by simple passwords. You can configure a dictionary of prohibited passwords in advance and load it to the device. When a new user is added or a user password needs to be changed, the system will prevent the passwords in this dictionary from being used.

The weak password dictionary is stored as a text file and supports only the .txt format. Each line contains a password. The following is an example of the weak password dictionary **pwd\_dict.txt**.

```
Abcd@123
Huawei@123
Aaabb@321
Raatr@321
```

After a weak password dictionary is loaded, the password settings in the device login CLI, configuration file management, SNMP configuration, M-LAG configuration, AAA configuration, and system's master key configuration will be affected. For details, see the configuration precautions of these features and related command reference.


#### Licensing Requirements

The weak password dictionary is not under license control.


#### Hardware Requirements

All products support the weak password dictionary maintenance function.


#### Feature Limitations

Limitations on the content of the weak password dictionary file are as follows:

* The maximum size of a weak password file is 1 MB.
* Each weak password contains a maximum of 128 characters.
* A maximum of 1000 weak passwords can be loaded on the device.

#### Procedure

* Load a weak password dictionary.
  
  
  ```
  [load security weak-password-dictionary](cmdqueryname=load+security+weak-password-dictionary) filePath
  ```
  
  Before the loading, ensure that the weak password dictionary in .txt format has been uploaded to the device.
* Unload the weak password dictionary.
  
  
  ```
  [unload security weak-password-dictionary](cmdqueryname=unload+security+weak-password-dictionary)
  ```

#### Verifying the Configuration

Run the [**display security weak-password-dictionary**](cmdqueryname=display+security+weak-password-dictionary) command to check the weak passwords that are prohibited from being used on the device.