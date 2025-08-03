dldp authentication-mode
========================

dldp authentication-mode

Function
--------



The **dldp authentication-mode** command configures a DLDP authentication mode for DLDPDUs exchanged between the local port and the peer port.

The **undo dldp authentication-mode** command restores the default mode.



By default, DLDP are not authenticated.


Format
------

**dldp authentication-mode simple** *simplePassword*

**dldp authentication-mode md5** *md5Password*

**dldp authentication-mode sha** *shaPassword*

**dldp authentication-mode hmac-sha256** *hmacPassword*

**undo dldp authentication-mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **md5** *md5Password* | Uses MD5 mode to authenticate DLDPDUs exchanged between the local and peer ports.  For the sake of security, using the HMAC-SHA256 algorithm rather than the MD5 algorithm is recommended. | The value is a string of 1 to 16 non-cipher text characters or a string of 24, 32, 48, 108, or 128 ciphertext characters (excluding question marks). The value is case sensitive.  Ciphertext passwords with various lengths configured in an earlier version are also supported in the target version. |
| **sha** *shaPassword* | Uses SHA256 to authenticate DLDP packets exchanged between the local and peer interfaces.  To ensure high security, using the HMAC SHA256 algorithm instead of the SHA256 algorithm is recommended. | The value is a string of 1 to 16 non-cipher text characters or a string of 24, 32, 48, 108, or 128 ciphertext characters (excluding question marks). The value is case sensitive.  Ciphertext passwords with various lengths configured in an earlier version are also supported in the target version. |
| **hmac-sha256** *hmacPassword* | Uses HMAC-SHA256 mode to authenticate DLDPDUs exchanged between the local and peer ports. | The value is a string of 1 to 16 non-cipher text characters or a string of 24, 32, 48, 108, or 128 ciphertext characters (excluding question marks). The value is case sensitive. |
| **simple** *simplePassword* | Uses simple mode to authenticate DLDPDUs exchanged between the local and peer ports.   * The new password is at least eight characters long and contains at least two of the following types: upper-case letters, lower-case letters, digits, and special characters. * For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password. | The value is a string of 1 to 16 non-cipher text characters or a string of 24, 32, 48, 108, or 128 ciphertext characters (excluding question marks). The value is case sensitive.  Ciphertext passwords with various lengths configured in an earlier version are also supported in the target version. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent network attacks and malicious detection, you can run this command to configure DLDP packet authentication on an interface as follows:

* None authentication: The sender sets the authentication field to all 0s and the authentication type field to 0. The receiver compares the authentication key and authentication type in the DLDPDU with those configured on the local end. If they are different, the receiver discards the DLDPDU.
* Simple authentication: The device that sends DLDPDUs sets the authentication field to the non-cipher text authentication password and the authentication type field to 1. The receiver compares the authentication key and authentication type in the DLDPDU with those configured on the local end. If they are different, the receiver discards the DLDPDU.
* MD5 authentication: The sender sets the authentication field to the digest of the password encrypted using the MD5 algorithm, and sets the authentication type field to 2. The receiver compares the authentication key and authentication type in the DLDPDU with the digest of the local password encrypted using the MD5 algorithm and the local authentication type. If they are different, the receiver discards the DLDPDU.
* SHA authentication: The sender sets the authentication field to the digest of the password encrypted using the SHA256 algorithm, and sets the authentication type field to 3. The receiver compares the authentication key and authentication type in the DLDPDU with the digest of the local password encrypted using the SHA256 algorithm and the local authentication type. If they are different, the receiver discards the DLDPDU.
* HMAC SHA256 authentication: The sender sets the authentication field to the digest of the password encrypted using the HMAC SHA256 algorithm, and sets the authentication type field to 4. The receiver compares the authentication key and authentication type in the DLDPDU with the digest of the local password encrypted using the HMAC SHA256 algorithm and the local authentication type. If they are different, the receiver discards the DLDPDU. The HMAC SHA256 algorithm is recommended.

**Prerequisites**

DLDP has been enabled globally using the **dldp enable** command.

**Configuration Impact**

If DLDP on the ports on both ends or on one port is operating, the peer entries on both ends are removed to re-start a negotiation after the dldp authentication-mode command is run.

**Precautions**

If a DLDP authentication mode has been configured, ensure that the same DLDP authentication mode and password are configured on the ports on both ends connected by fiber pairs. Otherwise, DLDP authentication fails. DLDP can operate properly only when DLDPDUs are authenticated.


Example
-------

# Set the authentication mode between two devices to HMAC-SHA256 authentication and the authentication password to YsHsjx\_202206.
```
<HUAWEI> system-view
[~HUAWEI] dldp authentication-mode hmac-sha256 YsHsjx_202206

```