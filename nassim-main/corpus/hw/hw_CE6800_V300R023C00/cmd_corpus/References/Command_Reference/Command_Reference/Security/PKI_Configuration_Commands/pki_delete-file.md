pki delete-file
===============

pki delete-file

Function
--------



The **pki delete-file** command deletes a certificate file saved on the Flash.




Format
------

**pki delete-file** *file-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *file-name* | Specifies the name of the certificate file to be deleted. | The value is a string of 1 to 64 case-sensitive characters, and cannot contain spaces. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Remove the certificate file from the memory before removing it form the Flash.


Example
-------

# Delete the local certificate file 1.pem.
```
<HUAWEI> pki delete-file 1.pem
Warning: Confirm to delete the file?Please select [Y/N]:y
Info: Delete Success.

```