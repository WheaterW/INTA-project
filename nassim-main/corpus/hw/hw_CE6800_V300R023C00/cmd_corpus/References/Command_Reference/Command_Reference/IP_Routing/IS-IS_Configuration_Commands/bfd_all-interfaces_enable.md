bfd all-interfaces enable
=========================

bfd all-interfaces enable

Function
--------



The **bfd all-interfaces enable** command enables BFD in an IS-IS process.

The **undo bfd all-interfaces enable** command disables BFD from an IS-IS process.



By default, BFD is disabled in an IS-IS process.


Format
------

**bfd all-interfaces enable**

**undo bfd all-interfaces enable**


Parameters
----------

None

Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BFD can provide millisecond-level fault detection, help IS-IS to detect the faults that occur on neighboring devices or links more quickly, and instruct IS-IS to recalculate routes for correct packet forwarding. The **bfd all-interfaces enable** command enables BFD in an IS-IS process.

**Prerequisites**

BFD has been enabled globally, An IS-IS process has been created, and the IS-IS process has been started on a specified interface.

**Configuration Impact**

After the **bfd all-interfaces enable** command is run, the local end can establish a BFD session with its neighbor through a specified interface and periodically send BFD packets on this session.

**Precautions**

If BFD is not enabled globally, you can configure IS-IS BFD, but a BFD session cannot be established.When BFD is enabled in the IS-IS process using the **bfd all-interfaces enable** command, no BFD session is established on the interface in the following cases:

* The **isis bfd block** command is run on the interface to block BFD from the interface. To establish a BFD session on the interface, run the **undo isis bfd block** command.
* When the **isis bfd static** command is run on the interface, no BFD session is established on the interface. To establish a BFD session on the interface, run the **undo isis bfd static** command.The priority of BFD configured on an interface is higher than that of BFD configured in a process. If BFD is enabled on an interface, a BFD session is established according to the BFD parameters set on the interface.This command conflicts with **multi-instance enable iid** command.

Example
-------

# Configure BFD in an IS-IS process.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] bfd all-interfaces enable

```