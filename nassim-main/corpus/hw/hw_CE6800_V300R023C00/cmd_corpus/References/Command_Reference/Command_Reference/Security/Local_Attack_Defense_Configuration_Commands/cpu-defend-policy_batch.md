cpu-defend-policy batch
=======================

cpu-defend-policy batch

Function
--------



The **cpu-defend-policy batch** command applies an attack defense policy.

The **undo cpu-defend-policy batch** command cancels the application of an attack defense policy.



By default, the default attack defense policy is applied to the device.


Format
------

**cpu-defend-policy** *policy-name* **batch** **slot** { *start-slot* [ **to** *end-slot* ] } &<1-12>

**undo cpu-defend-policy batch slot** { *start-slot* [ **to** *end-slot* ] } &<1-12>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of the attack defense policy. | The attack defense policy must already exist. |
| **batch** *start-slot* | Indicates the start slot ID to which the attack defense policy is applied. | The value is an integer ranging from 1 to 31. |
| **slot** | Indicates the slot. | - |
| **to** *end-slot* | Indicates the end slot ID to which the attack defense policy is applied. | The value is an integer ranging from 1 to 31. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An attack defense policy takes effect only after it is applied to a device. Only one attack defense policy can be applied to a board.

**Prerequisites**

An attack defense policy has been created by using the **cpu-defend policy** command.


Example
-------

# Apply the attack defense policy named test.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] quit
[*HUAWEI] cpu-defend-policy test batch slot 1

```