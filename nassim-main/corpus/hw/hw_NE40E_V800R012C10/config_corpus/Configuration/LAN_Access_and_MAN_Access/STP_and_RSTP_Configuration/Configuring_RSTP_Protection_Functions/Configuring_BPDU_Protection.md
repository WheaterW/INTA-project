Configuring BPDU Protection
===========================

After bridge protocol data unit (BPDU) protection is enabled on a device, the device shuts down an edge port if the edge port receives a BPDU and notifies the NMS of the shutdown event.

#### Context

Edge ports are directly connected to user terminals and normally, the edge ports will not receive bridge protocol data units (BPDUs). Some attackers may send pseudo BPDUs to attack the device. If the edge ports receive the BPDUs, the device automatically configures the edge ports as non-edge ports and triggers new spanning tree calculation. Network flapping then occurs. BPDU protection can be used to protect devices against malicious attacks.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Perform the following steps on a device with an edge port:



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**stp bpdu-protection**](cmdqueryname=stp+bpdu-protection)
   
   
   
   BPDU protection is enabled on the device.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

To allow an edge port to automatically start after being shut down, you can run the [**error-down auto-recovery**](cmdqueryname=error-down+auto-recovery) **cause** *cause-item* **interval** *interval-value* command to configure the auto recovery function and set the delay on the port. After the delay expires, the port automatically goes Up. **interval** *interval-value* ranges from 30 to 86400, in seconds. Note the following when setting this parameter:

* There is no default value for the recovery time. Therefore, you must specify a delay when configuring this command.
* The smaller the *interval-value* is, the shorter it takes for the edge port to go Up, and the more frequently the edge port alternates between Up and Down.
* The larger the *interval-value* is, the longer it takes for the edge port to go Up, and the longer the service interruption lasts.