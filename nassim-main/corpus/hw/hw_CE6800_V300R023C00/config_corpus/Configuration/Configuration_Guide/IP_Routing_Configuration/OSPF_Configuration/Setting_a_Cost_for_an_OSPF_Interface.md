Setting a Cost for an OSPF Interface
====================================

Setting a Cost for an OSPF Interface

#### Prerequisites

Before setting a cost for an OSPF interface, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

You can adjust and optimize route selection by setting OSPF interface costs. After the OSPF interface costs are set, the interface with the lowest cost is selected to transmit routing information. The OSPF interface cost can be set or calculated based on the interface bandwidth.


#### Procedure

* Manually set a cost for an OSPF interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Set a cost for the OSPF interface.
     
     
     ```
     [ospf cost](cmdqueryname=ospf+cost) value
     ```
     
     By default, the OSPF interface cost is calculated using the **Interface cost = Bandwidth reference value/Interface bandwidth** formula, in which the bandwidth reference value can be changed using the [**bandwidth-reference**](cmdqueryname=bandwidth-reference) command.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Set a bandwidth reference value to implement automatic OSPF interface cost calculation.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the OSPF view.
     
     
     ```
     [ospf](cmdqueryname=ospf) [ process-id ]
     ```
  3. Set a bandwidth reference value.
     
     
     ```
     [bandwidth-reference](cmdqueryname=bandwidth-reference) value
     ```
     
     By default, the bandwidth reference is 100 Mbit/s. Therefore, the interface cost equals 100 Mbit/s (100,000,000 bit/s) divided by the interface bandwidth (in bit/s).
     
     The calculation formula is as follows: **Interface cost = Bandwidth reference value/Interface bandwidth**. The integer of the calculation result is used as the cost of the interface. If the result is smaller than 1, the cost is 1.
  4. Enable the device to use the configuration bandwidth of the OSPF interface to calculate a cost for the interface.
     
     
     ```
     [bandwidth-config enable](cmdqueryname=bandwidth-config+enable)
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** [ **all** | **no-peer** | *interface-type* *interface-number* ] [ **verbose** ] command to check information about the OSPF interface. You can view the interface cost from the **Cost** field in the command output.