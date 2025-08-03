tcp-algorithm-id
================

tcp-algorithm-id

Function
--------



Using the **tcp-algorithm-id** command, you can specify TCP algorithm ids to represent algorithms supported by the keychain uniquely.

Using the **undo tcp-algorithm-id** command, you can restore the default values specified by Internet Assigned Numbers Authority (IANA).



By default, the algorithm IDs supported by IANA are used.


Format
------

**tcp-algorithm-id md5** *md5-algorithm-id*

**tcp-algorithm-id sha-1** *sha1-algorithm-id*

**tcp-algorithm-id hmac-md5** *hmac-md5-algorithm-id*

**tcp-algorithm-id hmac-sha1-12** *hmac-sha1-12-algorithm-id*

**tcp-algorithm-id hmac-sha1-20** *hmac-sha1-20-algorithm-id*

**tcp-algorithm-id hmac-sha-256** *hmac-sha-256-algorithm-id*

**tcp-algorithm-id sha-256** *sha-256-algorithm-id*

**tcp-algorithm-id sm3** *sm3-algorithm-id*

**tcp-algorithm-id hmac-sha-384** *hmac-sha-384-algorithm-id*

**tcp-algorithm-id hmac-sha-512** *hmac-sha-512-algorithm-id*

**undo tcp-algorithm-id md5**

**undo tcp-algorithm-id sha-1**

**undo tcp-algorithm-id hmac-md5**

**undo tcp-algorithm-id hmac-sha1-12**

**undo tcp-algorithm-id hmac-sha1-20**

**undo tcp-algorithm-id hmac-sha-256**

**undo tcp-algorithm-id sha-256**

**undo tcp-algorithm-id sm3**

**undo tcp-algorithm-id hmac-sha-384**

**undo tcp-algorithm-id hmac-sha-512**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *md5-algorithm-id* | Specifies the TCP algorithm ID representing the MD5 algorithm. | The value is of the character type. It ranges from 1 to 63, and the default value is 3. |
| **sha-1** | Indicates that SHA-1 is used for packet encryption and authentication.  To ensure high security, do not use the SHA-1 algorithm. | The length of the key is 20 bytes. |
| *sha1-algorithm-id* | Specifies the TCP algorithm ID representing the SHA-1 algorithm. | The value is of the character type. It ranges from 1 to 63, and the default value is 4. |
| **hmac-md5** | Indicates that HMAC-MD5 is used for packet encryption and authentication.  To ensure high security, do not use the HMAC-MD5 algorithm. | The length of the key is 16 bytes. |
| *hmac-md5-algorithm-id* | Specifies the TCP algorithm ID representing the HMAC-MD5 algorithm. | The value is of the character type. It ranges from 1 to 63, and the default value is 5. |
| **hmac-sha1-12** | Indicates that HMAC-SHA1-12 is used for packet encryption and authentication. | The length of the key is 12 bytes. |
| *hmac-sha1-12-algorithm-id* | Specifies the TCP algorithm ID representing the HMAC-SHA1-12 algorithm. | The value is of the character type. It ranges from 1 to 63, and the default value is 2. |
| **hmac-sha1-20** | Indicates that HMAC-SHA1-20 is used for packet encryption and authentication. | The length of the key is 20 bytes. |
| *hmac-sha1-20-algorithm-id* | Specifies the TCP algorithm ID representing the HMAC-SHA1-20 algorithm. | The value is of the character type. It ranges from 1 to 63, and the default value is 6. |
| **hmac-sha-256** | Indicates that HMAC-SHA-256 is used for packet encryption and authentication. | The length of the key is 32 bytes. |
| *hmac-sha-256-algorithm-id* | Specifies the TCP algorithm ID representing the HMAC-SHA-256 algorithm. | The value is of the character type. It ranges from 1 to 63, and the default value is 7. |
| **sha-256** | Indicates that SHA-256 is used for packet encryption and authentication. | The length of the key is 32 bytes. |
| *sha-256-algorithm-id* | Specifies the TCP algorithm ID representing the SHA-256 algorithm. | The value is of the character type. It ranges from 1 to 63, and the default value is 8. |
| **sm3** | Indicates that SM3 is used for packet encryption and authentication. | The length of the key is 32 bytes. |
| *sm3-algorithm-id* | Specifies the TCP algorithm ID representing the SM3 algorithm. | The value is of the character type. It ranges from 1 to 63, and the default value is 9. |
| **hmac-sha-384** | Indicates that HMAC-SHA-384 is used for packet encryption and authentication. | The key length is 48 bytes. |
| *hmac-sha-384-algorithm-id* | Specifies the TCP algorithm ID representing the HMAC-SHA-384 authentication algorithm. | The value is of the character type. It ranges from 1 to 63, and the default value is 11. |
| **hmac-sha-512** | Indicates that HMAC-SHA-512 is used for packet encryption and authentication. | The key length is 64 bytes. |
| *hmac-sha-512-algorithm-id* | Specifies the TCP algorithm ID representing the HMAC-SHA-512 authentication algorithm. | The value is of the character type. It ranges from 1 to 63, and the default value is 12. |
| **md5** | Indicates that MD5 is used for packet encryption and authentication.  To ensure high security, do not use the MD5 algorithm. | The length of the key is 16 bytes. |



