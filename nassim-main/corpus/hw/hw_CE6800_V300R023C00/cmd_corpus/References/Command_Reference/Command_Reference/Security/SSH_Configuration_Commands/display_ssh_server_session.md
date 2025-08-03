display ssh server session
==========================

display ssh server session

Function
--------



The **display ssh server session** command displays the session information of the SSH server.




Format
------

**display ssh server session**


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

After configuring the SSH attributes, you can run the display ssh server command to view the current session of the SSH server.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display SSH server session.
```
<HUAWEI> display ssh server session
--------------------------------------------------------------------------------
Session                                 : 1
Connect type                            : VTY 0
Version                                 : 2.0
State                                   : Started
Username                                : root123
Retry                                   : 1
Client to Server cipher                 : aes256-ctr
Server to Client cipher                 : aes256-ctr
Client to Server HMAC                   : hmac-sha2-256
Server to Client HMAC                   : hmac-sha2-256
Client to Server compression            : zlib
Server to Client compression            : zlib
Key exchange algorithm                  : diffie-hellman-group-exchange-sha256
Public key                              : ECC
User authentication public key          : -
Service type                            : stelnet
Authentication type                     : password
Connection port number                  : 22
Idle time                               : 00:00:00
Total Packet Number                     : 117
Packet Number after Rekey               : 117
Total Data(MB)                          : 0
Data after Rekey(MB)                    : 0
Time after Session Established(Minute)  : 7
Time after Rekey(Minute)                : 7
Total self check random counts          : 72
Total self check random fails           : 0
Self check random result                : 0
Total self check keypair counts         : 1
Total self check keypair fails          : 0
Self check keypair result               : 0

--------------------------------------------------------------------------------

```

**Table 1** Description of the **display ssh server session** command output
| Item | Description |
| --- | --- |
| Session | Indicates the session ID. |
| Version | Indicates the protocol version of the SSH session. |
| State | Indicates the status of the SSH session. |
| Username | Indicates the username of the user for the session. |
| Retry | Indicates the number of retries. |
| Public key | Indicates the type of the public key. RSA\_SHA2\_512, RSA\_SHA2\_256, RSA, ECC, and DSA are supported currently.  To ensure better security, it is recommended that you use the more secure RSA SHA2-512 or RSA SHA2-256 authentication algorithm. |
| Key exchange algorithm | Indicates the name of the key exchange algorithm. |
| User authentication public key | Indicates the type of the public key used during user authentication. |
| Authentication type | Indicates the SSH user authentication type. The following are the authentication types:   * password. * rsa. * password-rsa. * all. * ecc. * password-ecc. * dsa. * password-dsa. * sm2. * password-sm2.   You are advised to use a more secure ECC authentication algorithm for higher security. |
| Service type | Indicates the SSH user service mode. There are three types of service modes:   * sftp. * stelnet. * snetconf. |
| Connection port number | Indicates the port number through which SSH session connections are established. |
| Idle time | Indicates the SSH session idle time. |
| Time after Session Established(Minute) | Indicates the connection duration after the SSH session connection is activated, in minutes. |
| Time after Rekey(Minute) | Indicates the connection duration after the SSH session connection is activated and the key is re-negotiated, in minutes. |
| Total Packet Number | Indicates the total number of SSH session packets. |
| Total Data(MB) | Indicates the total data volume of the SSH session connection, in MB. |
| Total self check random counts | Indicates the number of random number self-check times. |
| Total self check random fails | Indicates the number of random number self-check failures. |
| Total self check keypair counts | Indicates the number of key pair consistency check times. |
| Total self check keypair fails | Indicates the number of key pair consistency check failures. |
| Packet Number after Rekey | Indicates the total number of SSH session packets after key re-negotiation. |
| Data after Rekey(MB) | Indicates the total data volume of the SSH session connection after key re-negotiation, in MB. |
| Self check random result | Indicates the random number self-check result. |
| Self check keypair result | Indicates the result of the key pair consistency check. |
| Connect type | Indicates the interface of the VTY terminal used by the SSH session.   * VTY. * NCA. * SFTP. |
| Client to Server cipher | Indicates the name of the encryption algorithm from the client to the server. |
| Client to Server HMAC | Indicates the name of the HMAC algorithm from the client to the server. |
| Client to Server compression | Indicates the name of the compression algorithm from the client to the server. |
| Server to Client cipher | Indicates the name of the encryption algorithm from the server to the client. |
| Server to Client HMAC | Indicates the name of the HMAC algorithm from the server to the client. |
| Server to Client compression | Indicates the name of the compression algorithm from the server to the client. |