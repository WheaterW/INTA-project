terminal command forward matched upper-view
===========================================

terminal command forward matched upper-view

Function
--------



The **terminal command forward matched upper-view** command enables the intelligent rollback function.

The **undo terminal command forward matched upper-view** command disables the intelligent rollback function.



By default, the intelligent rollback function is enabled.


Format
------

**terminal command forward matched upper-view**

**undo terminal command forward matched upper-view**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* When configuring services, you need to enter the view of the command to be configured to complete the configuration. In this case, you need to run the **quit** command repeatedly to exit the current view and enter the required view. The intelligent rollback function allows you to run commands of other views in the current view to reduce repeated quit operations.
* Intelligent rollback enables the system to automatically return to the previous view if a command fails to be executed in the current view. The system continues to attempt to return to the required view until it returns to the system view. If the command is successfully matched, the command is run in the current view and the corresponding view is displayed.
* This function is valid only for sessions where this command is executed.
* If you do not need to use the intelligent rollback function, run the **undo terminal command forward matched upper-view** command to disable the function.

**Precautions**

* If command matching fails because an ambiguous command is entered in the current view, no intelligent rollback can be performed.
* Intelligent rollback is not performed when a command fails to be matched.
* The **undo** commands do not support intelligent rollback.
* If the intelligent rollback function is enabled, commands may be executed in unexpected views, and services may be interrupted. Before configuring a command, check whether the command to be configured exists in the view. If the command does not exist, run the command in the correct view.

Example
-------

# Enable the intelligent rollback function.
```
<HUAWEI> terminal command forward matched upper-view

```