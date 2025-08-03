ntp authentication-keyid
========================

ntp authentication-keyid

Function
--------



The **ntp authentication-keyid authentication-mode** command sets the NTP verification key.

The **undo ntp authentication-keyid** command cancels the NTP verification key.



By default, no authentication key is set.


Format
------

**ntp authentication-keyid** *keyId* **authentication-mode** { **md5** | **hmac-sha256** | **aes-128-cmac** | **aes-256-cmac** } { *password* | **cipher** *password* }

**undo ntp authentication-keyid** *keyId*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **md5** | Indicates MD5 authentication.  The MD5 algorithm is insecure and is not recommended. You are advised to use other encryption algorithms for NTP key authentication. | - |
| **hmac-sha256** | Indicates HMAC-SHA256 authentication. | - |
| **aes-128-cmac** | Indicates AES-128-CMAC authentication. | - |
| **aes-256-cmac** | Indicates AES-256-CMAC authentication. | - |
| *password* | Sets an authentication password, which is in simple text.   * When password complexity-check is disabled: the new password is at least eight characters long and contains at least two of the following types: upper-case letters, lower-case letters, digits, and special characters. * When password complexity-check is enabled: the password must consist of at least 12 characters, and consist 4 types of characters, including lowercase letters, uppercase letters, digits, and special characters. * For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password. | If the password complexity check is enabled, the value is a string of 12 to 255 case-sensitive characters, spaces supported.  If the password complexity check is disabled, the value is a string of 1 to 255 case-sensitive characters, spaces supported.  In aes-128-cmac mode, the value is a string of case-sensitive characters, spaces supported. Its length is 16 in cleartext mode.  In AES-256-CMAC authentication mode, the value is a string of case-sensitive characters, spaces supported. Its length is 32 in cleartext mode. |
| **cipher** *password* | Sets a ciphertext authentication password. | The password is a string of case-sensitive characters, with spaces supported. A ciphertext password is a string of 20 to 432 characters. |
| **authentication-keyid** *keyId* | Authentication key number. | The value is an integer in the range from 1 to 4294967295. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On some networks that require high security, you need to enable the authentication function when running the NTP protocol. Password authentication on the client and server ensures that the client synchronizes only with the authenticated device, improving network security.

**Follow-up Procedure**



After the NTP verification key is configured, you need to run the **ntp trusted authentication-keyid** command to set the key to be reliable.



**Precautions**



If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command to the configuration file to disable the NTP server function. To enable the NTP server function, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file when you delete this command.The md5 parameter in this command can be used only after the weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.




Example
-------

# Set the HMAC-SHA256 authentication.
```
<HUAWEI> system-view
[~HUAWEI] ntp authentication-keyid 10 authentication-mode hmac-sha256 YsHsjx_202206

```