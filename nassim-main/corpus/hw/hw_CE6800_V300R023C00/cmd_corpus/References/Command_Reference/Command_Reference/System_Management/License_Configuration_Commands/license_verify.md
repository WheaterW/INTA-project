license verify
==============

license verify

Function
--------



The **license verify** command verifies the license file of the device.




Format
------

**license verify** *file-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *file-name* | Specifies the name of the license file to be verified. | The value is a string of 5 to 127 characters. It cannot contain spaces. The file name extension must be .dat, .zip, or .xml. The actual file name extension depends on the license file that is applied for. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To verify the license file of the device, run the **license verify** command. The verification result can be:

* Verification failed: The possible causes include invalid License file, unmatched ESN, unmatched product model, and unmatched version information.
* Verification succeeded: If the result is "Verify license succeeded, this license file can be activated.

**Prerequisites**



Before running this command to verify the license file of the device, ensure that the license file exists on the device.




Example
-------

# Verify the license file license.xml of the device.
```
<HUAWEI> license verify license.xml
Info: Verify license succeeded.

```