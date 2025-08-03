traffic-policy atomic-update-mode
=================================

traffic-policy atomic-update-mode

Function
--------



The **traffic-policy atomic-update-mode** command enables the device to provide nonstop services during MQC-based traffic classification rule modification.

The **undo traffic-policy atomic-update-mode** command cancels the configuration.



By default, this function is disabled.


Format
------

**traffic-policy atomic-update-mode**

**undo traffic-policy atomic-update-mode**


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

After this command is used, the system first delivers the modified traffic classification rules, and then deletes the old traffic classification rules. This ensures nonstop services.

**Precautions**

* After this function is enabled, when editing or modifying traffic classification rules in a traffic policy, ensure that the number of remaining ACL resources is at least one more than the number of chip resources occupied by traffic classification rules in the traffic policy.
* A traffic policy configured with a time range cannot be delivered in atomic update mode. As a result, it cannot be guaranteed that services are not interrupted during traffic policy rule modification.

Example
-------

# Enable the device to provide nonstop services during MQC-based traffic classification rule modification.
```
<HUAWEI> system-view
[~HUAWEI] traffic-policy atomic-update-mode

```