Configuring an Initiator
========================

This section describes how to configure an initiator that sends simulated service traffic. You can set initiator parameters based on usage scenarios and test indicator types.

#### Context

On the network shown in [Figure 1](dc_vrp_nqa_cfg_0046.html#EN-US_TASK_0172373103__fig_dc_vrp_nqa_cfg_004601) of "Configuring an RFC 2544 Generalflow Test Instance", the following two roles are involved in a generalflow test:

* Initiator: sends simulated service traffic to a reflector.
* Reflector: loops the service traffic back to the initiator.

The process of configuring the initiator is as follows:

1. Create a generalflow test instance.
2. Configure basic information about simulated service traffic based on test scenarios.
3. Set key test parameters based on indicators.
4. Set generalflow test parameters.
5. Start the generalflow test instance.

#### Procedure

1. Create a generalflow test instance.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name* *test-name* command to create an NQA test instance and enter its view.
   3. Run the [**test-type**](cmdqueryname=test-type) **generalflow** command to set the test instance type to generalflow.
   4. Run the [**measure**](cmdqueryname=measure) { **throughput** | **loss** | **delay** } command to configure the measurement indicator type.
2. Set basic simulated service parameters.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The basic simulated service parameters on the initiator must be the same as those configured on the reflector.
   
   
   | Usage Scenario | Configuration Procedure | Configuration Note |
   | --- | --- | --- |
   | Layer 2 | 1. Run the [**destination-address**](cmdqueryname=destination-address) **mac** *macAddress* command to specify the destination MAC address of test packets. 2. (Optional) Run the [**source-address**](cmdqueryname=source-address) **mac** *mac-address* command to specify the source MAC address of test packets. 3. Run the [**forwarding-simulation inbound-interface**](cmdqueryname=forwarding-simulation+inbound-interface) *interface-type interface-number* [ **share-mode** ]command to specify the inbound interface of simulated service packets.  NOTE:  If **share-mode** is configured, both test flows and non-test flows can pass through; otherwise, only test flows can pass through. 4. Run the [**vlan**](cmdqueryname=vlan) *vlan-id* or [**pe-vid**](cmdqueryname=pe-vid) *pe-vid* **ce-vid** *ce-vid* command to configure VLAN IDs for simulated service packets. | The initiator shown in [Figure 1](dc_vrp_nqa_cfg_0046.html#EN-US_TASK_0172373103__fig_dc_vrp_nqa_cfg_004601) of "Configuring an RFC 2544 Generalflow Test Instance" has the following parameters:  * Destination MAC address: MAC address of the reflector's UNI-B or a MAC address that has never been used * Source MAC address: MAC address of the initiator's UNI-A (simulated inbound interface) or a MAC address that has never been used * Simulated inbound interface: UNI-A * VLAN ID: VLAN IDs configured on interfaces NOTE:  You can run the [**display nqa reflector**](cmdqueryname=display+nqa+reflector) command on the reflector to view the recommended destination MAC address. |
   | Layer 3 | 1. Run the [**destination-address**](cmdqueryname=destination-address) **ipv4** *destAddress* command to specify the destination IP address of test packets. 2. Run the [**source-address**](cmdqueryname=source-address) **ipv4** *srcAddress* command to specify the source IP address of test packets. 3. Run the [**forwarding-simulation inbound-interface**](cmdqueryname=forwarding-simulation+inbound-interface) *interface-type interface-number* command to specify the inbound interface of simulated service packets. 4. (Optional) Run the [**vlan**](cmdqueryname=vlan) *vlan-id* or [**pe-vid**](cmdqueryname=pe-vid) *pe-vid* **ce-vid** *ce-vid* command to configure VLAN IDs for simulated service packets. NOTE:  * If the initiator does not have an ARP entry corresponding to the source IP address in test packets, run the [**arp static**](cmdqueryname=arp+static) *ip-address* *mac-address* command to configure a static ARP entry for the source IP address. * In a Layer 3 scenario, the outbound interface must be specified when static ARP is configured on the initiator. | The initiator shown in [Figure 1](dc_vrp_nqa_cfg_0046.html#EN-US_TASK_0172373103__fig_dc_vrp_nqa_cfg_004601) of "Configuring an RFC 2544 Generalflow Test Instance" has the following parameters:  * Destination IP address: an IP address on the same network segment as the reflector's UNI-B * Source IP address: an IP address on the same network segment as UNI-A's IP address * Simulated inbound interface: UNI-A |
   | IP and IP gateway | 1. Run the [**destination-address**](cmdqueryname=destination-address) **ipv4** *destAddress* command to specify the destination IP address of test packets. 2. Run the [**source-address**](cmdqueryname=source-address) **ipv4** *srcAddress* command to specify the source IP address of test packets. 3. Run the [**source-interface**](cmdqueryname=source-interface) *ifType* *ifNum* command to specify the outbound interface of test packets. 4. (Optional) Run the [**vlan**](cmdqueryname=vlan) *vlan-id* or [**pe-vid**](cmdqueryname=pe-vid) *pe-vid* **ce-vid** *ce-vid* command to configure VLAN IDs for simulated service packets. | The initiator shown in [Figure 1](dc_vrp_nqa_cfg_0046.html#EN-US_TASK_0172373103__fig_dc_vrp_nqa_cfg_004601) of "Configuring an RFC 2544 Generalflow Test Instance" has the following parameters:  * Destination IP address: CE's IP address or an IP address on the same network segment as the CE * Source IP address: an IP address on the same network segment as UNI-A's IP address |
   | L2VPN accessing L3VPN | 1. Run the [**destination-address**](cmdqueryname=destination-address) **ipv4** *destAddress* **mac** *macAddress* command to specify the destination IP and MAC addresses of test packets. 2. Run the [**source-address**](cmdqueryname=source-address) **ipv4** *srcAddress* command to specify the source IP address of test packets. 3. Run the [**forwarding-simulation inbound-interface**](cmdqueryname=forwarding-simulation+inbound-interface) *interface-type interface-number* command to specify the inbound interface of simulated service packets. | The initiator shown in [Figure 1](dc_vrp_nqa_cfg_0046.html#EN-US_TASK_0172373103__fig_dc_vrp_nqa_cfg_004601) of "Configuring an RFC 2544 Generalflow Test Instance" has the following parameters:  * Destination IP address: CE's IP address or an IP address on the same network segment as the CE * Destination MAC address: MAC address of the Layer 3 gateway interface * Source IP address: an IP address on the same network segment as UNI-A's IP address * Simulated inbound interface: UNI-A |
3. Set key test parameters based on indicators.
   
   
   
   | Indicator | Configuration Procedure |
   | --- | --- |
   | Throughput | 1. Run the [**rate**](cmdqueryname=rate) *rateL* *rateH* command to configure upper and lower rate thresholds. 2. Run the [**interval**](cmdqueryname=interval) **seconds** *interval* command to set the interval at which test packets are transmitted at a specific rate. 3. Run the [**precision**](cmdqueryname=precision) *precision-value* command to set the throughput precision. 4. Run the [**fail-ratio**](cmdqueryname=fail-ratio) *fail-ratio-value* command to configure the failure threshold for a throughput test. The value is expressed in 1/10000. During a throughput test, if the actual packet loss rate is lower than the specified threshold, the test is successful and can continue. |
   | Delay | 1. Run the [**rate**](cmdqueryname=rate) *rateL* command to set the rate at which test packets are sent. 2. Run the [**interval**](cmdqueryname=interval) **seconds** *interval* command to set the interval at which test packets are sent. |
   | Packet loss rate | 1. Run the [**rate**](cmdqueryname=rate) *rateL* command to set the rate at which test packets are sent. |
4. Configure common parameters for the test instance.
   1. Run the [**datasize**](cmdqueryname=datasize) *datasizeValue* & <1-7> command to set the size of the Data field in an NQA test packet.
      
      
      
      In Layer 2 and Layer 3 scenarios, the *datasizeValue* value cannot be greater than the maximum MTU of the simulated inbound interface.
   2. Run the [**duration**](cmdqueryname=duration) *duration* command to set the duration of the test instance.
   3. Run the [**records**](cmdqueryname=records) **result** *number* command to configure the maximum number of records in the result table.
   4. Run the [**priority 8021p**](cmdqueryname=priority+8021p) *priority-value* command to configure an 802.1p priority value for generalflow test packets in an Ethernet scenario.
   5. Run the [**tos**](cmdqueryname=tos) *tos-value* command to configure a ToS value for test packets.
   6. (Optional) Run the [**exchange-port enable**](cmdqueryname=exchange-port+enable) command to enable the switching between the UDP source port number and UDP destination port number.
5. Run [**start**](cmdqueryname=start) **now**
   
   
   
   The NQA test is started.
   
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   Currently, an RFC 2544 generalflow test can be started only by running the [**start**](cmdqueryname=start) **now** command. However, user services will be interrupted during the test.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.