echo-passive
============

echo-passive

Function
--------



The **echo-passive** command enables passive BFD echo.

The **undo echo-passive** command disables passive BFD echo.



By default, passive BFD echo is disabled.


Format
------

**echo-passive** { **all** | **acl** *basic-acl-number* }

**undo echo-passive**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Enables passive echo for all BFD sessions. | - |
| **acl** *basic-acl-number* | Specifies the number of a basic ACL, which determines rules for enabling passive BFD echo. | The value is an integer ranging from 2000 to 2999. |



Views
-----

BFD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



BFD provides asynchronous detection mode. An auxiliary function of the mode is the echo function, which must work in this mode. When the echo function is activated, the local system sends a BFD control packet and the remote system loops back the packet through the forwarding channel. If several consecutive echo packets are not received, the session is declared to be Down.If a device that supports the echo function is deployed on a network, you can run the **echo-passive** command to enable passive BFD echo for interworking with other vendors' devices.



**Prerequisites**

BFD has been globally enabled using the **bfd** command in the system view.The ACL and its rules have been configured respectively using the **acl** and **rule** commands if an ACL is used to determine rules for enabling passive echo.

**Precautions**

Passive BFD echo applies only to single-hop IP link scenarios and works with asynchronous BFD. When a BFD session works in asynchronous echo mode, the two endpoints of the BFD session perform both slow detection in asynchronous mode and quick detection in echo mode.If an ACL rule is created or modified after a BFD session goes Up through negotiations, this ACL rule can take effect only after the BFD session goes Down and then Up or the parameters of the BFD session are modified.You can enable passive echo for BFD control packets that match the permit action and disable passive echo for BFD control packets that match the deny action or do not match any ACL rules.


Example
-------

# Enable passive echo for BFD sessions that match ACL 2000 rules.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl-basic-2000] rule permit source 10.1.1.1 0
[*HUAWEI-acl-basic-2000] rule permit source 10.1.1.2 0
[*HUAWEI-acl-basic-2000] quit
[*HUAWEI] bfd
[*HUAWEI-bfd] echo-passive acl 2000

```