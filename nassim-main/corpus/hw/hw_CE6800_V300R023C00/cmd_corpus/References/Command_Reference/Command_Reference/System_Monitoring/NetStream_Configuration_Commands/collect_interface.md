collect interface
=================

collect interface

Function
--------



The **collect interface** command allows the flexible flow statistics exported to the NSC to contain the indexes of inbound and outbound interfaces, as well as the packet sampling mode.

The **undo collect interface** command restores the default setting.



By default, the flexible flow statistics exported to the NSC do not contain the indexes of the inbound and outbound interfaces, as well as the packet sampling mode.


Format
------

**collect interface** { **input** | **output** | **sampler-info** }

**undo collect interface** { **input** | **output** | **sampler-info** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **input** | Indicates that the flexible flow statistics exported to the NSC contain the index of inbound interface. | - |
| **output** | Indicates that the flexible flow statistics exported to the NSC contain the index of outbound interface. | - |
| **sampler-info** | Configures the statistics sent to the NSC to contain the traffic sampling mode. | - |



Views
-----

IPv4 flexible flow statistics template view,IPv6 flexible flow statistics template view,VXLAN flexible flow statistics template view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



To obtain richer flow statistics, configure whether flexible flow statistics exported to the NSC contain indexes of inbound and outbound interfaces, as well as the packet sampling mode.



**Prerequisites**

A flexible flow statistics template has been created.

**Precautions**

If a flexible flow statistics template has been applied to an interface, the template configuration cannot be modified or deleted.


Example
-------

# Configure the flexible flow statistics template record1 to export the flexible flow statistics containing the inbound interface index to the NSC.
```
<HUAWEI> system-view
[~HUAWEI] netstream record record1 ip
[*HUAWEI-netstream-record-ipv4-record1] collect interface input

```