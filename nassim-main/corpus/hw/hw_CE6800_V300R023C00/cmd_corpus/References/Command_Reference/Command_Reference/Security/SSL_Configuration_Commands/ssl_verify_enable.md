ssl verify enable
=================

ssl verify enable

Function
--------



The **ssl verify enable** command enables digital certificate verification.

The **undo ssl verify enable** command disables digital certificate verification.



By default, digital certificate verification is disabled.


Format
------

**ssl verify basic-constrain enable**

**ssl verify version cert-version3 enable**

**ssl verify version crl-version2 enable**

**ssl verify key-usage enable**

**undo ssl verify basic-constrain enable**

**undo ssl verify version cert-version3 enable**

**undo ssl verify version crl-version2 enable**

**undo ssl verify key-usage enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **version** | Indicates the basic constraint fields of a digital certificate. | - |
| **cert-version3** | Indicates the X.509v3 digital certificate. | - |
| **crl-version2** | Indicates the X.509v2 certificate revocation list (CRL). | - |
| **key-usage** | Indicates the extended key usage field of a digital certificate. | - |
| **basic-constrain** | Indicates the basic constraint fields of a digital certificate. | - |



Views
-----

SSL policy view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* The digital certificate is verified to check the validity of the digital certificate path. This prevents invalid digital certificates from being used and improves security.
* The **ssl verify version cert-version3 enable** command is used to check whether a locally loaded digital certificate is of the X.509v3 version.
* The **ssl verify version crl-version2 enable** command is used to check whether the locally loaded CRL is of the X.509v2 version.
* The **ssl verify key-usage enable** command is used to verify only the enhanced key usage field of the peer digital certificate. If this field exists, the verification is performed. If this field does not exist, the verification is not performed. When the local end functions as a client, it checks whether the digital certificate sent by the server contains SSL server (id-kp 1, OID 1.3.6.1.5.5.7.3.1). When the local end functions as a server, it checks whether the digital certificate sent by the client contains SSL client (id-kp 2, OID 1.3.6.1.5.5.7.3.2).
* The **ssl verify basic-constrain enable** command is used only to verify the basic constraint fields of the CA certificate sent by the peer end to determine whether the body type is CA. If the basic constraint field does not exist or the basic constraint field exists but the entity type is not CA, the validation fails.

**Prerequisites**

An SSL policy has been created using the **ssl policy** command.

**Precautions**

* When the version check function is enabled, if a file that does not meet the requirements exists on the device, the system displays a check error message and the name of the file that does not meet the requirements. The check succeeds only after the file is uninstalled.
* After the version check function is enabled, the device can load only the files that meet the requirements. If you load a file that does not meet the requirements, the system displays a message indicating that the loading fails.
* The peer digital certificate verification function takes effect only when the peer digital certificate verification function is enabled for the service bound to the SSL policy.

Example
-------

# Enable verification on the basic constraint fields of a digital certificate.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy abc
[*HUAWEI-ssl-policy-abc] ssl verify basic-constrain enable

```