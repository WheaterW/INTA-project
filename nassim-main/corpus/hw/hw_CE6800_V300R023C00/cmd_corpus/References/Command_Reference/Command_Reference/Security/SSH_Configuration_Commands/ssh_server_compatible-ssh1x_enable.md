ssh server compatible-ssh1x enable
==================================

ssh server compatible-ssh1x enable

Function
--------



The **ssh server compatible-ssh1x enable** command enables the earlier version-compatible function on an SSH server.

The **undo ssh server compatible-ssh1x enable** command disables the earlier version-compatible function on the SSH server.



By default, the earlier version-compatible function is disabled on an SSH server.


Format
------

**ssh server compatible-ssh1x enable**

**undo ssh server compatible-ssh1x enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The earlier version-compatible function of an SSH server is applicable to the protocol version negotiation between the client and server. The client negotiates the protocol version, by comparing its own protocol version with the received packet. When the client version is earlier than the server version, the client uses its own version; otherwise, the client uses the higher version. After a TCP connection is set up between the client and server, the SSH client starts to negotiate with the server on the protocol version by running which they can work normally.By comparing the protocol versions, the server determines whether to work with the client.

* If the client runs a protocol version that is earlier than 1.3 or later than 2.0, version negotiation fails and the server terminates the TCP connection with the client.
* If the client runs a protocol version that is between 1.3 and 1.99 (including V1.3), the SSH1.5 server module is established when the "compatibility configuration option" of SSH is SSH1.x-compatible. The system then proceeds with the SSH1.x process. The server terminates the TCP connection with the client when the "compatibility configuration option" of SSH is SSH1.x-incompatible.
* That is 1.99 or 2.0, the SSH2.0 server module is established. The system then proceeds with the SSH2.0 process.

**Precautions**

* If SSH1.3 and SSH1.5 are disabled, all clients connected in SSH1.X-compatible mode go offline.
* If the SSH protocol is enabled to be compatible with earlier versions, the system displays a message indicating that security risks exist.
* The SSHv1 service is insecure. You are advised to use the SSHv2 service with higher security.
* The configuration takes effect upon the next login.
* To ensure high security, you are advised to enable the SSH protocol of a later version.
* This command can be used only after the weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.
* When SSHv1 is used to establish a connection, algorithm negotiation is not performed after version negotiation, and the public key is directly verified.
* The SSHv1 public key algorithm supports only the RSA algorithm. The DES, 3DES, and BLOWFISH algorithms are supported.
* The key exchange algorithm, encryption algorithm, public key algorithm, and HMAC algorithm configured on the server do not take effect in SSHv1.


Example
-------

# Enable the compatibility with SSH 1.x version.
```
<HUAWEI> system-view
[~HUAWEI] ssh server compatible-ssh1x enable

```