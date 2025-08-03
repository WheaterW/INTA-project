install public-key
==================

install public-key

Function
--------



The **install public-key** command installs a public key.




Format
------

**install public-key** *public-key-name* **fingerprint** *fingerprint-key*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **fingerprint** *fingerprint-key* | Specifies the public key fingerprint to be installed. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **public-key** *public-key-name* | Specifies the name of the public key file to be installed. | The value is a string of 1 to 127 case-sensitive characters. It cannot contain spaces. |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The corresponding public key must be installed for signature verification of the description file of the image software package and the configuration file of the application.

**Prerequisites**

Before installing the public key, run the **create virtual-partition** command to create the image storage partition flash:/oas/images/, and upload the public key file to the directory.


Example
-------

# Install the public key.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] install public-key public-key4.txt fingerprint 1652C1AA2AC09172521572E7F359D9A17DE5BFD5
Info: Operating, please wait for a moment......done.
Info: The public key is installed successfully.

```