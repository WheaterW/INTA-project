ospf trans-delay
================

ospf trans-delay

Function
--------



The **ospf trans-delay** command sets the delay for transmitting LSAs on an interface.

The **undo ospf trans-delay** command restores the default value.



By default, the delay is 1 second.


Format
------

**ospf trans-delay** *delayvalue*

**undo ospf trans-delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delayvalue* | Specifies the delay for transmitting LSAs on an interface. | The value is an integer ranging from 1 to 500, in seconds. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The aging time of each LSA in the LSDB increases by one every second, but LSAs do not age during transmission. To configure an LSA transmission delay on a multi-area adjacency interface so that an extension period (the configured delay) is added to the LSAs to be sent, run the ospf trans-delay multi-area command. This configuration is extremely important on low-speed networks.

**Precautions**

The command cannot be run on a null interface.


Example
-------

# Specify the delay for transmitting LSAs on an interface to 3 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf trans-delay 3

```