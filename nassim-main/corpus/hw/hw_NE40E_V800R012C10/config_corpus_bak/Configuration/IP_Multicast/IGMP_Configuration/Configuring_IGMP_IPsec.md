Configuring IGMP IPsec
======================

If you want to authenticate the sent and received IGMP messages, configure IGMP IP Security (IPsec). IGMP IPsec protects a device against attacks launched using forged IGMP messages.

#### Usage Scenario

IGMP IPsec provides a complete set of security protection mechanisms to authenticate the sent and received IGMP messages, protecting devices against attacks launched using forged IGMP messages.

IGMP IPsec configured in the interface view has the same function as that configured in the IGMP view, but their application scopes are different:

* IGMP IPsec configured in the interface view applies only to the current interface.
* IGMP IPsec configured in the IGMP view applies to all interfaces.

IGMP IPsec configured in the interface view takes precedence over IGMP IPsec configured in the IGMP view. If no IGMP IPsec configuration exists in the interface view, the interface uses the IGMP IPsec configuration in the IGMP view.


#### Pre-configuration Tasks

Before configuring IGMP IPsec, complete the following tasks:

* [Configure basic IGMP functions](dc_vrp_multicast_cfg_2044.html).

#### Procedure

* Configure global IGMP IPsec.
  + Configure IPsec authentication for IGMP messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**igmp**](cmdqueryname=igmp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The IGMP view is displayed.
  3. Run [**ipsec sa**](cmdqueryname=ipsec+sa) *sa-name*
     
     
     
     IGMP IPsec is configured globally, enabling the device to authenticate the sent and received IGMP messages based on the specified SA.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  + Configure IPsec authentication for IGMP Query messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**igmp**](cmdqueryname=igmp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The IGMP view is displayed.
  3. Run [**query ipsec sa**](cmdqueryname=query+ipsec+sa) *sa-name*
     
     
     
     IGMP IPsec is configured globally, enabling the device to authenticate the sent and received IGMP Query messages based on the specified SA.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the [**ipsec sa**](cmdqueryname=ipsec+sa) and [**query ipsec sa**](cmdqueryname=query+ipsec+sa) commands are both configured, the command configured later overrides the command configured earlier.
* Configure IGMP IPsec in the interface view.
  + Configure IPsec authentication for IGMP messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**igmp ipsec sa**](cmdqueryname=igmp+ipsec+sa) *sa-name*
     
     
     
     IGMP IPsec is configured on an interface, enabling the interface to authenticate the sent and received IGMP messages based on the specified SA.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  + Configure IPsec authentication for IGMP Query messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**igmp query ipsec sa**](cmdqueryname=igmp+query+ipsec+sa) *sa-name*
     
     
     
     IGMP IPsec is configured on an interface, enabling the interface to authenticate the sent and received IGMP Query messages based on the specified SA.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the [**igmp ipsec sa**](cmdqueryname=igmp+ipsec+sa) and [**igmp query ipsec sa**](cmdqueryname=igmp+query+ipsec+sa) commands are both configured, the command configured later overrides the command configured earlier.

#### Verifying the Configuration

Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* ] **interface** [ *interface-type* *interface-number* | **up** | **down** ] **verbose** command to check the detailed configuration on an interface.