Views
-----

Keychain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A keychain ensures a secure protocol packet transmission by changing the authentication algorithm and key dynamically. Packets to be transmitted over non-TCP and TCP connections are authenticated using the authentication and encryption algorithms corresponding to a key ID. The two connections differ in that the TCP connection needs to be authenticated to enhance the security.The TCP connection is authenticated using the authentication algorithm specified by the algorithm ID. The algorithm ID is not defined by the IANA. Different vendors use different algorithm IDs to identify authentication algorithms. When two devices of different vendors are connected, ensure that algorithm IDs configured on the two devices are identical.



**Prerequisites**



The authentication algorithm used to authenticate the TCP connection needs to be specified.



**Implementation Procedure**

The TCP authentication algorithm IDs configured for the two communication devices must be identical.The characteristics of each authentication algorithm are as follows:

* Message Digest 5 (MD5): generates a 128-bit message digest based on an entered message of any length.
* Secure Hash Algorithm 1 (SHA-1): generates a 160-bit message digest based on an entered message with the length of shorter than the 64th power of 2.
* Keyed-Hashing for Message Authentication-MD5 (HMAC-MD5): generates a 128-bit message digest based on a 512-bit message that is converted from an entered message of any length. If the length of the entered message is less than 512 bits, 0s are added to make up a 512-bit message. If the length of the entered message is greater than 512 bits, the message is converted into a 128-bit message through the MD5 algorithm. After that, 0s are added to make up a 512-bit message.
* HMAC-SHA1-12: generates a 160-bit message digest based on a 512-bit message that is converted from an entered message of any length. The most significant 96 bits (12 x 8) are used as the authentication code.
* HMAC-SHA1-20: generates a 160-bit message digest based on a 512-bit message that is converted from an entered message of any length. All the 160 bits are used as the authentication code.
* SHA-256: generates a 256-bit message digest based on an entered message with the length of shorter than the 64th power of 2.
* HMAC-SHA-256: generates a 256-bit message digest based on a 512-bit message that is converted from an entered message of any length. All the 256 bits are used as the authentication code.
* HMAC-SHA-384: generates a 384-bit message digest based on a 512-bit message that is converted from an entered message of any length. All the 384 bits are used as the authentication code.
* HMAC-SHA-512: generates a 512-bit message digest based on a 512-bit message that is converted from an entered message of any length. All the 512 bits are used as the authentication code.The calculation speed of MD5 is faster than that of SHA, whereas SHA is more secure than MD5. Compared with MD5 and SHA, HMAC is more secure, but slower in calculation. For security purposes, the MD5 and SHA-1 algorithms are not recommended.

**Precautions**



Each algorithm ID uniquely identifies an algorithm.




Example
-------

# Configure the hmac-sha-256 TCP algorithm-id as 1.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei mode absolute
[*HUAWEI-keychain-huawei] tcp-algorithm-id hmac-sha-256 1

```