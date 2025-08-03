authentication-mode hmac-sha256 password
========================================

authentication-mode hmac-sha256 password

Function
--------



The **authentication-mode hmac-sha256 password** command configures the authentication mode and password for transmitting iNOF packets.



By default, no authentication mode or password is configured for transmitting iNOF packets.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**authentication-mode hmac-sha256 password** *passwd*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **password** *passwd* | Configures the authentication password. | The value is a string of 8 to 16 case-sensitive characters in plaintext or a string of 128 case-sensitive characters in ciphertext. The characters can be letters, symbols, or digits. When double quotation marks (") are used to include the string, spaces are allowed in the string. |



Views
-----

iNOF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To ensure secure transmission of iNOF packets in an iNOF system, you can configure the authentication mode and password for transmitting iNOF packets on iNOF devices. An iNOF device then can encapsulate authentication information into iNOF packets and send the packets to the peer device. The peer device accepts only iNOF packets that pass the authentication, improving the security and reliability of the iNOF system.The authentication mode for transmitting iNOF packets is HMAC-SHA256. The receiver uses the HMAC-SHA256 algorithm to encrypt the locally configured password and generates digest information. After receiving iNOF packets, the receiver compares the authentication key and authentication type in the packets with the digest information and the locally configured authentication type. If they are different, the receiver discards the packets.

**Precautions**

If you need to change the password, change the passwords of both the local and peer devices. Changing the password interrupts services for a short period of time. After the passwords of the two devices are changed to be the same, the two devices automatically re-establish the connection.


Example
-------

# Set the authentication mode of iNOF packets to HMAC-SHA256 and the authentication password to YsHsjx\_202206.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] authentication-mode hmac-sha256 password YsHsjx_202206

```