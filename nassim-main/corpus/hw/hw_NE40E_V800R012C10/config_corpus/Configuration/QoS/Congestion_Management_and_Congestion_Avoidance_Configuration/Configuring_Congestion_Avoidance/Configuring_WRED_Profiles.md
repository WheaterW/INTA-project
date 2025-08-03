Configuring WRED Profiles
=========================

You can configure the lower drop threshold, upper drop threshold, and drop probability for packets of different colors in WRED profiles.

#### Context

Each WRED profile supports processing of a maximum of red, yellow, and green packets. Generally, green packets have the smallest drop probability and the highest thresholds (both lower and upper drop thresholds); yellow packets have the medium drop probability and thresholds; red packets have the highest drop probability and the lowest thresholds (both lower and upper drop thresholds).

By configuring a WRED profile, you can set upper and lower drop thresholds (in percentages) and drop probability for queues.

* When the percentage of the actual length of a packet queue over the length of a port queue is less than the lower drop threshold, the system does not drop packets.
* When the percentage of the actual length of a packet queue over the length of a port queue is between the upper and lower drop thresholds, the system drops packets through the WRED mechanism. The longer the queue length, the higher the drop probability.
* When the percentage of the actual length of a packet queue over the length of a port queue is greater than the higher drop threshold, the system drops all subsequent packets.

The drop thresholds and drop probability of packets of each color are configurable.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* If you do not configure a WRED profile for a port queue, the system uses the default tail drop policy.
* The upper and lower drop thresholds for red packets can be set to the minimum; those for yellow packets can be greater; those for green packets can be set to the maximum.
* In the actual configuration, the lower drop threshold is recommended to begin with 50% and be adjusted based on the drop precedence. It is recommended that the drop probability be set to 100%.

Perform the following steps on the Router.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**port-wred**](cmdqueryname=port-wred) *port-wred-name*
   
   
   
   A WRED profile is created, and the WRED profile view is displayed.
3. Run [**color**](cmdqueryname=color) { **green** | **yellow** | **red** } **low-limit** *low-limit-percentage* **high-limit** *high-limit-percentage* **discard-percentage** *discard-percentage*
   
   
   
   The lower drop threshold, upper drop threshold, and drop probability are set for packets of different colors.
4. (Optional) Run [**queue-depth**](cmdqueryname=queue-depth) { *queue-depth-value* | **buffer-time** *queue-depth-time* }
   
   
   
   The depth of a port queue is adjusted.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.