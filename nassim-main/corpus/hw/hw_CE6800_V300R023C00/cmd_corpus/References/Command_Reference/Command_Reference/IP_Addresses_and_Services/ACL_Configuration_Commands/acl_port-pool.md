acl port-pool
=============

acl port-pool

Function
--------



The **acl port-pool** command creates an ACL port pool and enters the ACL port pool view.

The **undo acl port-pool** command deletes an ACL port pool.



By default, no ACL port pool has been created.


Format
------

**acl port-pool** *pool-name*

**undo acl port-pool** *pool-name*

**undo acl port-pool**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pool-name* | Specifies the name of an ACL port pool. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The value can be any combination of letters, digits, and symbols. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In typical ACL usage scenarios, such as QoS traffic policy, a user may need to match multiple port numbers. To implement policy-based routing using advanced ACL rules to match multiple source and destination port numbers, the user needs to specify all possible combinations of source and destination port numbers when configuring ACL rules. On large-scale networks, tens of millions of ACL rules may need to be manually configured to match the port numbers, which is not viable.To reduce the configuration workload, run the acl port-pool command to create an ACL port pool. You only need to configure an ACL rule with a specified port pool name (pool-name) to match multiple port numbers.



**Follow-up Procedure**



Run the eq | lt | gt | neq | range command to configure the port range of the port pool.



**Precautions**



The device can only create an advanced ACL port pool.




Example
-------

# Create an ACL port pool named p1.
```
<HUAWEI> system-view
[~HUAWEI] acl port-pool p1

```