join-prune triggered-message-cache disable
==========================================

join-prune triggered-message-cache disable

Function
--------



The **join-prune triggered-message-cache disable** command disables the Join/Prune message packaging function.

The **undo join-prune triggered-message-cache disable** enables the Join/Prune message packaging function.



By default, this function is enabled.


Format
------

**join-prune triggered-message-cache disable**

**undo join-prune triggered-message-cache disable**


Parameters
----------

None

Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The efficiency for sending PIM Join/Prune messages in a package is higher than that for separately sending a large number of PIM Join/Prune messages. By default, a device sends PIM Join/Prune messages in a package. Because the size of a PIM Join/Prune message package is large, devices that have poor performance cannot receive the PIM Join/Prune message package. If such devices exist, run the **join-prune triggered-message-cache disable** command to disable the Join/Prune message packaging function to prevent packet discarding.


Example
-------

# Disable the Join/Prune message packaging function.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] join-prune triggered-message-cache disable

```