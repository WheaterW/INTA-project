Configuring ND VLAN CAR
=======================

Limiting the rate of ND packets based on interfaces ensures that interfaces are isolated when ND attacks occur, minimizing the impact on devices and services. After the ND VLAN CAR alarm function is enabled, the device reports an alarm when the number of ND packets sent by an interface exceeds the ND VLAN CAR threshold.

#### Context

Perform the following steps on the Router interface that requires ND packet attack defense:


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**slot**](cmdqueryname=slot) *slot-id* command to enter the slot view.
3. Run the [**undo alarm ipv6 nd**](cmdqueryname=undo+alarm+ipv6+nd+na+ns-multicast+ns-unicast+attack+disable) { **na** | **ns-multicast** | **ns-unicast** } **attack disable** command to enable the ND VLAN CAR alarm function.
   
   
   
   In VS mode, this command is supported only by the admin VS.
4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
5. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
6. Run the [**ipv6 nd**](cmdqueryname=ipv6+nd+na+ns-multicast+ns-unicast+rate-limit) { **na** | **ns-multicast** | **ns-unicast** } **rate-limit** *rate* command to configure an ND VLAN CAR threshold for ND packets that are allowed to pass through the interface.
7. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
8. (Optional) Configure the percentage of the level-2 CAR bandwidth for ND VLAN CAR in the CP-CAR bandwidth for ND packets.
   1. Run the [**slot**](cmdqueryname=slot) *slot-id* command to enter the slot view.
   2. Run the [**ipv6 nd**](cmdqueryname=ipv6+nd+na+ns-multicast+ns-unicast+rate-limit-percent) { **na** | **ns-multicast** | **ns-unicast** } **rate-limit-percent** *rate-value* command to configure the percentage of the level-2 CAR bandwidth for ND VLAN CAR in the CP-CAR bandwidth for ND packets.
      
      
      
      In VS mode, this command is supported only by the admin VS.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.

#### Verifying the Configuration

After the configuration is complete, verify it.

1. Run the [**display ipv6 nd**](cmdqueryname=display+ipv6+nd+na+ns-multicast+ns-unicast+rate-limit+interface) { **na** | **ns-multicast** | **ns-unicast** } **rate-limit interface** { *interface-type* *interface-num* | *interface-name* } command to check the VLAN CAR threshold for ND packets that are allowed to pass through the specified interface.
2. Run the [**display ipv6 nd**](cmdqueryname=display+ipv6+nd+na+ns-multicast+ns-unicast+attack+interface) { **na** | **ns-multicast** | **ns-unicast** } **attack interface** { *interface-type* *interface-num* | *interface-name* } [ **vlan-id** *vlan-number* | **pe-vid** *pe-vid* **ce-vid** *ce-vid* ] [ **history** ] command to check ND packet attack information about the specified interface.
3. Run the [**display ipv6 nd**](cmdqueryname=display+ipv6+nd+na+ns-multicast+ns-unicast+attack+slot+all) { **na** | **ns-multicast** | **ns-unicast** } **attack slot** { *slotid* | **all** } [ **history** ] command to check ND packet attack information about the specified board.