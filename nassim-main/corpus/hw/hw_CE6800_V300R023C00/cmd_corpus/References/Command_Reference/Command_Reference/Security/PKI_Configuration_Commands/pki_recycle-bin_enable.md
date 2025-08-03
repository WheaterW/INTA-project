pki recycle-bin enable
======================

pki recycle-bin enable

Function
--------



The **pki recycle-bin enable** command moves overwritten files to the recycle bin.

The **undo pki recycle-bin enable** command cancels moving overwritten files to the recycle bin.



By default, overwritten files are permanently deleted.


Format
------

**pki recycle-bin enable**

**undo pki recycle-bin enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Overwritten files are permanently deleted by default and cannot be restored. If you want to restore overwritten files in case new files are unavailable, run the **pki recycle-bin enable** command to enable the function of moving overwritten files to the recycle bin.The **pki recycle-bin enable** command applies only to the following scenarios:

* Run the **pki ldap-server-template** command to overwrite the existing certificate and CRL.
* Run the **pki cmp initial-request session** command to overwrite the existing certificate.
* Run the **pki cmp certificate-request session** command to overwrite the existing certificate.
* Run the **pki cmp keyupdate-request session** command to overwrite the existing certificate.
* Run the **pki enroll-certificate** command to overwrite the existing certificate.
* Run the **pki create-certificate** command to overwrite the existing certificate.
* Run the **pki export-certificate** command to overwrite the existing certificate.
* Run the **pki export-certificate default** command to overwrite the existing certificate.
* Run the **pki export rsa-key-pair** command to overwrite the existing RSA key pair.
* Run the **pki export sm2-key-pair** command to overwrite the existing SM2 key pair.


Example
-------

# Enable the function of moving overwritten files to the recycle bin.
```
<HUAWEI> system-view
[~HUAWEI] pki recycle-bin enable

```