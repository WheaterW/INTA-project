Configuring IP Addresses for an Interface
=========================================

Configuring IP Addresses for an Interface

#### Prerequisites

Before configuring IP addresses for an interface, configure link layer protocol parameters for the interface to ensure that its link layer protocol status is up.


#### Context

To run IP services on an interface, configure IP addresses for the interface.

Each interface on a device can be configured with multiple IP addresses. If IP addresses are configured in primary/secondary mode, one primary and multiple secondary IP addresses can be configured on an interface. If the primary or secondary status of IP addresses is ignored, the device does not differentiate between primary and secondary IP addresses.

If IP addresses are configured in primary/secondary mode, you need to configure only one primary IP address for an interface. In some special cases, you need to configure one or more secondary IP addresses for an interface. For example, a device connects to a physical network through one of its interfaces. Hosts on the physical network belong to two different Class C networks. To allow the device to communicate with all the hosts on the physical network, configure a primary IP address and a secondary IP address for the interface on the device.

If the device ignores the primary or secondary status of IP addresses, you need to configure only one IP address for an interface. In some special cases, you need to configure multiple IP addresses for an interface. For example, multiple IP addresses need to be configured for an interface to differentiate user services. To delete an IP address on an interface without affecting other IP addresses during a service cutover, enable the device to ignore the primary or secondary status of IP addresses so that any IP address configured on the interface can be deleted.

By default, IP addresses are configured in primary/secondary mode.

![](public_sys-resources/note_3.0-en-us.png) For IP addresses in primary/secondary mode:

* One primary IP address and multiple secondary IP addresses can be configured on an interface.
* If a secondary IP address exists, the primary IP address cannot be deleted.
* If both primary and secondary IP addresses are configured on an interface of a device, the device cannot be enabled to ignore the primary or secondary status of IP addresses.

For IP addresses whose primary or secondary status is ignored:

* Multiple IP addresses can be configured on an interface.
* Any IP address configured on an interface can be deleted.
* If multiple IP addresses are configured on an interface of a device, the device cannot be configured to differentiate between primary and secondary IP addresses.



#### Procedure

* **For IP addresses whose primary or secondary status is ignored:**
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enable the device to ignore the primary or secondary status of IP addresses.
     
     
     ```
     [ip address ignore primary-sub enable](cmdqueryname=ip+address+ignore+primary-sub+enable)
     ```
  3. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) { interface-name | interface-type interface-number } 
     ```
  4. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
  5. Configure an IP address for the interface.
     
     
     ```
     [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length }[ tag tag-value ]
     ```
     
     You can repeat the command to configure multiple IP addresses for the interface. A maximum of 256 IP addresses can be configured for each interface.
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* **For IP addresses in primary/secondary mode:**
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure the device to differentiate between primary and secondary IP addresses.
     
     
     ```
     [undo ip address ignore primary-sub enable](cmdqueryname=undo+ip+address+ignore+primary-sub+enable)
     ```
  3. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) { interface-name | interface-type interface-number } 
     ```
  4. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
  5. Configure a primary IP address for the interface.
     
     
     ```
     [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length }[ tag tag-value ]
     ```
     
     Each interface has only one primary IP address. If you configure multiple primary IP addresses for an interface, the last configured IP address becomes the primary IP address of the interface.
  6. Configure a secondary IP address for the interface.
     
     
     ```
     [ip address](cmdqueryname=ip+address+sub) ip-address { mask | mask-length } sub [ tag tag-value ]
     ```
     
     To save IP address space, you can configure secondary IP addresses with 31-bit masks for an interface. A maximum of 255 secondary IP addresses can be configured for each interface.
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

* Run the [**display ip interface**](cmdqueryname=display+ip+interface) [ *interface-type* *interface-number* ] or [**display ip interface**](cmdqueryname=display+ip+interface+brief+slot+card+ip-configured+except) **brief** [ *interface-type* [ *interface-number* ] | **slot** *slot-id* [ **card** *card-number* ] | **ip-configured** [ **except** *interface-type* ] ] command to check the IP address configuration of an interface.
* Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] command to check information about an interface.
* Run the [**display ip interface multi-address**](cmdqueryname=display+ip+interface+multi-address) command to check information about all interfaces configured with multiple IP addresses.

#### Example

# Set the primary and secondary IP addresses of 100GE 1/0/1 to 172.16.1.1 and 172.16.2.1, respectively.
```
<HUAWEI> system-view
[~HUAWEI] sysname DeviceA
[*DeviceA] commit
[~DeviceA] interface 100ge 1/0/1
[~DeviceA-100GE1/0/1] undo portswitch 
[*DeviceA-100GE1/0/1] ip address 172.16.1.1 255.255.255.0
[*DeviceA-100GE1/0/1] ip address 172.16.2.1 255.255.255.0 sub
[*DeviceA-100GE1/0/1] quit
[*DeviceA] commit
```

# Verify the configuration.

* Ping a host on the network segment 172.16.1.0 from the device. The ping operation is successful.
  ```
  [~DeviceA] ping 172.16.1.2
    PING 172.16.1.2: 56  data bytes, press CTRL_C to break
      Reply from 172.16.1.2: bytes=56 Sequence=1 ttl=255 time=614 ms
      Reply from 172.16.1.2: bytes=56 Sequence=2 ttl=255 time=16 ms
      Reply from 172.16.1.2: bytes=56 Sequence=3 ttl=255 time=2 ms
      Reply from 172.16.1.2: bytes=56 Sequence=4 ttl=255 time=3 ms
      Reply from 172.16.1.2: bytes=56 Sequence=5 ttl=255 time=2 ms
    --- 172.16.1.2 ping statistics ---
      5 packet(s) transmitted
      5 packet(s) received
      0.00% packet loss
      round-trip min/avg/max = 25/26/27 ms
  ```
* Ping a host on the network segment 172.16.2.0 from the device. The ping operation is successful.
  ```
  [~DeviceA] ping 172.16.2.2
    PING 172.16.2.2: 56  data bytes, press CTRL_C to break
      Reply from 172.16.2.2: bytes=56 Sequence=1 ttl=255 time=13 ms
      Reply from 172.16.2.2: bytes=56 Sequence=2 ttl=255 time=2 ms
      Reply from 172.16.2.2: bytes=56 Sequence=3 ttl=255 time=2 ms
      Reply from 172.16.2.2: bytes=56 Sequence=4 ttl=255 time=2 ms
      Reply from 172.16.2.2: bytes=56 Sequence=5 ttl=255 time=2 ms
    --- 172.16.2.2 ping statistics ---
      5 packet(s) transmitted
      5 packet(s) received
      0.00% packet loss
      round-trip min/avg/max = 25/25/26 ms
  ```