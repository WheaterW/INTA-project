Configuring an Interface as a Trusted Interface
===============================================

After Dynamic Host Configuration Protocol (DHCP) snooping is enabled, trusted interfaces must be configured so that clients can go online through trusted interfaces.

#### Context

After DHCP snooping is enabled on a device, you can configure interfaces of the device as trusted or untrusted.

* After receiving DHCP reply packets from a trusted interface, the device forwards the packets so that DHCP clients can obtain correct IP addresses.
* After receiving DHCP reply packets from an untrusted interface, the device discards the packets to prevent DHCP clients from obtaining incorrect IP addresses.

Generally, the interfaces connected to legitimate DHCP servers are configured as trusted and all other interfaces are configured as untrusted.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

After DHCP snooping is enabled, trusted interfaces must be configured and server-side interfaces and user-side interfaces must be in the same virtual local area network (VLAN). DHCP clients cannot go online if server-side interfaces and user-side interfaces are in different VLANs.



#### Procedure

* Configure an interface as a trusted interface in a VLAN to prevent Layer 2 devices from bogus DHCP server attacks.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
     
     The VLAN view is displayed.
  3. Run [**dhcp snooping trusted**](cmdqueryname=dhcp+snooping+trusted) [ **interface** *interface-type* *interface-number* ]
     
     An interface is configured as a trusted interface in the VLAN.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Before you configure an interface as a trusted interface in the VLAN view, make sure that the interface is in the VLAN.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure an interface as a trusted interface in the interface view to prevent Layer 3 devices from bogus DHCP server attacks.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The interface view is displayed.
  3. Run [**dhcp snooping trusted**](cmdqueryname=dhcp+snooping+trusted)
     
     The interface is configured as a trusted interface.
     
     The [**dhcp snooping trusted**](cmdqueryname=dhcp+snooping+trusted) command can be configured on the NNI in a VSI scenario. If multiple VSIs share the same NNI, the [**dhcp snooping trusted**](cmdqueryname=dhcp+snooping+trusted) command takes effect on all VSIs, which may provoke the following problems:
     + VSIs cannot be identified when the NNI sends DHCP reply messages to the host. As a result, DHCP snooping does not take effect, but users can go online.
     + The NNI sends DHCP reply messages to the host even when DHCP snooping is not enabled on some of the VSIs, which increases device load.To prevent the preceding problems, do not run the [**dhcp snooping trusted**](cmdqueryname=dhcp+snooping+trusted) command on the NNI, and run the [**dhcp snooping nni server enable**](cmdqueryname=dhcp+snooping+nni+server+enable) command in the VSI view instead.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure interfaces as trusted interfaces in the BD view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     The BD view is displayed.
  3. Run [**dhcp snooping trusted**](cmdqueryname=dhcp+snooping+trusted)
     
     Interfaces in the BD are configured as trusted interfaces.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.