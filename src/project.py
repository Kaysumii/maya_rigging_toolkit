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

def main():
    create_control()


if __name__ == "__main__":
    main()