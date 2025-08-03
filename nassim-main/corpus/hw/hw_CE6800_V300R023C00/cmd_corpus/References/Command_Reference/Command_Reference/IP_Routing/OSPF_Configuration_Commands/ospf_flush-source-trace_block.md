ospf flush-source-trace block
=============================

ospf flush-source-trace block

Function
--------



The **ospf flush-source-trace block** command disables OSPF flush LSA source tracing on an interface.

The **undo ospf flush-source-trace block** command enables OSPF flush LSA source tracing on an interface.



By default, OSPF flush LSA source tracing is enabled on all interfaces.


Format
------

**ospf flush-source-trace block**

**undo ospf flush-source-trace block**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, the OSPF flush LSA source tracing function is enabled on all interfaces of a specified OSPF process. To disable this function on an interface, run the **ospf flush-source-trace block** command.


Example
-------

# Disable OSPF flush LSA source tracing on a specified interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf flush-source-trace block

```