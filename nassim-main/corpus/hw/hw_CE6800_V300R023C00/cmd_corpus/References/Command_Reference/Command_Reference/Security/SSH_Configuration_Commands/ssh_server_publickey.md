ssh server publickey
====================

ssh server publickey

Function
--------



The **ssh server publickey** command enables the public key algorithm function of the SSH server.

The **undo ssh server publickey** command restores all the public key algorithms of the SSH server to the default public key algorithms RSA\_SHA2\_256 and RSA\_SHA2\_512.



By default, ECC, RSA\_SHA2\_256, and RSA\_SHA2\_512 public key algorithms are enabled.

When the device starts with factory settings, the RSA\_SHA2\_256 and RSA\_SHA2\_512 public key algorithms are enabled.


Format
------

**ssh server publickey** { **dsa** | **ecc** | **rsa** | **sm2** | **x509v3-ssh-rsa** | **rsa\_sha2\_256** | **rsa\_sha2\_512** | **x509v3-rsa2048-sha256** } \*

**undo ssh server publickey**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dsa** | Indicates the DSA algorithm. | - |
| **ecc** | Indicates the ECC algorithm. | - |
| **rsa** | Indicates the RSA algorithm. | - |
| **sm2** | Indicates the SM2 algorithm. | - |
| **x509v3-ssh-rsa** | Indicates the X509-SSH-RSA algorithm. | - |
| **rsa\_sha2\_256** | Indicates the RSA SHA2-256 algorithm. | - |
| **rsa\_sha2\_512** | Indicates the RSA SHA2-512 algorithm. | - |
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

* You can run this command to configure a more secure public key algorithm for device login and deny other public key algorithms, improving device security. RSA\_SHA2\_256 and RSA\_SHA2\_512 public key algorithms are recommended.
* Run the ssh server publickey + specified public key algorithm command to allow the use of this public key algorithm and deny the use of other public key algorithms. For example, ssh server publickey dsa indicates that the DSA algorithm can be used and other algorithms cannot be used. If you run this command multiple times, only the latest configuration takes effect.
* To ensure high security, do not use the RSA algorithm whose length is less than 3072 bits as the authentication mode for SSH users. You are advised to use the RSA\_SHA2\_256 or RSA\_SHA2\_512 authentication algorithm, which is more secure.
* If the public key algorithm specified for the SSH server is X509V3-SSH-RSA or X509V3-RSA2048-SHA256, run the ssh server assign pki <pki-keyname> command to bind the SSH server to a PKI realm.

**Precautions**

* For security purposes, you are advised to use the following algorithms with higher security: ecc, rsa\_sha2\_256, and rsa\_sha2\_512.
* A public key algorithm can be used for login only after it is enabled on both the client and server.
* The **undo ssh server publickey** command restores all the public key algorithms of the SSH server to default settings, with no parameters.
* If the authentication mode of SSH users is set to public key authentication using the **ssh user** command, the public key algorithm must be the same as that enabled in this command; otherwise, users cannot log in to the device. For example, if the ssh server publickey ecc command is run, you need to run the ssh user <user-name> authentication-type { ecc | password-ecc | all } command to set the authentication mode of SSH users to ECC, Password-ECC, or ALL.
* This command takes effect for both IPv4 and IPv6 clients.
* The dsa and rsa parameters in this command can be used only after the weak security algorithm/protocol feature package (WEAKEA) is installed using the **install feature-software WEAKEA** command.
* When a device starts with factory defaults, the RSA\_SHA2\_256 and RSA\_SHA2\_512 public key algorithms are enabled.


Example
-------

# Allow using of the ECC algorithm and deny other algorithms.
```
<HUAWEI> system-view
[~HUAWEI] ssh server publickey ecc

```

# Allow using of the SM2 algorithm and deny other algorithms.
```
<HUAWEI> system-view
[~HUAWEI] ssh server publickey sm2

```

# Allow using of the x509v3-ssh-rsa algorithm and deny other algorithms.
```
<HUAWEI> system-view
[~HUAWEI] ssh server publickey x509v3-ssh-rsa

```