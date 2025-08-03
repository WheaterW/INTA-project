rip enable
==========

rip enable

Function
--------



The **rip enable** command enables a RIP process on an interface.

The **undo rip enable** command disables a RIP process from an interface.



By default, no RIP process is enabled on an interface.


Format
------

**rip enable** *process-id*

**undo rip enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Indicates the ID of a RIP process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To enable a RIP process on an interface, run the **rip enable** command.After the **rip enable** command is run on an interface, routes to all the network segments where the interface is located are advertised using RIP packets.NOTE:The **rip enable** command takes precedence over the **network** command.


Example
-------

# Enable RIP process 1 on an interface.
```
<HUAWEI> system-view
[~HUAWEI] rip 1
[*HUAWEI] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip enable 1

```