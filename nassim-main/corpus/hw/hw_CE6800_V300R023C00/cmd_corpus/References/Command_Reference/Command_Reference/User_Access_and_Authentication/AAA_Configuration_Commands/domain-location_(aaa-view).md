domain-location (aaa-view)
==========================

domain-location (aaa-view)

Function
--------

The **domain-location** command configures the position of a domain name.

The **undo domain-location** command restores the default position of a domain name.

By default, the domain name in the AAA view is placed behind the domain name delimiter.



Format
------

**domain-location** { **after-delimiter** | **before-delimiter** }

**undo domain-location**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **after-delimiter** | Indicates that the domain name is placed behind the domain name delimiter. | - |
| **before-delimiter** | Indicates that the domain name is placed before the domain name delimiter. | - |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

The format of a user name is user name@domain name. If before-delimiter is specified, the format domain name@user name is used.

You can use the domain-location command only when there is no online user.

**Precautions**

If you run the domain-location command in the AAA view, the position of a domain is configured globally and the configuration takes effect for all users.



Example
-------

# Configure the domain name before the domain name delimiter.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] domain-location before-delimiter

```