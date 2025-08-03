bfd trigger if-down
===================

bfd trigger if-down

Function
--------

The **bfd trigger if-down** command associates the BFD session status with the bound interface status.

Using the **undo bfd trigger if-down** command cancels the association between the BFD session status and the bound interface status.

By default, a BFD session is not associated with the bound interface status.



Format
------

**bfd trigger if-down**

**undo bfd trigger if-down**



Parameters
----------

None


Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Eth-Trunk member interface view,Layer 2 GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

After a fault on a physical interface is detected by BFD and rapidly removed, the BFD session goes Down, whereas the physical interface goes Up. This causes some traffic to fail to be switched and then discarded. To prevent packet loss, run the **bfd trigger if-down** command to trigger a transient interruption on the interface, which ensures that all traffic is rapidly switched.

**Prerequisites**

* A static single-hop BFD session bound to the interface has been created.
* The **process-pst** command has been configured to allow BFD sessions to modify the PST.

**Configuration Impact**

If BFD goes Down, the associated interface alternates between Up and Down.

**Precautions**

If a BFD session is bound to or tracked by an interface, the BFD session trigger function cannot be configured at the same time. If both the BFD session and the interface are configured, the BFD session and the interface may go down. In this case, you need to delete either of them.



Example
-------

# Associate the BFD session status with the bound interface status.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] bfd trigger if-down

```