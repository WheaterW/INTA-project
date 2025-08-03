authorization-scheme (AAA view)
===============================

authorization-scheme (AAA view)

Function
--------

The **authorization-scheme** command creates an authorization scheme and enters the authorization scheme view, or directly enters an existing authorization scheme view.

The **undo authorization-scheme** command deletes an authorization scheme.

By default, the default authorization scheme is used. This default authorization scheme can be modified but cannot be deleted. In the default authorization scheme, local authorization is used and command line authorization is disabled.



Format
------

**authorization-scheme** *authorization-scheme-name*

**undo authorization-scheme** *authorization-scheme-name*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *authorization-scheme-name* | Specifies the name of an authorization scheme. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces or the following symbols: / \ : \* ? " < > |. The value cannot be - or --. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

RADIUS integrates authentication and authorization; therefore, RADIUS authorization and authentication must be used together. HWTACACS separates authentication from authorization; therefore, you can configure another authorization type even if HWTACACS authentication, local authentication is used. You must run the **authorization-scheme** command to create an authorization scheme before performing authorization-relevant configurations, for example, setting the authorization mode and command line authorization function.

**Follow-up Procedure**

After an authorization scheme is created:

* Run the **authorization-mode** command to configure an authorization mode in an authorization scheme.
* Run the **authorization-cmd** command to configure command line authorization for users at a certain level.After an authorization scheme is configured, run the authorization-scheme (AAA domain view) command to apply the authorization scheme to a domain.

**Precautions**

* If the configured authorization scheme does not exist, the authorization-scheme (AAA view) command creates an authorization scheme and displays the authorization scheme view.
* If the configured authorization scheme already exists, the authorization-scheme (AAA view) command directly displays the authorization scheme view.To delete the authorization scheme applied to a domain, run the undo authorization-scheme (AAA domain view) command.


Example
-------

# Create an authorization scheme named scheme0.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] authorization-scheme scheme0
[*HUAWEI-aaa-author-scheme0]

```

# Enter the default authorization scheme view.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] authorization-scheme default
[*HUAWEI-aaa-author-default]

```