if-match any
============

if-match any

Function
--------



The **if-match any** command configures a matching rule based on all data packets in a traffic classifier.

The **undo if-match any** command deletes a matching rule based on all data packets in a traffic classifier.



By default, a matching rule based on all data packets is not configured in a traffic classifier.


Format
------

**if-match any**

**undo if-match any**


Parameters
----------

None

Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To process all the data packets in the same manner, run the if-match any command.

**Precautions**

If the if-match any, if-match acl, and if-match ipv6 acl commands are configured in the same traffic classifier on the device, the if-match any command takes effect, and the if-match acl and if-match ipv6 acl commands do not take effect. If packets match ACL rules, the if-match acl and if-match ipv6 acl policies take effect. If packets do not match ACL rules, the if-match any policy takes effect.


Example
-------

# Configure a matching rule based on all data packets in the traffic classifier c1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1 type and
[*HUAWEI-classifier-c1] if-match any

```