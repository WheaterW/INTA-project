domain-name-delimiter
=====================

domain-name-delimiter

Function
--------

The **domain-name-delimiter** command configures a domain name delimiter.

The **undo domain-name-delimiter** command restores the default domain name delimiter.

By default, the domain name delimiter in the AAA view is @.



Format
------

**domain-name-delimiter** *delimiter*

**undo domain-name-delimiter**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delimiter* | Specifies a domain name delimiter of only one bit. | The value is a string of 1 case-sensitive character. It cannot contain spaces. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

Different AAA servers may use different domain name delimiters. To ensure that an AAA server obtains the correct user name and domain name, configure the same domain name delimiter on the device and the AAA server.

For example, if the domain name delimiter is %, the user name of user1 in the domain dom1 is user1%dom1 or dom1%user1.

**Precautions**

Before using the domain-name-delimiter command, ensure that no local user exists.If you run the domain-name-delimiter command in the AAA view, the domain name delimiter is configured globally and the configuration takes effect for all users.When the command is executed in the AAA view, the configuration takes effect for all users.



Example
-------

# Configure the domain name delimiter as / in the AAA view.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] domain-name-delimiter /

```