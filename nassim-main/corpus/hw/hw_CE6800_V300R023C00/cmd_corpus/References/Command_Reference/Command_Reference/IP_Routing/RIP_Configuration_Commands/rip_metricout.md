rip metricout
=============

rip metricout

Function
--------



The **rip metricout** command sets the metric that is added to the RIP routes sent by an interface.

The **undo rip metricout** command restores the default metric.



By default, the metric is 1.


Format
------

**rip metricout** *value*

**rip metricout** { { *acl-number* | **acl-name** *acl-name* } *value1* }

**rip metricout** { **ip-prefix** *ip-prefix-name* *value1* }

**undo rip metricout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies the metric that is added to the routes to be advertised. | The value is an integer ranging from 1 to 15. |
| *acl-number* | Specifies a basic ACL number. | The value is an integer ranging from 2000 to 2999. |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| *value1* | Increases the metric of a route that matches the ACL or ip-prefix. | The value is an integer ranging from 2 to 15. |
| **ip-prefix** *ip-prefix-name* | Specifies the name of an IP prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set the metric that is added to the RIP routes sent by an interface, run the rip metricout command. You can specify an ACL or IP prefix list so that the metric is added to only the RIP routes that matches the ACL or IP prefix list.

**Configuration Impact**

When a RIP route is advertised, the additional metric is added to the route. Therefore, increasing the metric of an interface also increases the metric of the RIP routes sent by the interface. However, the metrics of the routes in the routing table remain unchanged.


Example
-------

# Increase the metric of the RIP routes that match ACL 2050 by 12.
```
<HUAWEI> system-view
[~HUAWEI] acl 2050
[*HUAWEI-acl4-basic-2050] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip metricout 2050 12

```

# Increase the metric of the RIP routes that match the IP prefix list named p1 by 12.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix p1 permit 10.10.10.1 24
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip metricout ip-prefix p1 12

```

# Increase the metric of the sent RIP routes by 12.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip metricout 12

```