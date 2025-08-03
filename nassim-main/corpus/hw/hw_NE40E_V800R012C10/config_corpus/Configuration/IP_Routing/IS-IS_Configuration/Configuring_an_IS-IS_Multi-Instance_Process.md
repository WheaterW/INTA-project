Configuring an IS-IS Multi-Instance Process
===========================================

To reduce the interface count and configuration workload required by multiple conventional IS-IS processes, you can configure IS-IS multi-instance processes. A conventional IS-IS process and multiple IS-IS multi-instance processes can be configured on the same interface.

#### Usage Scenario

On IS-IS networks, multiple IS-IS processes need to be used to isolate different access rings. To close the access rings, the IS-IS processes on all access rings need to be enabled. In this case, you need to enable different IGP processes on one interface. This reduces the interface count and configuration workload of the access rings.


#### Pre-configuration Tasks

Before configuring an IS-IS multi-instance process, complete the following tasks:

* Configure a link layer protocol.
* Configure IP addresses for interfaces and ensure that neighboring devices are reachable at the network layer.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   An IS-IS process is created, and its view is displayed.
   
   
   
   *process-id* specifies the ID of an IS-IS process. If *process-id* is not specified, 1 is used as the IS-IS process ID. To associate an IS-IS process with a VPN instance, run the [**isis**](cmdqueryname=isis) *process-id* **vpn-instance** *vpn-instance-name* command.
3. Run [**multi-instance enable**](cmdqueryname=multi-instance+enable) **iid** *iid-value*
   
   
   
   The IS-IS process is configured as an IS-IS multi-instance process.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
6. Run the [**isis enable**](cmdqueryname=isis+enable) [ *process-id* ] command to enable IS-IS on the interface and associate the IS-IS process with the interface or run the [**isis ipv6 enable**](cmdqueryname=isis+ipv6+enable) *process-id* command to enable IS-IS IPv6 on the interface and associate the IS-IS process with the interface.
7. Configure parameters for the IS-IS multi-instance process as required.
   
   
   * Run the [**isis process-id**](cmdqueryname=isis+process-id) *process-id* [**authentication-mode**](cmdqueryname=authentication-mode) command to configure the IS-IS interface to authenticate Hello packets using the specified authentication mode and password.
   * Run the [**isis process-id**](cmdqueryname=isis+process-id) *process-id* [**cost**](cmdqueryname=cost) command to set a link cost for the IS-IS interface.
   * Run the [**isis process-id**](cmdqueryname=isis+process-id) *process-id* [**ipv6**](cmdqueryname=ipv6) [**cost**](cmdqueryname=cost) command to set a link cost in the IPv6 topology.
   * Run the [**isis process-id**](cmdqueryname=isis+process-id) *process-id* [**circuit-type**](cmdqueryname=circuit-type) command to simulate an IS-IS broadcast interface as a P2P interface.
   * Run the [**isis process-id**](cmdqueryname=isis+process-id) *process-id* [**prefix-sid**](cmdqueryname=prefix-sid) command to configure the IP address of a loopback interface as a Segment Routing prefix segment ID (SID).
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   
   
   For details on how to configure other functions for an IS-IS process, see [Creating an IPv4 IS-IS process](dc_vrp_isis_cfg_1001.html) or [Creating an IPv6 IS-IS process](dc_vrp_isis_cfg_1024.html).

#### Checking the Configurations

After configuring an IS-IS multi-instance process, check the configurations.

* Run the [**display isis**](cmdqueryname=display+isis) **interface** *interface-type* *interface-number* [ **verbose** ] command to check information about the IS-IS interface. The command output shows more than one IS-IS process on the interface.