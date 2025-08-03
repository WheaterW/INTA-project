acl ip-pool
===========

acl ip-pool

Function
--------



The **acl ip-pool** command creates an ACL IP address pool and displays the ACL address pool view.

The **undo acl ip-pool** command deletes an ACL IP address pool.



By default, no ACL IP address pool is configured.


Format
------

**acl ip-pool** *pool-name*

**undo acl ip-pool** *pool-name*

**undo acl ip-pool**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pool-name* | Specifies the name of an ACL IP address pool. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The value can be any combination of letters, digits, and symbols. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In some typical ACL application scenarios, you need to match both the source and destination IP addresses. On a large-scale network, there are tens of thousands of combinations of source and destination IP addresses. It is unreasonable to manually configure tens of thousands of ACL rules to match these source and destination IP addresses at the same time.To reduce the configuration workload, run the acl ip-pool command to create an ACL IP address pool. In this case, you only need to configure an ACL rule with a specified IP address pool name (pool-name) to match multiple IP addresses. In scenarios in which ACL rules are used to match both source and destination IP addresses carried in packets, run the acl ip-pool command to create an ACL source IP address pool (which includes all needed IP addresses) and an ACL destination IP address pool (which includes all needed destination IP addresses), respectively.



**Follow-up Procedure**



Run the **ip address** command to add an IP address to an ACL IP address pool.



**Precautions**



The device can only create an advanced ACL IP address pool.




Example
-------

# Create an ACL IP address pool named test.
```
<HUAWEI> system-view
[~HUAWEI] acl ip-pool test

```