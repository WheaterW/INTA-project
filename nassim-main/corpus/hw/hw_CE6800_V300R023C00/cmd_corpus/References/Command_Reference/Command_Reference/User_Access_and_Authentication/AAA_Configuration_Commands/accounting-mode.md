accounting-mode
===============

accounting-mode

Function
--------



The **accounting-mode** command configures an accounting mode in an accounting scheme.

The **undo accounting-mode** command restores the default accounting mode in an accounting scheme.



By default, the accounting mode is none.


Format
------

**accounting-mode** { **hwtacacs** | **none** | **radius** }

**undo accounting-mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hwtacacs** | Indicates that accounting is performed by an HWTACACS server. | - |
| **none** | Indicates non-accounting. | - |
| **radius** | Indicates that accounting is performed by a RADIUS server. | - |



Views
-----

Accounting scheme view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Enterprises or carriers need to generate revenue by charging users who are accessing the Internet.When a user goes online, accounting starts after the user is authenticated and authorized. When the user goes offline, accounting stops. The client sends the account packet containing the user's online duration to the accounting server.To charge users, set the accounting mode to RADIUS or HWTACACS. Generally, the accounting mode is consistent with the authentication mode. If you do not need to charge users, set the accounting mode to none.

**Follow-up Procedure**

Apply the accounting scheme to a domain to enable the device to charge the users in the domain using the domain command.

**Precautions**

The device does not support local accounting. When the authentication scheme configured using the authentication-mode command defines local authentication, you need to run the **accounting-mode none** command to configure non-accounting or run the **accounting start-fail** command to configure a policy for accounting-start failures.


Example
-------

# Set the accounting mode to RADIUS in the accounting scheme scheme1.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] accounting-scheme scheme1
[*HUAWEI-aaa-accounting-scheme1] accounting-mode radius

```