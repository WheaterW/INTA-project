isis purge-lsp auto-protect disable
===================================

isis purge-lsp auto-protect disable

Function
--------



The **isis purge-lsp auto-protect disable** command disables IS-IS purge LSPs from triggering master/slave main control board switchovers.

The **undo isis purge-lsp auto-protect disable** command restores the default configuration.



By default, IS-IS purge LSPs trigger master/slave main control board switchovers.


Format
------

**isis purge-lsp auto-protect disable**

**undo isis purge-lsp auto-protect disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When an IS-IS process on a device proactively sends a purge LSP, the device deletes the corresponding LSP and floods it to the network. In most cases, before the device sends a purge LSP, the end that generated the corresponding LSP sends an updated LSP. If the clock on the device runs fast, the device frequently floods purge LSPs to devices on the entire network, causing network flapping. If the device generates more than five purge LSPs for 80% or more non-pseudonode LSPs with a zero fragment number in the local LSDB within 6500s, a master/slave main control board switchover is performed if the device has two main control boards, or the device is restarted if it has only one main control board. The switchover or restart prevents network flapping.By default, IS-IS purge LSPs trigger master/slave main control board switchovers. To disable IS-IS purge LSPs from triggering master/slave main control board switchovers, run the **isis purge-lsp auto-protect disable** command.


Example
-------

# Disable IS-IS purge LSPs from triggering master/slave main control board switchovers.
```
<HUAWEI> system-view
[~HUAWEI] isis purge-lsp auto-protect disable

```