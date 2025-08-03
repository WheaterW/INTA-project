clock synchronization
=====================

clock synchronization

Function
--------



The **clock synchronization enable** command enables clock synchronization for a line clock source.

The **undo clock synchronization enable** command disables clock synchronization for a line clock source.



By default, clock synchronization is disabled for a line clock source.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clock synchronization enable**

**undo clock synchronization enable**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To enable a line clock source to participate in clock source selection, enable clock synchronization for this line clock source.


Example
-------

# Enable clock synchronization for a line clock source.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] clock synchronization enable

```