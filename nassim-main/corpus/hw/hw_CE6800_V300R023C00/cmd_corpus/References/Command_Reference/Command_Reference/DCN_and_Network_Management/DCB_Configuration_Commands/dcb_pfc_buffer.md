dcb pfc buffer
==============

dcb pfc buffer

Function
--------



The **dcb pfc buffer** command sets the thresholds for triggering and stopping PFC frames, guaranteed buffer threshold, and headroom buffer threshold for a PFC queue in the inbound direction.

The **undo dcb pfc buffer** command deletes the manually configured thresholds for triggering and stopping PFC frames, guaranteed buffer threshold, and headroom buffer threshold for a PFC queue in the inbound direction.



By default, the thresholds for triggering and stopping PFC frames, guaranteed buffer threshold, and headroom buffer threshold for a PFC queue in the inbound direction are not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K:

**dcb pfc buffer** *queue-index* **xon** **static** *xon-value* { **kbytes** | **mbytes** } **xoff** **static** *xoff-value* { **kbytes** | **mbytes** }

**undo dcb pfc buffer** *queue-index* **xon** **static** *xon-value* { **kbytes** | **mbytes** } **xoff** **static** *xoff-value* { **kbytes** | **mbytes** }

For CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K:

**dcb pfc buffer** *queue-index* **xon** **dynamic** *alpha-value* **xoff** **dynamic** *alpha-value*

**undo dcb pfc buffer** *queue-index* **xon** **dynamic** *alpha-value* **xoff** **dynamic** *alpha-value*

For CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-LL (low latency mode), CE6885-SAN, CE8855, CE8851-32CQ4BQ:

**dcb pfc buffer** *queue-index* **guaranteed** *guaranteed-value* [ **bytes** | **kbytes** ]

**dcb pfc buffer** *queue-index* **hdrm** *hdrm-value* [ **kbytes** ]

**undo dcb pfc buffer** [ *queue-index* [ **guaranteed** [ *guaranteed-value* [ **bytes** | **kbytes** ] ] ] ]

**undo dcb pfc buffer** [ *queue-index* [ **hdrm** [ *hdrm-value* [ **kbytes** ] ] ] ]

For CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-LL (low latency mode), CE6885-SAN, CE8855, CE8851-32CQ4BQ:

**dcb pfc buffer** *queue-index* **xoff** { **static** *xoff-value* [ **kbytes** | **mbytes** ] | **dynamic** *alpha-value* } [ **xon** **offset** *offset-value* [ **kbytes** | **mbytes** ] ]

