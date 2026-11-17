import maya.cmds as cmds

def create_control():
    selected = cmds.ls(selection=True, type="joint")

    if not selected:
        cmds.warning("Please select at least one joint.")
        return

    for jnt in selected:
        # Create a circle
        con = cmds.circle(name = jnt.replace("JNT", "CON"), nr = [1,0,0]) [0]
     
        # Group the Circle
        grp = cmds.group(con)

        # Match transforms
        cmds.matchTransform(grp, jnt)
    
        # Constrain the Joint
        cmds.ParentConstraint(con, jnt)

    print("Controls created successfully!")