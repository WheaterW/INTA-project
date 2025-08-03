start
=====

start

Function
--------



The **start** command is used to start an application that has been installed in the open application system.

The **undo start** command stops an installed application in the open application system.



By default, applications in the open application system are not started.


Format
------

**start position** { **slot** *slot-id* | **type** *board-type* }

**undo start position** { **slot** *slot-id* | **type** *board-type* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies a slot ID. | - |
| **type** *board-type* | Specifies the board type. | Only the specified character string is supported. Currently, only "MPU" is supported. |
| **position** | Specify where the application starts. | - |



Views
-----

OAS application view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Before starting an application, you must specify the image software package. Otherwise, the application fails to be started.


Example
-------

# Start the application.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] application app1
[*HUAWEI-oas-app1] start position slot 1

```

# Stop the application.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] application app1
[*HUAWEI-oas-app1] undo start position slot 1
Warning: The application instance app1 will be stopped. Continue? [Y/N]:y

```