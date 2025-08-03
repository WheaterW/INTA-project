pki delete whitelist
====================

pki delete whitelist

Function
--------



The **pki delete whitelist** command deletes certificate whitelist files from the memory.




Format
------

**pki delete whitelist filename** *file-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **filename** *file-name* | Specifies the name of a certificate whitelist file. | The value must be an existing certificate whitelist file name and cannot contain tildes, backslashes (\), spaces, double quotation marks ("), single quotation marks ('), asterisks (\*), colons (:), less-than signs (<), question marks (?), slashes (/), or vertical bars (|). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a certificate whitelist file is no longer required, run this command to delete it from the memory.

**Prerequisites**

The certificate whitelist file has been imported to the device memory using the **pki import whitelist** command.


Example
-------

# Delete a certificate whitelist file from the memory.
```
<HUAWEI> system-view
[~HUAWEI] pki delete whitelist filename pki_bls.xml

```