isis purge-source-trace block
=============================

isis purge-source-trace block

Function
--------



The **isis purge-source-trace block** command disables IS-IS purge LSP source tracing on an interface.

The **undo isis purge-source-trace block** command enables IS-IS purge LSP source tracing on an interface.



By default, IS-IS purge LSP source tracing on an interface is enabled on all interfaces.


Format
------

**isis purge-source-trace block**

**undo isis purge-source-trace block**


Parameters
----------

None

Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, the IS-IS purge LSP source tracing function is enabled on all interfaces of a specified IS-IS process. To disable this function on an interface, run the **isis purge-source-trace block** command.


Example
-------

# Disable IS-IS purge LSP source tracing on a specified interface.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis purge-source-trace block

```