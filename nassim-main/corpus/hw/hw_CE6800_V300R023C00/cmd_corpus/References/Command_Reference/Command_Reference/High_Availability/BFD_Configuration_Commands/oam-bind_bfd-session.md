oam-bind bfd-session
====================

oam-bind bfd-session

Function
--------



The **oam-bind ingress bfd-session** command enables unidirectional fault transmission from a BFD session to an interface.

The **undo oam-bind ingress bfd-session** command disables unidirectional fault transmission from a BFD session to an interface.



By default, fault transmission from a BFD session to an interface is disabled.


Format
------

**oam-bind ingress bfd-session** { *bfd-session-id* | **session-name** *bfd-session-name* } **trigger** **if-down** **egress** **interface** { *interface-name* | *interface-type* *interface-number* }

**undo oam-bind ingress bfd-session** { *bfd-session-id* | **session-name** *bfd-session-name* } **trigger** **if-down** **egress** **interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **session-name** *bfd-session-name* | Specifies·the·BFD·session·name. | The value is a string of 1 to 64 case-sensitive characters, spaces not supported. |
| **trigger** | Triggers an interface status change. | - |
| **if-down** | Configures the associated interface to go down. | - |
| **egress** | Specifies the interface associated with downstream traffic. | - |
| **interface** *interface-name* *interface-type* *interface-number* | Specifies the name, type, and ID of an interface. | - |
| **ingress** | Specifies the session for upstream transmission. | - |
| **bfd-session** *bfd-session-id* | Specifies the local discriminator of a BFD session. | The value is an integer ranging from 1 to 16384. |



Views
-----

OAM management view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Configure unidirectional fault transmission from a BFD session to an interface. When detecting a link fault, the BFD session on the local device notifies the associated interface and triggers the interface to go down. When the faulty link recovers, the BFD session on the local device notifies the associated interface and t riggers the interface to go up.

**Prerequisites**

The transmission of fault information from a BFD session to an interface can be configured only when the following requirements are met:

* A BFD session has been created and its status is UP.
* The BFD session is a static BFD session.
* The BFD session and the interface are associated with each other. That is, after an interface is associated with a BFD session, the interface cannot be associated with other BFD sessions. Likewise, when a BFD session is associated with an interface, the BFD session cannot be associated with another interface.

**Precautions**

The transmission of fault information between a BFD session and an interface can be configured only when the following requirements are met:

* The **oam-bind ingress bfd-session trigger if-down egress interface** command applies only to physical main interfaces.
* If the interface on which BFD session negotiation depends is associated with an interface configured with fault information transmission, the BFD session status and interface status may fail to go up.
* If a BFD session is associated with an interface or tracks an interface, the BFD session trigger function cannot be configured on both the tracked and associated interfaces. Otherwise, the BFD session and interface go down.

Example
-------

# Configure the unidirectional transmission of information about a fault from BFD session to the interface.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd session bind peer-ip 10.10.20.2
[*HUAWEI-bfd-session-session] discriminator local 1
[*HUAWEI-bfd-session-session] discriminator remote 2
[*HUAWEI-bfd-session-session] quit
[*HUAWEI] oam-mgr
[*HUAWEI-oam-mgr] oam-bind ingress bfd-session 1 trigger if-down egress interface 100GE 1/0/1

```