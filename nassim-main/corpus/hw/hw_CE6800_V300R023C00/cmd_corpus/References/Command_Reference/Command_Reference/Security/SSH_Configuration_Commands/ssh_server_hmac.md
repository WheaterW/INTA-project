ssh server hmac
===============

ssh server hmac

Function
--------



The **ssh server hmac** command configures HMAC authentication algorithms on an SSH server.

The **undo ssh server hmac** command restores the default HMAC authentication algorithms on the SSH server.



By default, the SSH server supports these HMAC authentication algorithms: SHA2\_512 and SHA2\_256.


Format
------

**ssh server hmac** { **md5** | **md5\_96** | **sha1** | **sha1\_96** | **sha2\_256** | **sha2\_256\_96** | **sha2\_512** | **sm3** } \*

**undo ssh server hmac**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **md5** | Specifies an HMAC MD5 authentication algorithm. | - |
| **md5\_96** | Specifies an HMAC MD5\_96 authentication algorithm. | - |
| **sha1** | Specifies an HMAC SHA1 authentication algorithm. | - |
| **sha1\_96** | Specifies an HMAC SHA1\_96 authentication algorithm. | - |
| **sha2\_256** | Specifies an HMAC SHA2\_256 authentication algorithm. This algorithm is recommended. | - |
| **sha2\_256\_96** | Specifies an HMAC SHA2\_256\_96 authentication algorithm. | - |
| **sha2\_512** | Specifies an HMAC SHA2\_512 authentication algorithm. | - |
| **sm3** | Specifies an HMAC SM3 authentication algorithm. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To configure HMAC authentication algorithms on an SSH server, run the **ssh server hmac** command. The SSH client and server negotiate authentication algorithms for the packets exchanged between them. During negotiation, the client sends its authentication algorithms to the server. After comparing the received authentication algorithms with the local ones on the server, the server selects the first matching authentication algorithm received for packet transmission. If no matching authentication algorithm is found, the negotiation fails.

**Precautions**

* For security purposes, you are advised to use the HMAC algorithm sha2\_512 or sha2\_256.
* This command applies to both IPv4 and IPv6.
* The algorithms specified by md5, md5\_96, sha1, sha1\_96, and sha2\_256\_96 parameters in this command can be used only after the weak security algorithm/protocol feature package (WEAKEA) is installed using the **install feature-software WEAKEA** command.


Example
-------

# Configure HMAC SHA2\_256.
```
<HUAWEI> system-view
[~HUAWEI] ssh server hmac sha2_256

```