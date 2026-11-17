import maya.cmds as cmds

def create_control():
    selected = cmds.ls(selection=True, type="joint", long=True)

    if not selected:
        cmds.warning("Please select at least one joint.")
        return

    for jnt in selected:
        # Get the joints short name
        joint_name = jnt.split("|")[-1]
        # Create a circle
        con = cmds.circle(name = jnt.replace("JNT", "CON"), nr = [1,0,0]) [0]
     
        # Group the Circle
        grp = cmds.group(con)

        # Match transforms
        cmds.matchTransform(grp, jnt)
    
        # Constrain the Joint
        cmds.ParentConstraint(con, jnt)

    print("Controls created successfully!")

def main():
    create_control()


if __name__ == "__main__":
    main()