inof bfd enable
===============

inof bfd enable

Function
--------



The **inof bfd enable** command enables the BFD for iNOF function.

The **undo inof bfd enable** command disables the BFD for iNOF function.



By default, the BFD for iNOF function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**inof bfd enable**

**undo inof bfd enable**


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

You can run this command to enable BFD in the iNOF system for fast link fault detection. In this way, the link fault information can be notified to hosts in the same iNOF zone in time, ensuring timely link switching.

**Prerequisites**

Before running this command, ensure the following operations have been performed:

* BFD has been globally enabled using the **bfd** command in the system view.
* iNOF has been enabled and the iNOF view has been entered using the inof command in the AI service view.

**Precautions**

The BFD for iNOF function depends on the global BFD function and takes effect only after BFD is enabled globally.This command can be configured only when the device functions as an iNOF reflector.


Example
-------

# Enable the BFD for iNOF function.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] inof bfd enable

```