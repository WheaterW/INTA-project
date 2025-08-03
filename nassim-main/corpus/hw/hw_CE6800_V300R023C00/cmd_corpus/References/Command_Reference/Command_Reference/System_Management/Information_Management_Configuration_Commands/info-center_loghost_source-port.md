info-center loghost source-port
===============================

info-center loghost source-port

Function
--------



The **info-center loghost source-port** command configures a source interface through which the device sends information to the log host.

The **undo info-center loghost source-port** command deletes the configuration of the source interface through which the device sends information to the log host.



By default, the source interface number is 38514.


Format
------

**info-center loghost source-port** *source-port*

**undo info-center loghost source-port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *source-port* | Specifies the number of the source interface through which the device sends information to the log host. | The value is an integer ranging from 1025 to 65535. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To improve system security, run the **info-center loghost source-port** command to change the source port through which the device sends information to the log host.


Example
-------

# Change the number of the source interface through which the device sends information to the log host to 1026.
```
<HUAWEI> system-view
[~HUAWEI] info-center loghost source-port 1026

```