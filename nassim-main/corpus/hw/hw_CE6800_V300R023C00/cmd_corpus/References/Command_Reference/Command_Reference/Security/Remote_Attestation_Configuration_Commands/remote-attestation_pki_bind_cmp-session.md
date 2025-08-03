remote-attestation pki bind cmp-session
=======================================

remote-attestation pki bind cmp-session

Function
--------



The **remote-attestation pki bind cmp-session** command binds remote attestation to a PKI CMP session.

The **undo remote-attestation pki bind cmp-session** command unbinds remote attestation from a PKI CMP session.



By default, remote attestation is not bound to a PKI CMP session.


Format
------

**remote-attestation pki bind cmp-session** *session-name*

**undo remote-attestation pki bind cmp-session**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cmp-session** *session-name* | Specifies the PKI CMP session to be bound. | The value must be an existing CMP session name. |



Views
-----

Trust environment management


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Public Key Infrastructure (PKI) is a framework consisting of protocols and encryption algorithms. It provides multiple services, such as identity authentication, integrity protection, and confidentiality and access control.The remote attestation function uses the PKI authentication mechanism and attestation identity key (AIK) certificates to check the reliability of devices. Run the **remote-attestation pki bind cmp-session** command to bind remote attestation to the created PKI CMP session. Then, the device applies for a local attestation key (LAK) certificate from the specified CA server through the bound session.

**Prerequisites**

A PKI CMP session has been created using the **pki cmp session** command, and the **cmp-request origin-authentication-method signature** command has been run in the PKI CMP session view to set the authentication mode for CMPv2-based initial certificate application to signature authentication.

**Precautions**

Only HTM profiles support this command.


Example
-------

# Bind remote attestation to a PKI CMP session.
```
<HUAWEI> system-view
[~HUAWEI] trustem
[*HUAWEI-trustem] remote-attestation pki bind cmp-session lak-session

```