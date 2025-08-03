Configuring MLD IPsec
=====================

If you want to encrypt and authenticate the sent and received MLD messages, configure MLD IP Security (IPsec). MLD IPsec protects a device against attacks launched using forged MLD messages.

#### Usage Scenario

MLD IPsec provides a complete set of security protection mechanisms to authenticate the sent and received MLD messages, protecting devices against attacks launched using forged MLD messages.

MLD IPsec configured in the interface view has the same function as that configured in the MLD view, but their application scopes are different:

* MLD IPsec configured in the interface view: applies only to the current interface.
* MLD IPsec configured in the MLD view: applies to all interfaces.

MLD IPsec configured in the interface view takes precedence over MLD IPsec configured in the MLD view. If no MLD IPsec configuration exists in the interface view, the interface uses the MLD IPsec configuration in the MLD view.


#### Pre-configuration Tasks

Before configuring MLD IPsec, complete the following tasks:

* [Configure basic MLD functions](dc_vrp_multicast_cfg_2073.html).
* Configure basic IPsec functions.

#### Procedure

* Configure global MLD IPsec.
  + Configure IPsec authentication for MLD messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mld**](cmdqueryname=mld)
     
     
     
     The MLD view is displayed.
  3. Run [**ipsec sa**](cmdqueryname=ipsec+sa) *sa-name*
     
     
     
     MLD IPsec is configured globally, enabling the device to authenticate the sent and received MLD messages based on the specified SA policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  + Configure IPsec authentication for MLD Query messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mld**](cmdqueryname=mld)
     
     
     
     The MLD view is displayed.
  3. Run [**query ipsec sa**](cmdqueryname=query+ipsec+sa) *sa-name*
     
     
     
     MLD IPsec is configured globally, enabling the device to authenticate the sent and received MLD Query messages based on the specified SA policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the [**ipsec sa**](cmdqueryname=ipsec+sa) and [**query ipsec sa**](cmdqueryname=query+ipsec+sa) commands are both configured, the command configured later overrides the command configured earlier.
* Configure MLD IPsec in the interface view.
  + Configure IPsec authentication for MLD messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**mld ipsec sa**](cmdqueryname=mld+ipsec+sa) *sa-name*
     
     
     
     MLD IPsec is configured on an interface, enabling the interface to authenticate the sent and received MLD messages based on the specified SA policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  + Configure IPsec authentication for MLD Query messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**mld query ipsec sa**](cmdqueryname=mld+query+ipsec+sa) *sa-name*
     
     
     
     MLD IPsec is configured on an interface, enabling the interface to authenticate the sent and received MLD Query messages based on the specified SA policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the [**mld ipsec sa**](cmdqueryname=mld+ipsec+sa) and [**mld query ipsec sa**](cmdqueryname=mld+query+ipsec+sa) commands are both configured, the command configured later overrides the command configured earlier.

#### Checking the Configurations

Run the [**display mld interface**](cmdqueryname=display+mld+interface) [ *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ] command to check the detailed MLD IPsec configuration on an interface.