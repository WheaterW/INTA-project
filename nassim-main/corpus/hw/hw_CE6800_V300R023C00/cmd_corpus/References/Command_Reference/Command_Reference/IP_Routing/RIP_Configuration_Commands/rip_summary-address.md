rip summary-address
===================

rip summary-address

Function
--------



The **rip summary-address** command configures a device to send summarized routes.

The **undo rip summary-address** command disables a device from sending summarized routes.



By default, route summarization is disabled on interfaces.


Format
------

**rip summary-address** *ip-address* *mask* [ **avoid-feedback** ]

**undo rip summary-address** *ip-address* *mask*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the network IP address to be summarized. | The value is in dotted decimal notation. |
| *mask* | Specifies the IP address mask. | The value is in dotted decimal notation. |
| **avoid-feedback** | Disables an interface from learning the summarized routes advertised by itself. | - |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If avoid-feedback is set, an interface no longer learns the summarized route with the same IP address as that of the summarized route advertised by the interface, which prevents routing loops.


Example
-------

# Set a summarized IP address.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip summary-address 10.0.0.0 255.0.0.0

```