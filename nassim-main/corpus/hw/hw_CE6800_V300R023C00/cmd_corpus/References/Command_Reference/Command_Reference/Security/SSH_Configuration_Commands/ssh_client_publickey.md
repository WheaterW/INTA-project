ssh client publickey
====================

ssh client publickey

Function
--------



The **ssh client publickey** command enables the public key algorithm function of the SSH client.

The **undo ssh client publickey** command restores all the public key algorithms of the SSH client to default settings.



By default, ECC, RSA\_SHA2\_256, and RSA\_SHA2\_512 public key algorithms are enabled.

When the device starts with factory settings, the RSA\_SHA2\_256 and RSA\_SHA2\_512 public key algorithms are enabled.


Format
------

**ssh client publickey** { **dsa** | **ecc** | **rsa** | **sm2** | **rsa\_sha2\_256** | **rsa\_sha2\_512** | **x509v3-ssh-rsa** | **x509v3-rsa2048-sha256** } \*

**undo ssh client publickey**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dsa** | Indicates the DSA algorithm. | - |
| **ecc** | Indicates the ECC algorithm. | - |
| **rsa** | Indicates the RSA algorithm. | - |
| **sm2** | Indicates the SM2 algorithm. | - |
| **rsa\_sha2\_256** | Indicates the RSA SHA2-256 algorithm. | - |
| **rsa\_sha2\_512** | Indicates the RSA SHA2-512 algorithm. | - |
| **x509v3-ssh-rsa** | Indicates the X509 RSA algorithm. | - |
| **x509v3-rsa2048-sha256** | Indicates the X509-RSA-SHA2-256 algorithm. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* This command enables you to use a more secure public key algorithm when logging in to the device, while rejects other public key algorithms, thereby improving device security. The RSA\_SHA2\_256 and RSA\_SHA2\_512 public key algorithms are recommended.
* To allow a public key algorithm and reject other public key algorithms, run the **ssh client publickey** command and specify the specific public key algorithm in the command. For example, after the ssh client publickey ecc command is run, the ECC public key algorithm is allowed and the DSA, RSA, SM2, and other public key algorithms are rejected. If this command is run multiple times, the latest configuration overrides the previous one.

**Precautions**

* When a device boots with factory defaults, the RSA\_SHA2\_256 and RSA\_SHA2\_512 public key algorithms are enabled.
* When a device loads the configuration file on startup (for example, the device loads the configuration file using ZTP for initial configuration), and the configuration file does not include the **ssh client publickey** command, the ECC, RSA\_SHA2\_256, and RSA\_SHA2\_512 public key algorithms are enabled.
* A public key algorithm can be used for login only after it is enabled on both the client and server.
* The **undo ssh client publickey** command restores all the public key algorithms of the SSH client to default settings, with no parameters.
* If the **ssh client first-time enable** command is run, a message is displayed asking you to save the server's public key when a client attempts to log in to the server. When the save operation is performed, the SSH client automatically selects a public key algorithm that can ensure successful negotiation with the SSH client among all the public key algorithms configured using the **ssh client publickey** command, and allocates the selected algorithm to the SSH server.
* If the function corresponding to the **ssh client first-time enable** command is disabled, you must run the **ssh client peer assign** command to allocate a public key algorithm to the SSH server. Ensure that the SSH server can use the allocated public key algorithm to successfully negotiate with the SSH client for which a public key algorithm has been configured using the **ssh client publickey** command. In this way, the SSH client can pass the public key authentication by the SSH server.
* This command takes effect for both IPv4 and IPv6 clients.
* The dsa and rsa parameters in this command can be used only after the weak security algorithm/protocol feature package (WEAKEA) is installed using the **install feature-software WEAKEA** command.
* For security purposes, do not use the RSA algorithm with the key length fewer than 3072 bits. The more secure algorithms, RSA\_SHA2\_256 and RSA\_SHA2\_512, are recommended.


Example
-------

# Allow using of the ECC algorithm and deny other algorithms.
```
<HUAWEI> system-view
[~HUAWEI] ssh client publickey ecc

```

# Allow using of the SM2 algorithm and deny other algorithms.
```
<HUAWEI> system-view
[~HUAWEI] ssh client publickey sm2

```