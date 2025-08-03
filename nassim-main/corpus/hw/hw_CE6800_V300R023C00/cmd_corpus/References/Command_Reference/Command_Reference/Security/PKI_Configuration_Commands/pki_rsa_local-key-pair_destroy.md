pki rsa local-key-pair destroy
==============================

pki rsa local-key-pair destroy

Function
--------



The **pki rsa local-key-pair destroy** command deletes the specified RSA key pair.




Format
------

**pki rsa local-key-pair destroy** *key-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *key-name* | Specifies the name of the RSA key pair to be deleted. | The value must be the name of an existing key pair. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



It is recommended that you run this command to destroy the specified RSA key pair if it is leaked, damaged, unused, or lost.



**Prerequisites**



The RSA key pair has been imported to the memory using the **pki import rsa-key-pair** command.



**Precautions**



The RSA key pair referenced by a PKI realm cannot be deleted. They can be deleted only after the reference relationship is removed.




Example
-------

# Delete the RSA key pair test.
```
<HUAWEI> system-view
[~HUAWEI] pki import rsa-key-pair test pem pki01_rsa.pem
The current password is required, please enter the password <length 1-32>:
Warning: Keys less than 3072 digits impose security risks. Using keys of more than or equal to 3072 digits is recommended.
Info: It will take a few seconds or more. Please wait a moment.
Info: Succeeded in importing the RSA key pair in PEM format.

[~HUAWEI] pki rsa local-key-pair destroy test
Warning: The name of the key pair to be deleted is test.
Are you sure you want to delete the key pair? [y/n]:y
Info: Delete RSA key pair success.

```