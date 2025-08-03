vrrp vrid track nqa
===================

vrrp vrid track nqa

Function
--------



The **vrrp vrid track nqa** command enables a VRRP group to track an NQA test instance to implement a rapid master/backup VRRP switchover.

The **undo vrrp vrid track nqa** command disables a VRRP group from tracking an NQA test instance to implement a rapid master/backup VRRP switchover.



By default, a VRRP group does not track an NQA test instance.


Format
------

**vrrp vrid** *virtual-router-id* **track** **nqa** *admin-name* *test-name* [ **reduce** *value-reduced* ]

**undo vrrp vrid** *virtual-router-id* **track** **nqa** [ *admin-name* *test-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *admin-name* | Specifies the administrator name for an NQA test instance. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  When double quotation marks are used around the string, spaces are allowed in the string. |
| *test-name* | Specifies the name of an NQA test instance. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  When double quotation marks are used around the string, spaces are allowed in the string. |
| **reduce** *value-reduced* | Specifies a value by which the priority reduces when a tracked NQA test instance detects that the uplink is unreachable. | The value is an integer ranging from 1 to 255.  The value 0 is reserved for special use. If a backup device receives a VRRP Advertisement packet carrying a priority of 0, the backup device immediately preempts the Master state.  By default, the priority reduces by 10 when a tracked NQA test instance detects that the uplink is unreachable. |
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

To improve network reliability, VRRP can be configured on a device to track the following objects:

* Interface.
* BFD session.Failure of a tracked object can trigger a rapid master/backup VRRP switchover to ensure service continuity. If a cross-device uplink fails, VRRP is unable to detect the fault. As a result, user traffic is dropped. To resolve the preceding issue, you can associate VRRP with an NQA test instance.After the association is complete, the NQA test instance periodically sends ICMP packets to check the reachability of destination IP addresses. If the NQA test instance detects that the destination IP address is unreachable, it notifies VRRP of the fault. VRRP then reduces the priority by a specified value, implementing a rapid master/backup VRRP switchover.

**Prerequisites**

* A VRRP group has been created using the vrrp vrid command.
* An NQA test instance has been created using the **nqa test-instance** command.
* Run the test-type specifies the test type for an NQA test instance.

**Precautions**

You cannot enable an IP address owner or a service VRRP group to track an NQA test instance.


Example
-------

# Enable VRRP group 1 to track an NQA test instance named user1 on Vlanif1, and set the value by which the priority reduces to 20 when the NQA test instance detects that the destination IP address is unreachable.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user user1
[*HUAWEI-nqa-user-user1] test-type icmp
[*HUAWEI-nqa-user-user1] quit
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] q
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] vrrp vrid 1 virtual-ip 10.10.10.11
[*HUAWEI-Vlanif1] vrrp vrid 1 track nqa user user1 reduce 20

```