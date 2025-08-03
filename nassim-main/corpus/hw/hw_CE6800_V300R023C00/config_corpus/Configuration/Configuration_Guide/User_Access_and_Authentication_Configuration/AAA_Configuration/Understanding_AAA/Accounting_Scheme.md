Accounting Scheme
=================

An accounting scheme defines a user accounting method.

#### Accounting Methods Supported by a Device

* RADIUS accounting: A RADIUS server is used to perform user accounting.
* HWTACACS accounting: An HWTACACS server is used to perform user accounting.
* Non-accounting: Users can access a network without being charged.

You can specify only one accounting method at a time in an accounting scheme.


#### Order in Which Accounting Methods Take Effect

According to [RADIUS Packets](galaxy_aaa_cfg_0023.html), RADIUS accounting packets are classified into Accounting-Request and Accounting-Response packets. After the accounting function is enabled, the device sends Accounting-Request packets recording user activities to the AAA server. The AAA server then performs user accounting and auditing based on information in the packets. The following example uses RADIUS accounting. Accounting-Request packets are divided into three types:

* Accounting-Request(Start) packet: When a user is successfully authenticated and begins to access network resources, the device sends an Accounting-Request(Start) packet to the RADIUS server.
* Accounting-Request(Stop) packet: When a user is disconnected proactively (or forcibly by the NAS), the device sends an Accounting-Request(Stop) packet to the server.
* Accounting-Request(Interim-update) packet: To reduce the accounting deviation and ensure that the accounting server can receive Accounting-Request(Stop) packets and stop user accounting, you can configure the real-time accounting function on the device. In this case, the device periodically sends an Accounting-Request(Interim-update) packet to the RADIUS server.

Typically, each Accounting-Request packet sent by a device is responded by the server with an Accounting-Response packet. If the device does not receive a corresponding Accounting-Response packet due to network faults, accounting fails. If accounting fails, the device uses a specific policy to determine whether a user can remain online based on the Accounting-Request packet type. This policy is called an accounting failure policy. The following describes the accounting failure policies corresponding to different types of Accounting-Request packets:

* Accounting-start failure: The user is allowed to go online by default.
* Real-time accounting failure: The user is allowed to remain online by default.
* Accounting-stop failure: The device retransmits an Accounting-Request(Stop) packet.