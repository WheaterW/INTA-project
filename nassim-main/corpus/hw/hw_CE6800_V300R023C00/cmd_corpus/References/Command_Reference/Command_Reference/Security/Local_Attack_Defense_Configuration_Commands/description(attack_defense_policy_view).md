description(attack defense policy view)
=======================================

description(attack defense policy view)

Function
--------



The **description** command configures the description of an attack defense policy.

The **undo description** command deletes the description of an attack defense policy.



By default, no description is configured for an attack defense policy.


Format
------

**description** *description*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description* | Specify CPU defend policy description. | It is a string of 1 to 63 case-sensitive characters with spaces. |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **description** command configures the description of an attack defense policy, for example, the usage or application scenario of the attack defense policy. The description is used to differentiate attack defense policies.

**Precautions**

If you run the **description** command in the same attack defense policy view multiple times, only the latest configuration takes effect.


Example
-------

# Configure the description defend\_arp\_attack for the attack defense policy named test.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] description defend_arp_attack

```