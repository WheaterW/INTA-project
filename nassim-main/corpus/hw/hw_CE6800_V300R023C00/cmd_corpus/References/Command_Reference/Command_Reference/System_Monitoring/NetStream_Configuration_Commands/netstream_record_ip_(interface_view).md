netstream record ip (interface view)
====================================

netstream record ip (interface view)

Function
--------



The **netstream record ip** command applies the IPv4 flexible flow statistics template to an interface.

The **undo netstream record ip** command deletes a specified IPv4 flexible flow statistics template on an interface.



By default, no flexible flow statistics template is applied to an interface.


Format
------

**netstream record** *record-name* **ip**

**undo netstream record** *record-name* **ip**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *record-name* | Specifies the name of the flexible flow statistic template. | The record-name must already exist. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,Sub-interface view,Interface group view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After a flexible flow statistics template is configured, run the command to apply the template to an interface.The interface then aggregates flows based on the configured aggregation keywords, collects flow statistics, and exports aged flows to the NSC.

**Prerequisites**

Before an IPv4 flexible flow statistics template is applied to an interface, the template must contain at least one aggregation keyword; otherwise, the template cannot be applied to an interface. The keyword is configured using the **match ip** command.

**Precautions**



Each interface can be configured with only one IPv4 flexible flow statistics template. Before modifying the IPv4 flexible flow statistics template in the same interface view, run the **undo netstream record ip** command to delete the existing configuration.If the IPv4 flexible flow statistics template has been applied to an interface, the template configuration cannot be modified or deleted.




Example
-------

# Configure the flexible flow statistics template abc1. Apply such configurations to interface.
```
<HUAWEI> system-view
[~HUAWEI] netstream record abc1 ip
[*HUAWEI-netstream-record-ipv4-abc1] match ip destination-address
[*HUAWEI-netstream-record-ipv4-abc1] collect counter bytes
[*HUAWEI-netstream-record-ipv4-abc1] quit
[*HUAWEI] commit
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] netstream record abc1 ip

```