radius-server user-name
=======================

radius-server user-name

Function
--------

The **radius-server user-name domain-included** command configures the device to encapsulate the domain name in the user name in RADIUS packets to be sent to a RADIUS server.

The **radius-server user-name original** command configures the device not to modify the user name entered by the user in the packets sent to the RADIUS server.

The **undo radius-server user-name domain-included** command configures the device not to encapsulate the domain name in the user name when sending RADIUS packets to a RADIUS server.

The **undo radius-server user-name domain-included except-eap** command configures the device not to encapsulate the domain name in the user name in RADIUS packets to be sent to a RADIUS server (other authentication modes except EAP authentication).

By default, the device encapsulate the domain name in the user name in the packets sent to the RADIUS server.



Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**radius-server user-name original**

**radius-server user-name domain-included**

**undo radius-server user-name domain-included**

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**undo radius-server user-name domain-included except-eap**



Parameters
----------

None


Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

The format of a user name is user name@domain name. In the user name, @ is the domain name delimiter. The domain name delimiter can also be any of the following symbols: \ / : < > | ' %.

If the RADIUS server does not accept the user name with the domain name, run the
**undo radius-server user-name domain-included** command to delete the domain name from the user name.

**Precautions**

If the user names in the RADIUS packets sent from the device to the RADIUS server contain domain names, ensure that the total length of a user name (user name + domain name delimiter + domain name) is not longer than 253 characters; otherwise, the user name cannot be contained in RADIUS packets. As a result, authentication will fail.

In EAP relay authentication scenarios, if the authentication user name is the domain name carried in the EAP message, run the
**undo radius-server user-name domain-included except-eap** command to disable the device from processing the RADIUS attribute user-name of EAP users.

Example
-------

# Configure the device not to encapsulate the domain name in the user name in RADIUS packets to be sent to a RADIUS server.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template template1
[*HUAWEI-radius-template1] undo radius-server user-name domain-included

```