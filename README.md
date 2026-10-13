# Open Maya Wrapper

An egornomic and typed Python API for Maya.

We love good IDE tools and LSP, and omw makes using the Maya API fun again!

## Here's an example of how much cleaner omw code is:

Using omw

```
from omw.node import MultiplyDivideNode

# Create two wrapped nodes
source = MultiplyDivideNode.create("sourceMultiply")
result = MultiplyDivideNode.create("resultMultiply")


source.input1.x.set(2.0)
source.input2.x.set(3.0)

result.input2.x.set(10.0)

# Connect source.outputX -> result.input1X
source.output.x.connect_to(result.input1.x)

# The result is (2 * 3) * 10 = 60
print(result.output.x.get())
```

Using normal maya.cmds

```
from maya import cmds

# Create two multiplyDivide nodes
source = cmds.createNode("multiplyDivide", name="sourceMultiply")
result = cmds.createNode("multiplyDivide", name="resultMultiply")

# Set values on the source node
cmds.setAttr(f"{source}.input1X", 2.0)
cmds.setAttr(f"{source}.input2X", 3.0)

# Set another value on the result node
cmds.setAttr(f"{result}.input2X", 10.0)

# Connect source.outputX -> result.input1X
cmds.connectAttr(
    f"{source}.outputX",
    f"{result}.input1X",
)

# The result is (2 * 3) * 10 = 60
print(cmds.getAttr(f"{result}.outputX"))
```
