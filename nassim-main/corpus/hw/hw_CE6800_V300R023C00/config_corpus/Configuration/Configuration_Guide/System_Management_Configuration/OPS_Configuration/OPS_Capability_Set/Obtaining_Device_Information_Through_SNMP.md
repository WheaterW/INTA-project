Obtaining Device Information Through SNMP
=========================================

Obtaining Device Information Through SNMP

#### Application Phase

Subscription and execution phases


#### Function Prototype

result1\_value, result2\_description = \_ops.snmp.get(oid)

result1\_value, result2\_description = \_ops.snmp.getnext(oid)


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| oid | Specifies the OID of a leaf MIB object. | The value is a string of 1 to 1047 characters, for example, 1.3.6.1.2.1.7.1.0. |



#### Return Values

**result1\_value** and **result2\_description** in the function prototype indicate return values.

**result1\_value** is the first return value and specifies a node value or next node value. **None** indicates that the information fails to be obtained. Other values indicate that the information is obtained successfully.

**result2\_description** is the second return value and describes the result. This value is a character string.


#### Usage Description

This API enables you to obtain detailed information of a specified leaf object and the next leaf object.


#### Usage Examples

When a subscribed event is matched, the OIDs of the current and next objects are obtained.

```
test.py
import ops
opsObj = ops.ops()
curValue, ret = opsObj.snmp.get("1.3.6.1.2.1.2.2.1.1")
print("ret is",ret,"and current value of OID is",curValue,"\n)
nextVal, nextOid, ret = opsObj.snmp.getnext("1.3.6.1.2.1.2.2.1.1")
print("ret is", ret,"the next OID of the current OID is", nextOid,"and the corresponding value is",nextVal,"\n")
```