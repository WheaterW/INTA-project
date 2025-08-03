expand application volume size
==============================

expand application volume size

Function
--------



The **expand application volume size** command expands the storage space of an application.




Format
------

**expand application** *application-name* **volume** **size** *expand-size*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **size** *expand-size* | Specifies the target storage space of the application. | The value is a 64-bit unsigned integer. |
| **application** *application-name* | Specifies the name of an application. | The value is a string of 1 to 63 case-sensitive characters without spaces. |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

* You can run this command to expand the storage space of an application when the application is running.
* After this command is executed, the application automatically restarts for the expansion to take effect.

Example
-------

# Expand the storage space of an application.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] expand application app1 volume size 1000
Warning: The specified application will be restarted in expand progress.Continue? [Y/N]:y
Info: Operating, please wait for a moment...............done.
Info: Succeeded in expand the application's volume.

```