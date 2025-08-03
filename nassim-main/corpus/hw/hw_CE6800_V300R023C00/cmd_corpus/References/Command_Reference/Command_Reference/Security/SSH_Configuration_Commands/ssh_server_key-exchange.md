ssh server key-exchange
=======================

ssh server key-exchange

Function
--------



The **ssh server key-exchange** command configures a key exchange algorithm list on an SSH server.

The **undo ssh server key-exchange** command restores the default configuration.



The device starts without configuration. The key exchange algorithm is customized by the product. After the undo command is executed, the SSH server uses the dh\_group\_exchange\_sha256, dh\_group16\_sha512, and curve25519\_sha256 key exchange algorithms by default.


Format
------

**ssh server key-exchange** { **dh\_group\_exchange\_sha256** | **dh\_group\_exchange\_sha1** | **dh\_group1\_sha1** | **ecdh\_sha2\_nistp256** | **ecdh\_sha2\_nistp384** | **ecdh\_sha2\_nistp521** | **sm2\_kep** | **dh\_group14\_sha1** | **dh\_group16\_sha512** | **curve25519\_sha256** } \*

**undo ssh server key-exchange**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dh\_group\_exchange\_sha256** | Specifies that the Diffie-hellman-group-exchange-sha256 algorithm is contained in the key exchange algorithm list configured on the SSH server. | - |
| **dh\_group\_exchange\_sha1** | Specifies that the Diffie-hellman-group-exchange-sha1 algorithm is contained in the key exchange algorithm list configured on the SSH server. | - |
| **dh\_group1\_sha1** | Specifies that the Diffie-hellman-group1-sha1 algorithm is contained in the key exchange algorithm list configured on the SSH server. | - |
| **ecdh\_sha2\_nistp256** | Specifies that the Elliptic curve Diffie-hellman-sha2-nistp256 algorithm is contained in the key exchange algorithm list configured on the SSH server. | - |
| **ecdh\_sha2\_nistp384** | Specifies that the Elliptic curve Diffie-hellman-sha2-nistp384 algorithm is contained in the key exchange algorithm list configured on the SSH server. | - |
| **ecdh\_sha2\_nistp521** | Specifies that the Elliptic curve Diffie-hellman-sha2-nistp521 algorithm is contained in the key exchange algorithm list configured on the SSH server. | - |
| **sm2\_kep** | Specifies that the SuperMemo 2 Key Exchange Protocol algorithm is contained in the key exchange algorithm list configured on the SSH server. | - |
| **dh\_group14\_sha1** | Specifies that the Diffie-hellman-group14-sha1 algorithm is contained in the key exchange algorithm list configured on the SSH server. | - |
| **dh\_group16\_sha512** | Specifies that the Diffie-hellman-group16-sha512 algorithm is contained in the key exchange algorithm list configured on the SSH server. | - |
| **curve25519\_sha256** | Specifies that the Curve25519-sha256 algorithm is contained in the key exchange algorithm list configured on the SSH server. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The client and server negotiate the key exchange algorithm used for packet transmission. You can run the ssh client key-exchange command to configure a key exchange algorithm list on the SSH client. The SSH server compares the configured key exchange algorithm list with the counterpart sent by the client and then selects the first matched key exchange algorithm for packet transmission. If the key exchange algorithm list sent by the client does not match any algorithm in the key exchange algorithm list configured on the server, the negotiation fails.This command takes effect for both IPv4 and IPv6 SSH clients.

**Precautions**



To ensure high security, you are advised to use the more secure curve25519\_sha256 key exchange algorithm.Under the same security conditions, compared with the ECDH key exchange algorithm, the DH and DHE key exchange algorithms have higher CPU usage during negotiation. You are advised to use the ECDH-type key exchange algorithms ecdh\_sha2\_nistp256, ecdh\_sha2\_nistp384, ecdh\_sha2\_nistp521 and curve25519\_sha256.The dh\_group\_exchange\_sha1, dh\_group1\_sha1, and dh\_group14\_sha1 parameters in this command can be used only after the weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.




Example
-------

# Configure key exchange algorithm lists dh\_group\_exchange\_sha256 on the SSH server.
```
<HUAWEI> system-view
[~HUAWEI] ssh server key-exchange dh_group_exchange_sha256

```