hard-zoning enable
==================

hard-zoning enable

Function
--------

The **hard-zoning enable** command enables the iNOF zone isolation function.

The **undo hard-zoning enable** command disables the iNOF zone isolation function.

By default, the iNOF zone isolation function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**hard-zoning enable**

**undo hard-zoning enable**


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

**Usage Scenario**

After iNOF zone isolation takes effect, inter-zone host communication is restricted.

* Hosts in different iNOF zones cannot communicate with each other. Hosts added to the default zone cannot communicate with hosts added to a customized zone.
* Hosts in the same iNOF zone cannot communicate with each other only if they are both initiators or both targets; in other cases, they can communicate with each other.
  
  A host can be added to multiple iNOF customized zones. As long as the zones to which two hosts are added overlap and the two hosts are not both initiators or both targets, they can communicate with each other.

**Precautions**

When the local device functions as an iNOF client, this command cannot be configured.


Example
-------

# Enable the iNOF zone isolation function.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] hard-zoning enable
```