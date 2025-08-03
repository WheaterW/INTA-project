anti-attack fragment enable
===========================

anti-attack fragment enable

Function
--------



The **anti-attack fragment enable** command enables defense against packet fragment attacks.

The **anti-attack fragment disable** command disables defense against packet fragment attacks.

The **undo anti-attack fragment enable** command disables defense against packet fragment attacks.



By default, defense against packet fragment attacks is enabled.


Format
------

**anti-attack fragment enable**

**anti-attack fragment disable**

**undo anti-attack fragment enable**


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

If an attacker sends error packet fragments to a device, the device consumes a large number of resources to process the error packet fragments, affecting normal services. To prevent the system from breaking down and to ensure normal network services, run the anti-attack fragment enable command to enable defense against packet fragment attacks.The device detects error packet fragments after defense against error packet fragments is enabled. If the device detects error packet fragments, the device limits the rate of these fragments to ensure that the device CPU works properly.


Example
-------

# Enable defense against packet fragment attacks.
```
<HUAWEI> system-view
[~HUAWEI] anti-attack fragment enable

```