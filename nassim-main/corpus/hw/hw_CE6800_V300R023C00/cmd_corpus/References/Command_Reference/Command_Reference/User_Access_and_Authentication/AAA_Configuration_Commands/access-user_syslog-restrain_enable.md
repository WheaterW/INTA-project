access-user syslog-restrain enable
==================================

access-user syslog-restrain enable

Function
--------

The **access-user syslog-restrain enable** command enables system log suppression.

The **undo access-user syslog-restrain enable** command disables system log suppression.

By default, system log suppression is not enabled.



Format
------

**access-user syslog-restrain enable**

**undo access-user syslog-restrain enable**



Parameters
----------

None


Views
-----

System view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

When a user fails in authentication or goes offline, the device records a system log. The system log contains the MAC addresses of access device and access user and the authentication time.

If a user repeatedly attempts to go online after authentication failures or frequently goes online and offline in a short period, a lot of system logs are generated, which waste system resources and degrade system performance. System log suppression can address this problem. After the device generates a system log, it will not generate the same log within the suppression period (set by access-user syslog-restrain period).

**Precautions**

The same system logs refer to the system logs containing the same MAC addresses. For example, after the device generates a system log for a user failing in authentication, the device will not generate new system log for this user in the suppression period if the user fails in authentication again. The system logs for users logging offline are generated in the same way. If a system log has no MAC address, such system logs are suppressed based on the user name.



Example
-------

# Enable system log suppression.
```
<HUAWEI> system-view
[~HUAWEI] access-user syslog-restrain enable

```