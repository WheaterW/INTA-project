radius-reject local
===================

radius-reject local

Function
--------



The **radius-reject local** command configures an administrator to be authenticated using the local authentication mode after the administrator's RADIUS authentication request is rejected.

The **undo radius-reject local** command restores the default setting.



By default, an administrator is not authenticated using the local authentication mode after the administrator's RADIUS authentication request is rejected.


Format
------

**radius-reject local**

**undo radius-reject local**


Parameters
----------

None

Views
-----

Authentication scheme view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

By default, after the RADIUS authentication request is rejected, that is, the RADIUS server responds with an Access-Reject packet, the authentication process ends and the administrator fails to be authenticated. To configure an administrator to be authenticated using the local authentication mode after the administrator's RADIUS authentication request is rejected in some special scenarios, run the **radius-reject local** command.

**Precautions**

* This function takes effect only for the administrators.
* To implement this function, the authentication mode must be RADIUS + local authentication.

Example
-------

# Configure an administrator to be authenticated using the local authentication mode after the administrator's RADIUS authentication request is rejected.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] authentication-scheme authen1
[*HUAWEI-aaa-authen-authen1] authentication-mode radius local
[*HUAWEI-aaa-authen-authen1] radius-reject local

```