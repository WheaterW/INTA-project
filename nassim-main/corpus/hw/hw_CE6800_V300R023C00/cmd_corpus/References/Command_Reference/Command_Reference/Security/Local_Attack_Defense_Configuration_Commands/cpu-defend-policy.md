cpu-defend-policy
=================

cpu-defend-policy

Function
--------



The **cpu-defend-policy** command applies an attack defense policy.

The **undo cpu-defend-policy** command cancels the application of an attack defense policy.



By default, the default attack defense policy is applied to all devices.


Format
------

**cpu-defend-policy** *policy-name* [ **slot** *slot-id* ]

**undo cpu-defend-policy** [ *policy-name* ] [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of the attack defense policy. | The attack defense policy must already exist. |
| **slot** *slot-id* | Indicates that the attack defense policy is applied locally. slot-id specifies the slot ID of the device. If slot slot-id is not specified, the attack defense policy is applied on the device. | The value is an integer ranging from 1 to 31. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



An attack defense policy takes effect only after it is applied to a device.



**Prerequisites**

An attack defense policy has been created by using the **cpu-defend policy** command.


Example
-------

# Apply the attack defense policy named test.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] quit
[*HUAWEI] cpu-defend-policy test slot 1

```