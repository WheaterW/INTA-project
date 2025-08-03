license export
==============

license export

Function
--------



The **license export** command stores a license file which is activated in the current system in the root directory of a storage device.



By default, an activated license file is not stored in the root directory.


Format
------

**license export** *file-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *file-name* | Specifies the name of the license file to be stored in the root directory. | The value is a string of 5 to 127 case-sensitive characters without spaces. The extension of a file is ".zip". |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to store the activated license file in the root directory of the storage device.

**Follow-up Procedure**

After you store the license file in the user root directory, run the **license active** command to activate the license file.

**Precautions**

The extension of a license file must be ".zip". The license file can be activated only when it is stored in the root directory of the storage device.


Example
-------

# Store the license file huawei.zip in the root directory.
```
<HUAWEI> license export huawei.zip

```