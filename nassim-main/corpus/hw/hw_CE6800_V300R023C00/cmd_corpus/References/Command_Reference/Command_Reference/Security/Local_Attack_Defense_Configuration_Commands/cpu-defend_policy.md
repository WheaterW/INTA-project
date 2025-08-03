cpu-defend policy
=================

cpu-defend policy

Function
--------



The **cpu-defend policy** command creates an attack defense policy and displays the attack defense policy view.

The **undo cpu-defend policy** command deletes an attack defense policy.



By default, the default attack defense policy exists on the device and is applied to the device. The default attack defense policy cannot be deleted or modified.


Format
------

**cpu-defend policy** *policy-name*

**undo cpu-defend policy** *policy-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **policy** *policy-name* | Specifies the name of the attack defense policy. | The value is a string of 1 to 31 case-sensitive characters. The string cannot contain the following characters: > $ | . The value cannot start with the underscore (\_). When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A large number of packets including malicious attack packets are sent to the CPU on a network. If excess packets are sent to the CPU, the CPU usage becomes high and CPU performance deteriorates. The attack packets affect services and may even cause system breakdown. To solve the problem, create an attack defense policy and configure CPU attack defense and attack source tracing in the attack defense policy.

**Precautions**

The device supports a maximum of 49 attack defense policies, including the default attack defense policy. The default attack defense policy is generated in the system by default and is applied to the device. The default attack defense policy cannot be deleted or modified. The other 48 policies can be created, modified, and deleted.The configuration in a user-defined attack defense policy overrides the configuration in the default attack defense policy. If no parameter is set in the user-defined attack defense policy, the configuration in the default attack defense policy is used.When the default attack defense policy is used, protocol packets sent to the CPU are limited based on the default CIR value.


Example
-------

# Create an attack defense policy named test.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test]

```