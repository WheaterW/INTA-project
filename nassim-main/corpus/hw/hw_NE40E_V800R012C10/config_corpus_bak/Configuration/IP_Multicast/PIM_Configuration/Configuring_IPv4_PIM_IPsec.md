Configuring IPv4 PIM IPsec
==========================

If you want to authenticate sent and received IPv4 PIM messages, configure IPv4 PIM IP Security (IPsec). IPv4 PIM IPsec protects a device against attacks launched using forged IPv4 PIM messages.

#### Usage Scenario

IPv4 PIM IPsec provides a complete set of security protection mechanisms to authenticate the sent and received IPv4 PIM messages, protecting devices against attacks launched using forged IPv4 PIM messages.

IPv4 PIM IPsec configured in the interface view has the same effect as that configured in the IPv4 PIM view, but their application scopes are different:

* IPv4 PIM IPsec configured in the interface view: applies only to the current interface.
* IPv4 PIM IPsec configured in the IPv4 PIM view: applies to all interfaces.

IPv4 PIM IPsec configured in the interface view takes precedence over IPv4 PIM IPsec configured in the IPv4 PIM view. If no IPv4 PIM IPsec configuration exists in the interface view, the interface uses the IPv4 PIM IPsec configuration in the IPv4 PIM view.


#### Pre-configuration Tasks

Before configuring IPv4 PIM IPsec, complete the following tasks:

* [Configure PIM-SM](dc_vrp_multicast_cfg_0006.html).

#### Procedure

* Configure IPv4 PIM IPsec in the PIM view.
  + Configure IPsec authentication for IPv4 PIM messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The PIM view is displayed.
  3. Run [**ipsec**](cmdqueryname=ipsec) [ [**unicast-message**](cmdqueryname=unicast-message) ] **sa** *sa-name*
     
     
     
     IPv4 PIM IPsec is configured globally, enabling the device to authenticate the sent and received IPv4 PIM messages based on the specified SA.
     
     If you specify [**unicast-message**](cmdqueryname=unicast-message) in the command, the device authenticates IPv4 PIM unicast messages based on the specified SA.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  + Configure IPsec authentication for IPv4 PIM Hello messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The PIM view is displayed.
  3. Run [**hello ipsec**](cmdqueryname=hello+ipsec) [**sa**](cmdqueryname=sa) *sa-name*
     
     
     
     IPv4 PIM IPsec is configured globally, enabling the device to authenticate the sent and received IPv4 PIM Hello messages based on the specified SA.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the [**ipsec sa**](cmdqueryname=ipsec+sa) and [**hello ipsec sa**](cmdqueryname=hello+ipsec+sa) commands are both configured, the command configured later overrides the command configured earlier.
* Configure IPv4 PIM IPsec in the interface view.
  + Configure IPsec authentication for IPv4 PIM messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**pim ipsec sa**](cmdqueryname=pim+ipsec+sa) *sa-name*
     
     
     
     IPv4 PIM IPsec is configured on the interface, enabling the interface to authenticate the sent and received IPv4 PIM messages based on the specified SA.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  + Configure IPsec authentication for IPv4 PIM Hello messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**pim hello ipsec sa**](cmdqueryname=pim+hello+ipsec+sa) *sa-name*
     
     
     
     IPv4 PIM IPsec is configured on the interface, enabling the interface to authenticate the sent and received IPv4 PIM Hello messages based on the specified SA.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the [**pim ipsec sa**](cmdqueryname=pim+ipsec+sa) and [**pim hello ipsec sa**](cmdqueryname=pim+hello+ipsec+sa) commands are both configured, the command configured later overrides the command configured earlier.

#### Verifying the Configuration

Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* ] **interface** [ *interface-type interface-number* | **up** | **down** ] **verbose** command to check the detailed IPv4 PIM IPsec configuration on an interface.

# Display the IPv4 PIM IPsec configuration on GE 0/1/0. The command output shows that IPv4 PIM IPsec has been configured on GE 0/1/0, the SA is named **sa1**.