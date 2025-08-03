ssm-mapping policy
==================

ssm-mapping policy

Function
--------



The **ssm-mapping policy** command configures an IPv4 SSM mapping policy.

Using the **undo ssm-mapping policy** command deletes an IPv4 SSM mapping policy.



By default, no IPv4 SSM mapping policy is configured.


Format
------

**ssm-mapping policy** *policy-name*

**undo ssm-mapping policy** *policy-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Sets an SSM mapping policy name. | The name is a string of 1 to 31 characters and case sensitive. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When users connected to different interfaces want to watch programs multicast by different multicast sources, run the **ssm-mapping policy** command to configure different SSM mapping policies on different interfaces. After that, IGMP packets received by different interfaces can be mapped to different multicast sources and users' requirements can be answered.

**Prerequisites**

SSM mapping and a corresponding policy have been enabled on the interface using the **igmp ssm-mapping enable** command.When an IPv4 SSM mapping policy is deleted, all the configuration information of the policy will be deleted.


Example
-------

# Create an SSM mapping policy named ssmmap1 in the system view.
```
<HUAWEI> system-view
[~HUAWEI] ssm-mapping policy ssmmap1

```