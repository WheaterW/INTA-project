undo info-center loghost character-set
======================================

undo info-center loghost character-set

Function
--------



The **undo info-center loghost character-set** command restores the default character set used for sending logs to the server.



By default, the UTF-8 character set is used to send logs to the server.


Format
------

**undo info-center loghost character-set**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After the log server to which logs are sent is configured, if logs carry Chinese characters, garbled characters may be displayed on the log server because the character set configured on the log server is different from that on the device. In this case, you can run this command to set the character set used by the device to send logs to the log server to be the same as that on the log server.


Example
-------

# Restore the character set for sending logs to the default value UTF-8.
```
<HUAWEI> system-view
[~HUAWEI] undo info-center loghost character-set

```