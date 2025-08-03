aaa online-fail-record
======================

aaa online-fail-record

Function
--------

The **aaa online-fail-record** command enables the device to record users' online failures.

The **undo aaa online-fail-record** command disables the device from recording users' online failures.

By default, the device records users' online failures.



Format
------

**aaa online-fail-record**

**undo aaa online-fail-record**



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

The administrator can run the **aaa online-fail-record** command to enable the function of recording user login failures.

After the
**undo aaa online-fail-record** command running and before the
**aaa online-fail-record** command works, no online failure information is recorded.

Example
-------

# Enable the device to record users' online failures.
```
<HUAWEI> system-view
[~HUAWEI] aaa online-fail-record

```

# Disable the device from recording users' online failures.
```
<HUAWEI> system-view
[~HUAWEI] undo aaa online-fail-record

```