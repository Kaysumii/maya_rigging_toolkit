import maya.cmds as cmds

def create_control():
    selected = cmds.ls(selection=True, type="joint", long=True)

    if not selected:
        cmds.warning("Please select at least one joint.")
        return

    for jnt in selected:
        # Get the joints name
        joint_name = jnt.split("|")[-1]

        # remove the joint suffix
        base_name = joint_name.replace("_JNT","")

        # Name the control and group
        control_name = base_name + "_CON"
        group_name = base_name + '_GRP'

        # Create a circle
        con = cmds.circle(name = control_name, nr = [1,0,0]) [0]
     
        # Group the Circle
        grp = cmds.group(con, name= group_name)

        # Match transforms
        cmds.matchTransform(grp, jnt)
    
        # Constrain the Joint
        cmds.parentConstraint(con, jnt, maintainOffset= True)

    print("Controls created successfully!")

def color_control():
    for con in cmds.ls("L_*_CON"):
        shapes = cmds.listRelatives(con, shapes=True)
        if shapes:
            cmds.setAttr(shapes[0] + ".overrideEnabled", 1)
            cmds.setAttr(shapes[0] + ".overrideColor", 6)
    for con in cmds.ls("R_*_CON"):
            shapes = cmds.listRelatives(con, shapes=True)
            if shapes:
                cmds.setAttr(shapes[0] + ".overrideEnabled", 1)
                cmds.setAttr(shapes[0] + ".overrideColor", 13)
    for con in cmds.ls("*_CON"):
        if not con.startswith(("L_","R_")):
            shapes = cmds.listRelatives(con, shapes=True)
            cmds.setAttr(shapes[0] + ".overrideEnabled", 1)
            cmds.setAttr(shapes[0] + ".overrideColor", 6)

def scale_controls(size):
    sel= cmds.ls(selection = True)
    if not sel:
        cmds.warning("Please select a control.")
        return
    for each in sel:
        if each.endswith("_CON"):
            cmds.scale(size, size, size, each + ".cv[*]", r= True)

def reset_controls():
    sel = cmds.ls(selection = True, type="transform")

    if not sel:
        cmds.warning("Please select a control.")
        return
    for con in sel:
        if con.endswith("_CON"):
            for axis in ["X","Y","Z"]:
                cmds.setAttr(con +".translate" + axis, 0)

def main():
    create_control()
    color_control

if __name__ == "__main__":
    main()