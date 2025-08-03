ripng metricout
===============

ripng metricout

Function
--------



The **ripng metricout** command sets the metric that is added to the RIPng routes sent by an interface.

The **undo ripng metricout** command restores the default setting.



By default, the metric that is added to the RIPng routes sent by an interface is 1.


Format
------

**ripng metricout** *value*

**ripng metricout** { { *acl6-number* | **acl6-name** *acl6-name* } *value* }

**ripng metricout** { **ipv6-prefix** *ipv6-prefix-name* *value* }

**undo ripng metricout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies the metric that is added to the routes that match the filtering conditions of the ACL6 or IPv6 prefix list. | The value is an integer ranging from 1 to 15. |
| *acl6-number* | Specifies a basic ACL6 number. | The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 64 case-sensitive characters starting with a letter. It cannot contain spaces. |
| **ipv6-prefix** *ipv6-prefix-name* | Specifies the name of an IPv6 prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set the metric that is added to the RIPng routes sent by an interface, run the ripng metricout command. You can specify value in the command so that the metric is added to only the RIPng routes that match the filtering conditions of the ACL or IP prefix list.

**Configuration Impact**

When a RIPng route is being advertised, the additional metric is added to the route. Therefore, increasing the metric of an interface also increases the metric of the RIPng route sent by the interface. However, the metric of the route in the routing table remains unchanged.


Example
-------

# Set the metric that is added to sent RIPng routes to 12.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ripng metricout 12

```

# Increase the metric of the RIPng routes that match the filtering conditions of the IPv6 prefix list named p1 by 12.
```
<HUAWEI> system-view
[~HUAWEI] ip ipv6-prefix p1 permit 2001:db8:1::1 128
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ripng metricout ipv6-prefix p1 12

```

# Increase the metric of the RIPng routes that match the filtering conditions of ACL6 2050 by 12.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2050
[*HUAWEI-acl6-basic-2050] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ripng metricout 2050 12

```