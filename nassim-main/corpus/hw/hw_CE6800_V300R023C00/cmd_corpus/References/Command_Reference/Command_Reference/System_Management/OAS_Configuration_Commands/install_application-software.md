install application-software
============================

install application-software

Function
--------



The **install application-software** command installs an image software package.




Format
------

**install application-software** *software-path*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *software-path* | Specifies the image software package to be installed. | The value is a string of 1 to 127 case-sensitive characters without spaces. |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

An image software package is a .zip package that contains an image, the image description file, and the signature file of the description file. After the openness function is enabled, you can run this command to install the image software package.

**Prerequisites**

Before installing the image software package, run the **create virtual-partition** command to create the image storage partition flash:/oas/images/ and upload the software package to the directory.


Example
-------

# Install the image software package.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] install application-software flash:/oas/images/oas.zip
Info: Operating, please wait for a moment......done.
Info: The application software package is successfully installed.

```