Configuring PHP
===============

When you configure penultimate hop popping (PHP), specify a label that the egress assigns to the penultimate hop.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**label advertise**](cmdqueryname=label+advertise+explicit-null+implicit-null+non-null) { **explicit-null** | **implicit-null** | **non-null** }
   
   
   
   The label assigned to the penultimate node is specified.
   
   
   
   * **explicit-null**: disables PHP. If this parameter is configured, the egress assigns an explicit null label with value 0 to the penultimate node. **explicit-null** supports MPLS QoS. Setting this parameter helps reduce label resource consumption on the egress and prevents Exp value loss. Given this, when the QoS attributes of an end-to-end service need to be carried in the EXP field of labels, you can specify this parameter.
   * **non-null**: disables PHP. If this parameter is configured, the egress assigns a label with a value greater than or equal to 16 to the penultimate node. The non-null label consumes resources on the egress, which is not recommended. This parameter can be specified when the egress needs to identify services based on labels.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   PHP takes effect on LSPs that are to be established, but not on existing LSPs.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.