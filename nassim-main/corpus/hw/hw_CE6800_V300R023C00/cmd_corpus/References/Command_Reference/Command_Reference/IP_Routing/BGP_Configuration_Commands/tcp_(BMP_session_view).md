tcp (BMP session view)
======================

tcp (BMP session view)

Function
--------



The **tcp** command configures parameters for the TCP connection between the router and the monitoring server.

The **undo tcp** command restores the default configuration.



By default, no parameters are configured for TCP connections.


Format
------

**tcp connect port** *port-number* [ **password** **md5** *cipher-password* | **keychain** *keychain-name* ]

**undo tcp connect port** *port-number*

**undo tcp connect port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **password** | Specifies the authentication. | - |
| **md5** *cipher-password* | Specifies the authentication password for the TCP connection. | The value is a string of case-sensitive characters, spaces not supported. If the password is input in plaintext mode, the password length ranges from 1 to 255; if the password is input in ciphertext mode, the password length ranges from 20 to 432. When double quotation marks are used around the string, spaces are allowed in the string. |
| **keychain** *keychain-name* | Specifies the name of the Keychain authentication.  Before configuring this parameter, run the keychain command to create a keychain. Then, run the key-id, key-string, and algorithm commands to configure a key ID, a password, and an authentication algorithm for this keychain. Otherwise, the authentication will fail, and the BGP peer relationship fails to be established. | The value is a string of 1 to 47 case-insensitive characters. The string cannot contain question marks (?) or spaces. However, when double quotation marks ("") are used around the string, spaces are allowed in the string. |
| **connect** | Configures the device to initiate unsolicited TCP connection requests. | - |
| **port** *port-number* | BMP server port number of the TCP connection. | The value is an integer in the range from 1 to 65535. |



Views
-----

BMP session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To establish a BMP session and ensure the validity and security of the TCP connection, run the **tcp** command to configure parameters for the TCP connection between the router and the monitoring server. The configurable parameters are the TCP connection mode (whether the device initiates unsolicited TCP connection requests or accepts TCP connection requests), TCP connection port number, authentication password of the TCP connection or the name of the Keychain authentication..



**Precautions**



The encryption algorithm used for MD5 authentication poses security risks. Therefore, you are advised to use an authentication mode based on a more secure encryption algorithm.




Example
-------

# Configure parameters for the TCP connection between the router and the monitoring server.
```
<HUAWEI> system-view
[~HUAWEI] bmp
[*HUAWEI-bmp] bmp-session 10.1.1.1
[*HUAWEI-bmp-session-10.1.1.1] tcp connect port 5364

```