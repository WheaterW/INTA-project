Configuring Network Slice Interfaces
====================================

You can configure network slice interfaces and specify the network slice instances to which they belong.

#### Context

Base and network slice interfaces can be constructed on the same main interface (or FlexE interfaces in the same group). Interfaces in network slicing scenarios are classified as base or network slice interfaces, which are defined as follows:

* Base interface: An address prefix is configured for route calculation. It can also be used as a network slice interface.
* Network slice interface: No address prefix is configured, and only the network slices to which the interface belongs are specified.

After a base interface is configured for network slicing, traffic diverted to that base interface is forwarded through the corresponding network slice interface based on network slicing requirements.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If the outbound interface and slice interface are different FlexE interfaces in the same group, you need to run the **basic-slice** command for the remote inbound interface according to the **basic-slice** command configuration for the base interface of the outbound interface.



#### Procedure

1. Configure a base interface.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
      
      
      
      IPv6 is enabled on the interface.
   4. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* }
      
      
      
      A global unicast address is configured for the interface.
   5. (Optional) Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* | **auto** } **link-local**
      
      
      
      A link-local address is configured for the interface.
   6. Run [**network-slice**](cmdqueryname=NETWORK-SLICE%28NETSLICINGOM%29) *slice-id* { **data-plane** | **flex-channel** *flex-channel-value* [ **exclusive** | **flex-channel-pir** *pir-value* ] }
      
      
      
      A slice ID is configured for the base interface.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure a network slice interface.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number**.subinterface-number*
      
      
      
      The sub-interface view is displayed.
   3. Run [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id*
      
      
      
      The sub-interface is associated with a VLAN.
   4. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
      
      
      
      IPv6 is enabled on the sub-interface.
   5. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* | **auto** } **link-local**
      
      
      
      A link-local address is configured for the sub-interface.
   6. Run [**mode channel enable**](cmdqueryname=mode+channel+enable)
      
      
      
      The channelization function is enabled for the sub-interface.
   7. (Optional) Run [**mode channel bandwidth**](cmdqueryname=mode+channel+bandwidth) *bwvalue*
      
      
      
      The bandwidth of the channelized sub-interface is configured.
   8. Run [**basic-slice**](cmdqueryname=basic-slice) *slice-id*
      
      
      
      A base interface is configured for the network slice interface.
      
      
      
      The value of *slice-id* here must be the same as the slice ID of the base interface. Multiple network slice interfaces that belong to the same base interface form a network slice interface group. When forwarding an SRv6 packet, a device searches the network slice interface group corresponding to the outbound interface for the network slice interface that has the same slice ID as that in the HBH header.
   9. Run [**network-slice**](cmdqueryname=network-slice) *slice-id* [ **data-plane** | **flex-channel** *flex-channel-value* [ **exclusive** | **flex-channel-pir** *pir-value* ] ]
      
      
      
      A slice ID is configured for the network slice interface.
      
      
      
      * Before configuring a slice ID for a network slice interface, you must configure a global network slice instance. When deleting a network slice interface, you must specify the slice ID.
      * Before configuring a slice ID with parameters specified for an interface, enable IPv6. Before configuring a FlexE interface as a base interface, configure a global IPv6 address for the interface.
      * If the data-plane mode is specified, traffic is transmitted through the corresponding slice and shares the interface bandwidth with other services. As such, bandwidth resources cannot be guaranteed in this case.
      * The *slice-id* values configured for sub-interfaces of the same main interface that is not a FlexE interface cannot be the same.
      * The *slice-id* values configured for FlexE interfaces in the same group cannot be the same.
      * A Flex-channel refers to a service channel that is allocated independent queue and bandwidth resources based on the HQoS mechanism. The bandwidths of Flex-channels are strictly isolated. An independent bandwidth reservation sub-channel can be configured for a network slice on a physical interface to implement flexible bandwidth allocation. Flex-channels provide flexible and fine-grained interface resource reservation and enable each network slice to exclusively occupy the bandwidth and scheduling tree, thereby providing resource reservation for slice services. After **flex-channel** *flex-channel-value* is configured, the **exclusive** parameter can be used to set the bandwidth multiplexing mode for the Flex-channel, and the **flex-channel-pir** *pir-value* parameter can be used to set the peak information rate (PIR) of the Flex-channel. Note that *pir-value* must be greater than *flex-channel-value*.
   10. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.