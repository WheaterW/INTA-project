any-flow
========

any-flow

Function
--------



The **any-flow** command creates an Any-Flow view and displays the view, or displays an existing Any-Flow view.

The **undo any-flow** command deletes the Any-Flow view.



By default, no Any-Flow view is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**any-flow**

**undo any-flow**


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

You can run the any-flow command to enter the Any-Flow view. In the Any-Flow view, you can run related commands to analyze network traffic.


Example
-------

# Enter the Any-Flow view.
```
<HUAWEI> system-view
[~HUAWEI] any-flow
[*HUAWEI-any-flow]

```