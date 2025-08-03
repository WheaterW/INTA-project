default-zone enable
===================

default-zone enable

Function
--------



The **default-zone enable** command enables the function of automatically adding hosts to the default zone in an iNOF system.

The **undo default-zone enable** command disables the function of automatically adding hosts to the default zone.



By default, the function of automatically adding hosts to the iNOF default zone is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**default-zone enable**

**undo default-zone enable**


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

An iNOF system has a default zone that does not support manual addition of zone members. You can run this command to enable the function of automatically adding hosts to the default zone in an iNOF system. After this function is enabled, newly connected hosts are automatically added to the default zone as zone members.If the IP address of a host has been manually added to a customized zone in the iNOF system using the **host** command, the host will not be automatically added to the default zone as a zone member.

**Precautions**

The device functions as an iNOF client. The function of automatically adding hosts to the default zone configured locally does not take effect, but the configuration synchronized from the iNOF reflector prevails.


Example
-------

# Disable the function of automatically adding hosts to the default zone in an iNOF system.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] undo default-zone enable

```