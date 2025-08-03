pki ldap-server-template
========================

pki ldap-server-template

Function
--------



The **pki ldap-server-template** command configures the device to download the CA certificate, local certificate, or CRL through LDAP.




Format
------

**pki ldap-server-template** *template-name* **attribute** *attr-value* *save-name* **dn** *dn-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **attribute** *attr-value* | Specifies the attribute value used by the device to obtain a certificate or CRL from the LDAP server. | The value is a string of 1 to 64 case-sensitive characters. |
| *save-name* | Specifies the name of a CA certificate, local certificate, or CRL saved on the flash of the device. | The value is a string of 1 to 64 case-sensitive characters, spaces not supported. The file name extension is .pem, .crt, .cer, or .crl. |
| **dn** *dn-value* | Specifies the DN used by the device to obtain a certificate or CRL from the LDAP server. | The value is a string of 1 to 128 characters. It cannot contain spaces. |
| **ldap-server-template** *template-name* | Specifies the name of an LDAP server template. | The value must be an existing LDAP server template name. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Note the following points when configuring a device to download a CA certificate, local certificate, or CRL through LDAP, the flash of the device has enough space for accommodating the CA certificate, local certificate, or CRL file to avoid downloading failed.

**Prerequisites**

An LDAP server template has been created using the **ldap-server template** command.


Example
-------

# Reference the LDAP server template user1 to download certificate ca.cer whose attribute value is cACertificate and DN is admin.
```
<HUAWEI> system-view
[~HUAWEI] ldap-server template user1
[*HUAWEI-ldap-user1] commit
[*HUAWEI-ldap-user1] quit
[~HUAWEI] pki ldap-server-template user1 attribute cACertificate;binary ca.cer dn admin

```