aaa offline-record
==================

aaa offline-record

Function
--------

The **aaa offline-record** command enables the device to record users' normal logout information.

The **undo aaa offline-record** command disables the device from recording users' normal logout information.

By default, the device is enabled to record user normal logout information.



Format
------

**aaa offline-record**

**undo aaa offline-record**



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

If users fail to get offline, run **aaa offline-record** command to enable the record function for fault locating.

After the
**undo aaa offline-record** command is run, no logout information is recorded unless the
**aaa offline-record** command is run.

Example
-------

# Enable the device to record users' normal logout information.
```
<HUAWEI> system-view
[~HUAWEI] aaa offline-record

```

# Disable the device from recording users' normal logout information.
```
<HUAWEI> system-view
[~HUAWEI] undo aaa offline-record

```