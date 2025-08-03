ssh client hmac
===============

ssh client hmac

Function
--------



The **ssh client hmac** command configures HMAC authentication algorithms on an SSH client.

The **undo ssh client hmac** command restores the default HMAC authentication algorithms on an SSH client.



By default,

* When the device starts with no configuration, the SSH client uses the following HMAC authentication algorithms: SHA2\_512 and SHA2\_256.
* When a device starts with a loaded configuration file (for example, a configuration file is loaded using ZTP for initial configuration), the SSH client uses MD5, MD5\_96, SHA2\_512, SHA1, SHA1\_96, SHA2\_256, and SHA2\_256\_96 as HMAC-based authentication algorithms.


Format
------

**ssh client hmac** { **md5** | **md5\_96** | **sha1** | **sha1\_96** | **sha2\_256** | **sha2\_256\_96** | **sha2\_512** | **sm3** } \*

**undo ssh client hmac**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **md5** | Specifies an HMAC MD5 authentication algorithm. | - |
| **md5\_96** | Specifies an HMAC MD5\_96 algorithm. | - |
| **sha1** | Specifies an HMAC SHA1 algorithm. | - |
| **sha1\_96** | Specifies an HMAC SHA1\_96 algorithm. | - |
| **sha2\_256** | Specifies an HMAC SHA1 algorithm. This algorithm is recommended. | - |
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

To configure HMAC authentication algorithms on an SSH client, run the **ssh client hmac** command. The SSH client and server negotiate authentication algorithms for the packets exchanged between them. During negotiation, the client sends its authentication algorithms to the server. After comparing the received authentication algorithms with local ones, the server selects the first matching authentication algorithm received for packet transmission. If no matching authentication algorithm is found, the negotiation fails.

**Precautions**

* For security purposes, you are advised to use the HMAC algorithm sha2\_512 or sha2\_256.
* This command applies to both IPv4 and IPv6.
* The algorithms specified by md5, md5\_96, sha1, sha1\_96, and sha2\_256\_96 parameters in this command can be used only after the weak security algorithm/protocol feature package (WEAKEA) is installed using the **install feature-software WEAKEA** command.


Example
-------

# Configure an HMAC SHA2\_256 authentication algorithm.
```
<HUAWEI> system-view
[~HUAWEI] ssh client hmac sha2_256

```