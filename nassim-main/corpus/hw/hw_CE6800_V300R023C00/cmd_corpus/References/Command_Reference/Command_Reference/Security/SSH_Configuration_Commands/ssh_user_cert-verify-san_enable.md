ssh user cert-verify-san enable
===============================

ssh user cert-verify-san enable

Function
--------



The **ssh user cert-verify-san enable** command enables SAN/CN verification.



By default, the system does not check whether the common name (CN) or subject alternative name (SAN) in the certificate contains the realm of the authenticated user.


Format
------

**ssh user** *user-name* **cert-verify-san** **enable**

**undo ssh user** *user-name* **cert-verify-san** **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-name* | Indicates the name of an SSH user. | The value is a string of 1 to 253 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To ensure security, the common name (CN) or subject alternative name (SAN) in the certificate is verified.

**Prerequisites**

Specifies a PKI realm for an SSH user.


Example
-------

# Enable SAN/CN authentication for SSH users.
```
<HUAWEI> system-view
[~HUAWEI] ssh user aa cert-verify-san enable

```