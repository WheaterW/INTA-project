algorithm
=========

algorithm

Function
--------



The **algorithm** command configures a key ID authentication algorithm.

The **undo algorithm** command deletes the configured key ID authentication algorithm.



By default, no algorithm is configured.


Format
------

**algorithm** { **md5** | **sha-1** | **hmac-md5** | **hmac-sha1-12** | **hmac-sha1-20** | **hmac-sha-256** | **sha-256** | **sm3** | **hmac-sha-384** | **hmac-sha-512** }

**undo algorithm**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **md5** | Indicates that MD5 is used for packet encryption and authentication.  To ensure high security, do not use the MD5 algorithm. | - |
| **sha-1** | Indicates that SHA-1 is used for packet encryption and authentication.  To ensure high security, do not use the SHA-1 algorithm. | - |
| **hmac-md5** | Indicates that HMAC-MD5 is used for packet authentication.  To ensure high security, do not use the HMAC-MD5 algorithm. | - |
| **hmac-sha1-12** | Indicates that HMAC-Secure Hash Algorithm 1-12 (SHA1-12) is used for packet encryption and authentication. | - |
| **hmac-sha1-20** | Indicates that HMAC-SHA1-20 is used for packet encryption and authentication. | - |
| **hmac-sha-256** | Indicates that HMAC-Secure Hash Algorithm-256 (SHA-256) is used for packet encryption and authentication.  HAMC-SHA-256 authentication mode is better and more secure than other authentication modes. To ensure high security, HAMC-SHA-256 authentication algorithm is recommended. | - |
| **sha-256** | Indicates that SHA-256 is used for packet encryption and authentication. | - |
| **sm3** | Indicates that SM3 is used for packet encryption and authentication. | - |
| **hmac-sha-384** | Indicates that HMAC-SHA-384 is used for packet authentication.  HMAC-SHA-384 authentication provides higher security than other authentication modes. To ensure high security, you are advised to use HMAC-SHA-384 for authentication. | - |
| **hmac-sha-512** | Indicates that HMAC-SHA-512 is used for packet authentication.  HMAC-SHA-512 authentication provides higher security than other authentication modes. To ensure high security, you are advised to use HMAC-SHA-512 for authentication. | - |



Views
-----

weekly Key-ID view,yearly Key-ID view,daily Key-ID view,monthly Key-ID view,absolute Key-ID view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A keychain ensures the security of application protocol packet transmission by dynamically changing the authentication algorithm and key string. A keychain consists of multiple key IDs, each of which needs to be configured with an authentication algorithm. Different key IDs are valid within different time periods, ensuring dynamic change of keychain authentication algorithms.Protocol packets are authenticated and encrypted based on the authentication algorithm associated with a specified key ID, improving the packet transmission security.The characteristics of each authentication algorithm are as follows:

* Message Digest 5 (MD5): generates a 128-bit message digest based on an entered message of any length.
* Secure Hash Algorithm 1 (SHA-1): generates a 160-bit message digest based on an entered message with the length of shorter than the 64th power of 2.
* Keyed-Hashing for Message Authentication-MD5 (HMAC-MD5): generates a 128-bit message digest based on a 512-bit message that is converted from an entered message of any length. If the length of the entered message is less than 512 bits, 0s are added to make up a 512-bit message. If the length of the entered message is greater than 512 bits, the message is converted into a 128-bit message through the MD5 algorithm. After that, 0s are added to make up a 512-bit message.
* HMAC-SHA1-12: generates a 160-bit message digest based on a 512-bit message that is converted from an entered message of any length. The most significant 96 bits (12 x 8) are used as the authentication code.
* HMAC-SHA1-20: generates a 160-bit message digest based on a 512-bit message that is converted from an entered message of any length. All the 160 bits are used as the authentication code.
* SHA-256: generates a 256-bit message digest based on an entered message with the length of shorter than the 64th power of 2.
* HMAC-SHA-256: generates a 256-bit message digest based on a 512-bit message that is converted from an entered message of any length. All the 256 bits are used as the authentication code.
* SM3: generates a 256-bit message digest based on an entered message with the length of shorter than the 64th power of 2.
* HMAC-SHA-384: generates a 384-bit message digest based on a 512-bit message that is converted from an entered message of any length. All the 384 bits are used as the authentication code.
* HMAC-SHA-512: generates a 512-bit message digest based on a 512-bit message that is converted from an entered message of any length. All the 512 bits are used as the authentication code.The calculation speed of MD5 is faster than that of SHA, whereas SHA is more secure than MD5. Compared with MD5 and SHA, HMAC is more secure, but slower in calculation. For security purposes, the MD5 and SHA-1 algorithms are not recommended.

**Prerequisites**



Key IDs have been configured.



**Precautions**



Key IDs configured on the sender and receiver of packets must correspond to the same authentication and encryption algorithms. Otherwise, packet transmission fails for not passing the authentication.If no authentication algorithm is configured, the key ID remains inactive.The md5, sha-1, hmac-md5, hmac-sha1-12, and hmac-sha1-20 parameters can be used only after the weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.




Example
-------

# Configure algorithm HMAC-SHA-256 on key-id 1.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei mode absolute
[*HUAWEI-keychain-huawei] key-id 1
[*HUAWEI-keychain-huawei-keyid-1] algorithm hmac-sha-256

```