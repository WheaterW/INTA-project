ospf timer wait
===============

ospf timer wait

Function
--------



The **ospf timer wait** command sets the wait timer on an OSPF interface.

The **undo ospf timer wait** command restores the default value.



By default, on broadcast interfaces, the wait interval is 40 seconds; on NBMA interfaces, it is 120 seconds.


Format
------

**ospf timer wait** *interval*

**undo ospf timer wait**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the wait timer on an OSPF interface. | The value is an integer ranging from 1 to 235926000, in seconds. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To change the wait timer, run the ospfv3 timer wait command. If no Backup Seen event is received within the timer, the designated router (DR) election starts. Setting a proper value for the wait timer can slow down changes of the DR and the backup designated router (BDR) on the network, reducing network flapping. When setting the wait timer, note the following points:

* The wait timer takes effect only on broadcast and NBMA interfaces.
* The value of the wait timer cannot be greater than the value of the dead timer.

**Precautions**

The command cannot be run on a null interface.


Example
-------

# Set the wait timer on an interface to 30 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf timer wait 30

```