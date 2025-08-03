display pki realm
=================

display pki realm

Function
--------



The **display pki realm** command displays PKI realm information.




Format
------

**display pki realm** [ *realm-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **realm** *realm-name* | Displays the detailed information about a PKI realm.  If the parameter is left blank, information about all PKI realms is displayed. | The PKI realm name must already exist. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command displays details about a PKI realm, including PKI realm name, associated CA, CA certificate subject name, PKI entity name, digital fingerprint algorithm of CA certificate, and digital fingerprint of CA certificate.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the PKI realm abc.
```
<HUAWEI> system
[HUAWEI] pki realm abc
[HUAWEI-pki-realm-abc] q
[HUAWEI] display pki realm abc
 Total Number: 1

 Realm Name : abc
 CA ID: -
 CA Name: -
 Entity Name: -
 OCSP Nonce: Enable
 OCSP URL: -
 Method for Getting CRL: LDAP
 Certificate Revocation Check Method: -
 Key Type: -                                                                                                                    
 Key Name: -
 Password: -
 Key-usage: -
 Vpn-instance: -
 Source IP: -
 Enrollment-request Signature Message-digest-method: SHA256

```

**Table 1** Description of the **display pki realm** command output
| Item | Description |
| --- | --- |
| Total Number | Total count. |
| Realm Name | PKI realm name. It is configured using the pki realm (system view) command. |
| CA ID | ID of the CA associated with the PKI realm. It is configured using the ca-name command. |
| CA Name | Subject name of a CA certificate. |
| Entity Name | PKI entity name. It is configured using the entity command. |
| OCSP Nonce | Whether a nonce extension is added to the OCSP request sent by a PKI entity.   * Enable: A nonce extension is added to the OCSP request sent by a PKI entity. * Disable: A nonce extension is not added to the OCSP request sent by a PKI entity.   It is configured using the ocsp nonce enable command. |
| OCSP URL | OCSP server's URL. It is configured using the ocsp url command. |
| Method for Getting CRL | Method for getting CRL. |
| Certificate Revocation Check Method | Certificate status check method. It is configured using the certificate-check command. |
| Key Type | Key pair type. |
| Key Name | Key pair name. |
| Source IP | Source IP address used by the device to communicate with the PKI server. It is configured using the source command. |
| Enrollment-request Signature Message-digest-method | Digest method used for the enrollment request packet of signed certificate. It is configured using the enrollment-request signature message-digest-method command. |
| Password | Password used to apply for or revoke a certificate. It is configured using the password (PKI realm view) command. |
| Key-usage | Purpose information carried in a certificate request packet. It is configured using the key-usage command. |
| Vpn-instance | VPN to which the PKI realm is added. It is configured using the vpn-instance command. |