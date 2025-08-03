domain (System view)
====================

domain (System view)

Function
--------

The **domain admin** command configures a global default domain.

The **undo domain admin** command restores the default setting.

By default, the global default domain for administrators is named default\_admin, and the global default domain for access users is named default.



Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**domain** *domain-name* **admin**

**undo domain admin**

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**domain** *domain-name* **access**

**undo domain access**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *domain-name* | Specifies the name of a global default domain. | The value is a string of 1 to 64 case-insensitive characters. It cannot contain spaces. |
| **admin** | Configures a domain for administrations. | - |
| **access** | Configures a domain for access users.     NOTE:   This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |




Views
-----

System view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

The device can manage users based on domains. A domain is the minimum unit for user management. You can configure an authentication scheme, an authorization scheme, an accounting scheme, and an authentication server template for users in a domain. The domain used by a user is determined by the user name used by the user to log in to the device. If the user name does not contain a domain name or the domain name is not configured on the device, the device cannot determine the domain to which the user belongs. In this case, the device adds the user to the global default domain based on the user type.

Administrators and access users use different global default domains, which are configured using the
**domain domain-name**
*admin*and
**domain domain-name**
*access*commands, respectively.

**Prerequisites**

You must create a domain before configuring the domain as the global default domain.



Example
-------

# Create a domain abc and specify it as an access domain.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] domain abc
[*HUAWEI-aaa-domain-abc] quit
[*HUAWEI-aaa] quit
[*HUAWEI] domain abc access

```

# Create domain abc and specify it as the global default domain of administrators.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] domain abc
[*HUAWEI-aaa-domain-abc] quit
[*HUAWEI-aaa] quit
[*HUAWEI] domain abc admin

```