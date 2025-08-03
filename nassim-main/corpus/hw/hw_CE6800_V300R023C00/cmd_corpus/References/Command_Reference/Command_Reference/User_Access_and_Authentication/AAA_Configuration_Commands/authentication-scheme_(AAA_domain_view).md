authentication-scheme (AAA domain view)
=======================================

authentication-scheme (AAA domain view)

Function
--------

The **authentication-scheme** command applies an authentication scheme to a domain.

The **undo authentication-scheme** command restores the default configuration of the authentication scheme in a domain.

By default, the authentication scheme named default is applied to the default domain, the authentication scheme named default is applied to the default\_admin domain, and the authentication scheme named default is applied to other domains.



Format
------

**authentication-scheme** *authentication-scheme-name*

**undo authentication-scheme**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *authentication-scheme-name* | Specifies the name of an authentication scheme. | The value must be an existing authentication scheme name. |




Views
-----

AAA domain view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To authenticate users in a domain, run the authentication-scheme (AAA domain view) command to apply an authentication scheme to a domain.

**Prerequisites**

An authentication scheme has been created and configured with required parameters, for example, the authentication mode and authentication mode for upgrading user levels.



Example
-------

# Apply the authentication scheme named scheme1 to a domain named domain1.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] domain domain1
[*HUAWEI-aaa-domain-domain1] authentication-scheme scheme1

```