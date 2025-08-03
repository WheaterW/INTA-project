(Optional) Configuring E-Trunk Parameters
=========================================

To ensure reliable E-Trunk communication, configure proper E-Trunk parameters.

#### Context

For an Eth-Trunk interface that is a member interface of an E-Trunk, the link aggregation control protocol (LACP) system priority and LACP system ID are referred to as the LACP E-Trunk system priority and LACP E-Trunk system ID, respectively.

When an E-Trunk consists of Eth-Trunk interfaces working in static LACP mode, each member Eth-Trunk interface and the connected peer Eth-Trunk interface use LACP E-Trunk system priorities to determine the priority of the device at either end of the Eth-Trunk link. The device with the higher priority functions as the LACP Actor and determines which member interfaces in its Eth-Trunk interface are active based on the interface priorities. The other device selects the member interfaces connected to the active member interfaces on the Actor as active member interfaces.

If the LACP E-Trunk system priority and LACP system priority are both configured, after an Eth-Trunk interface working in static LACP mode is added to an E-Trunk, only the LACP E-Trunk system priority takes effect for the Eth-Trunk interface.

If two devices have the same LACP E-Trunk system priority, the LACP E-Trunk system IDs are used to determine the devices' priorities. A smaller LACP E-Trunk system ID indicates a higher priority.


#### Procedure

