access-filter
=============

access-filter

Function
--------



The **access-filter** command displays the iNOF host access interface whitelist view.

The **undo access-filter** command deletes the iNOF host access interface whitelist view and all configurations in the view.



By default, the iNOF host access interface whitelist view is not created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**access-filter**

**undo access-filter**


Parameters
----------

None

Views
-----

iNOF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to enter the iNOF host access interface whitelist view and configure a whitelist of interfaces through which hosts access the iNOF.


Example
-------

# Enter the iNOF host access interface whitelist view.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] access-filter
[*HUAWEI-ai-service-inof-access-filter]

```