license delete
==============

license delete

Function
--------



The **license delete** command deletes a specified license file in the $\_license directory.




Format
------

**license delete** *file-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *file-name* | Specifies the name of the license file to be deleted. | The value is a string of 1 to 127 case-sensitive characters. It cannot contain spaces.  If the file to be deleted is a pure file name and the file exists, the dedicated directories of all chassis are deleted.  Specified license file in the $\_license directory: If the name of the file to be deleted contains the full path and the file exists, only the specified file in the path is deleted. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To delete unwanted or useless license files in the $\_license directory, run the license delete command.

**Prerequisites**

The license file already exists in the $\_license directory.

**Precautions**

This command cannot be used to delete a license file that has the same content as an activated license file or a ZIP package that contains a license file with the same content as an activated license file.


Example
-------

# Delete the license file license.xml from the device.
```
<HUAWEI> license delete license.xml
Warning: The file license.xml cannot be recycled. Continue? [Y/N]:y
Info: Unreserved deleting file flash:/$_license/license.xml...Done.

```