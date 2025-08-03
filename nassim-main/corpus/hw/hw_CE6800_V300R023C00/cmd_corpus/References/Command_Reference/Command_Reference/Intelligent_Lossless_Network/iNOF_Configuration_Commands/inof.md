inof
====

inof

Function
--------



The **inof** command enables iNOF and displays the iNOF view.

The **undo inof** command deletes all configurations in the inof view and disables the inof.



By default, iNOF is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**inof**

**undo inof**


Parameters
----------

None

Views
-----

AI Service view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run the **inof** command to enter the iNOF view to configure the iNOF network and manage the hosts connected to the network.


Example
-------

# Enable iNOF and enter the iNOF view.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof]

```