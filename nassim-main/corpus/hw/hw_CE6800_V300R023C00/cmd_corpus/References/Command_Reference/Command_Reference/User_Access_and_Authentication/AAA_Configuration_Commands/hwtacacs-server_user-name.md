hwtacacs-server user-name
=========================

hwtacacs-server user-name

Function
--------

The **hwtacacs-server user-name domain-included** command configures the device to encapsulate the domain name in the user name in HWTACACS packets to be sent to an HWTACACS server.

The **hwtacacs-server user-name original** command configures the device not to modify the user name entered by the user in the packets sent to the HWTACACS server.

The **undo hwtacacs-server user-name domain-included** command configures the device not to encapsulate the domain name in the user name when sending HWTACACS packets to an HWTACACS server.

By default, the device does not modify the user name entered by the user in the packets sent to the HWTACACS server.



Format
------

**hwtacacs-server user-name domain-included**

**hwtacacs-server user-name original**

**undo hwtacacs-server user-name domain-included**



Parameters
----------

None


Views
-----

HWTACACS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

The format of a user name is user name@domain name. In the user name, @ is the domain name delimiter.

If the HWTACACS server does not accept the user name with the domain name, run the
**undo hwtacacs-server user-name domain-included** command to delete the domain name from the user name.

**Precautions**

You can modify this configuration only when the HWTACACS server template is not in use.

If the user names in the HWTACACS packets sent from the device to HWTACACS server contain domain names, ensure that the total length of a user name (user name + domain name delimiter + domain name) is not longer than 253 characters; otherwise, the user name cannot be contained in HWTACACS packets. As a result, authentication will fail.If the
**hwtacacs-server user-name domain-included** command has been configured and a user does not use a domain name for authentication, the original user name entered by the user is carried in the requests sent to the HWTACACS server.

Example
-------

# Configure the device to encapsulate the domain name in the user name when sending HWTACACS packets to an HWTACACS server.
```
<HUAWEI> system-view
[~HUAWEI] hwtacacs-server template template1
[*HUAWEI-hwtacacs-template1] hwtacacs-server user-name domain-included

```