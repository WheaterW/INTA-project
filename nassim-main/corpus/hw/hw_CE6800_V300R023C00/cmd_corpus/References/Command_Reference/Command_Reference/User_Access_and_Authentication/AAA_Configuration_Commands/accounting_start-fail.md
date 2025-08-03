accounting start-fail
=====================

accounting start-fail

Function
--------



The **accounting start-fail** command configures a policy for accounting-start failures.

The **undo accounting start-fail** command restores the default policy for accounting-start failures.



By default, users are allowed to go online if accounting-start fails. That is, the online policy is used.


Format
------

**accounting start-fail** { **offline** | **online** }

**undo accounting start-fail**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **offline** | Rejects users' online requests if accounting-start fails. | - |
| **online** | Allows users to go online if accounting-start fails. | - |



Views
-----

Accounting scheme view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If a user goes online after an accounting scheme is applied, the device sends an accounting-start packet to an accounting server. When the network is working properly, the accounting server responds to the accounting-start packet. If a fault occurs on the network, the device may not receive the response packet from the accounting server. As a result, accounting fails. The device provides the following policies for accounting failures:

* online: To prevent users from being affected by network faults, use the online policy to allow paid users to go online.
* offline: To stop providing services when accounting fails, use the offline policy to disconnect paid users.

**Precautions**

The command takes effect only when the accounting mode configured using the **accounting-mode** command is HWTACACS or RADIUS.


Example
-------

# In the accounting scheme scheme1, use the online policy for accounting-start failures.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] accounting-scheme scheme1
[*HUAWEI-aaa-accounting-scheme1] accounting start-fail online

```