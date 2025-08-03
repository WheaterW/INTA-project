monitor-link group
==================

monitor-link group

Function
--------



The **monitor-link group** command creates a Monitor Link group and enters the Monitor Link group view. If a Monitor Link group exists, the command enters the specified Monitor Link group view.

The **undo monitor-link group** command deletes a Monitor Link group.



By default, no Monitor Link group is created.


Format
------

**monitor-link group** *group-id*

**undo monitor-link group** *group-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-id* | Specifies the ID of a Monitor Link group. | The value is an integer ranging from 1 to 24. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Monitor Link is an interface association mechanism. Monitor Link checks the uplink interface in a Monitor Link group and sets the downlink interface status accordingly. After an uplink fault occurs, Monitor Link immediately notifies downstream devices of the fault. This process minimizes traffic loss by avoiding a delayed notification of the uplink fault. To configure basic functions of Monitor Link, run the monitor-link group command to create a Monitor Link group and enter the Monitor Link group view.



**Follow-up Procedure**



Configure uplink and downlink interfaces in the Monitor Link group.



**Precautions**



Before deleting a Monitor Link group when it has member interfaces, run the **undo port** command to delete all member interfaces from the Monitor Link group.




Example
-------

# Add 100GE 1/0/1 to Monitor Link group 1 and specify the interface as the uplink interface.
```
<HUAWEI> system-view
[~HUAWEI] monitor-link group 1

```