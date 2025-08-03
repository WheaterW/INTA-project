reset application
=================

reset application

Function
--------



The **reset application** command restarts an application in the open application system.




Format
------

**reset application** *application-name* **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *application-name* | Specifies the name of an application. | The value is a string of 1 to 63 case-sensitive characters without spaces. |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 49 case-sensitive characters without spaces. |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After changing the image software package and running options of an application, restart the application for the modification to take effect.


Example
-------

# Restart an application.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] reset application app1 slot 1
Warning: The application app1 will be reset. Continue? [Y/N]:y
Info: The application was successfully reset.

```