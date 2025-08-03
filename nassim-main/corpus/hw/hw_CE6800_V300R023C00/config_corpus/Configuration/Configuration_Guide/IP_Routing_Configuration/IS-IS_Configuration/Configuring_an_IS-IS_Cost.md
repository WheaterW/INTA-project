Configuring an IS-IS Cost
=========================

Configuring an IS-IS Cost

#### Context

The costs of IS-IS interfaces can be determined in the following modes (in descending order of priority):

* Interface cost: configured for a specified interface
* Global cost: configured for all interfaces
* Automatically calculated cost: automatically calculated based on the interface bandwidth

The value range of the interface cost depends on the cost style. By default, the cost of an IS-IS interface is 10, and the cost style is narrow.

![](public_sys-resources/note_3.0-en-us.png) 

If you need to change the cost style of IS-IS routes, configure it when configuring basic IS-IS functions. If you change the IS-IS cost style when IS-IS is running, the current IS-IS process will be restarted, which may trigger neighbor relationship reestablishment.



#### Procedure

* Configure an IS-IS cost style.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) [ process-id ] [ vpn-instance vpn-instance-name ]
     ```
  3. Configure an IS-IS cost style.
     
     
     ```
     [cost-style](cmdqueryname=cost-style) { { narrow | wide | wide-compatible } | { compatible | narrow-compatible } [ relax-spf-limit ] }
     ```
     
     By default, a device sends and accepts routes with the IS-IS cost style being narrow. The cost value range of an interface and the cost value range of the routes that can be accepted by the interface vary with the cost style.
     
     If the cost style is **narrow**, the cost of an interface ranges from 1 to 63, and the maximum cost of the routes that can be accepted by the interface is 1023.
     
     If the cost style is **narrow-compatible** or **compatible**, the cost of an interface ranges from 1 to 63, and the cost value range of the routes that can be accepted by the interface is related to the **relax-spf-limit** parameter.
     
     If the cost style is **wide** or **wide-compatible**, the cost of an interface ranges from 1 to 16777214 or the maximum value (16777215). The maximum cost of the routes that can be accepted by the interface is 16777214.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a cost for a specified IS-IS interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode from Layer 2 to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Configure a cost for the IS-IS interface.
     
     
     ```
     [isis](cmdqueryname=isis) cost cost [ level-1 | level-2 ]
     ```
     
     By default, the cost of an IS-IS interface is 10.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     To change the cost of a loopback interface, you can only run the [**isis cost**](cmdqueryname=isis+cost) command in the interface view.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a global IS-IS cost.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) [ process-id ]
     ```
  3. Configure a global IS-IS cost.
     
     
     ```
     [circuit-cost](cmdqueryname=circuit-cost) cost [ level-1 | level-2 ]
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure IS-IS to automatically calculate interface costs.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) [ process-id ]
     ```
  3. Configure a bandwidth reference value.
     
     
     ```
     [bandwidth-reference](cmdqueryname=bandwidth-reference) value
     ```
     
     By default, the bandwidth reference value is 100 Mbit/s.
  4. Configure IS-IS to automatically calculate interface costs.
     
     
     ```
     [auto-cost enable](cmdqueryname=auto-cost+enable)
     ```
     
     The bandwidth reference value configured using the [**bandwidth-reference**](cmdqueryname=bandwidth-reference) command is valid only when the cost style is wide or wide-compatible. In this case, the cost of each interface is calculated using the following formula: Interface cost = (Bandwidth-reference/Interface bandwidth) x 10.
     
     If the cost style is narrow, narrow-compatible, or compatible, the cost of an interface is determined by the interface bandwidth range. [Table 1](#EN-US_TASK_0000001130784112__table10137203131118) lists the interface costs corresponding to different interface bandwidth ranges.
     
     **Table 1** Mapping between IS-IS interface costs and interface bandwidth ranges
     | Cost Value | Interface Bandwidth Range |
     | --- | --- |
     | 60 | Interface bandwidth â¤ 10 Mbit/s |
     | 50 | 10 Mbit/s < Interface bandwidth â¤ 100 Mbit/s |
     | 40 | 100 Mbit/s < Interface bandwidth â¤ 155 Mbit/s |
     | 30 | 155 Mbit/s < Interface bandwidth â¤ 622 Mbit/s |
     | 20 | 622 Mbit/s < Interface bandwidth â¤ 2.5 Gbit/s |
     | 10 | Interface bandwidth > 2.5 Gbit/s |
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

* Run the **display this** command in the IS-IS view to check the IS-IS cost style.
* Run the [**display isis**](cmdqueryname=display+isis) **interface** [ **verbose** ] [ [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* ] command to check IS-IS interface link costs.