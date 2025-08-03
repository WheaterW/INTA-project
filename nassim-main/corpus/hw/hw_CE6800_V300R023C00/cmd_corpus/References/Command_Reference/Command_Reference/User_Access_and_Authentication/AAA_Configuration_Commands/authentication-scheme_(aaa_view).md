authentication-scheme (aaa view)
================================

authentication-scheme (aaa view)

Function
--------

The **authentication-scheme** command creates an authentication scheme and displays its view.

The **undo authentication-scheme** command deletes an authentication scheme.

By default, the authentication scheme named default exists on the device. It can be modified but cannot be deleted. Its policy is as follows:

* Local authentication is used.
* If a user fails the authentication, the user is disconnected.

By default, the system has an authentication scheme named radius. Its policy is as follows:

* RADIUS authentication is used.
* If a user fails the authentication, the user is disconnected.



Format
------

**authentication-scheme** *authentication-scheme-name*

**undo authentication-scheme** *authentication-scheme-name*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *authentication-scheme-name* | Specifies the name of an authentication scheme. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces or the following symbols: / \ : \* ? " < > | . The value cannot be - or --. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To authenticate users, run the **authentication-scheme** command to create an authentication scheme. Creating an authentication scheme is necessary before performing authentication-relevant configurations.

**Follow-up Procedure**

After an authentication scheme is created, run the authentication-mode (authentication scheme view) command to configure an authentication mode in an authentication scheme.

After an authentication scheme is configured, run the authentication-scheme (AAA domain view) command to apply the authentication scheme to a domain.

**Precautions**

If the configured authentication scheme does not exist, the **authentication-scheme** command creates an authentication scheme and displays the authentication scheme view. If the configured authentication scheme already exists, the **authentication-scheme** command directly displays the authentication scheme view.To delete an authentication scheme applied to a domain, run the undo authentication-scheme (AAA domain view) command.



Example
-------

# Create an authentication scheme named newscheme.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] authentication-scheme newscheme
[*HUAWEI-aaa-authentication-newscheme]

```

# Access the default authentication scheme view.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] authentication-scheme default
[*HUAWEI-aaa-authentication-default]

```