display ssh client session
==========================

display ssh client session

Function
--------



The **display ssh client session** command displays the session status information of the SSH client.




Format
------

**display ssh client session**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view current session connection information of the SSH client, run the display ssh client session command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display current status information about the SSH client.
```
<HUAWEI> display ssh client session
--------------------------------------------------------------------------
Session                                 : 1
Version                                 : 2.0
CTOS Cipher                             : aes256-ctr
STOC Cipher                             : aes256-ctr
CTOS Hmac                               : hmac-sha2-256
STOC Hmac                               : hmac-sha2-256
CTOS Compress                           : none
STOC Compress                           : none
Public Key                              : RSA_SHA2_512
User Authentication Public Key          : RSA_SHA2_512
Total Packet Number                     : 152
Packet Number after Rekey               : 152
Total Data(MB)                          : 0
Data after Rekey(MB)                    : 0
Time after Session Established(Minute)  : 2
Time after Rekey(Minute)                : 2
Total self check random counts          : 53
Total self check random fails           : 0
Self check random result                : 0
Total self check keypair counts         : 1
Total self check keypair fails          : 0
Self check keypair result               : 0
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display ssh client session** command output
| Item | Description |
| --- | --- |
| Session | SSH session ID. |
| Version | Version information of the protocol that the SSH session connection uses. |
| CTOS Cipher | Encryption algorithm from the client to the server. |
| CTOS Hmac | HMAC algorithm from the client to the server. |
| CTOS Compress | Compression algorithm from the client to the server. |
| STOC Cipher | Encryption algorithm from the server to the client. |
| STOC Hmac | HMAC algorithm from the server to the client. |
| STOC Compress | Compression algorithm from the server to the client. |
| Public Key | Indicates the type of the public key. |
| User Authentication Public Key | The type of public key used during user authentication. |
| Total Packet Number | Total number of SSH session packets. |
| Total Data(MB) | Total data volume of the SSH session connection, in MB. |
| Total self check random counts | Indicates total number of random number self-check times. |
| Total self check random fails | Indicates total number of random number self-check failures. |
| Total self check keypair counts | Indicates total number of key pair consistency tests. |
| Total self check keypair fails | Indicates total number of key pair consistency test failures. |
| Packet Number after Rekey | Total number of SSH session packets after key re-negotiation. |
| Data after Rekey(MB) | Total data volume of the SSH session connection after key re-negotiation, in MB. |
| Time after Session Established(Minute) | Connection duration after the SSH session connection is activated, in minutes. |
| Time after Rekey(Minute) | Connection duration after the SSH session connection is activated and the key is re-negotiated, in minutes. |
| Self check random result | Indicates the result of random number self-check. |
| Self check keypair result | Indicates the result of key pair self-check. |