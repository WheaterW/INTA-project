originating-rp
==============

originating-rp

Function
--------



The **originating-rp** command specifies an interface whose address is used to replace the actual source RP address in a source active (SA) message. Such an interface is called a logical RP.

The **undo originating-rp** command restores the default configuration.



By default, an SA message carries the actual source RP address.


Format
------

**originating-rp** { *interface-type* *interface-number* | *interface-name* }

**undo originating-rp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | - |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To implement Anycast-RP in a PIM-SM domain, you must run the originating-rp command. This is because when a Multicast Source Discovery Protocol (MSDP) peer performs the reverse path forwarding (RPF) check on a received SA message, it discards the message if the RP address in the SA message is the same as the local RP address. To prevent this problem, you need to specify a logical RP address for SA messages on each Router where Anycast-RP is to be deployed.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

After this command is run, the SA message sent by the device carries the logical RP address, which replaces the RP address in the SA message header. After reaching the peer, the SA message can pass the RPF check.

**Precautions**

The interface functioning as a logical RP cannot be an actual RP interface. Generally, specify interfaces that set up MSDP peer relationships as logical RPs.


Example
-------

# In the public network instance, specify 100GE 1/0/1 as the logical RP for SA messages.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] originating-rp 100GE 1/0/1

```