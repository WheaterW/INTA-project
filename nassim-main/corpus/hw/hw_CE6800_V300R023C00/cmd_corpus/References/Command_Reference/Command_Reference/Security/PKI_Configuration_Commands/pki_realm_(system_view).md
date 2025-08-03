pki realm (system view)
=======================

pki realm (system view)

Function
--------



The **pki realm** command creates a PKI realm and displays the PKI realm view, or displays the view of an existing PKI realm.

The **undo pki realm** command deletes a PKI realm.



By default, there is a PKI realm named default in the system, and this realm can be modified but cannot be deleted.


Format
------

**pki realm** *realm-name*

**undo pki realm** *realm-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *realm-name* | Specifies a PKI domain name. | The value is a string of 1 to 64 case-insensitive characters without spaces, question marks (?), and slashes (/). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A PKI realm is a set of identity information required when a PKI entity enrolls a certificate.

**Precautions**

A PKI realm configured on a device is unavailable to certificate authorities (CAs) or other devices.When a certificate is requested using a PKI realm, the system names the certificate file PKI realm name\_local.cer. Therefore, if you will use a created PKI realm to request certificates, ensure that the PKI realm name length is shorter than 50 characters, because a certificate file with a name longer than 64 characters cannot be saved on a storage device.


Example
-------

# Create a PKI realm abc.
```
<HUAWEI> system-view
[~HUAWEI] pki realm abc
[*HUAWEI-pki-realm-abc]

```