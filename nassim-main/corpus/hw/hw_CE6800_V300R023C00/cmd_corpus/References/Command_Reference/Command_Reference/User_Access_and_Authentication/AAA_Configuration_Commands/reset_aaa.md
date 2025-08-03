reset aaa
=========

reset aaa

Function
--------



The **reset aaa** command clears records of abnormal offline, user offline and failure to get online.




Format
------

**reset aaa** { **abnormal-offline-record** | **offline-record** | **online-fail-record** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **abnormal-offline-record** | Clears records of user abnormal offline. | - |
| **offline-record** | Clears records of user offline. | - |
| **online-fail-record** | Clears records of user failure to get online. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

This command allows you to clear records of user offline, abnormal offline, and failure to get online. After the records are cleared, the function of recording information is enabled.


Example
-------

# Clear user offline records.
```
<HUAWEI> system-view
[~HUAWEI] reset aaa offline-record

```