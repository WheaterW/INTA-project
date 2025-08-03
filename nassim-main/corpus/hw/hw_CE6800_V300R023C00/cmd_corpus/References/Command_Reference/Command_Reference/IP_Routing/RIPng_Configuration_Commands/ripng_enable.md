ripng enable
============

ripng enable

Function
--------



The **ripng enable** command enables RIPng on an interface.

The **undo ripng** command disables RIPng from an interface.



By default, RIPng is disabled on an interface.


Format
------

**ripng** *process-id* **enable**

**undo ripng**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of a RIPng process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To enable RIPng on an interface, run the **ripng enable** command. Ensure that an IPv6 address has been configured for the interface before you run this command; otherwise, this command cannot be run.


Example
-------

# Enable RIPng 100 on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] ripng 100
[*HUAWEI-ripng-100] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8::1/64
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ripng 100 enable

```