return
======

return

Function
--------



The **return** command enables the system to return to the user view from any other review.




Format
------

**return**


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

You can run the **return** command to return to the user view from another view.

**Configuration Impact**

* When the current view is not the user view, run the **return** command, and you can return to the user view.
* When the current view is the user view, run the **return** command, and you still stay in the user view.

**Precautions**

You can press the shortcut key Ctrl+Z that functions the same as the **return** command.


Example
-------

# Return from the system view to the user view.
```
<HUAWEI> system-view
[~HUAWEI] return
<HUAWEI>

```