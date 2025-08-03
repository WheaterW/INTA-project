info-center logbuffer
=====================

info-center logbuffer

Function
--------



The **info-center logbuffer size** command sets the number of logs to be displayed.

The **undo info-center logbuffer size** command restores the default number of logs to be displayed.

The **info-center logbuffer** command enables the log buffer.

The **undo info-center logbuffer** command disables the log buffer.



By default, info-center logbuffer is enabled and a maximum of 512 logs are displayed.


Format
------

**info-center logbuffer size** *buffersize*

**info-center logbuffer**

**undo info-center logbuffer size**

**undo info-center logbuffer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **size** *buffersize* | Specifies the number of logs to be displayed. | The value is an integer ranging from 0 to 10240. The default value is 512.  If buffersize is set to 0, no log will be displayed. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* You can run the **info-center logbuffer** command to enable the log buffer so that the device starts to record logs.
* You can run the **info-center logbuffer size** command to set the number of logs to be displayed at a time.

**Configuration Impact**

If you run the **info-center logbuffer size** command multiple times, only the latest configuration takes effect.


Example
-------

# Set the number of logs to be displayed to 50.
```
<HUAWEI> system-view
[~HUAWEI] info-center logbuffer size 50

```