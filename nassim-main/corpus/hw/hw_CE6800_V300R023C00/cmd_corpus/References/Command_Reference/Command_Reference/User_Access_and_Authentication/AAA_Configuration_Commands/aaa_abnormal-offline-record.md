aaa abnormal-offline-record
===========================

aaa abnormal-offline-record

Function
--------

The **aaa abnormal-offline-record** command enables the device to record users' abnormal logout information.

The **undo aaa abnormal-offline-record** command disables the device from recording users' abnormal logout information.

By default, the device records users' abnormal logout information.



Format
------

**aaa abnormal-offline-record**

**undo aaa abnormal-offline-record**



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

If users abnormally log out, run **aaa abnormal-offline-record** command to enable the record function for fault locating. After the **undo aaa abnormal-offline-record** command is run, no abnormal logout information is recorded unless the **aaa abnormal-offline-record** command is run.



Example
-------

# Enable the device to record users' abnormal logout information.
```
<HUAWEI> system-view
[~HUAWEI] aaa abnormal-offline-record

```

# Disable the device from recording users' abnormal logout information.
```
<HUAWEI> system-view
[~HUAWEI] undo aaa abnormal-offline-record

```