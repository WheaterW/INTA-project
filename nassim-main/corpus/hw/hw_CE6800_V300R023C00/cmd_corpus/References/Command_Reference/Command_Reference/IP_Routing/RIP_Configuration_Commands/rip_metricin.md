rip metricin
============

rip metricin

Function
--------



The **rip metricin** command sets the metric that is added to the routes carried in received RIP packets.

The **undo rip metricin** command restores the default metric.



By default, the metric is 0.


Format
------

**rip metricin** *value*

**rip metricin** { { *aclNumber* | **acl-name** *aclName* } *metricInVal* }

**rip metricin** { **ip-prefix** *ip-prefix-name* *metricInVal* }

**undo rip metricin**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies the metric that is added to received routes. | The value is an integer in the range 0 to 15. |
| *aclNumber* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| **acl-name** *aclName* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| *metricInVal* | Specifies the metric that is added to the routes that match the ACL or IP prefix list. | The value is an integer in the range 0 to 15. |
| **ip-prefix** *ip-prefix-name* | Specifies an IP prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When an interface receives a route, RIP adds the interface metric to the route, and then adds the route to the routing table. Therefore, increasing the interface metric also increases the metric of RIP routes received by the interface.You can specify the metric to be added to the RIP routes that match the ACL or IP prefix list. If a RIP route fails to match the ACL or IP prefix list, the metric is not added to the route.

**Configuration Impact**

If the metric of a route is greater than 16 after the configured value is added, 16 is used as its metric.NOTE:If the route is unreachable after the **rip metricin** command is run, run the **undo rip metricin** command to restore the default value.


Example
-------

# Increase the metric of the RIP routes that match ACL 2000 by 10.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip metricin 2000 10

```

# Increase the metric of the RIP routes received by Gigabit Ethernet 1/0/1 by 12.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip metricin 12

```