Configuring IPv6 PIM IPsec
==========================

If you want to encrypt and authenticate sent and received IPv6 PIM messages, configure IPv6 PIM IP Security (IPsec). IPv6 PIM IPsec protects a device against attacks launched using forged IPv6 PIM messages.

#### Usage Scenario

IPv6 PIM IPsec provides a complete set of security protection mechanisms to authenticate the sent and received IPv6 PIM messages, protecting devices against attacks launched using forged IPv6 PIM messages.

IPv6 PIM IPsec configured in the interface view has the same effect as that configured in the IPv6 PIM view, but their application scopes are different:

* IPv6 PIM IPsec configured in the interface view: applies only to the current interface.
* IPv6 PIM IPsec configured in the IPv6 PIM view: applies to all interfaces.

IPv6 PIM IPsec configured in the interface view takes precedence over IPv6 PIM IPsec configured in the IPv6 PIM view. If no IPv6 PIM IPsec configuration exists in the interface view, the interface uses the IPv6 PIM IPsec configuration in the IPv6 PIM view.


#### Pre-configuration Tasks

Before configuring IPv6 PIM IPsec, complete the following tasks:

* [Configure IPv6 PIM-SM](dc_vrp_multicast_cfg_2005.html).
* Configure basic IPsec functions.

#### Procedure

* Configure global IPv6 PIM IPsec.
  + Configure IPsec authentication for IPv6 PIM messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
     
     
     
     The IPv6 PIM view is displayed.
  3. Run [**ipsec**](cmdqueryname=ipsec) [ **unicast-message** ] **sa** *sa-name*
     
     
     
     IPv6 PIM IPsec is configured globally, enabling the device to authenticate the sent and received IPv6 PIM messages based on the specified SA policy. If you specify [**unicast-message**](cmdqueryname=unicast-message) in the command, the device authenticates only the sent and received IPv6 PIM unicast messages based on the specified SA policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  + Configure IPsec authentication only for IPv6 PIM Hello messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
     
     
     
     The IPv6 PIM view is displayed.
  3. Run [**hello ipsec**](cmdqueryname=hello+ipsec) **sa** *sa-name*
     
     
     
     IPv6 PIM IPsec is configured globally, enabling the device to authenticate the sent and received IPv6 PIM Hello messages based on the specified SA policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the [**ipsec sa**](cmdqueryname=ipsec+sa) and [**hello ipsec sa**](cmdqueryname=hello+ipsec+sa) commands are both configured, the command configured later overrides the command configured earlier.
* Configure IPv6 PIM IPsec in the interface view.
  + Configure IPsec authentication for IPv6 PIM messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**pim ipv6 ipsec sa**](cmdqueryname=pim+ipv6+ipsec+sa) *sa-name*
     
     
     
     IPv6 PIM IPsec is configured on the interface, enabling the interface to authenticate the sent and received IPv6 PIM messages based on the specified SA policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  + Configure IPsec authentication for IPv6 PIM Hello messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**pim ipv6 hello ipsec sa**](cmdqueryname=pim+ipv6+hello+ipsec+sa) *sa-name*
     
     
     
     IPv6 PIM IPsec is configured on the interface, enabling the interface to authenticate the sent and received IPv6 PIM Hello messages based on the specified SA policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the [**pim ipv6 ipsec sa**](cmdqueryname=pim+ipv6+ipsec+sa) and [**pim ipv6 hello ipsec sa**](cmdqueryname=pim+ipv6+hello+ipsec+sa) commands are both configured, the command configured later overrides the command configured earlier.

#### Checking the Configurations

Run the [**display pim ipv6 interface**](cmdqueryname=display+pim+ipv6+interface) *interface-type interface-number* **verbose** command to check the detailed IPv6 PIM IPsec configuration on an interface.

# Display the IPv6 PIM IPsec configuration on GE0/1/0. The command output shows that IPv6 PIM IPsec has been configured on GE0/1/0, the SA policy is named **1**, and IPsec authentication applies only to IPv6 PIM Hello messages.