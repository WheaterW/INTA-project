trustem
=======

trustem

Function
--------



The **trustem** command creates and displays the trusted management view.

The **undo trustem** command deletes the trusted management view.



By default, no trusted management view is created.


Format
------

**trustem**

**undo trustem**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **trustem** command to enter the trusted management view and configure remote attestation.

**Precautions**

Only HTM profiles support this command.


Example
-------

# Enter the trusted management view.
```
<HUAWEI> system-view
[~HUAWEI] trustem

```