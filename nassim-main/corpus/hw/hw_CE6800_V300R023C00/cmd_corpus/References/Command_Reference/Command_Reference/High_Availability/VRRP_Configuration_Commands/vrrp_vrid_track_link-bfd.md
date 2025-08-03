vrrp vrid track link-bfd
========================

vrrp vrid track link-bfd

Function
--------



The **vrrp vrid track link-bfd** command sets a threshold for the number of link BFD sessions tracked by a VRRP group that go Down. When the number of link BFD sessions tracked by the VRRP group that go Down reaches or exceeds the specified threshold, the VRRP group performs a master/backup switchover.

The **undo vrrp vrid track link-bfd** command deletes the configured threshold.



By default, a VRRP group performs a master/backup VRRP switchover only when all link BFD sessions tracked by it go Down.


Format
------

**vrrp vrid** *virtual-router-id* **track** **link-bfd** *down-number*

**undo vrrp vrid** *virtual-router-id* **track** **link-bfd**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *down-number* | Specifies a threshold for the number of link BFD sessions tracked by a VRRP group that go Down. | The value is an integer ranging from 1 to 8. |
| **vrid** *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a VRRP group is bound to multiple link BFD sessions and the vrrp vrid track link-bfd command is not run, the VRRP group performs a master/backup VRRP switchover only when all link BFD sessions go Down. To improve network stability and reliability, run the vrrp vrid track link-bfd command to set a threshold for the number of link BFD sessions tracked by the VRRP group that go Down.

* If the number of link BFD sessions tracked by the VRRP group that go Down reaches or exceeds the specified threshold, the VRRP group performs a master/backup VRRP switchover.
* If the number of link BFD sessions tracked by the VRRP group that go Down does not reach the specified threshold, the VRRP group does not perform a master/backup VRRP switchover.
* If the number of link BFD sessions tracked by the VRRP group is less than the value specified by the parameter, the VRRP group performs a master/backup VRRP switchover only when all tracked link BFD sessions go Down.

**Prerequisites**

A VRRP group and a link BFD session have been configured.


Example
-------

# Set the threshold for the number of link BFD sessions tracked by a VRRP group that go Down to 2 on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.10.10.6 24
[*HUAWEI-100GE1/0/1] vrrp vrid 1 virtual-ip 10.10.10.185
[*HUAWEI-100GE1/0/1] vrrp vrid 1 track link-bfd 2

```