(Optional) Configuring PPP Negotiation Parameters
=================================================

For a PPP link to be established between two communicating devices that have PPP enabled, configure the following PPP negotiation parameters: MRU, negotiation timeout period, PPP LCP link dead duration, and DNS server IP address.

#### Context

A PPP link is established between two communicating devices after successful LCP negotiation and NCP negotiation. After the physical link goes Up, the two devices enter the link establishment phase, during which one device initiates LCP negotiation. After LCP negotiation succeeds, if the two devices have a network layer protocol configured, the device continues to initiate NCP negotiation on network layer packet attributes and types.

**Table 1** Usage scenario for negotiation parameters
| Negotiation Parameter | Usage Scenario | Negotiation Phase |
| --- | --- | --- |
| PPP MRU | If an MTU is configured on an interface of a PPP link, enable the PPP MRU negotiation function so that interfaces on both ends of the PPP link have the same MTU, which ensures proper data transmission. If the interfaces have different MTUs, the smaller MTU will be selected as the PPP link MTU after the negotiation. | LCP negotiation phase |
| Negotiation timeout period | During LCP negotiation, the local device sends an LCP negotiation packet to the remote device. If the local device does not receive a reply packet from the remote device within the specified negotiation timeout period, the local device resends an LCP negotiation packet. | LCP negotiation phase |
| LCP link dead duration | During LCP negotiation, if the local device fails to receive a reply packet from the remote device after retransmitting LCP negotiation packets for a specified number of times, the LCP negotiation enters the Dead state, and the devices stop performing LCP negotiation. In this situation, configure an LCP link dead duration. After the duration elapses, the local device will re-initiate LCP negotiation. | LCP negotiation phase |
| DNS server IP address | During IPCP negotiation, the local device can either provide a DNS server IP address for the remote device or accept the DNS server IP address assigned by the remote device. A DNS server is responsible for resolving domain names.  * When a device is connected to a remote device over a PPP link, for example, a PC dials up to the device, configure the device to assign a DNS server IP address to the PC. * When a device is connected to a carrier's access server over a PPP link, configure the device to accept the DNS server IP address assigned by the access server. | NCP negotiation phase |
| OSICP and MPLSCP | When the default OSICP and MPLSCP configurations differ on devices that are to communicate, enables or disables negotiation to ensure consistent configurations on both devices. | NCP negotiation phase |


![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, the configuration of Negotiation timeout period is supported only on the admin VS.



#### Procedure

* Configure PPP MRU negotiation.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ppp mru-negotiate**](cmdqueryname=ppp+mru-negotiate) { **ipv4** | **ipv6** }
     
     
     
     MRU negotiation is enabled at the link control layer.
     
     
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     If an IPv6 MTU is configured on the interface, enable PPP IPv6 MRU negotiation for the device. After PPP MRU negotiation is enabled, to make this configuration take effect, you must run the [**shutdown**](cmdqueryname=shutdown), [**commit**](cmdqueryname=commit), [**undo shutdown**](cmdqueryname=undo+shutdown), and [**commit**](cmdqueryname=commit) commands in sequence, or run the [**restart**](cmdqueryname=restart) and [**commit**](cmdqueryname=commit) commands.
* Configure a negotiation timeout period.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ppp timer negotiate**](cmdqueryname=ppp+timer+negotiate) *seconds*
     
     
     
     A negotiation timeout period is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a PPP LCP link dead duration.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ppp timer link-dead**](cmdqueryname=ppp+timer+link-dead) *time*
     
     
     
     The PPP LCP link dead duration is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a DNS server IP address
  
  
  + Configure the device to assign a DNS server IP address to the remote device.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
       
       The interface view is displayed.
    3. Run [**ppp ipcp dns**](cmdqueryname=ppp+ipcp+dns) *primary-dns-address* [ *secondary-dns-address* ]
       
       The device is configured to assign a DNS server IP address to the remote device.
  + Configure the device to accept any DNS server IP address assigned by the remote device.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
       
       The interface view is displayed.
    3. Run [**ppp ipcp dns admit-any**](cmdqueryname=ppp+ipcp+dns+admit-any)
       
       The device is configured to accept any DNS server address assigned by the remote device.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If the remote device forcibly assigns a DNS server address to the local device, the local device may refuse to accept the address, causing a negotiation failure between the two devices. To prevent this situation, run the **ppp ipcp dns admit-any** command to configure the local device to accept any DNS server IP address assigned by the remote device.![](../../../../public_sys-resources/notice_3.0-en-us.png) 
  
  After a DNS server address is configured, to make this configuration take effect, you must run the [**shutdown**](cmdqueryname=shutdown), [**commit**](cmdqueryname=commit), [**undo shutdown**](cmdqueryname=undo+shutdown), [**commit**](cmdqueryname=commit), or [**restart**](cmdqueryname=restart), [**commit**](cmdqueryname=commit) commands.
* Configure the OSICP and MPLSCP
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ppp osicp**](cmdqueryname=ppp+osicp) { **enable** | **disable** } or [**ppp mplscp**](cmdqueryname=ppp+mplscp) { **enable** | **disable** }
     
     
     
     The negotiation between two devices before OSICP and MPLSCP go Up on both devices can be enabled or disabled.
     
     
     
     When the default OSICP and MPLSCP configurations differ on devices that are to communicate, run the [**ppp osicp**](cmdqueryname=ppp+osicp) or [**ppp mplscp**](cmdqueryname=ppp+mplscp) command as follows to ensure consistent configurations on both devices:
     + If OSICP and MPLSCP are configured to go Up without negotiation on a peer device, run the [**ppp osicp**](cmdqueryname=ppp+osicp) **disable** or [**ppp mplscp**](cmdqueryname=ppp+mplscp) **disable** command on a local device.
     + If OSICP and MPLSCP are configured to go Up only after negotiation on a peer device, run the [**ppp osicp**](cmdqueryname=ppp+osicp) **enable** or [**ppp mplscp**](cmdqueryname=ppp+mplscp) **enable** command on a local device.
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Run the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) command in the interface view to make the configuration take effect.