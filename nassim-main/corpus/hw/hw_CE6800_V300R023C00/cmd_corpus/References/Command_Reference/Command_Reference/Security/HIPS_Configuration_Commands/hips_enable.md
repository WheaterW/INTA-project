hips enable
===========

hips enable

Function
--------



The **hips enable** command enables the host-based intrusion prevention system (HIPS).

The **undo hips enable** command disables HIPS.



By default, HIPS is enabled.


Format
------

**hips enable**

**undo hips enable**


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

**Usage Scenario**

After HIPS is enabled, the policy file determines whether each detection module is enabled.


Example
-------

# Enable HIPS.
```
<HUAWEI> system-view
[~HUAWEI] hips enable

```