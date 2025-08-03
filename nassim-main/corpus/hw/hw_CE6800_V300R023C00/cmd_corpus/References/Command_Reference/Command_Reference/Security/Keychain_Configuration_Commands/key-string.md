key-string
==========

key-string

Function
--------



Using the **key-string** command, you can specify a key-string that is used for encryption and decryption.

Using the **undo key-string** command, you can delete the key-string configuration.



By default, no key-string is configured.


Format
------

**key-string** *plain-cipher-text*

**key-string cipher** *plain-cipher-text*

**key-string plain** *plain-text*

**undo key-string**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *plain-cipher-text* | Indicates the cipher text used for authentication. | The value is a string of case-sensitive characters that can be letters or digits. The authentication password can be a string of 1 to 255 characters in simple text or a string of 20 to 432 characters in encrypted text. A 24-character ciphertext password configured in an earlier version is also supported in this version.  Except the question mark (?) and space. However, when quotation marks (") are used around the password, spaces are allowed in the password. |
| **cipher** | Specifies the key-string used for encryption and decryption. | - |
| **plain** *plain-text* | Indicates the simple text used for authentication. | The value is a string of 1 to 255 case-sensitive characters that can be letters or digits.  Except the question mark (?) and space. However, when quotation marks (") are used around the password, spaces are allowed in the password.  Select the ciphertext mode because the configured text is saved in the configuration file as a simple text if you select the simple text mode, which has a high risk. To ensure device security, change the password periodically. |



Views
-----

weekly Key-ID view,yearly Key-ID view,daily Key-ID view,monthly Key-ID view,absolute Key-ID view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In keychain authentication mode, secure protocol packet transmission is provided by changing the authentication algorithm and key dynamically. This can prevent unauthorized users from obtaining the key, and authentication and encryption algorithms, and reduce the workload of changing the algorithm and key manually.Each keychain consists of multiple key IDs that are valid within different time periods and each key ID is configured with an authentication algorithm. When a key ID becomes valid, the corresponding authentication algorithm is used.When configuring an authentication algorithm, configure a key for protocol packet authentication.



**Precautions**



An authentication key configured in cipher text mode will be displayed also in cipher text mode. Therefore, remember the plain-text key string when configuring the key in cipher text mode.If the authentication key is not configured, the corresponding key ID remains in the inactive state.




Example
-------

# Configure the key-string Huawei-13579.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei mode absolute
[*HUAWEI-keychain-huawei] key-id 1
[*HUAWEI-keychain-huawei-keyid-1] key-string cipher Huawei-13579

```