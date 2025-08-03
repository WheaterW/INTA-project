Disabling an SAID Node
======================

Disabling an SAID Node

#### Context

By default, the device detects and diagnoses all SAID nodes. If a certain service is not deployed on the device or does not need to be detected or diagnosed, disable the corresponding SAID node.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable an SAID node.
   
   
   ```
   [set said-node](cmdqueryname=set+said-node) said-node-name disable
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display said-node status**](cmdqueryname=display+said-node+status) [ **slot** *slot-id* [ **cpu** *cpu-id* ] ] command to view brief information about SAID nodes.