netstream record vxlan inner-ip (interface view)
================================================

netstream record vxlan inner-ip (interface view)

Function
--------



The **netstream record vxlan inner-ip** command creates a VXLAN flexible flow statistics template or displays the view of an existing VXLAN flexible flow statistics template.

The **undo netstream record vxlan inner-ip** command deletes a VXLAN flexible flow statistics template.



By default, no VXLAN flexible flow statistics template is configured.


Format
------

**netstream record** *record-name* **vxlan** **inner-ip**

**undo netstream record** *record-name* **vxlan** **inner-ip**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *record-name* | Specifies the name of a VXLAN flexible flow statistics template. | The record-name must already exist. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,Sub-interface view,Interface group view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After a VXLAN flexible flow statistics template is configured, run the **netstream record vxlan inner-ip** command to apply the template to an interface. If a template is not applied to an interface, the VXLAN flexible flow statistics collection will not take effect.The interface aggregates flows based on the aggregation keywords configured in the template, collects flow statistics, and exports aged flows to the NSC.

**Prerequisites**

The template must contain at least one aggregation keyword for VXLAN flexible flow statistics collection; otherwise, the template cannot be applied to interfaces. The keyword is configured using the **match inner-ip** command.

**Precautions**



Each interface can be configured with only one VXLAN flexible flow statistics template. Before changing a flexible flow statistics template in the same interface view, run the **undo netstream record vxlan inner-ip** command to delete the existing configuration.If a VXLAN flexible flow statistics template has been applied to the interface, the template configuration cannot be modified or deleted.




Example
-------

# Configure a flexible flow statistics template abc1 and apply it to an interface.
```
<HUAWEI> system-view
[~HUAWEI] netstream record abc1 vxlan inner-ip
[*HUAWEI-netstream-record-vxlan-abc1] match inner-ip destination-address
[*HUAWEI-netstream-record-vxlan-abc1] collect counter bytes
[*HUAWEI-netstream-record-vxlan-abc1] quit
[*HUAWEI] commit
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] netstream record abc1 vxlan inner-ip

```