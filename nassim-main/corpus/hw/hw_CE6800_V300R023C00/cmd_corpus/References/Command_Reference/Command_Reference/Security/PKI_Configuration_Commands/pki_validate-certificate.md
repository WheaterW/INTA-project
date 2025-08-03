pki validate-certificate
========================

pki validate-certificate

Function
--------



The **pki validate-certificate** command allows you to verify the validity of a CA certificate or a local certificate.




Format
------

**pki validate-certificate** { **ca** | **local** } { **realm** *realm-name* | **filename** *file-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ca** | Checks validity of the CA certificate. | - |
| **local** | Checks validity of the local certificate. | - |
| **realm** *realm-name* | Specifies the PKI realm name of a certificate to be checked. | The value must be an existing PKI realm name. |
| **filename** *file-name* | Specifies the file name of the certificate to be checked. | The value must be an existing certificate file name. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When an end entity verifies a peer certificate, it checks the status of the peer certificate. For example, the end entity checks whether the peer certificate has expired.To verify the validity of a CA certificate or a local certificate, run the pki validate-certificate command.

**Prerequisites**

A PKI realm has been configured using the pki realm(system realm) command or the specified certificate files already exist on the device.

**Precautions**

The **pki validate-certificate ca** command allows you to verify only the root CA certificate, but not subordinate CA certificates. When multiple CA certificates are imported on a device, you can use only the **pki validate-certificate local** command to verify the validity of subordinate certificates.


Example
-------

# Configure the device to check validity of the local certificate using CRL.
```
<HUAWEI> system-view
[~HUAWEI] pki validate-certificate local realm abc
Info: The certificate is invalid.
abc contains 1 certificates.
Certificate                      Subject                          Status           Reason
test_local.cer                   /CN=test                         Invalid          Failed to be verified.

```

**Table 1** Description of the **pki validate-certificate** command output
| Item | Description |
| --- | --- |
| Certificate | Certificate name. |
| Subject | Subject of a certificate. The subject includes the following attributes:   * C: country code of a PKI entity. * ST: name of the state or province to which a PKI entity belongs. * L: geographic area where a PKI entity is located. * O: organization to which a PKI entity belongs. * OU: department to which a PKI entity belongs. * CN: common name of a PKI entity. |
| Status | Possible status:   * Invalid. * Valid. * Self-sign. |
| Reason | Possible reason:   * Failed to be verified. * Wait for verfication result. * The certificate does not exist. * The certificate is invalid. * The certificate is ineffective or expired. * The CA certificate does not exist. * The certificate has been revoked. * The CRL file does not exist. |