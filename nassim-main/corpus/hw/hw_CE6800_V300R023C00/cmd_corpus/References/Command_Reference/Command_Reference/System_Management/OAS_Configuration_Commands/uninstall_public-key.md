uninstall public-key
====================

uninstall public-key

Function
--------



The **uninstall public-key** command uninstalls a public key.




Format
------

**uninstall public-key** *public-key-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *public-key-name* | Name of a public key file. | The value is a string of 1 to 127 case-sensitive characters without spaces. |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

In an open application system, you can run this command to uninstall the public key if you want to stop using an application.


Example
-------

# Uninstall a public key.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] uninstall public-key public-key18.txt
Info: Operating, please wait for a moment..........done.
Info: The public key is uninstalled successfully.

```