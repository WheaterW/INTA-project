(Optional) Disabling URPF for a Specified Flow
==============================================

(Optional) Disabling URPF for a Specified Flow

#### Context

After URPF is configured on an interface, the device performs URPF check on all incoming packets on the interface. To prevent certain packets from being discarded (for example, enable the device to trust all packets from a server and not perform URPF check for such packets), you can disable URPF for the specified flow. The configuration procedure is as follows:

1. Configure a traffic classifier. The traffic classifier defines a group of matching rules to classify packets that do not require URPF check. For details, see "Configuring a Traffic Classifier" under "MQC Configuration" in Configuration Guide > QoS Configuration.
2. Configure a traffic behavior and disable URPF in the traffic behavior. For details, see "Procedure" in this section.
3. Configure a traffic policy, bind the traffic classifier to the traffic behavior, and disable URPF for the classified packets. For details, see "Configuring a Traffic Policy" under "MQC Configuration" in Configuration Guide > QoS Configuration.
4. Apply the traffic policy in the corresponding view as required. For details, see "Applying a Traffic Policy" under "MQC Configuration" in Configuration Guide > QoS Configuration.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a traffic behavior and enter the traffic behavior view, or enter the view of an existing traffic behavior.
   
   
   ```
   [traffic behavior](cmdqueryname=traffic+behavior) behavior-name
   ```
3. Disable URPF check for a specified flow.
   
   
   ```
   [ip urpf disable](cmdqueryname=ip+urpf+disable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display traffic behavior**](cmdqueryname=display+traffic+behavior) [ *behavior-name* ] command to check the traffic behavior configuration.