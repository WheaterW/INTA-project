quit
====

quit

Function
--------



The **quit** command quits the current view command and displays the previous view.




Format
------

**quit**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

0: Visit level


Usage Guidelines
----------------

**Usage Scenario**

The views in the ascending order of levels are as follows:

* User view
* System view
* Routing protocol view, interface view, or VPN group viewYou can run the **quit** command to return from the current command view to a lower-level command view.

**Configuration Impact**

Run the **quit** command in the user view to log out of the system.


Example
-------

# Return to the system view from the interface view, and then return to the user view.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] quit
[~HUAWEI] quit

```