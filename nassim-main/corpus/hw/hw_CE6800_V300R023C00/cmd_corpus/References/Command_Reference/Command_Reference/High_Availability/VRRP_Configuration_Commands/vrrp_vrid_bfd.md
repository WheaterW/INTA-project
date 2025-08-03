vrrp vrid bfd
=============

vrrp vrid bfd

Function
--------



The **vrrp vrid bfd** command configures parameters for a VRID-based dynamic BFD session.

The **vrrp vrid bfd peer-ip** command creates a VRID-based dynamic BFD session for a VRRP backup group and configures a peer IP address for the session.

The **undo vrrp vrid bfd** command restores the default parameter values for a VRID-based dynamic BFD session, deletes a VRID-based dynamic BFD session and the peer IP address configured for the session.



By default, no VRID-based dynamic BFD session is created for a VRRP backup group. The default minimum intervals at which the local device receives and sends BFD control packets are 10 ms, and the default local detection multiplier is 3.


Format
------

**vrrp vrid** *virtual-router-id* **bfd** **peer-ip** *peer-ip-address*

**vrrp vrid** *virtual-router-id* **bfd** { **min-tx-interval** *transmit-interval* | **min-rx-interval** *receive-interval* | **detect-multiplier** *multiplier-value* } \*

**undo vrrp vrid** *virtual-router-id* **bfd**

**undo vrrp vrid** *virtual-router-id* **bfd** { **min-tx-interval** | **min-rx-interval** | **detect-multiplier** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer-ip** *peer-ip-address* | Specifies the peer IP address of a VRID-based dynamic BFD session. | It is in dotted decimal notation. |
| **vrid** *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |
| **min-tx-interval** *transmit-interval* | Specifies the minimum interval at which the local device sends BFD control packets. | The value is an integer that ranges from 10 to 1000, in milliseconds. |
| **min-rx-interval** *receive-interval* | Specifies the expected minimum interval at which the local device receives BFD control packets. | The value is an integer that ranges from 10 to 1000, in milliseconds. |
| **detect-multiplier** *multiplier-value* | Specifies the local detection multiplier. | The value is an integer ranging from 3 to 50. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the link between devices in a VRRP backup group fails, the VRRP backup group performs a master/backup VRRP switchover only after a period of three times the interval at which VRRP Advertisement packets are sent. During this period, service data may be lost. To prevent this issue, run the **vrrp vrid bfd** command to create a VRID-based dynamic BFD session for the VRRP backup group. After the creation is complete, the BFD session monitors the link status in real time. When the BFD session detects a link fault and goes Down, the BFD module immediately instructs the VRRP module to perform a rapid master/backup VRRP switchover.

**Prerequisites**

* **vrrp vrid virtual-ip** command.
* **bfd** command.

**Configuration Impact**

After you run the **vrrp vrid bfd** command to create a VRID-based dynamic BFD session for a VRRP backup group, you cannot associate the VRRP backup group with a peer BFD session.The actual minimum interval at which the local device receives BFD control packets is obtained after the negotiation between the locally configured receive-interval value and the remotely configured transmit-interval value. If the local device does not receive any BFD control packet from its peer within the actual minimum interval multiplied by the multiplier-value value, the local device declares that the link fails and notifies the VRRP module of the fault.


Example
-------

# Create a VRID-based dynamic BFD session for VRRP backup group 1 on 100GE 1/0/7, and set the peer IP address of the session to 10.1.1.2.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] interface 100GE1/0/7
[*HUAWEI-100GE1/0/7] undo portswitch
[*HUAWEI-100GE1/0/7] vrrp vrid 1 virtual-ip 10.1.1.3
[*HUAWEI-100GE1/0/7] vrrp vrid 1 bfd peer-ip 10.1.1.2

```

# Set the minimum interval at which the local device receives BFD control packets and the local detection multiplier to 400 ms and 4, respectively.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] interface 100GE1/0/7
[*HUAWEI-100GE1/0/7] undo portswitch
[*HUAWEI-100GE1/0/7] vrrp vrid 1 virtual-ip 10.1.1.3
[*HUAWEI-100GE1/0/7] vrrp vrid 1 bfd min-rx-interval 400 detect-multiplier 4

```