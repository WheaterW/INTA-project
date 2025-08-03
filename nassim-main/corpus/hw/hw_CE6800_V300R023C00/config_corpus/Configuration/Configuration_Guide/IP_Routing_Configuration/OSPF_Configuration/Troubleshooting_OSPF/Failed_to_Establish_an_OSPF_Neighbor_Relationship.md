Failed to Establish an OSPF Neighbor Relationship
=================================================

Failed to Establish an OSPF Neighbor Relationship

#### Fault Symptom

An OSPF neighbor relationship cannot be established between two devices.


#### Procedure

1. Check whether the physical status and protocol status of interfaces at both ends are up and stable, whether packet loss occurs on the interfaces, and whether the two devices can ping each other with large packets.
   
   
   
   If the physical status or protocol status of either interface is not up or unstable (an interface flaps, for example), check the physical link and link layer protocol. Ensure that both the physical status and protocol status of each interface are up and that the interfaces have no error packet statistics.
   
   You can perform a ping test for a long time with large packets (with each being 1500 bytes or longer) to check whether any packet loss occurs on the interfaces.
2. Check whether the OSPF processes on the two devices have the same router ID.
   
   
   
   Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **brief** command on each device to check the router ID in the OSPF process.
   
   Each router ID must be unique on the entire network. If router ID conflict occurs, devices at both ends cannot establish an OSPF neighbor relationship, and routing information is incorrect. In this case, you are advised to set a unique router ID for each OSPF process on each device.
   
   If the OSPF processes on the devices have the same router ID, run the [**ospf**](cmdqueryname=ospf) [ *process-id* ] **router-id** *router-id* command in the system view to change the router ID on either device and ensure that the two devices have different router IDs in the same OSPF process.
   
   After changing the router ID, run the [**reset ospf**](cmdqueryname=reset+ospf) [ *process-id* ] **process** command in the user view to allow the new router ID to take effect.
3. Check whether the two devices have the same OSPF area ID.
   
   
   
   Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **brief** command on each device to check the OSPF area ID.
   
   If the devices have different OSPF area IDs, run the [**area**](cmdqueryname=area) *area-id* command in the OSPF view on either device to change the OSPF area ID and ensure that the two devices have the same OSPF area ID.
4. Check whether the OSPF interfaces at both ends have the same network type.
   
   
   
   Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** command on each device to check the OSPF interface network type.
   
   The network types of the OSPF interfaces at both ends of a link must be the same; otherwise, the two interfaces cannot establish an OSPF neighbor relationship.
   
   If the network types of the two OSPF interfaces are different, run the [**ospf network-type**](cmdqueryname=ospf+network-type) { **broadcast** | **nbma** | **p2mp** | **p2p** } command in the OSPF interface view on either device to change the network type and ensure that the OSPF interfaces at both ends have the same network type.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   If the network types of OSPF interfaces at both ends are set to NBMA, run the [**peer**](cmdqueryname=peer) *ip-address* [ **dr-priority** *priority* ] command in the OSPF view on each device to configure the NBMA neighbor.
5. Check whether the OSPF interfaces at both ends have the same IP address mask.
   
   
   
   Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **interface** *interface-type* *interface-number* command on each device to check the IP address information of the specified OSPF interface.
   
   The IP address masks of OSPF interfaces at both ends of a link must be the same; otherwise, the two interfaces cannot establish an OSPF neighbor relationship. On a P2MP network, however, you can run the [**ospf p2mp-mask-ignore**](cmdqueryname=ospf+p2mp-mask-ignore) command in the OSPF interface view to disable a device from checking the network mask so that an OSPF neighbor relationship can be established.
   
   If the two OSPF interfaces have different IP address masks, run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } command in the OSPF interface view on either device to change the IP address mask and ensure that the two OSPF interfaces have the same IP address mask.
6. Check whether the network segment that the IP addresses of the two OSPF interfaces belong to is included in the network segment specified in the **network** command.
   
   
   
   Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **interface** *interface-type* *interface-number* command on each device to check the IP address of the specified OSPF interface, and run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration** **ospf** command on each device to check the OSPF process configuration.
   
   OSPF can run on an interface only if the following two conditions are met:
   
   * The mask length of the interface's IP address is greater than or equal to that converted from the wildcard mask specified in the **network** command. OSPF uses the wildcard mask. For example, 0.0.0.255 indicates that the mask length is 24 bits.
   * The primary IP address (if any) of the interface must be within the network segment specified in the **network** command.
   
   If the IP address of an interface does not meet the preceding conditions, run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } command in the OSPF interface view to change the IP address of the interface, or run the [**network**](cmdqueryname=network) command in the OSPF area view to change the specified network segment so that the IP address of the interface can meet the preceding conditions.
7. Check whether the DR priorities of the two OSPF interfaces are not 0.
   
   
   
   Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** command on each device to check the OSPF interface's DR priority.
   
   On a broadcast or NBMA network, ensure that the DR priority of at least one OSPF interface on the link is not 0 so that the DR can be elected. Otherwise, the neighbor status of both ends can only reach **2-Way**.
   
   In this case, run the [**ospf dr-priority**](cmdqueryname=ospf+dr-priority) *priority* command in the OSPF interface view on either device to change the DR priority and ensure that at least one OSPF interface has a non-zero DR priority.
8. Check whether the intervals at which the OSPF interfaces on both ends of the link send Hello packets are the same.
   
   
   
   Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** command on devices at both ends of the link to check the interval for sending Hello packets on OSPF interfaces.
   
   If the intervals at which OSPF interfaces on both ends of a link send Hello packets are different, the OSPF neighbor relationship may fail to be established. In this case, run the **[**ospf timer hello**](cmdqueryname=ospf+timer+hello)** *interval* command in the interface view to change the interval at which OSPF interfaces send Hello packets and ensure that the intervals at the two ends are the same.