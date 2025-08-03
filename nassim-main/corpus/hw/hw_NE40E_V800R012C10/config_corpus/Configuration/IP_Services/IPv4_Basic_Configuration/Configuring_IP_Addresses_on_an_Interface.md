Configuring IP Addresses on an Interface
========================================

This section describes how to configure IP addresses for a device so that the device can communicate with other devices on the network.

#### Usage Scenario

To run IP services on an interface, configure an IP address for the interface. Each interface on a device can be configured with multiple IP addresses. If IP addresses are configured in primary or secondary mode, one primary and multiple secondary IP addresses can be configured on an interface. If the primary or secondary status of IP addresses is ignored, the device does not differentiate primary IP addresses from secondary IP addresses.

If IP addresses are configured in primary or secondary mode, you need to configure only one primary IP address for an interface. In some special cases, you need to configure one or more secondary IP addresses for an interface. For example, a device connects to a physical network through one of its interfaces. Hosts on the physical network belong to two different Class C networks. To allow the device to communicate with all the hosts on the physical network, configure a primary IP address and a secondary IP address for the interface on the device.

If the device ignores the primary or secondary status of IP addresses, you need to configure only one IP address for an interface. In some special cases, you need to configure multiple IP addresses for an interface. For example, multiple IP addresses need to be configured on an interface to differentiate user services. To delete an IP address on an interface without affecting other IP addresses during a service cutover, enable the device to ignore the primary or secondary status of IP addresses so that any IP address configured on the interface can be deleted.

By default, IP addresses are configured in primary or secondary mode.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* For IP addresses in primary/secondary mode:
  + One primary IP address and multiple secondary IP addresses can be configured on an interface.
  + If a secondary IP address exists, the primary IP address cannot be deleted.
  + If both primary and secondary IP addresses are configured on an interface of a device, you must delete the secondary IP address before enabling the device to ignore the primary/secondary status of IP addresses. Therefore, to prevent user services associated with the secondary IP address from being affected, plan the configuration in advance.
* For IP addresses whose primary or secondary status is ignored:
  + Multiple IP addresses can be configured on an interface.
  + Any IP address configured on an interface can be deleted.
  + If multiple IP addresses are configured on an interface of a device, the device cannot be configured to directly differentiate between primary and secondary IP addresses.
  + The [**ip address ignore primary-sub enable**](cmdqueryname=ip+address+ignore+primary-sub+enable) and [**ip address conflict check disable**](cmdqueryname=ip+address+conflict+check+disable) commands are mutually exclusive.
#### Pre-configuration Tasks

Before configuring IP addresses on an interface, configure link layer protocol parameters for the interface and ensure that the link layer protocol of the interface is Up.



#### Procedure

* **For IP addresses whose primary or secondary status is ignored:**
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**ip address ignore primary-sub enable**](cmdqueryname=ip+address+ignore+primary-sub+enable)
     
     The device is enabled to ignore the primary or secondary status of IP addresses.
     
     For IP addresses in primary/secondary mode, the device uses the primary IP address of the interface to interact with other devices when processing certain services. For IP addresses whose primary or secondary status is ignored, the device uses the first IP address of the interface to interact with other devices when processing certain services. For example, a routing protocol uses the first IP address of an interface to establish a neighbor relationship (you can run the [**display this**](cmdqueryname=display+this) command on the interface to check whether the first IP address of the interface is used to establish a neighbor relationship).
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The interface view is displayed.
  5. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **tag** *tag-value* ]
     
     An IP address is configured for the interface.
     
     Run this command multiple times on the interface to configure multiple IP addresses for the interface.
     
     A maximum of 256 IP addresses can be configured for each interface.
  6. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* **For IP addresses in primary/secondary mode:**
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. (Optional) Run [**undo ip address ignore primary-sub enable**](cmdqueryname=undo+ip+address+ignore+primary-sub+enable)
     
     The device is configured to differentiate primary IP addresses from secondary IP addresses.
  3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The interface view is displayed.
  4. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **tag** *tag-value* ]
     
     A primary IP address is configured.
     
     An interface can have only one primary IP address. If the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **tag** *tag-value* ] command is run more than once to configure a primary IP address for an interface, the latest configuration overrides the previous one.
  5. (Optional) Run [**ip address**](cmdqueryname=ip+address+sub) *ip-address* { *mask* | *mask-length* } **sub** [ **tag** *tag-value* ]
     
     A secondary IP address is configured for the interface.
     
     To save the IP address space, you can configure secondary IP addresses with 31-bit masks for an interface.
     
     A maximum of 255 secondary IP addresses can be configured for each interface.
  6. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Verifying the Configuration

* Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] command to check interface information.
* Run the [**display ip interface multi-address**](cmdqueryname=display+ip+interface+multi-address) command to check all interfaces configured with multiple IP addresses.