**undo dcb pfc buffer** [ *queue-index* [ **xoff** [ **static** [ *xoff-value* [ **kbytes** | **mbytes** ] ] | **dynamic** [ *alpha-value* ] ] [ **xon** **offset** [ *offset-value* [ **kbytes** | **mbytes** ] ] ] ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *queue-index* | Specifies the index of an interface queue. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 0 to 7.  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM:The value is an integer ranging from 0 to 5. |
| **xon** *xon-value* | Specifies the threshold for stopping PFC frames. When the occupied buffer space is lower than this threshold, PFC frames are not sent.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM. | The value is an integer ranging from 1 to 6144, in kbytes. The default value is 100 kbytes. The default unit is kbytes.  The configured value of xon must be smaller than or equal to the configured value of xoff. |
| **static** | Specifies the static threshold. | - |
| **kbytes** | Specifies that a threshold is expressed in kbytes. | - |
| **mbytes** | Specifies that a threshold is expressed in mbytes. | - |
| **xoff** *xoff-value* | Specifies the threshold for triggering PFC frames. When the occupied buffer space is higher than this threshold, PFC frames are sent. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 30720, in kbytes. The default unit is kbytes.  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM:The value is an integer ranging from 1 to 6144, in kbytes. The default value is 125 kbytes. The default unit is kbytes.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 9216, in kbytes. The default unit is kbytes. |
| **dynamic** *alpha-value* | Specifies the dynamic threshold. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 12. The default value is 3.  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM:The value is an integer ranging from 0 to 10. |
| **guaranteed** *guaranteed-value* | Specifies the guaranteed buffer threshold for a PFC queue in the inbound direction. The buffer space specified by this threshold cannot be used by other queues.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 640 to 25600, in bytes. The default value is 1600 bytes. The default unit is bytes.  For the CE6885-LL (low latency mode):The value is an integer ranging from 640 to 25600, in bytes. The default value is 1632 bytes. The default unit is bytes. |
| **bytes** | Specifies that the threshold is expressed in bytes.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **hdrm** *hdrm-value* | Specifies the headroom buffer threshold for a PFC queue in the inbound direction. If the volume of traffic received after PFC frames are sent exceeds the buffer space specified by this threshold, the traffic is discarded.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 16 to 30720, in kbytes. The default value is 256 kbytes. The default unit is kbytes.  For the CE6885-LL (low latency mode):The value is an integer ranging from 16 to 9216, in kbytes. The default value is 256 kbytes. The default unit is kbytes. |
| **offset** *offset-value* | Specifies the offset of the Xon value relative to the Xoff value.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ: The value is an integer ranging from 1 to 30720, in kbytes. The default value is 6 kbytes. The default unit is kbytes.  The configured value of offset must be smaller than the configured value of xoff. The difference between them is the Xon value, which is the threshold for stopping PFC frames.  The actual effective threshold for stopping PFC frames is the larger value between the Xon protection value and the value obtained by subtracting the configured offset value from the configured xoff value.  The Xon protection value is that of the Xon-Lowest field in the display dcb pfc buffer command output.  For the CE6885-LL (low latency mode): The value is an integer ranging from 1 to 9216, in kbytes. The default value is 6 kbytes. The default unit is kbytes.  The configured value of offset must be smaller than the configured value of xoff. The difference between them is the Xon value, which is the threshold for stopping PFC frames.  The actual effective threshold for stopping PFC frames is the larger value between the Xon protection value and the value obtained by subtracting the configured offset value from the configured xoff value.  The Xon protection value is that of the Xon-Lowest field in the display dcb pfc buffer command output. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the buffer space of a queue on an interface of the receive device exceeds the threshold, a backpressure signal is sent to the transmit device, requesting the transmit device to stop sending packets in the corresponding priority queue. You can run this command to adjust the threshold of a queue on an interface of the receive device.After PFC is enabled, the device has default thresholds for triggering and stopping PFC frames in the inbound direction. If you find that the default thresholds cannot meet your expectation, you can run this command to manually set the thresholds.The sum of the threshold for triggering PFC frames and the headroom buffer threshold in the inbound direction of a queue must be smaller than both the lower WRED threshold and queue-level service buffer threshold. Otherwise, packet loss occurs.When traffic is transmitted from multiple inbound interfaces to one outbound interface, the sum of the threshold for triggering PFC frames and the headroom buffer threshold of all these inbound interfaces must be smaller than both the lower WRED threshold and queue-level service buffer threshold of the single outbound interface. Otherwise, packet loss occurs.You can run the **display dcb pfc buffer** command to check the thresholds.**For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, and CE6863E-48S8CQ:**

* The actual effective threshold for stopping PFC frames is the larger value between the Xon protection value and the value obtained by subtracting the configured offset value from the configured xoff value. The Xon protection value is that of the Xon-Lowest field in the **display dcb pfc buffer** command output.
* If you run the **undo dcb pfc buffer** command without specifying the queue-index parameter, the manually configured thresholds for triggering and stopping PFC frames, guaranteed buffer threshold, and headroom buffer threshold for all PFC queues in the inbound direction are deleted.
* If you run the undo dcb pfc buffer <queue-index> command with only the queue index parameter specified, the manually configured thresholds for triggering and stopping PFC frames, guaranteed buffer threshold, and headroom buffer threshold for the specified PFC queue in the inbound direction are deleted.

**Precautions**

When an interface is transmitting traffic and encountering a congestion, the threshold for triggering PFC frames may fail to be configured on the interface. Therefore, you are advised to configure the threshold when the interface is not congested or after the interface is shut down using the **shutdown** command. (To check whether the interface is congested, run the **display qos buffer-usage** command.)**For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, and CE6863E-48S8CQ:**

* If PFC is enabled in a queue of an interface and packet loss occurs in the inbound direction of the interface, you are advised to run the dcb pfc buffer <queue-index> hdrm <hdrm-value> [ kbytes ] command in the interface view to increase the headroom buffer threshold for the specified PFC queue in the inbound direction.
* The buffer space is divided by fixed small blocks. Therefore, the actually effective buffer thresholds and the thresholds for triggering and stopping PFC frames are integer multiples of the fixed small block value rounded up. For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ, the fixed small block value is 320 bytes. For the CE6885-LL (low-latency mode), the fixed small block value is 96 bytes. The values in the **display dcb pfc buffer** command output are the actually effective ones.
* A single device supports a maximum of 30 profiles for the guaranteed buffer threshold, 28 profiles for the thresholds for triggering and stopping PFC frames, and 31 profiles for the headroom buffer threshold. If the number of used profiles reaches the upper limit, you need to delete historical configurations before delivering new configurations. Specifying a buffer threshold or both thresholds for triggering and stopping PFC frames occupies a profile. A value with a different unit, a dynamic threshold, and a static threshold each occupy a profile. Example:
  + Setting <guaranteed-value> to 700 bytes for queue 1 on an interface occupies a profile. In this case, if <guaranteed-value> is set to 800 bytes for queue 2 on an interface, this configuration occupies a new profile, and the two configurations occupy two profiles.
  + Setting <guaranteed-value> to 700 bytes for queue 1 on an interface occupies a profile. In this case, if <guaranteed-value> is also set to 700 bytes for queue 2 on an interface, this configuration does not occupy a profile, and the two configurations occupy the same profile.
  + Setting <guaranteed-value> to 700 bytes for queue 1 on an interface occupies a profile. In this case, if <guaranteed-value> is set to a different value (800 bytes) for this queue and no other interface queue has <guaranteed-value> set to 700 bytes, this configuration occupies a new profile. The previously occupied profile is released because no queue uses it. After the two configurations, only one profile is occupied.


Example
-------

# On 100GE1/0/1, set the threshold for triggering PFC frames to 300 kbytes and the threshold offset to 200 kbytes for queue 1, and set the guaranteed and headroom buffer thresholds to 25 kbytes and 1000 kbytes for the queue in the inbound direction. (CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, and CE6863E-48S8CQ)
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] dcb pfc buffer 1 guaranteed 25 kbytes
[*HUAWEI-100GE1/0/1] dcb pfc buffer 1 xoff static 300 kbytes xon offset 200 kbytes
[*HUAWEI-100GE1/0/1] dcb pfc buffer 1 hdrm 1000 kbytes

```

# On 100GE1/0/1, set the thresholds for triggering and stopping PFC frames to dynamic 10 and dynamic 5, respectively, for queue 3. (CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM)
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] dcb pfc buffer 3 xon dynamic 5 xoff dynamic 10

```