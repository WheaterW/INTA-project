mtu (interface view)
====================

mtu (interface view)

Function
--------



The **mtu** command sets the maximum transfer unit (MTU) value for an interface to send IPv4 packets.

The **undo mtu** command restores the default MTU value for an interface to send IPv4 packets.



By default, the MTU is 1500 bytes. The default MTU value varies according to the hardware and interface. For details, see the parameter description field.


Format
------

**mtu** *mtu*

**undo mtu**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mtu* | Specifies the MTU of an Ethernet interface. | The value is an integer ranging from 46 to 9600, in bytes.  The preceding values are for reference only. The value ranges and default values vary according to hardware and interfaces. The supported interface types, value ranges, and default values depend on the actual device. You can run the display default-parameter interface command to view the MTU of an interface. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Sub-interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, the IP layer controls the maximum length of frames that are sent each time. Any time the IP layer receives an IP packet to be sent, it checks to which local interface the packet is to be sent and queries the MTU of the interface. Then, the IP layer compares the MTU with the packet length to be sent. If the packet length is greater than the MTU, the IP layer fragments the packet to ensure that the length of each fragment is smaller or equal to the MTU.If forcible unfragmentation is configured, certain packets are lost during data transmission at the IP layer. To ensure jumbo packets are not dropped during transmission, you need to configure forcible fragmentation. In this case, you can run the mtu command to set the size of a fragment.

**Configuration Impact**

If the MTU is set too small and the size of packets is large, packets are broken into a great number of fragments, and may be discarded by QoS queues.

**Precautions**

The device supports MTU check for IP packets forwarded by the CPU through software, but does not support MTU check for IP packets forwarded by the chip.It is recommended that the MTUs at both ends of a link be the same to prevent impact on the running of protocols such as OSPF and IS-IS and packet forwarding. After an OSPF or IS-IS neighbor relationship is established, changing the MTU of a single-ended interface may cause the neighbor relationship to be disconnected.For IS-IS:

* If the MTU configured on an interface is smaller than the value of max-size configured using the lsp-length originate command plus 3, the neighbor relationship on the interface goes Down immediately.
* By default, a broadcast interface sends standard Hello packets with the padding field. If the MTUs on both ends of a link are different, the local or remote neighbor may go Down due to timeout.
* After the neighbor relationship is established on a P2P interface or a broadcast interface configured with isis small-hello, the interface sends small Hello packets without the padding field. After a neighbor relationship is established, if the MTUs of the interfaces on both ends of the link are changed to be different, the neighbor relationship does not go Down immediately. However, the neighbor relationship may fail to be re-established after it goes Down due to other reasons.

For the OSPF protocol:

* By default, MTU check is disabled on an OSPF interface, and the MTU value is 0 when the interface sends DD packets. If the MTUs of the two ends of a link are different, the OSPF neighbor relationship can be established. Changing the interface MTU does not re-establish the neighbor relationship. However, the packets whose length exceeds the local MTU sent by the peer end may be discarded, and the routes carried in the packets cannot be learned. As a result, services may be interrupted.
* After the **ospf mtu-enable** command is run on an OSPF interface and MTU check is enabled, the interface fills in the MTU value when sending DD packets. In addition, the device checks whether the MTU carried in the DD packet from the neighbor exceeds the local MTU. If the MTU exceeds the local MTU, the device does not establish an OSPF neighbor relationship. If the interface MTU is changed, the device attempts to reestablish an OSPF neighbor relationship. If the MTUs are different, the OSPF neighbor relationship cannot be established.


Example
-------

# Set the MTU of an interface to 1400.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] mtu 1400

```