* Configure E-Trunk parameters in the system view.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Perform one or more operations in [Table 1](#EN-US_TASK_0172362920__tab_1) to set desired E-Trunk parameters.
     
     **Table 1** E-Trunk parameters
     | E-Trunk Parameter | Command | Description |
     | --- | --- | --- |
     | LACP E-Trunk system ID | [**lacp e-trunk system-id**](cmdqueryname=lacp+e-trunk+system-id) *mac-address* | The LACP E-Trunk system IDs of the two devices in an E-Trunk are optional. However, if they are configured, they must be identical.  The step takes effect only for Eth-Trunk interfaces in static LACP mode that are added to an E-Trunk. |
     | LACP E-Trunk system priority | [**lacp e-trunk priority**](cmdqueryname=lacp+e-trunk+priority) *priority* | Two devices in an E-Trunk must have the same LACP E-Trunk system priority.  The step takes effect only for Eth-Trunk interfaces in static LACP mode that are added to an E-Trunk. |
     | UDP/UDP6 port number used to send and receive E-Trunk packets | [**e-trunk port**](cmdqueryname=e-trunk+port) *port-number*  [**e-trunk ipv6 port**](cmdqueryname=e-trunk+ipv6+port) *port-number*  The *port-number* value is in the range of 1025 to 65535. If the UDP port number in this range is used by another protocol, the port number cannot be used to send or receive E-Trunk packets. | E-Trunk is Huawei-specific. The default UDP/UDP6 port number used to send and receive E-Trunk packets may conflict with the UDP/UDP6 port number used by another protocol. To ensure the forwarding of E-Trunk packets, change the UDP/UDP6 port number used to send and receive E-Trunk packets.  The two devices in an E-Trunk must have the same port number. If you change the UDP/UDP6 port number when E-Trunk is running, complete the change before E-Trunk negotiation times out.  If you change the UDP/UDP6 port number when E-Trunk is running, the two devices in the E-Trunk may not be able to communicate. If E-Trunk negotiation times out, both devices in the E-Trunk may become master devices. |
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure E-Trunk parameters in the E-Trunk view.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
     
     The E-Trunk view is displayed.
  3. Perform one or more operations in [Table 2](#EN-US_TASK_0172362920__tab_2) to set desired E-Trunk parameters.
     
     **Table 2** E-Trunk parameters
     | E-Trunk Parameter | Command | Description |
     | --- | --- | --- |
     | E-Trunk priority | [**priority**](cmdqueryname=priority+%28E-Trunk+view%29) *priority* (E-Trunk view) | The priority values of the two devices are used to determine their master and backup status. The smaller the value, the higher the priority. The device with a higher E-Trunk priority functions as the master device. If the two devices have the same E-Trunk priority, the device with the smaller system ID functions as the master device. |
     | E-Trunk authentication and encryption mode | [**authentication-mode**](cmdqueryname=authentication-mode) { **hmac-sha1** | **hmac-sha256** | **enhanced-hmac-sha256** } | To improve system security, configure the E-Trunk authentication and encryption mode.  Two devices in an E-Trunk must have the same E-Trunk authentication and encryption mode.  To improve system security, run the [**authentication-mode**](cmdqueryname=authentication-mode) command to set the E-Trunk authentication and encryption mode to HMAC-SHA2-256 or ENHANCED-HMAC-SHA256. |
     | Password for encrypting packets | [**security-key**](cmdqueryname=security-key) { **simple** *simple-key* | **cipher** { *cipher-key1* | *cipher-key2* | *cipher-key3* } } | This enhances system security. The same encryption password must be configured on the two devices in an E-Trunk. You can specify **simple** or **cipher** as required. + If **simple** is specified, the password is displayed in clear text in the configuration file. + When the password is encrypted in cipher text mode, the password is displayed as garbled characters in the configuration file.    - *cipher-key1*: If the password is entered in ciphertext, the value is a string of 32 to 432 characters.   - *cipher-key2*: A 24-character ciphertext password configured in an earlier version is also supported in this version.   - *cipher-key3*: If the password is entered in clear text, the value must be a string of 1 to 255 case-sensitive characters. It cannot contain spaces. NOTICE:  If **simple** is specified, the password is displayed in clear text in the configuration file. In this case, other users can obtain the password by querying the configuration file, which poses a security risk. As such, you are advised to select **cipher** to save the password in cipher text.  For security purposes, you are advised not to use the **simple** weak security algorithm. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command first to enable the weak security algorithm function. |
     | Internal at which Hello packets are sent | [**timer hello**](cmdqueryname=timer+hello) *hello-value* | If the peer device is the backup and does not receive Hello packets sent by the local device within the timeout period, the peer device becomes the master after timeout. The timeout period referred to in this case is contained in the Hello packet sent by the peer device rather than the local device.  If the Hello packet from the peer device does not contain the timeout period, the timeout period of the local device is used.  NOTE:  Timeout period = Interval at which Hello packets are sent x Time multiplier for detecting Hello packets. You are recommended to set the Timeout period to larger than 5 minutes. |
     | Time multiplier for detecting Hello packets | [**timer hold-on-failure multiplier**](cmdqueryname=timer+hold-on-failure+multiplier) *multiplier* |
     | Switchback delay time | [**timer revert delay**](cmdqueryname=timer+revert+delay) *delay-value* | When an E-Trunk works together with L2VPN services, after the fault on the master device is rectified, the status of the member Eth-Trunk interface on the master device is restored preferentially over PW. After the master device recovers, if traffic on the member Eth-Trunk interface is immediately switched back to the master device, service traffic will be interrupted.  After the E-Trunk switchover delay is configured, the local member Eth-Trunk interface of the E-Trunk becomes master only when the switchback delay timer expires. This delays switching traffic on the member Eth-Trunk interface back to the master device, and therefore preventing service interruption.  NOTE:  When a master device in an E-Trunk restores from a fault, run the [**revert disable**](cmdqueryname=revert+disable) command to enable the non-revertive function on the E-Trunk to prevent traffic loss caused by the traffic switchback.  The configured E-Trunk switchback delay must be the same on the upstream and downstream devices; otherwise, service traffic may be lost. |
     | Description for an E-Trunk | [**description**](cmdqueryname=description) *description* | The [**description**](cmdqueryname=description) command can be used to configure a description for an E-Trunk configured on a device. The description can contain the name of the remote device. This is convenient for maintenance. |
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.