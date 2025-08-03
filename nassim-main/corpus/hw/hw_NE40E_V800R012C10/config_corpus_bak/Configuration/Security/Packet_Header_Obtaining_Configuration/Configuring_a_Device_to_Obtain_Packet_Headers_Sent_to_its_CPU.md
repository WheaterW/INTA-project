Configuring a Device to Obtain Packet Headers Sent to its CPU
=============================================================

This section describes how to configure a device to obtain packet headers sent to its central processing unit (CPU).

#### Usage Scenario

With the expansion of networks and the increasing number of applications, device CPUs may become overloaded if required to process large numbers of packets. The high CPU usage deteriorates device performance and affects normal service processing. To address these issues, specify filter criteria and configure devices to obtain packet headers sent to their CPUs based on the criteria. You can then analyze the obtained packet headers and locate network faults accordingly.

Before using an access control list (ACL) as a filter criterion, you must create it. For details about the ACL configuration, see "ACL Configuration" in *NE40E Configuration Guide - IP Services*.


#### Pre-configuration Tasks

Before configuring a device to obtain packet headers sent to its CPU, complete the following tasks:

* Configure link layer protocol parameters for interfaces to ensure that the link layer protocol status of the interfaces is Up.
* Create an ACL.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Configure an ACL rule.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After an ACL rule is configured, the headers of packets that match the ACL rule can be obtained.
   
   With the packet header obtaining function, packets are processed as follows:
   * If packets match the ACL rule with the permit action, their headers are obtained.
   * If packets match the ACL rule with the deny action, they are dropped instead of being forwarded. This may adversely affect services.
   * If packets match no ACL rule, they are properly forwarded, without having their headers obtained.
   * If the referenced ACL does not exist or an existent ACL in which no rule is defined is referenced, packets are properly forwarded, without having their headers obtained.
   * When packets are matched against an ACL rule, the **vpn-instance** *vpn-instance-name* parameter configured in the rule does not take effect.
   
   **Table 1** ACL rule configuration
   | ACL Configuration Category | Step 1: ACL Creation Through the [**acl**](cmdqueryname=acl) Command | Step 2: ACL Rule Configuration Through the [**rule**](cmdqueryname=rule) Command |
   | --- | --- | --- |
   | Configuring a Basic ACL | [Creating a Basic ACL](dc_vrp_acl4_cfg_0050.html) | [Configuring a Basic ACL Rule](dc_vrp_acl4_cfg_0051.html) |
   | Configuring an Advanced ACL | [Creating an Advanced ACL](dc_vrp_acl4_cfg_0056.html) | [Configuring an Advanced ACL Rule](dc_vrp_acl4_cfg_0057.html) |
   | Configuring a Layer 2 ACL | [Creating a Layer 2 ACL](dc_vrp_acl4_cfg_0079.html) | [Configuring Rules for a Layer 2 ACL](dc_vrp_acl4_cfg_0080.html) |
   | Configuring a Basic ACL6 | [Creating a Basic ACL6](dc_vrp_acl6_cfg_0050.html) | [Configuring a Basic ACL6 Rule](dc_vrp_acl6_cfg_0051.html) |
   | Configuring an Advanced ACL6 | [Creating an Advanced ACL6](dc_vrp_acl6_cfg_0056.html) | [Configuring an Advanced ACL6 Rule](dc_vrp_acl6_cfg_0057.html) |
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**capture-packet local-host**](cmdqueryname=capture-packet+local-host)
   
   
   
   The device is configured to obtain packet headers sent to its CPU. For details about the command format, see *Command Reference > Security Commands > Packet Header Getting Configuration Commands > capture-packet local-host*.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * In the preceding command, the *time-value* and *packet-number* parameters can be configured to specify the timeout period and the number of packet headers to be obtained, respectively. If the specified timeout period expires or if the device has obtained the specified number of packet headers, packet header obtaining ends.
   * When configuring parameters for a packet header obtaining instance, set the parameter values based on the traffic volume on the target interface. Specifically, if a large number of packets are forwarded on the interface, set a small value for *time-value* but a large value for *packet-number*. Otherwise, set a large value for *time-value* but a small value for *packet-number*.
   * If you specify **file**, the device saves packet header obtaining information to a packet header obtaining file. If you specify **terminal**, the device displays packet header obtaining information on a terminal screen. When you specify **file**, the device can save packet header obtaining information only to a file with the maximum size of 2 MB each time the packet header obtaining command is run. If the size of packet header obtaining information exceeds 2 MB, the device discards excess information.
   * Obtaining packet headers sent to CPUs has no impact on system performance.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. (Optional) Run [**capture-packet file limit**](cmdqueryname=capture-packet+file+limit) *limit-value*
   
   
   
   The maximum number of packet header obtaining files (.cap files) in the packet header obtaining directory is specified. This command is supported only by the admin VS.

#### Verifying the Configuration

* Run the [**display capture-packet config-state**](cmdqueryname=display+capture-packet+config-state) command to check the configuration of obtaining packet headers sent to the CPU, such as the packet header obtaining index and packet header obtaining file name.
* Run the [**display capture-packet file**](cmdqueryname=display+capture-packet+file) *file-name* [ **original-packet** ] command to check information about the packet header obtaining file.
* Run the [**display capture-packet information**](cmdqueryname=display+capture-packet+information) [ **instance-id** *instance-id* [ **from** *begin-packet-number* [ **to** *end-packet-number* ] ] [ **format-cap** ] [ **verbose** ] ] command to check information about the packet header obtaining instance.